1. Create a new directory on your local desktop or on bucknell's linux remote server and enter that new  directory.
2. Open a terminal
3. Run the command git clone https://github.com/DerekAK/DNA_Sequencing.git. Also git pull to pull any recent changes in case this step is staggered.
4. If running from your local desktop, you need to install flask if not already installed either on your entire desktop or just in a local environment. You can run pip list to see if you have it installed already or flask --version. If not installed, you can either install it on your global environment and run pip install flask or create a new python environment using pipenv shell and then running pipenv install flask.
5. Run the command python3 app.py, and two ip addresses should appear in the terminal
6. If running from your local desktop, you can open either of the ip addresses in a web browser (either localhost (http://127.0.0.1:5001) or the public ip address). It's configured to run on port 5001, but if this port is being used on your computer you can change the port in app.py under main.
7. If running from a linux machine, you can only open the public ip address.
8. In the UI, choose an algorithm to run, choose your two DNA files, and click Run Algorithm to run the program
9. A result should appear on the UI, but the terminal will print out additional information on each of the sequences being compared to the query sequence
10. Read the report.txt file for runtime analyses of each of our 4 algorithms