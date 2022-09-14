---
description: After creating a query and adding counters to it, call the PdhCollectQueryData function to retrieve the current raw data for all counters in the query.
ms.assetid: 2534d387-a280-4716-9a9d-3e42f40e2f92
title: Collecting Performance Data
ms.topic: article
ms.date: 05/31/2018
---

# Collecting Performance Data

After [creating a query](creating-a-query.md) and adding counters to it, call the [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata) function to retrieve the current raw data for all counters in the query.

Many counters, such as rate counters, require two data samples to calculate a formatted data value. PDH maintains data for the current sample and the previously collected sample. The following procedure describes how to collect counter values that require two samples to calculate a displayable value.

**To collect counter values that require two samples to calculate a displayable value**

1.  Call [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata) to collect the first sample.
2.  Call the [**Sleep**](/windows/desktop/api/synchapi/nf-synchapi-sleep) function to wait a minimum of one second between collections.
3.  Call [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata) again to collect the second sample.
4.  Call the [**PdhGetFormattedCounterValue**](/windows/desktop/api/Pdh/nf-pdh-pdhgetformattedcountervalue) function to calculate a displayable value.
5.  Repeat steps 2 through 4.

As an alternative to implementing a wait period yourself, you can call the [**PdhCollectQueryDataEx**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydataex) function, which creates a timing thread that waits a specified amount of time, collects the sample, and then triggers an application-defined event.

If you want to query performance data from a log file, you can also define a time range. The time range limits the query to those samples that were collected within the time range (each sample contains a time stamp for when it was collected). For more information on how to set and retrieve time ranges, see [Setting a Time Range for a Query](setting-a-time-range-for-a-query.md).

If you want to collect performance data and write it to a log file, you would call the [**PdhUpdateLog**](/windows/desktop/api/Pdh/nf-pdh-pdhupdateloga) function instead of calling [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata). For details, see [Working with Log Files](working-with-log-files.md) and [Writing Performance Data to a Log File](writing-performance-data-to-a-log-file.md).

For details on calculating a displayable sample value, see [Displaying Performance Data](displaying-performance-data.md).

## Understanding Multiple Processor Counters

Some performance counters were designed for single processor systems and might not be accurate for multiprocessor computers. For example, a process is limited to 100 percent of a single processor; however, its threads can use several processors, totaling more than 100 percent.

The "\\Processor(\_Total)\\% Processor Time" counter value is the average usage of all processors. For example, if you have two processors, one at 100 percent and another at 0 percent, this counter will report 50 percent. So the range is from 0 through 100.

The "\\Process(X)\\% Process Time" counter value is the sum of the processor usage by all threads of process X. For example, in a computer with two processors, if a process has two threads, one taking up 75 percent of a CPU and the other taking 80 percent of another CPU, this counter will report 155 percent. The range for this counter is from 0 through 100 \* ProcessorCount.

When using the `Process` counterset,
you can receive values outside the expected range of values for CPU usage. To calculate the percentage of CPU usage, PDH needs two samples (each with a raw value and a time stamp). Because PDH uses only the instance name to match the processes, it can sometimes mix up samples from different processes. For example, if three processes with the same instance name are being sampled and one of the processes is terminated after the third sample, another process will move to the slot vacated by that terminated process. As a result, a formatted counter will provide an incorrect value when you format the fourth sample because it’s using the third sample from the terminated process and the fourth sample from the process that moved into the terminated process's slot.

The following table shows how this can occur if a process is terminated while data is being collected. The table shows five counter value samples for three instances of process X. The samples are collected in one second intervals. After the third sample is collected, process X in slot 1 is terminated. When process X in slot 1 is terminated, process X in slot 2 moves to slot 1. When you collect the fourth sample for process X in slot 2, the first value is now 20 instead of 1,000, and the second value is 1,500. When you format the counter value, you get 1,480 milliseconds instead of the expected 500 milliseconds. When you format the fifth sample value, you should get the expected value.

| Sample   | Slot 0 for process X | Slot 1 for process X           | Slot 2 for process X                     |
|----------|----------------------|--------------------------------|------------------------------------------|
| Sample 1 | 0                    | 0                              | 0                                        |
| Sample 2 | 20                   | 10                             | 500                                      |
| Sample 3 | 40                   | 20                             | 1,000                                    |
| Sample 4 | 60                   | 1,500 (from the former slot 2) | Not applicable. Now collected in slot 1. |
| Sample 5 | 80                   | 2,000                          | Not applicable. Now collected in slot 1. |

> [!TIP]
> Starting in Windows 10 20H2, you can avoid this issue by using the new `Process V2` counterset. The `Process V2` counterset includes the process ID in the instance name. This avoids the inconsistent results that appear with the original `Process` counterset.
