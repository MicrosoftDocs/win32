---
Description: Whenever a process creates or opens a directory object, it receives a handle to the object.
ms.assetid: 841c7daa-360c-4d96-8a14-6dcfa159a875
title: Directory Handles
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Directory Handles

Whenever a process creates or opens a directory object, it receives a handle to the object.

To obtain a handle to an existing directory, call the [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) function with the **FILE\_FLAG\_BACKUP\_SEMANTICS** flag.

You can pass a directory handle to the following functions.



| Function                                                         | Description                                                                                                                                                      |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BackupRead**](https://msdn.microsoft.com/library/windows/desktop/aa362509)                              | Back up a file or directory, including the security information.<br/>                                                                                      |
| [**BackupSeek**](https://msdn.microsoft.com/library/windows/desktop/aa362510)                              | Seeks forward in a data stream initially accessed by using the [**BackupRead**](https://msdn.microsoft.com/library/windows/desktop/aa362509) or [**BackupWrite**](https://msdn.microsoft.com/library/windows/desktop/aa362511) function.<br/> |
| [**BackupWrite**](https://msdn.microsoft.com/library/windows/desktop/aa362511)                            | Restore a file or directory that was backed up using [**BackupRead**](https://msdn.microsoft.com/library/windows/desktop/aa362509).<br/>                                                             |
| [**GetFileInformationByHandle**](/windows/win32/FileAPI/nf-fileapi-getfileinformationbyhandle?branch=master) | Retrieves file information for the specified file.<br/>                                                                                                    |
| [**GetFileSize**](/windows/win32/FileAPI/nf-fileapi-getfilesize?branch=master)                               | Retrieves the size of the specified file, in bytes.<br/>                                                                                                   |
| [**GetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724320)                              | Retrieves the date and time that a file or directory was created, last accessed, and last modified.<br/>                                                   |
| [**GetFileType**](/windows/win32/FileAPI/nf-fileapi-getfiletype?branch=master)                               | Retrieves the file type of the specified file.<br/>                                                                                                        |
| [**ReadDirectoryChangesW**](/windows/win32/WinBase/nf-winbase-readdirectorychangesw?branch=master)           | Retrieves information that describes the changes within the specified directory.<br/>                                                                      |
| [**SetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724933)                              | Sets the date and time that the specified file or directory was created, last accessed, or last modified.<br/>                                             |



 

 

 




