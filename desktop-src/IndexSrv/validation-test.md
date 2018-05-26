---
title: Validation Test
description: Validation Test
ms.assetid: edcefa51-a219-40cd-9747-4e182327d039
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Validation Test

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The validation test steps through the object one chunk at a time, verifying each individual chunk and all return codes. This function saves all returned [**STAT\_CHUNK**](/windows/win32/Filter/ns-filter-tagstat_chunk?branch=master) structures in a list. The validation test verifies the following conditions.

-   Chunk IDs are unique and increasing.
-   **STAT\_CHUNK.flags** is a recognized chunk state (CHUNK\_TEXT or CHUNK\_VALUE).
-   **STAT\_CHUNK.breakType** is a recognized break type (0,1,2,3,4).
-   If the filter initialization attributes specify that the filter should only return chunks containing internal value-type properties, **STAT\_CHUNK.idChunkSource** must equal 0.
-   If chunk is not derived—that is, if it is not a internal value-type property—**idChunkSource** must equal **idChunk**.
-   [**IFilter::GetChunk**](/windows/win32/Filter/nf-filter-ifilter-getchunk?branch=master) returns S\_OK or an accepted value (FILTER\_E\_END\_OF\_CHUNKS, FILTER\_E\_LINK\_UNAVAILABLE, and so forth).
-   If the chunk contains text, [**IFilter::GetText**](/windows/win32/Filter/nf-filter-ifilter-gettext?branch=master) returns S\_OK, FILTER\_S\_LAST\_TEXT, or FILTER\_E\_NO\_MORE\_TEXT.
-   If [**IFilter::GetText**](/windows/win32/Filter/nf-filter-ifilter-gettext?branch=master) returns FILTER\_S\_LAST\_TEXT, the next call to **IFilter::GetText** should return FILTER\_E\_NO\_MORE\_TEXT.
-   If the chunk contains a value, [**IFilter::GetValue**](/windows/win32/Filter/nf-filter-ifilter-getvalue?branch=master) returns S\_OK or FILTER\_E\_NO\_MORE\_VALUES.

 

 




