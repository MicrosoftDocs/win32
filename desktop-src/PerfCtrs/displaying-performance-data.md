---
Description: Most counters require two sample values in order to compute a displayable value.
ms.assetid: 75e45baf-51c5-400c-a31f-92bdab4ee492
title: Displaying Performance Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Displaying Performance Data

Most counters require two sample values in order to compute a displayable value. The formula for each counter determines if the counter requires two samples. For a list of counters and their formulas, see the Counter Types section of the [Windows Server 2003 Deployment Kit](Http://go.microsoft.com/fwlink/p/?linkid=84422).

[Collecting Performance Data](collecting-performance-data.md) shows how to retrieve sample data. Once you have the samples, you typically call [**PdhGetFormattedCounterValue**](/windows/win32/Pdh/nf-pdh-pdhgetformattedcountervalue?branch=master) to calculate a displayable value.

If you need to scale the counter value up or down in order to display the value, call the [**PdhSetCounterScaleFactor**](/windows/win32/Pdh/nf-pdh-pdhsetcounterscalefactor?branch=master) function before calling [**PdhGetFormattedCounterValue**](/windows/win32/Pdh/nf-pdh-pdhgetformattedcountervalue?branch=master). Counter values can be scaled by a power of ten from a factor of -7 to 7.

If the counter path contains a wildcard character for the instance name, call [**PdhGetFormattedCounterArray**](/windows/win32/Pdh/nf-pdh-pdhgetformattedcounterarraya?branch=master) to retrieve an array of formatted counter values for each instance collected.

You can also use the [**PdhCalculateCounterFromRawValue**](/windows/win32/Pdh/nf-pdh-pdhcalculatecounterfromrawvalue?branch=master) and [**PdhFormatFromRawValue**](/windows/win32/Pdh/nf-pdh-pdhformatfromrawvalue?branch=master) functions to compute a displayable value. To use these functions, you must retrieve the collected sample after each [**PdhCollectQueryData**](/windows/win32/Pdh/nf-pdh-pdhcollectquerydata?branch=master) call and store the sample yourself. To retrieve the sample, call the [**PdhGetRawCounterValue**](/windows/win32/Pdh/nf-pdh-pdhgetrawcountervalue?branch=master) or [**PdhGetRawCounterArray**](/windows/win32/Pdh/nf-pdh-pdhgetrawcounterarraya?branch=master) function. For time-based counter values, call [**PdhGetCounterTimeBase**](/windows/win32/Pdh/nf-pdh-pdhgetcountertimebase?branch=master) before **PdhFormatFromRawValue** to retrieve the counter's time base.

If you perform calculations using the raw data, always check the **CStatus** member of the [**PDH\_RAW\_COUNTER**](/windows/win32/Pdh/ns-pdh-_pdh_raw_counter?branch=master) structure before using the sample. The sample is not valid if the value of **CStatus** is not PDH\_CSTATUS\_NEW\_DATA or PDH\_CSTATUS\_VALID\_DATA.

## Displaying statistics for a counter

If you want to compute the minimum, maximum, and mean values of a counter, call the [**PdhComputeCounterStatistics**](/windows/win32/Pdh/nf-pdh-pdhcomputecounterstatistics?branch=master) function. When you collect samples, store the [**PDH\_RAW\_COUNTER**](/windows/win32/Pdh/ns-pdh-_pdh_raw_counter?branch=master) structures in an array that you pass to **PdhComputeCounterStatistics**. The function returns the statistical values in a [**PDH\_STATISTICS**](/windows/win32/Pdh/ns-pdh-_pdh_statistics?branch=master) structure.

You can also use this function to compress a log file. For example, read ten records from a log file, call [**PdhComputeCounterStatistics**](/windows/win32/Pdh/nf-pdh-pdhcomputecounterstatistics?branch=master) to compute the mean value and then write the mean value to an output log file.

 

 



