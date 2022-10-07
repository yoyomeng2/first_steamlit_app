import streamlit
import snowflake.connector
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog')
# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
# my_cur.execute("select color_or_style from catalog_for_website")
my_cur.execute("select current_user(), current_account(), current_region()")
my_catalog = my_cur.fetchone()
streamlit.text("hello form snowflake")
streamlit.text(my_catalog)
