#  Load Libraries
library(odbc)
library(dplyr) # We only need to load dplyr
library(magrittr)
library(tidylog)

# Create a connection to SMRA
SMRA_connection <- odbc::dbConnect(
  drv = odbc::odbc(),
  dsn = "SMRA",
  uid = rstudioapi::showPrompt(title = "Username", message = "Username:"),
  pwd = rstudioapi::askForPassword("SMRA Password:"),
  encoding = "ASCII"
)

