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


## FAQ

* Q: When running the automatic install / main Python file, the program fails to patch Overwolf
    * A: You're probably aren't running the Python script with admin permissions, rerun with admin permissions or use the Powershell autoinstall and hit yes when prompted to give appropriate permissions

* Q: Overwolf doesn't run after running automatic install
    * A: The replaced .dll has probably broken Overwolf, i.e Overwolf has updated to a newer version and this is out of data, please open an issue

* Q: Porofessor doesn't run after running automatic install
    * Overwolf is probably detecting that the files have changed, i.e Overwolf has updated and is running a new, unpatched `Overwolf.Extensions.dll` file, please open an issue

## Disclaimer

Using this is against Overwolf's and Porofessor's terms of services. I am not responsible nor liable for what happens should you use this software, you have been warned.