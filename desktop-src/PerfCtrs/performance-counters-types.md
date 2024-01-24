---
description: PDH defines the following data types.
ms.assetid: 8a2e8683-502a-4893-8b4f-5e2cf464a933
title: Performance Counters Data Types
ms.topic: article
ms.date: 05/31/2018
---

# Performance Counters Data Types

## Performance Data Helper (PDH) types

Consumers that use the [Performance Data Helper (PDH)](using-the-pdh-functions-to-consume-counter-data.md) functions use the following types:

| Data type | Description
|-----------|------------
| **PDH\_HQUERY**   | Handle to a query. The [**PdhOpenQuery**](/windows/win32/api/pdh/nf-pdh-pdhopenqueryw) function returns this handle. Close the handle using [**PdhCloseQuery**](/windows/win32/api/pdh/nf-pdh-pdhclosequery).
| **PDH\_HCOUNTER** | Handle to a counter. The [**PdhAddCounter**](/windows/win32/api/pdh/nf-pdh-pdhaddcounterw) function returns this handle. Close the handle using [**PdhRemoveCounter**](/windows/win32/api/pdh/nf-pdh-pdhremovecounter) or by closing the handle to the query that contains the counter. Do not call **PdhRemoveCounter** on a counter if the corresponding query has already been closed. PDH maintains the linkage between counters and queries and will automatically close counter handles when the corresponding query handle is closed.
| **PDH\_HLOG**     | Handle to a log file. The [**PdhOpenLog**](/windows/desktop/api/Pdh/nf-pdh-pdhopenloga) and [**PdhBindInputDataSource**](/windows/desktop/api/Pdh/nf-pdh-pdhbindinputdatasourcea) functions return this handle. Close the handle using [**PdhCloseLog**](/windows/win32/api/pdh/nf-pdh-pdhcloselog).
| **PDH\_STATUS**   | PDH status value. All PDH functions return a value of type **PDH\_STATUS**. If the function succeeds, the return value is ERROR\_SUCCESS. Otherwise, the function returns a [system error code](/windows/desktop/Debug/system-error-codes) or a [PDH error code](pdh-error-codes.md).
