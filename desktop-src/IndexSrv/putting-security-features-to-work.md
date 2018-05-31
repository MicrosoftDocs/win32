---
title: Putting Security Features to Work
description: Putting Security Features to Work
ms.assetid: 669b73e5-f9aa-4df6-af15-66db88c8d644
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Putting Security Features to Work

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses the security system built into Windows to check whether users have permission to view query results. NTFS file system supports access control lists (ACLs) on directories and files. Indexing Service will check these ACLs before returning a query result file by file.

-   [Security Summary](security-summary.md)

 

 




