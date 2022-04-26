So basically this whole thing is the most basic flask app we can make it 
doesn't require a lot of overhead and if you have to run each of the commands
as RUN in a dockerfile it should't be too much of a problem 
this whole thing is set up on windows so a few things to keep in mind:
 
    1. the shell scripts (*.ps1) are for power shell we'll need to update them for linux
 
    2. we assume we already have python installed as "python" and pip set up as a package manager
 
    3. flask normally uses port 5000 I explicitly said it here so that you can see where to change it.
 
 so to get started:
 
 1. first make sure you are set up with appropriate requirements as stated above.
 
 2. next open this folder in power shell
 
 3. run ".\Run_First.ps1"
 
 4. open a new power shell tab or window and navigate to this folder again
 
 5. run ".\test_ping.ps1"