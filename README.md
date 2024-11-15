# etf_excel
An excel file to simulate multiple ETF.



Excel file contains two VB macro:
  -  "Recupera dati ETF": this macro requires the flask webserver to be running. It reads ETF name (from ETF list sheet), find the ISIN, make a GET request to the webserver to get historical quotation of that ETF. For each ETF it creates a sheet with ISIN name and its data.
  -  "Genera Grafici": Based on time range on the Portfolio sheet, it creates a chart for every ETF, and a last chart with all ETF revenues combined


Python webserver use this [repository]([https://pages.github.com/](https://github.com/druzsan/justetf-scraping)). to get data from justetf.com

