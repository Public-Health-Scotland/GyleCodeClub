# Use this to show timings are same / similar
library(tictoc)

# Some SQL to do a simple extract
sql <-
  "Select LINK_NO, ADMISSION_DATE, DISCHARGE_DATE from ANALYSIS.SMR01_PI where DISCHARGE_DATE >= To_date('2019-06-01', 'YYYY-MM-DD')"

# Do the extract using the usual dbGetQuery (from odbc)
tic()
simple_1_extract <- dbGetQuery(SMRA_connection, sql)
toc()

# Use dbplyr
# Note we have to use upper case variable names
simple_2_query <- tbl(SMRA_connection, "SMR01_PI") %>%
  select(LINK_NO, ADMISSION_DATE, DISCHARGE_DATE) %>%
  filter(DISCHARGE_DATE >= To_date("2019-06-01", "YYYY-MM-DD"))

# This will print the 'translated' SQL for us to see
simple_2_query %>% show_query()

# Up until this point we haven't actually got the data
tic()
simple_2_extract <- collect(simple_2_query)
toc()

# Let's make sure the extracts are really identical
all_equal(
  simple_1_extract,
  simple_2_extract,
  ignore_col_order = FALSE,
  ignore_row_order = FALSE
)
