---
title: Caching Value-Type Properties
description: Caching Value-Type Properties
ms.assetid: ab959ef3-db10-4028-be40-1ebe57376d50
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Caching Value-Type Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

For either textual or non-textual value-type properties, Indexing Service can optionally store selected internal values in the property cache of the catalog for fast and efficient retrieval. If multiple instances of a value-type property occur for a document, the value in the cache is the last-encountered instance. External value-type properties are not stored in the property cache, but are accessed where they are natively stored.

The cached size of an internal value-type property is the number of bytes the value occupies in the property cache, and the storage level is either primary or secondary. As much of the information from primary and secondary caches is kept in memory as possible, to provide fast access. The primary cache has precedence for memory usage over the secondary cache, so typically the primary cache contains only a few, important, value-type properties. This means the values in the primary cache are usually memory-resident, and those in the secondary cache are memory-resident if there is enough storage available.

 

 




