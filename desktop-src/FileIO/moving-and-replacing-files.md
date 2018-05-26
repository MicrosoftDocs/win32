---
Description: Considerations for moving and replacing files by using the CopyFileEx, CreateFile, Replacefile, and MoveFileEx functions.
ms.assetid: 4872af0d-42e8-4576-9aa9-4b8671375f2e
title: Moving and Replacing Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Moving and Replacing Files

Before a file can be copied, it must be closed or opened only for reading. No thread can have the file opened for writing. To copy an existing file to a new one, use the [**CopyFile**](/windows/win32/WinBase/nf-winbase-copyfile?branch=master) or [**CopyFileEx**](/windows/win32/WinBase/nf-winbase-copyfileexa?branch=master) function. Applications can specify whether **CopyFile** and **CopyFileEx** fail if the destination file already exists. If the file does exist and is open, it must have been opened with applicable sharing permissions. For more information, see [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master).

The [**CopyFileEx**](/windows/win32/WinBase/nf-winbase-copyfileexa?branch=master) function also allows an application to specify the address of a callback function (see [**CopyProgressRoutine**](/windows/win32/WinBase/nc-winbase-lpprogress_routine?branch=master)) that is called each time another portion of the file has been copied. The application can use this information to display an indicator that shows the total number of bytes copied as a percent of the total file size.

The [**ReplaceFile**](/windows/win32/WinBase/nf-winbase-replacefilea?branch=master) function replaces one file with another file, with the option of creating a backup copy of the original file. The function preserves attributes of the original file, such as its creation time, ACLs, and encryption attribute.

A file must also be closed before an application can move it. The [**MoveFile**](/windows/win32/WinBase/nf-winbase-movefile?branch=master) and [**MoveFileEx**](/windows/win32/WinBase/nf-winbase-movefileexa?branch=master) functions copy an existing file to a new location and deletes the original.

The [**MoveFileEx**](/windows/win32/WinBase/nf-winbase-movefileexa?branch=master) function also allows an application to specify how to move the file. The function can replace an existing file, move a file across volumes, and delay moving the file until the operating system is restarted.

 

 



