---
title: Invalid Input Test
description: Invalid Input Test
ms.assetid: 5a41177d-8d75-40be-8c07-f9e44aebed4b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Invalid Input Test

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The ifilttst.exe program reinitializes the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface with the same parameters and performs an invalid input test. This test steps through the document one chunk at a time, making function calls incorrectly—such as the [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) method when the current chuck contains text. The test checks all return codes for compliance with the **IFilter** specification. The invalid input test verifies the following conditions.

-   If the current chunk contains text, [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) returns FILTER\_E\_NO\_VALUES. Then a call to [**IFilter::GetText**](/windows/desktop/api/Filter/nf-filter-ifilter-gettext) should succeed.
-   If the current chunk contains a value, [**IFilter::GetText**](/windows/desktop/api/Filter/nf-filter-ifilter-gettext) should return FILTER\_E\_NO\_TEXT. Then a call to [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) should succeed.
-   If the previous call to [**IFilter::GetText**](/windows/desktop/api/Filter/nf-filter-ifilter-gettext) returned FILTER\_E\_NO\_MORE\_TEXT, successive calls to **IFilter::GetText** should return FILTER\_E\_NO\_MORE\_TEXT.
-   If the previous call to [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) returned FILTER\_E\_NO\_MORE\_VALUES, successive calls to **IFilter::GetValue** should return FILTER\_E\_NO\_MORE\_VALUES.
-   If the previous call to [**IFilter::GetChunk**](/windows/desktop/api/Filter/nf-filter-ifilter-getchunk) returned FILTER\_E\_END\_OF\_CHUNKS, successive calls to **IFilter::GetChunk** should return FILTER\_E\_END\_OF\_CHUNKS.
-   In addition, the test compares the current chunk structures to those returned in the validation test to make sure they are identical.

 

 




