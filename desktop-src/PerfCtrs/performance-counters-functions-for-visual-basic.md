---
description: You can use the following functions to work with performance data in Visual Basic.
ms.assetid: c78eeb43-c713-42cc-a38f-f8aaa04f8dae
title: Performance Counters Functions for Visual Basic
ms.topic: article
ms.date: 05/31/2018
---

# Performance Counters Functions for Visual Basic

> [!IMPORTANT]
> The functions that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

You can use the following functions to work with performance data in Visual Basic.

- [**PdhCloseQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhclosequery)
- [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata)
- [**PdhRemoveCounter**](/windows/desktop/api/Pdh/nf-pdh-pdhremovecounter)
- [**PdhVbAddCounter**](pdhvbaddcounter.md)
- [**PdhVbCreateCounterPathList**](pdhvbcreatecounterpathlist.md)
- [**PdhVbGetCounterPathElements**](pdhvbgetcounterpathelements.md)
- [**PdhVbGetCounterPathFromList**](pdhvbgetcounterpathfromlist.md)
- [**PdhVbGetDoubleCounterValue**](pdhvbgetdoublecountervalue.md)
- [**PdhVbGetLogFileSize**](pdhvbgetlogfilesize.md)
- [**PdhVbGetOneCounterPath**](pdhvbgetonecounterpath.md)
- [**PdhVbIsGoodStatus**](pdhvbisgoodstatus.md)
- [**PdhVbOpenLog**](pdhvbopenlog.md)
- [**PdhVbOpenQuery**](pdhvbopenquery.md)
- [**PdhVbUpdateLog**](pdhvbupdatelog.md)

> [!NOTE]
> The `PdhVb***` functions work on a per-process session and are not thread-safe. These functions should only be used from simple single-threaded applications.
