# water-quality-turbidity

(Water quality from turbidity measurements)

This is a JSON file I/O test program.
We assess water quality from example turbidity measurements stored in a JSON file located ![here](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json).

The input data has the following format:

```
{
  "turbidity_data": [
   {
     "datetime": "2022-02-01 00:00",
     "sample_volume": 1.19,
     "calibration_constant": 1.022,
     "detector_current": 1.137,
     "analyzed_by": "C. Milligan"
   },
   {
     "datetime": "2022-02-01 01:00",
     "sample_volume": 1.15,
     "calibration_constant": 0.975,
     "detector_current": 1.141,
     "analyzed_by": "C. Milligan"
   },
 ... etc
```

- .gitignore: ignores any downloaded .json files
#### water.py
- calculate and print current water status and minimum required treatment time using a moving average window of 5 samples.
-  We calculate turbidity via the following equation    
 ```
 T = a0 * I90
 T = Turbidity in NTU Units (0 – 40)
 a0 = Calibration constant
 I90 = Ninety degree detector current
 ```
-  We calculate minimum required time for safe water via the following inequality    
 ```
 Ts > T0(1-d)**b
 Ts = Turbidity threshold for safe water
 T0 = Current turbidity
 d = decay factor per hour, expressed as a decimal
 b = hours elapsed
 ```
#### test_water.py
- tests the water program functions.

## Install:
Make sure to install pytest: `pip3 install --user pytest`.

## Run (via terminal):

Linux	: `python3 water.py` and/or `pytest`  
Windows	: `py water.py` and/or `pytest`

- If you do not have `wget` on your system, the JSON file linked above must be downloaded to `turbidity_data.json` in the same directory (use `Right-Click` and `Save As`).  
Otherwise, the program will autodownload the file using `wget`.  
- Note we assume `turbidity_data.json` is a static file for some of the tests (the file needs to be unchanged so the values can be checked).
## Example Output

#### water.py:  
```
Average turbidity based on most recent five measurements = 1.1544952000000002 NTU
WARNING:root:Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 7.111086148101843 hours
```
- If you have safe water, the program may output a message like the below:  
```
Average turbidity based on most recent five measurements = 0.9852 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours
```

#### tester:  
- Any tester output without an `AssertionError` is valid.

Please note this program only supports Python3, so the Windows command depends on your installation and aliases.