---
title: Consistency Test
description: Consistency Test
ms.assetid: 3b557fd0-2527-4ee7-a67b-defd5f027d12
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Consistency Test

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The ifilttxt.exe program reinitializes the [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) interface with the same parameters as in the validation test and performs a consistency test. If the **IFilter** implementation has been initialized with the IFILTER\_INIT\_INDEXING\_ONLY flag, the test releases the **IFilter** interface and re-binds it before making another call to the [**IFilter::Init**](/windows/win32/Filter/nf-filter-ifilter-init?branch=master) method. This test checks to make sure that the [**STAT\_CHUNK**](/windows/win32/Filter/ns-filter-tagstat_chunk?branch=master) structures returned are identical to those returned in the validation test. The consistency test verifies the following conditions.

-   Each [**STAT\_CHUNK**](/windows/win32/Filter/ns-filter-tagstat_chunk?branch=master) structure returned by the [**IFilter::GetChunk**](/windows/win32/Filter/nf-filter-ifilter-getchunk?branch=master) method is exactly identical to the corresponding **STAT\_CHUNK** returned in the validation test.
-   A **IFilter::GetChunk** method call returns S\_OK or an accepted value (FILTER\_E\_END\_OF\_CHUNKS, FILTER\_E\_LINK\_UNAVAILABLE, and so forth).

 

 




