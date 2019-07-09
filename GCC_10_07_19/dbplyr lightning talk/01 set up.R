# Install libraries (if required)
install.packages("tidyverse") # Core Tidyverse includes many packages
install.packages("odbc") # Used for connecting to databases
install.packages("tictoc") # Simple timing
install.packages("dbplyr") # Needs to be installed

#  Load Libraries
library(odbc)
library(dplyr) # We only need to load dplyr (not dbplyr)
library(magrittr)

# Create a connection to SMRA
SMRA_connection <- odbc::dbConnect(
  drv = odbc::odbc(),
  dsn = "SMRA",
  uid = rstudioapi::showPrompt(title = "Username", message = "Username:"),
  pwd = rstudioapi::askForPassword("SMRA Password:"),
  encoding = "ASCII"
)

