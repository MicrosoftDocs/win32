---
Description: If the data source is a log file, you can specify a time range for the query.
ms.assetid: 8d9c3e96-3645-4875-9b5f-a6c9ddf23ec3
title: Setting a Time Range for a Query
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting a Time Range for a Query

If the data source is a log file, you can specify a time range for the query. The query retrieves counter data from the log file that was collected during the specified time range. To set the time range, call the [**PdhSetQueryTimeRange**](/windows/win32/Pdh/nf-pdh-pdhsetquerytimerange?branch=master) function. **PdhSetQueryTimeRange** is not used to query performance data from real time data sources.

To create time value, use the following steps.

1.  Allocate a [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure and initialize the fields with the desired time value.
2.  Call [**SystemTimeToFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724948) to convert the [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure time value to a [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284) structure time.
3.  Cast the [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284) structure as a LONGLONG variable, keeping in mind the structure member padding conventions of your platform and compiler.
4.  Copy the LONGLONG value to the appropriate field in the [**PDH\_TIME\_INFO**](/windows/win32/Pdh/ns-pdh-_pdh_time_info?branch=master) structure.

To retrieve the time range of all of the performance data contained in a log file, call the [**PdhGetDataSourceTimeRange**](/windows/win32/Pdh/nf-pdh-pdhgetdatasourcetimerangea?branch=master) function.

 

 



