@echo off
::Discovery alerts service
::
::This script needs to be set to run on schedule by Windows Task Scheduler.
::You should ensure that the machine where the scheduler is set up is turned on during scheduled hours.
::It's a good idea to have a second, back-up machine that runs the script it hadn't been run already
::
::You need to set up the scheduler with space-separated parameters for username and password to the mailbox.
::
::The script outputs its logs into its working directory.
::
::If you have a virtual environment setup (as you probably should),
::replace "alerts" in "call activate alerts" with the name of your environment
::
::Amend the pushd command to the root folder with your code
::
echo Script started
call activate alerts
echo Virtual environment activated
pushd "C:\Users\germap01\Python\UNSORTED\GCC Demo\GCC_2019_10_16"
python simulate_email_burst.py %1 %2
echo Script finished. Press enter to exit...
set /p input=
popd