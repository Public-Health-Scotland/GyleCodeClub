# Doing more complicated extracts

# Set up a deaths extract
# For some reason need to use in_schema()
deaths <-
  tbl(
    SMRA_connection,
    dbplyr::in_schema("ANALYSIS", "GRO_DEATHS_C")
  ) %>%
  select(LINK_NO, DATE_OF_DEATH) %>%
  filter(DATE_OF_DEATH >= To_date("2019-06-01", "YYYY-MM-DD"))

# Use colnames to check variable names
colnames(tbl(
  SMRA_connection,
  dbplyr::in_schema("ANALYSIS", "GRO_DEATHS_C")
))

# See what the SQL looks like
deaths %>% show_query()

# Set up a simple SMR01 extract (same as in the previous example)
simple_SMR01 <- tbl(SMRA_connection, "SMR01_PI") %>%
  select(LINK_NO, ADMISSION_DATE, DISCHARGE_DATE) %>%
  filter(DISCHARGE_DATE >= To_date("2019-06-01", "YYYY-MM-DD"))

# Do a link using dplyr joins
# Alternative is (getting) complicated SQL
# Or extract separately and then join which is to be avoided!
linked_1_query <- simple_SMR01 %>% inner_join(deaths)

# We could probably write some slightly better SQL but not as easily!
linked_1_query %>% show_query()

# Do the extract
linked_1_extract <- collect(linked_1_query)

# The larger the extracts the faster this method is compared to joining separate extracts

# This is easily extended to multiple links, for example by including SMR04
simple_SMR04 <- tbl(SMRA_connection, "SMR04_PI") %>%
  select(LINK_NO, ADMISSION_DATE, DISCHARGE_DATE) %>%
  # Pick a recent date for the example
  filter(DISCHARGE_DATE >= To_date("2020-05-01", "YYYY-MM-DD"))

# Do a full join on the SMR01 and 04 data
linked_2_extract <- simple_SMR01 %>%
  # Flag where the data has come from
  mutate(source = "SMR01") %>%
  full_join(simple_SMR04 %>%
    mutate(source = "SMR04")) %>%
  # Inner join the deaths so we're left with only people who have died
  inner_join(deaths) %>%
  # Until this point we don't actually have any data
  # We only have translated SQL
  collect()
