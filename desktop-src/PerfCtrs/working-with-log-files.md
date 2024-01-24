---
description: To open a log file for reading, call PdhOpenQuery and specify a path to the log file.
ms.assetid: 1d8f8662-df1f-4f84-8b65-c152f79cc5c6
title: Working with Log Files
ms.topic: article
ms.date: 05/31/2018
---

# Working with Log Files

To open a log file for reading, call [**PdhOpenQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhopenquerya) and specify a path to the log file. To open a log file for writing, you must call [**PdhOpenLog**](/windows/desktop/api/Pdh/nf-pdh-pdhopenloga). To close a log file, call either [**PdhCloseQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhclosequery) or [**PdhCloseLog**](/windows/desktop/api/Pdh/nf-pdh-pdhcloselog) depending on which function you used to open the log file.

## Reading from a log file

Reading performance data from a log file is the same as reading data from a real time source—you open a query, add counters to the query and call [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata) to collect a sample from the log file. **PdhCollectQueryData** returns PDH\_NO\_MORE\_DATA when you reach the end of the log file.

Each sample in the log file contains a time stamp for when it was originally collected and written to the log file. To retrieve the time stamp for the first and last sample in the log file, call the [**PdhGetDataSourceTimeRange**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdatasourcetimerangea) function. If you want to limit the samples that you read from the log to a specific time range, see [Setting a Time Range for a Query](setting-a-time-range-for-a-query.md).

If you do not know which performance objects and counters exist in the log file, you can call [**PdhEnumObjects**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectsa) to determine the list of objects. Given an object, you can call either [**PdhEnumObjectItems**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectitemsa) or [**PdhExpandWildCardPath**](/windows/desktop/api/Pdh/nf-pdh-pdhexpandwildcardpatha) to retrieve a list of the object's instances and counters contained in the log file.

If you call [**PdhEnumObjectItems**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectitemsa), use the instance and counter lists to create a path for each possible combination of instance and counter. When you call [**PdhAddCounter**](/windows/desktop/api/Pdh/nf-pdh-pdhaddcountera) to add the counter to the query, the function will fail if the log file does not contain the given combination.

If you use [**PdhExpandWildCardPath**](/windows/desktop/api/Pdh/nf-pdh-pdhexpandwildcardpatha), you can create a path that contains a wildcard for the instance name and counter, for example, \\object(\*)\\\*. The function returns PDH\_INVALID\_PATH if the object does not contain an instance. In this case, call **PdhExpandWildCardPath** using a wildcard for counter only, for example, \\object\\\*.

Newer operating systems can read log files that were generated on older operating systems; however, log files that were created on Windows Vista and later operating systems cannot be read on earlier operating systems.

For an example that reads data from a log file, see [Reading Performance Data from a Log File](reading-performance-data-from-a-log-file.md).

## Reading from multiple log files

If you need to create a query that reads from several log files, call the [**PdhBindInputDataSource**](/windows/desktop/api/Pdh/nf-pdh-pdhbindinputdatasourcea) to bind the log files together. You then need to use PDH functions that end in 'H', for example, [**PdhOpenQueryH**](/windows/desktop/api/Pdh/nf-pdh-pdhopenqueryh).

## Writing to a log file

Before writing to a log file, call [**PdhOpenQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhopenquerya) to create a query and specify the source of the performance data, either real time data or a log file. Then, add the counters that you want to query.

To open the destination file, call [**PdhOpenLog**](/windows/desktop/api/Pdh/nf-pdh-pdhopenloga). Specify the query when you open the log file. To collect the performance data and write it to the log file, call [**PdhUpdateLog**](/windows/desktop/api/Pdh/nf-pdh-pdhupdateloga).

If the counter data is being written to comma-delimited (.csv) or tab-delimited (.tsv) log file and the path contains a wildcard instance, the path is expanded and only those instances that exist at the time the path is expanded are included in the log file. However, for binary (.blg) or SQL log files, the wildcard is not expanded so that the log file contains instances that are created during logging.

For an example that writes data to a log file, see [Writing Performance Data to a Log File](writing-performance-data-to-a-log-file.md).

## Compressing a log file

You can use the [**PdhComputeCounterStatistics**](/windows/desktop/api/Pdh/nf-pdh-pdhcomputecounterstatistics) function to compress a log file. For example, read ten records from a log file, call **PdhComputeCounterStatistics** to compute the mean value and then write the mean value to an output log file.

The following topic provides additional information on using a log file.

-   [Getting the Size of a Log File](getting-the-size-of-a-log-file.md)

 

 



