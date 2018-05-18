---
title: Binary or Null Filter
description: Binary or Null Filter
ms.assetid: 'e4e536e4-ec78-413f-99b3-1a2aea4410df'
---

# Binary or Null Filter

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When a registered binary file is encountered, the null filter (in Query.dll) is used. The null filter retrieves only the system properties. The contents of a binary file are not filtered. Examples of system properties are FileName, LastWriteTime, FileSize, and Attributes.

 

 




