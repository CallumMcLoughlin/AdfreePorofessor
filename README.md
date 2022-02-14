# AdfreePorofessor

Patcher for Porofessor to remove ads from the client

## Getting Started

### Dependencies

* [Python](https://www.python.org/)
    * 3.7+ 
* Overwolf 
    * v0.190.0.13 (Untested on different versions, might work for any)
* Porofessor 
    * v2.7.141 (Untested on different versions, should work for any)


### Installing

* Clone/download repository
* Change `config/config.json` file if using custom install directories
* Rightclick and run `autoinstall.ps1` with Powershell from the base of the repo
    * Alternatively run `src/main.py` with Python as admin 


#### Manual Install

* Copy over and replace `bin/Overwolf.Extensions.dll` to Overwolf's install location
* Edit Porofessor .html files to remove embedded ads


### Uninstalling

* Currently no backups of existing files are taken, to uninstall you will need to reinstall Porofessor and Overwolf


## FAQ

* Q: When running the automatic install / main Python file, the program fails to patch Overwolf
    * A: You probably aren't running the Python script with admin permissions, rerun with admin permissions or use the Powershell autoinstall and hit yes when prompted to give appropriate permissions

* Q: Overwolf doesn't run after running automatic install
    * A: The replaced .dll has probably broken Overwolf, i.e Overwolf has updated to a newer version and this is out of data, please open an issue and reinstall Overwolf

* Q: Porofessor doesn't run after running automatic install
    * A: Overwolf is probably detecting that the files have changed, i.e Overwolf has updated and is running a new, unpatched `Overwolf.Extensions.dll` file, please open an issue and reinstall Porofessor

* Q: Do I need to reinstall Porofessor/Overwolf to remove these changes?
    * A: Yes, however if Porofessor/Overwolf updates, these changes will be removed anyways
    
* Q: Porofessor has updated, what do I do?
    * A: Rerun the `autoinstall.ps1` script, provided they haven't changed too much this will still patch the newer version


## Disclaimer

Using this is against Overwolf's and Porofessor's terms of services. I am not responsible nor liable for what happens should you use this software, you have been warned.
