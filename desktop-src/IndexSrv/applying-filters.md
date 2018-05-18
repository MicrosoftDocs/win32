---
title: Applying Filters
description: Applying Filters
ms.assetid: '3d6ba1a9-4de0-4d1b-a08b-1976a1c4ab05'
---

# Applying Filters

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Clients call [**IFilter**](ifilter.md) interface implementations to extract text and properties from an object. Although clients of the **IFilter** interface may use the interface in any way they wish, it was designed to meet the specific needs of full-text search engines. The search engine of Indexing Service breaks the results of the [IFilter::GetText](ifilter-gettext.md) method into words, normalizes them, and saves them in an index. If available, the search engine uses the locale identifier (LCID) of a text chunk to perform language-specific word breaking and normalization.

This section includes the following topics.

-   [Filter DLLs](filter-dlls.md). A list of the dynamic-link libraries (DLLs) supplied by Indexing Service and the way you associate them to file types.
-   [Controlling Filtering](controlling-filtering.md). A list of ways you can control the filtering process for Indexing Service.

 

 




