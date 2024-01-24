---
description: Applications can use PDH to extract performance counters from SQL logs, or they can extract formatted or raw counters directly from the database through SQL queries.
ms.assetid: 89515dd9-2d65-4b19-bb7a-ef9e7d146caa
title: SQL Log File Schema
ms.topic: article
ms.date: 08/17/2020
---

# SQL Log File Schema

> [!IMPORTANT]
> PDH support for ODBC SQL databases may be altered or unavailable in the future.

Applications can use PDH APIs read and write performance counter data in compatible ODBC SQL databases and then perform further processing through SQL queries. This section describes the SQL schema used to store performance counters. You can use this information to create custom views and reports. The schema consists of the following three tables:

- [**CounterData**](counterdata.md)
- [**CounterDetails**](counterdetails.md)
- [**DisplayToID**](displaytoid.md)

> [!NOTE]
> PDH support for ODBC SQL databases only works with ODBC SQL drivers that support [Bulk Copy (BCP) Extensions](/sql/relational-databases/native-client-odbc-extensions-bulk-copy-functions/sql-server-driver-extensions-bulk-copy-functions).
