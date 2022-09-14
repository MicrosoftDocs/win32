---
description: Applications can retrieve and set the date and time a file is created, last modified, or last accessed by using the GetFileTime and SetFileTime functions.
ms.assetid: f8930be6-7c2a-4e50-a7a1-d25f6e2a3951
title: Setting and Getting the Timestamp of a File
ms.topic: article
ms.date: 05/31/2018
---

# Setting and Getting the Timestamp of a File

Applications can retrieve and set the date and time a file is created, last modified, or last accessed by using the [**GetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-getfiletime) and [**SetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-setfiletime) functions. For more information, see [File Times](/windows/desktop/SysInfo/file-times).

> [!Note]  
> Not all file systems can record creation and last access times, and not all file systems record them in the same manner. For example, on FAT file system, create time has a resolution of 10 milliseconds, write time has a resolution of 2 seconds, and access time has a resolution of 1 day (really, the access date). The NTFS file system delays update to the last access time for a file by up to one hour after the last access.

 

 

 
