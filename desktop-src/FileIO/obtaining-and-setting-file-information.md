---
description: Functions to use to get and set file information.
ms.assetid: 3b5fb709-c699-4651-8072-97210c8cf763
title: Obtaining and Setting File Information
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining and Setting File Information

The following topics describe how to get and set file information.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Retrieving File Type Information](retrieving-file-type-information.md)<br/>                               | The [**GetFileType**](/windows/desktop/api/FileAPI/nf-fileapi-getfiletype) function retrieves the type of a file: disk, character (such as a console), pipe, or unknown.<br/>                                                                                                                                               |
| [Determining the Size of a File](determining-the-size-of-a-file.md)<br/>                                   | The [**GetFileSize**](/windows/desktop/api/FileAPI/nf-fileapi-getfilesize) function retrieves the size of a file.<br/>                                                                                                                                                                                                      |
| [Searching for One or More Files](searching-for-one-or-more-files.md)<br/>                                 | An application can search the current directory for all file names that match a given pattern by using the [**FindFirstFile**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfilea), [**FindFirstFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfileexa), [**FindNextFile**](/windows/desktop/api/FileAPI/nf-fileapi-findnextfilea), and [**FindClose**](/windows/desktop/api/FileAPI/nf-fileapi-findclose) functions.<br/> |
| [Setting and Getting the Timestamp of a File](setting-and-getting-the-timestamp-of-a-file.md)<br/>         | Applications can retrieve and set the date and time a file is created, last modified, or last accessed by using the [**GetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-getfiletime) and [**SetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-setfiletime) functions.<br/>                                                                         |
| [Determining the Current Character Set Code Page](determining-the-current-character-set-code-page.md)<br/> | The [**AreFileApisANSI**](/windows/desktop/api/fileapi/nf-fileapi-arefileapisansi) function determines whether the file I/O functions are using the ANSI or OEM character set code page.<br/>                                                                                                                               |



 

 

