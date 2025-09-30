# Vendor-Performance-Analysis-Project
## Exploratory Data Analysis
### Summary Statistics

<img width="1048" height="550" alt="image" src="https://github.com/user-attachments/assets/10109c43-651f-4cf9-ae82-fae2acee2f88" />
<img width="1132" height="746" alt="image" src="https://github.com/user-attachments/assets/a66743ea-da52-4cb1-87c4-8434f3a7f416" />


Note: This is before removing inconsistencies.
#### Negative and Zero Values:
- Gross Profit: Minimum Value is -99071.83, indicating losses. Some products or transactions may be selling at a loss due to high costs or selling at discounts lower than the purchase price.
- Profit Margin:  Has a minimum of -infinity, which suggests cases where revenue is zero or even lower than cost (loss)
- Total Sales Quantity and Sales Dollars: Minimum values are 0, meaning some products were purchased but were never sold. These could be slow-moving or obsolete stock.

#### Outliers Indicated by High Standard Deviation:
- Purchase & Actual Prices: The max values are significantly higher (2222.21, 2799.990000) than the mean (1.420384e+01, 2.071030e+01), indicating potential premium products.
- Freight Cost: Huge Variation from 10.53 to 257032.070000, suggests logistics inefficiencies or bulk shipments.
- Stock Turnover: Ranges from 0 to 183, implying some products sell extremely fast while others remain in stock indefinitely. Value more than 1 indicates that sold quantity for that product is higher than purchased quantity due to sales being fulfilled from older stock.

## Data Filtering
To enhance the reliability of the insights, we removed the inconsistencies:
	- **Gross Profit ≤ 0** (to exclude transactions leading to losses)
	- **Profit Margin ≤ 0** (to ensure analysis focuses on profitable transactions)
	- **Total Sales Quantity = 0** (to eliminate the inventory that was never sold)
	<img width="1036" height="541" alt="image" src="https://github.com/user-attachments/assets/200435ad-381c-4470-8a08-ec8c5b3b81be" />

Note: This is after removing inconsistencies
## Correlation Insights:

<img width="1177" height="923" alt="image" src="https://github.com/user-attachments/assets/72504fa8-a270-41bd-9324-8673baa9dd3b" />

- PurchasePrice has weak correlation between Total Sales Dollars (-0.10) and Gross Profit (-0.19), suggesting that price variations do not significantly impact sales or profit.
- Strong correlation between total purchase quantity and sales quantity (0.83), confirming efficient inventory turnover.
- Less correlation between profit margin and total sales price (0.15) .
- StockTurnover has good correlation with Gross Profit (0.38) and Profit Margin (0.47) suggesting efficient inventory management is successfully translating into increased profits.
	
## Research Questions and Key Findings:
### Brands for Promotional or Pricing Adjustments
<img width="775" height="222" alt="image" src="https://github.com/user-attachments/assets/86a94125-8711-4b4c-ade6-21f80163fccd" />

From this, we can see that there are 2 companies which have lower sales but higher profit margins, which could benefit from targeted marketing, promotions, or price optimisations to increase volume without compromising profitability.

<img width="1091" height="702" alt="image" src="https://github.com/user-attachments/assets/f707d347-83e5-4ff2-b850-c7d4a9c0a376" />

### Top Vendors by Sales and Purchase Contribution
The top 10 vendors contribute 79.91%  of total purchases, while the remaining vendors contribute only 20.1%. This over-reliance over a few vendors may introduce risks such as supply chain disruptions, indicating a need for diversification.

<img width="1151" height="667" alt="image" src="https://github.com/user-attachments/assets/efdab9eb-1776-42eb-853a-b9313baf9cea" />

### Impact of Bulk Purchasing on Cost Savings

<img width="711" height="261" alt="image" src="https://github.com/user-attachments/assets/7c23853d-d3ce-4926-b708-3bc6661d57a0" />


Here, we observed a peculiar pattern. These are:


- Vendors buying in bulk (Large Order size) get the lowest unit price ($6.09 per unit), meaning higher margins if they can manage inventory efficiently.
- The price difference between Medium and Large is substantial (~54%) which is quite unique to observe. There is not particular pattern between small, medium and large. 
- It is observed that goods that are purchased in large quantities have unit price the least, then in the small category and the highest unit price is when we purchase goods in medium range.

  <img width="979" height="598" alt="image" src="https://github.com/user-attachments/assets/3a0f797b-2035-445c-9309-768832d551ca" />

 
### Identifying Vendors with Low Turnovers

<img width="584" height="389" alt="image" src="https://github.com/user-attachments/assets/e3cb4c8f-4702-4a0e-95a5-868a61493119" />

 

These results indicate excess stock or slow moving products.
I found out some strange results from the unsold inventory count:

<img width="428" height="55" alt="image" src="https://github.com/user-attachments/assets/b19e8493-6a9c-4ae0-9f21-40eb385a3f48" />

 
We are observing inconsistency in the TotalSalesQuantity and TotalPurchaseQuantity. The unsold inventory value should either be 0 or in positive, but our results suggests there is a report of selling more than the purchased quantity which is not possible.

<img width="688" height="517" alt="image" src="https://github.com/user-attachments/assets/73c8a1ed-aaf9-4653-9635-e4bd2b596bac" />

 

From this, we can see:
	HEAVEN HILL DISTILLERIES, DIAGEO NORTH AMERICA INC, PROXIMO SPIRITS INC. have no unsold inventory left
	TREASURY WINE ESTATES, DELICATO VINEYARDS INC have $23.97 and $18.36 worth of products unsold
	And companies like BANFI PRODUCTS CORP, BANFI PRODUCTS CORP, KOBRAND CORPORATION, MARSALLE COMPANY, LUXCO INC report negative unsold left, which can imply wrong input in database or inconsistency in their report.

### Profit margin Comparison: High vs. Low
Top Vendors Profit Margin: Mean=77.34, 95% CI = (64.52, 90.16)
Low Vendors Profit Margin: Mean=51.83, 95% CI = (33.55, 70.11)

<img width="1006" height="550" alt="image" src="https://github.com/user-attachments/assets/45b8af5b-3fc8-45c3-9e4a-cd273bdeccf5" />

From the above results, we observe the following:

- The confidence interval for top-performing vendors (64.52% to 90.16%) is greater than the confidence interval for low-performing vendors (33.55% to 70.11%)
- This suggests that vendors with higher sales tend to maintain higher profit margins, suggesting uniformity in the sales prices.
- For low-performing vendors: They could focus on the quality of their products and how can they improve from competitive products. Also, can focus on their pricing issues.
- For top-performing vendors: Their sales are in par with their pricing, hence, we don’t need to worry for them.
