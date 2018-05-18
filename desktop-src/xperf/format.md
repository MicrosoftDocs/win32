---
title: format
description: Displays time and timespan formats on the command line.
ms.assetid: '12628b72-e8a5-4bca-a282-c80184bcb5e3'
keywords: ["format Windows Performance Analyzer"]
topic_type:
- apiref
api_name:
- format
api_type:
- NA
---

# format

Displays time and timespan formats on the command line.

``` syntax
format
```

### Comments

Various xperf actions support options that take time and timespan parameters.

Time parameters are usually taken by -range options. Time can be read in one of the following formats:



|                                                              |                                                                                                                                                                                                                |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1234\[s\|ms\|us\|ns\] <br/>                            | 1234 \[seconds\|milliseconds\|microseconds\|nanoseconds\] since start of the trace file.<br/> Default unit: us \[microseconds\]<br/>                                                               |
| 2004/12/04:20:05:20.1234\[+UTC\] Wall clock time.<br/> | All date and time components are mandatory except for the timezone. If no timezone is specified, time is assumed to be in the local timezone. (This is also the time format used by -a tracestats.)<br/> |



 

> [!Note]  
> Only local timezone and UTC are currently supported.

 

Timespan parameters are usually taken by options accepting resolutions. Timespans can be read in one of the following formats:



|                                   |                                                                                                                    |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|
| 1234\[s\|ms\|us\|ns\] <br/> | 1234 \[seconds\|milliseconds\|microseconds\|nanoseconds\]<br/> Default unit: us \[microseconds\].<br/> |
| 20:05:20.1234 <br/>         | 20h 05min 20sec 123.4 milliseconds. All time components are mandatory.<br/>                                  |



 

> [!Note]  
> Event timestamps in the xperf trace dump are always presented in microseconds.

 

 

 





