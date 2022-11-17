import datetime
import pandas as pd
from datetime import datetime 




url = "http://127.0.0.1:5000"

# Extract tables
scraper = pd.read_html(url)

# Get first table                                                                                                           
dataframe = scraper[0]

# Extract columns                                                                                                           
donationreport = dataframe[[

 'ID', 
 'First Name',
 'Last Name', 
 'Email',   
 'Food Type',  
 'Amount',
 'Weight',
 'Gender',
 'Date'

 ]]

  
dt = datetime.now()
  
d = datetime.strftime(dt, "%d-%b-%Y-%H:%M:%S")

datetime.strptime(d,"%d-%b-%Y-%H:%M:%S")

donationreport.to_excel('pp_donations_{}.xlsx'.format(d))