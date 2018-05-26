---
Description: To create a new query that collects performance data from a real-time source or log file, call the PdhOpenQuery function. The function returns a handle to the query that you use in subsequent PDH function calls.
ms.assetid: 6fd4716e-b163-47a3-b0cb-5f9599f8681f
title: Creating a Query
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a Query

To create a new query that collects performance data from a real-time source or log file, call the [**PdhOpenQuery**](/windows/win32/Pdh/nf-pdh-pdhopenquerya?branch=master) function. The function returns a handle to the query that you use in subsequent PDH function calls.

After creating the query, call the [**PdhAddCounter**](/windows/win32/Pdh/nf-pdh-pdhaddcountera?branch=master) function for each counter that you want to add to the query. You can use one of the following methods to provide the fully qualified counter path.

-   Define the counter path as a static string. Use this method if you always monitor the same counter, and if you are familiar with the correct syntax of a counter path. For information on the correct syntax used to specify a counter, see [Specifying a Counter Path](specifying-a-counter-path.md).
-   Initialize a [**PDH\_COUNTER\_PATH\_ELEMENTS**](/windows/win32/Pdh/ns-pdh-_pdh_counter_path_elements_a?branch=master) structure with the names of the computer, object, counter, and instance. Pass this structure to [**PdhMakeCounterPath**](/windows/win32/Pdh/nf-pdh-pdhmakecounterpatha?branch=master) which will return a counter path for the specified elements.
-   Specify a counter path that contains wildcard characters and call [**PdhExpandWildCardPath**](/windows/win32/Pdh/nf-pdh-pdhexpandwildcardpatha?branch=master) to get a list of counter names that match the wildcard characters in the path. Scan through the list of counter names and add to the query the counters that you want from this list.
-   Call the [**PdhBrowseCounters**](/windows/win32/Pdh/nf-pdh-pdhbrowsecountersa?branch=master) function to display a dialog box that lets the user browse and select performance counters. For more information, see [Browsing Counters](browsing-counters.md).

Note that if a counter instance is specified that does not exist, [**PdhAddCounter**](/windows/win32/Pdh/nf-pdh-pdhaddcountera?branch=master) does not report an error condition. Instead, it returns ERROR\_SUCCESS. The reason for this behavior is that it is not known if a nonexistent counter instance has been specified or one that will exist but has not yet been created.

The missing counter instance will be reported by either [**PdhCollectQueryData**](/windows/win32/Pdh/nf-pdh-pdhcollectquerydata?branch=master), [**PdhGetRawCounterValue**](/windows/win32/Pdh/nf-pdh-pdhgetrawcountervalue?branch=master), or [**PdhGetFormattedCounterValue**](/windows/win32/Pdh/nf-pdh-pdhgetformattedcountervalue?branch=master). When calling **PdhCollectQueryData** for one counter instance only, and the counter instance still does not exist, it is assumed that the counter instance will not exist and the function returns PDH\_NO\_DATA. However, if more than one counter is queried, **PdhCollectQueryData** may still return ERROR\_SUCCESS even if one of the counter instances does not yet exist. In this case, call **PdhGetRawCounterValue** or **PdhGetFormattedCounterValue** for each of the counter instances of interest. If the instance does not exist when calling **PdhGetRawCounterValue**, the function returns ERROR\_SUCCESS and sets the **CStatus** member of [**PDH\_RAW\_COUNTER**](/windows/win32/Pdh/ns-pdh-_pdh_raw_counter?branch=master) to PDH\_STATUS\_NO\_INSTANCE. If the instance does not exist when calling **PdhGetFormattedCounterValue**, the function returns PDH\_INVALID\_DATA and sets the **CStatus** member of the [**PDH\_FMT\_COUNTERVALUE**](/windows/win32/Pdh/ns-pdh-_pdh_fmt_countervalue?branch=master) to PDH\_CSTATUS\_NO\_INSTANCE.

Note that the counter path specified in the [**PdhAddCounter**](/windows/win32/Pdh/nf-pdh-pdhaddcountera?branch=master) function must be localized. The [**PdhAddEnglishCounter**](/windows/win32/Pdh/nf-pdh-pdhaddenglishcountera?branch=master) function provides a locale-neutral way to add performance counters to the query. This function is the recommended way to add locale-neutral counters to a query.

To remove a counter from a query, call the [**PdhRemoveCounter**](/windows/win32/Pdh/nf-pdh-pdhremovecounter?branch=master) function.

After you finish collecting data for a query, call the [**PdhCloseQuery**](/windows/win32/Pdh/nf-pdh-pdhclosequery?branch=master) function to close the query and release all allocated system resources. **PdhCloseQuery** closes all counter handles associated with the query.

 

 



