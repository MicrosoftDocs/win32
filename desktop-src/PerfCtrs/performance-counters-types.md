---
Description: 'PDH defines the following data types.'
ms.assetid: '8a2e8683-502a-4893-8b4f-5e2cf464a933'
title: Performance Counters Data Types
---

# Performance Counters Data Types

PDH defines the following data types.



| Data type         | Description                                                                                                                                                                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PDH\_HQUERY**   | Handle to a query. The [**PdhOpenQuery**](pdhopenquery.md) function returns this handle.                                                                                                                                                                            |
| **PDH\_HCOUNTER** | Handle to a counter. The [**PdhAddCounter**](pdhaddcounter.md) function returns this handle. PDH maintains the linkage between counters and queries.                                                                                                                |
| **PDH\_HLOG**     | Handle to a log file. The [**PdhOpenLog**](pdhopenlog.md) and [**PdhBindInputDataSource**](pdhbindinputdatasource.md) functions return this handle.                                                                                                                |
| **PDH\_STATUS**   | PDH status value. All PDH functions return a value of type **PDH\_STATUS**. If the function succeeds, the return value is ERROR\_SUCCESS. Otherwise, the function returns a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381) or a [PDH error code](pdh-error-codes.md). |



 

 

 



