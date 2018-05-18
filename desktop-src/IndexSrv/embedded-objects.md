---
title: Embedded Objects
description: Embedded Objects
ms.assetid: '823f9dbe-82cd-4186-a465-1e28fda2a6e6'
---

# Embedded Objects

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The parent container of an object is responsible for binding to the **IFilter** interface of a child object and managing the chunk IDs to keep them unique. Nested chunks appear to the original caller as chunks of the outer object. There is no operating-system support provided for this operation. **IFilter** interface implementations are responsible for binding to the **IFilter** interface of embedded objects. If the current chunk is within an embedded object, all calls to the [**IFilter::GetText**](ifilter-gettext.md) and [**IFilter::GetValue**](ifilter-getvalue.md) methods should be passed directly to the **IFilter** interface of the embedded object, and the return values from the embedding should be returned to the client. Other calls require some additional work. The [**IFilter::GetChunk**](ifilter-getchunk.md) method, for example, may require that chunk IDs be renumbered to make them unique.

 

 




