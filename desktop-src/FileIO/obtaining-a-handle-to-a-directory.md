---
description: Whenever a process creates or opens a directory object, it receives a handle to the object.
ms.assetid: 841c7daa-360c-4d96-8a14-6dcfa159a875
title: Directory Handles
ms.topic: article
ms.date: 05/31/2018
---

# Directory Handles

Whenever a process creates or opens a directory object, it receives a handle to the object.

To obtain a handle to an existing directory, call the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function with the **FILE\_FLAG\_BACKUP\_SEMANTICS** flag.

You can pass a directory handle to the following functions.



| Function                                                         | Description                                                                                                                                                      |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BackupRead**](/windows/desktop/api/winbase/nf-winbase-backupread)                              | Back up a file or directory, including the security information.<br/>                                                                                      |
| [**BackupSeek**](/windows/desktop/api/winbase/nf-winbase-backupseek)                              | Seeks forward in a data stream initially accessed by using the [**BackupRead**](/windows/desktop/api/winbase/nf-winbase-backupread) or [**BackupWrite**](/windows/desktop/api/winbase/nf-winbase-backupwrite) function.<br/> |
| [**BackupWrite**](/windows/desktop/api/winbase/nf-winbase-backupwrite)                            | Restore a file or directory that was backed up using [**BackupRead**](/windows/desktop/api/winbase/nf-winbase-backupread).<br/>                                                             |
| [**GetFileInformationByHandle**](/windows/desktop/api/FileAPI/nf-fileapi-getfileinformationbyhandle) | Retrieves file information for the specified file.<br/>                                                                                                    |
| [**GetFileSize**](/windows/desktop/api/FileAPI/nf-fileapi-getfilesize)                               | Retrieves the size of the specified file, in bytes.<br/>                                                                                                   |
| [**GetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-getfiletime)                              | Retrieves the date and time that a file or directory was created, last accessed, and last modified.<br/>                                                   |
| [**GetFileType**](/windows/desktop/api/FileAPI/nf-fileapi-getfiletype)                               | Retrieves the file type of the specified file.<br/>                                                                                                        |
| [**ReadDirectoryChangesW**](/windows/desktop/api/WinBase/nf-winbase-readdirectorychangesw)           | Retrieves information that describes the changes within the specified directory.<br/>                                                                      |
| [**SetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-setfiletime)                              | Sets the date and time that the specified file or directory was created, last accessed, or last modified.<br/>                                             |



 

 

