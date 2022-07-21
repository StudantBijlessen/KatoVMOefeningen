# Assignment

You are given a .csv file containing information about traffic violations, more specifically speeding violations.
Every entry contains

* The date and time of the violation.
* The license plate of the offender.
* The speed measured by the speed camera.
* The address where the violation occurred.

Each violation results in a fine, which is computed as follows: for every km/h above 120, an additional euro is added.
For example,

* Driving 130 km/h results in a fine of 10 euros.
* Driving 200 km/h results in a fine of 80 euros.

An offender can have multiple violations.
You will have to determine the total fine for each individual offender.

Write your results to `output.txt` as follows:

* Each line corresponds to a single offender.
* A line contains the offender's license plate followed by a space, followed by the total fine.
* The lines are sorted in order of increasing fines.
  If two offenders have the same total fine, order them alphabetically by license plate (i.e., the default sorting order on strings).

## Example

Say the csv file contains the following data

```text
date,license_plate,speed,address
2019-11-21 02:36:03,67-PX78,147,Some place X
2019-03-09 23:26:59,RNM 384,201,Some place Y
2022-04-12 13:59:19,67-PX78,145,Some place Z
2010-04-12 16:03:01,BAD-661,201,Some other place
```

Here we have three offenders:

* `67-PX78` has been caught twice, once driving 147 km/h, once 145 km/h. The total fine should be 27+25=52 euros.
* `RNM 384` has been seen driving 201 km/h, so he will be fined 81 euro.
* `BAD-661` drove exactly the same speed as the previous offender.

We generate our report:

```text
67-PX78 52
BAD-661 81
RNM 384 81
```

Note that

* The lines are ordered in increasing order of fines.
* Because `BAD-661` and `RNM 384` have equal fines to pay, we order the lines by license plate.

## Hint

* Make sure to use an existing csv parser. Don't try to read the data in yourself.
* You might want to look up how to sort by two keys.
