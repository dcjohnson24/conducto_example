# Conducto Pipeline Example
To run the sample pipeline, use 

```python
python pipeline.py --local
```
The pipeline downloads data from the [Fraser Experimental Forest Headquarters station daily precipitation data: 1976-2003](https://www.fs.usda.gov/rds/archive/catalog/RDS-2005-0004) and plots a timeseries in `pandas` with optional resampling frequencies.  

The options include `--path`, `--resample`, and `--save`. `--path` specifies the path to the data file. `--resample` gives the sampling frequency used by `pandas.DataFrame.resample` method such as 'M' or 'Q'. `--save` will save the plot as a .png file

A successful run looks something like this
![img][/img/conducto_run.png]

## Note
Running this on WSL Windows 10 Home Ubuntu 16.04 LTS will give the error 

```
conducto.internal.host_detection.WSLMapError: The context path /home/dylan/conducto_example is not on a Windows drive accessible to Docker.  All image contexts paths must resolve to a location on the Windows file system.
```

This is likely because Docker Desktop for Windows cannot be installed directly in Windows 10 Home and can only be used through Docker Toolbox that hosts Docker on a virtual machine (https://docs.docker.com/toolbox/toolbox_install_windows/)

As a result, I had to run this example on an Ubuntu server.
