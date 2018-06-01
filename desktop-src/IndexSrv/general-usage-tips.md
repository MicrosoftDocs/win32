---
Description: The following are general tips to help ensure optimal performance for Indexing Service.
ms.assetid: ca14b749-a381-4796-975f-1c6867272ddc
title: General Usage Tips
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# General Usage Tips

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

The following are general tips to help ensure optimal performance for Indexing Service.

-   Do not store your catalogs in websites. If the catalog files are under a Web root or a virtual directory, Internet Information Service may occasionally lock the catalog files, preventing an update. This can also result in an endless indexing loop that uses up all of the processor capacity.
-   If you are using multiple catalogs, make a catalog folder on one of your drives and store each catalog in a subfolder in that folder.
-   Do not run antiviral or backup software when Indexing Service is running. These programs may lock files, causing Indexing Service to time out while trying to index. Antiviral software can also interfere with files in the catalog directory, causing the index to become corrupt. For example, AV software will sometimes hold files open that Indexing Service tries to delete. Indexing service does not expect to find the recreated file. Hence, when Indexing Service finds the file again, it will assume that the catalog is corrupt.
-   Indexing Service will not index documents with access control lists (ACLs) that exceed 64K.
-   Indexing Service will not index documents with custom properties that exceed 64K.

 

 



