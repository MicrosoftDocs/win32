---
title: Recommended Computer Configuration
description: Recommended Computer Configuration
ms.assetid: 9ecabdc3-9cc8-455f-9c77-9899b2e88eee
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Recommended Computer Configuration

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The minimum hardware configuration for Indexing Service is the same as for Windows XP. However, the performance of the indexing and search engines depends on the number and size of documents it indexes, the query submission rate, and the complexity of the queries. The amount of computer resources available to Indexing Service also affects performance. A computer with the minimum hardware configuration for Windows handles queries well if the number of concurrent queries is not too high. For a small organization, this might be sufficient. However, for a larger organization serving many users, you may choose to employ a more powerful configuration.

The following table shows recommended memory configuration based on the number of documents that Indexing Service would process.



| Number of documents to be indexed | Minimum memory (in megabytes)                  | Recommended memory                                                 |
|-----------------------------------|------------------------------------------------|--------------------------------------------------------------------|
| Fewer than 100,000                | 128 Windows 2000 128 for Windows XP<br/> | 256 Windows 2000 256 for Windows XP<br/>                     |
| From 100,000 through 250,00       | 128 Windows 2000 128 for Windows XP<br/> | 256 or more Windows 2000 256 or more for Windows XP<br/>     |
| From 250,000 through 500,000      | 128 Windows 2000 128 for Windows XP<br/> | 256 or more? Windows 2000 256 or more for Windows XP<br/>    |
| 500,000 or more                   | 256 Windows 2000 256 for Windows XP<br/> | 256 or more for Windows 2000 256 or more for Windows XP<br/> |



 

If the number of documents is large, insufficient memory will seriously affect performance. You can also improve performance by adding more memory and increasing the amount of memory dedicated to mapping the property cache. A faster CPU improves the performance of indexing and the speed of processing queries.

The total size of the documents Indexing Service would index and the type of file system you are using affects the amount of disk space required for storing Indexing Service data. On a FAT file system, the space needed for the catalog plus temporary workspace is about 30 percent of the indexed text. On an NTFS, file system the space required is about 15 percent of the indexed text.

 

 





