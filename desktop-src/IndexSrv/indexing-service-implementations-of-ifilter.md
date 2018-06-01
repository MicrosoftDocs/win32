---
Description: Indexing Service Implementations of IFilter
ms.assetid: 42e43be5-7fa0-462f-af2d-95a1167ad1f2
title: Indexing Service Implementations of IFilter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Indexing Service Implementations of IFilter

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Microsoft supplies several standard filters with Indexing Service. The following table lists the filter names, what they filter, and the DLL name. Selecting the name of a filter takes you to a description of the filter.



| Filter Name                                                              | Files Filtered                               | Filter DLL   |
|--------------------------------------------------------------------------|----------------------------------------------|--------------|
| [MIME Filter](mime-filter.md)                                           | Multipurpose Internet Mail Extensions (MIME) | mimefilt.dll |
| [HTML Filter](html-filter.md)                                           | HTML 3.0 or earlier                          | nlhtml.dll   |
| [Microsoft Office Document Filter](microsoft-office-document-filter.md) | Word, Excel, Microsoft PowerPoint            | offfilt.dll  |
| [Default or Plain Text Filter](default-or-plain-text-filter.md)         | Plain text files - Default Filter            | Query.dll    |
| [Binary or Null Filter](binary-or-null-filter.md)                       | Binary files - Null Filter                   | Query.dll    |



 

 

 



