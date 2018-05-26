---
Description: PDH defines the following data types.
ms.assetid: 8a2e8683-502a-4893-8b4f-5e2cf464a933
title: Performance Counters Data Types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Performance Counters Data Types

PDH defines the following data types.



| Data type         | Description                                                                                                                                                                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PDH\_HQUERY**   | Handle to a query. The [**PdhOpenQuery**](/windows/win32/Pdh/nf-pdh-pdhopenquerya?branch=master) function returns this handle.                                                                                                                                                                            |
| **PDH\_HCOUNTER** | Handle to a counter. The [**PdhAddCounter**](/windows/win32/Pdh/nf-pdh-pdhaddcountera?branch=master) function returns this handle. PDH maintains the linkage between counters and queries.                                                                                                                |
| **PDH\_HLOG**     | Handle to a log file. The [**PdhOpenLog**](/windows/win32/Pdh/nf-pdh-pdhopenloga?branch=master) and [**PdhBindInputDataSource**](/windows/win32/Pdh/nf-pdh-pdhbindinputdatasourcea?branch=master) functions return this handle.                                                                                                                |
| **PDH\_STATUS**   | PDH status value. All PDH functions return a value of type **PDH\_STATUS**. If the function succeeds, the return value is ERROR\_SUCCESS. Otherwise, the function returns a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381) or a [PDH error code](pdh-error-codes.md). |



 

 

 



