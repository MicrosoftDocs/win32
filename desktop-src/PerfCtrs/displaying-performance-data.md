---
description: Most counters require two sample values in order to compute a displayable value.
ms.assetid: 75e45baf-51c5-400c-a31f-92bdab4ee492
title: Displaying Performance Data
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Performance Data

Most counters require two sample values in order to compute a displayable value. The formula for each counter determines if the counter requires two samples. For a list of counters and their formulas, see the Counter Types section of the [Windows Server 2003 Deployment Kit](/previous-versions/windows/it-pro/windows-server-2003/cc776490(v=ws.10)).

[Collecting Performance Data](collecting-performance-data.md) shows how to retrieve sample data. Once you have the samples, you typically call [**PdhGetFormattedCounterValue**](/windows/desktop/api/Pdh/nf-pdh-pdhgetformattedcountervalue) to calculate a displayable value.

If you need to scale the counter value up or down in order to display the value, call the [**PdhSetCounterScaleFactor**](/windows/desktop/api/Pdh/nf-pdh-pdhsetcounterscalefactor) function before calling [**PdhGetFormattedCounterValue**](/windows/desktop/api/Pdh/nf-pdh-pdhgetformattedcountervalue). Counter values can be scaled by a power of ten from a factor of -7 to 7.

If the counter path contains a wildcard character for the instance name, call [**PdhGetFormattedCounterArray**](/windows/desktop/api/Pdh/nf-pdh-pdhgetformattedcounterarraya) to retrieve an array of formatted counter values for each instance collected.

You can also use the [**PdhCalculateCounterFromRawValue**](/windows/desktop/api/Pdh/nf-pdh-pdhcalculatecounterfromrawvalue) and [**PdhFormatFromRawValue**](/windows/desktop/api/Pdh/nf-pdh-pdhformatfromrawvalue) functions to compute a displayable value. To use these functions, you must retrieve the collected sample after each [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata) call and store the sample yourself. To retrieve the sample, call the [**PdhGetRawCounterValue**](/windows/desktop/api/Pdh/nf-pdh-pdhgetrawcountervalue) or [**PdhGetRawCounterArray**](/windows/desktop/api/Pdh/nf-pdh-pdhgetrawcounterarraya) function. For time-based counter values, call [**PdhGetCounterTimeBase**](/windows/desktop/api/Pdh/nf-pdh-pdhgetcountertimebase) before **PdhFormatFromRawValue** to retrieve the counter's time base.

If you perform calculations using the raw data, always check the **CStatus** member of the [**PDH\_RAW\_COUNTER**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter) structure before using the sample. The sample is not valid if the value of **CStatus** is not PDH\_CSTATUS\_NEW\_DATA or PDH\_CSTATUS\_VALID\_DATA.

## Displaying statistics for a counter

If you want to compute the minimum, maximum, and mean values of a counter, call the [**PdhComputeCounterStatistics**](/windows/desktop/api/Pdh/nf-pdh-pdhcomputecounterstatistics) function. When you collect samples, store the [**PDH\_RAW\_COUNTER**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter) structures in an array that you pass to **PdhComputeCounterStatistics**. The function returns the statistical values in a [**PDH\_STATISTICS**](/windows/desktop/api/Pdh/ns-pdh-pdh_statistics) structure.

You can also use this function to compress a log file. For example, read ten records from a log file, call [**PdhComputeCounterStatistics**](/windows/desktop/api/Pdh/nf-pdh-pdhcomputecounterstatistics) to compute the mean value and then write the mean value to an output log file.

 

 
