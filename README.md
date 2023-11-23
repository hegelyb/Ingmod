# ingmod.sh 

Ingmod.sh is a bash script that is designed to expand the capabilities of the Moodle teaching platform.
It allows multiple embedded (Cloze) questions to be specified, 
where the numbers for the numerical tasks are generated, 
the multiple choice questions are latex-based, and the appearance of the multiple answers questions are fully random. 

INSTALLATION

The ingmod.sh script should be found in your PATH environment variable, and the script must be
executed where the auxiliary files are located.

USAGE

In the working directory, the following files must be present:
*.xmltemp -- an xml template file
*.py -- a python calculation script
*.param -- the file which contains the parameter range for the python script
*.ingmod -- the control file of the ingmod.sh program

For more details, please type

ingmod.sh --help  

and see the attached samples.
