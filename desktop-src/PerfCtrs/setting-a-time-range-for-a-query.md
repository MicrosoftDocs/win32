---
description: If the data source is a log file, you can specify a time range for the query.
ms.assetid: 8d9c3e96-3645-4875-9b5f-a6c9ddf23ec3
title: Setting a Time Range for a Query
ms.topic: article
ms.date: 05/31/2018
---

# Setting a Time Range for a Query

If the data source is a log file, you can specify a time range for the query. The query retrieves counter data from the log file that was collected during the specified time range. To set the time range, call the [**PdhSetQueryTimeRange**](/windows/desktop/api/Pdh/nf-pdh-pdhsetquerytimerange) function. **PdhSetQueryTimeRange** is not used to query performance data from real time data sources.

To create time value, use the following steps.

1.  Allocate a [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure and initialize the fields with the desired time value.
2.  Call [**SystemTimeToFileTime**](/windows/desktop/api/timezoneapi/nf-timezoneapi-systemtimetofiletime) to convert the [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure time value to a [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) structure time.
3.  Cast the [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) structure as a LONGLONG variable, keeping in mind the structure member padding conventions of your platform and compiler.
4.  Copy the LONGLONG value to the appropriate field in the [**PDH\_TIME\_INFO**](/windows/desktop/api/Pdh/ns-pdh-pdh_time_info) structure.

To retrieve the time range of all of the performance data contained in a log file, call the [**PdhGetDataSourceTimeRange**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdatasourcetimerangea) function.

 

 
