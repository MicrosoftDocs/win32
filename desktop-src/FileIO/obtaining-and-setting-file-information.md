---
Description: Functions to use to get and set file information.
ms.assetid: 3b5fb709-c699-4651-8072-97210c8cf763
title: Obtaining and Setting File Information
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining and Setting File Information

The following topics describe how to get and set file information.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Retrieving File Type Information](retrieving-file-type-information.md)<br/>                               | The [**GetFileType**](/windows/win32/FileAPI/nf-fileapi-getfiletype?branch=master) function retrieves the type of a file: disk, character (such as a console), pipe, or unknown.<br/>                                                                                                                                               |
| [Determining the Size of a File](determining-the-size-of-a-file.md)<br/>                                   | The [**GetFileSize**](/windows/win32/FileAPI/nf-fileapi-getfilesize?branch=master) function retrieves the size of a file.<br/>                                                                                                                                                                                                      |
| [Searching for One or More Files](searching-for-one-or-more-files.md)<br/>                                 | An application can search the current directory for all file names that match a given pattern by using the [**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master), [**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master), [**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master), and [**FindClose**](/windows/win32/FileAPI/nf-fileapi-findclose?branch=master) functions.<br/> |
| [Setting and Getting the Timestamp of a File](setting-and-getting-the-timestamp-of-a-file.md)<br/>         | Applications can retrieve and set the date and time a file is created, last modified, or last accessed by using the [**GetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724320) and [**SetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724933) functions.<br/>                                                                         |
| [Determining the Current Character Set Code Page](determining-the-current-character-set-code-page.md)<br/> | The [**AreFileApisANSI**](/windows/win32/fileapi/nf-fileapi-arefileapisansi?branch=master) function determines whether the file I/O functions are using the ANSI or OEM character set code page.<br/>                                                                                                                               |



 

 

 




