import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode="a"
)

def get_vendor_summary(conn):
    # this function will merge the different tables to get the overall vendor sales summary and adding new columns to the resultant data

    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary as (
  SELECT
    VendorNumber,
    SUM(Freight) as FreightCost
  FROM vendor_invoice
  GROUP BY VendorNumber
),
                                         
PurchaseSummary as (
  SELECT
     p.VendorNumber,
     p.VendorName,
     p.Brand,
     p.Description,
     p.PurchasePrice,
     pp.Volume,
     pp.Price as ActualPrice,
     SUM(p.Quantity) as TotalPurchaseQuantity,
     SUM(p.Dollars) as TotalPurchaseDollars
     FROM purchases p
     join purchase_prices pp
     ON p.Brand = pp.Brand
     WHERE p.PurchasePrice > 0
     GROUP BY p.VendorNumber, p.VendorName, p.Brand
     ORDER BY TotalPurchaseDollars),
                                         
SalesSummary as (SELECT  
  VendorNo,
  Brand,                  
  SUM(SalesDollars) as TotalSalesDollars,
  SUM(SalesPrice) as TotalSalesPrice,
  SUM(SalesQuantity) as TotalSalesQuantity,
  SUM(ExciseTax) as TotalExciseTax
  FROM sales                  
  GROUP BY VendorNo, Brand)
SELECT
  ps.VendorNumber,
  ps.VendorName,
  ps.Brand,
  ps.Description,
  ps.PurchasePrice,
  ps.Volume,
  ps.ActualPrice,
  ps.TotalPurchaseQuantity,
  ps.TotalPurchaseDollars,
  ss.TotalSalesDollars,
  ss.TotalSalesPrice,
  ss.TotalSalesQuantity,
  ss.TotalExciseTax,
  fs.FreightCost
FROM PurchaseSummary ps
LEFT JOIN SalesSummary ss ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
LEFT JOIN FreightSummary fs ON ps.VendorNumber = fs.VendorNumber
ORDER BY ps.TotalPurchaseDollars DESC""", conn)
    return vendor_sales_summary



def clean_data(df):
    # this function will clean the data

    #changing datatype to float
    df['Volume'] = df['Volume'].astype(float)

    #filling missing values with 0
    df.fillna(0, inplace=True)

    # removing spaces from catagorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # creating new columns for better analysis
    df['VendorName'] = df['VendorName'].str.strip()
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / (df['TotalPurchaseQuantity'])
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / (df['TotalPurchaseDollars']) * 100

    return df

if __name__ == '__main__':
    conn = sqlite3.connect('inventory.db')
    logging.info('Connected to the database successfully')

    vendor_sales_summary = get_vendor_summary(conn)
    logging.info('Vendor sales summary extracted successfully')

    vendor_sales_summary = clean_data(vendor_sales_summary)
    logging.info('Data cleaned successfully')

    ingest_db(vendor_sales_summary, 'vendor_sales_summary', conn)
    logging.info('Vendor sales summary ingested into the database successfully')

    conn.close()
    logging.info('Database connection closed')