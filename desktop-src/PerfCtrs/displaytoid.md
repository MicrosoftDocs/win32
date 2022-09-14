---
description: The DisplayToID table relates the user-friendly string displayed by the System Monitor to the GUID stored in the other tables.
ms.assetid: 414d16f1-ab6f-45f0-9287-154810543a6d
title: DisplayToID
ms.topic: article
ms.date: 05/31/2018
---

# DisplayToID

The **DisplayToID** table relates the user-friendly string displayed by the System Monitor to the GUID stored in the other tables.

The **DisplayToID** table defines the following fields:

-   **GUID:** Unique identifier generated for a log. This field is the primary key of this table.
-   **RunID:** Reserved for internal use.
-   **DisplayString:** Name of the log file as displayed in the System Monitor.
-   **LogStartTime:** Time the logging process started in yyyy-mm-dd hh:mm:ss:nnn format.
-   **LogStopTime:** Time the logging process stopped in yyyy-mm-dd hh:mm:ss:nnn format. Multiple log files with the same **DisplayString** value can be differentiated by using the value in this and the **LogStartTime** fields. The values in the **LogStartTime** and **LogStopTime** fields also allows the total collection time to be accessed quickly.
-   **NumberOfRecords:** Number of samples stored in the table for each log collection.
-   **MinutesToUTC:** Value used to convert the row data stored in UTC time to local time.
-   **TimeZoneName:** Name of the time zone where the data was collected. If you are collecting or have relogged data from a file collected on systems in your own time zone, this field will state the location.

**Note**  Prior to Windows Vista, the data collector sets were stored in the registry at

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SysmonLog\\Log Queries**

. The fields listed above do not correspond to the values in registry. For Windows Vista, the data collector sets are not stored in the registry.

 

 



