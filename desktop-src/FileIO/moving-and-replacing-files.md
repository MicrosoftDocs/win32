---
description: Considerations for moving and replacing files by using the CopyFileEx, CreateFile, Replacefile, and MoveFileEx functions.
ms.assetid: 4872af0d-42e8-4576-9aa9-4b8671375f2e
title: Moving and Replacing Files
ms.topic: article
ms.date: 05/31/2018
---

# Moving and Replacing Files

Before a copy operation can be performed, the source file must be closed or opened only for reading. No thread can have the source file opened for writing. To copy an existing file to a new one, use the [**CopyFile**](/windows/desktop/api/WinBase/nf-winbase-copyfile) or [**CopyFileEx**](/windows/desktop/api/WinBase/nf-winbase-copyfileexa) function. Applications can specify whether **CopyFile** and **CopyFileEx** fail if the destination file already exists. If the destination file does exist and is open, it must have been opened with applicable sharing permissions. For more information, see [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea).

The [**CopyFileEx**](/windows/desktop/api/WinBase/nf-winbase-copyfileexa) function also allows an application to specify the address of a callback function (see [**CopyProgressRoutine**](/windows/desktop/api/WinBase/nc-winbase-lpprogress_routine)) that is called each time another portion of the file has been copied. The application can use this information to display an indicator that shows the total number of bytes copied as a percent of the total file size.

The [**ReplaceFile**](/windows/desktop/api/WinBase/nf-winbase-replacefilea) function replaces one file with another file, with the option of creating a backup copy of the original file. The function preserves attributes of the original file, such as its creation time, ACLs, and encryption attribute.

A file must also be closed before an application can move it. The [**MoveFile**](/windows/desktop/api/WinBase/nf-winbase-movefile) and [**MoveFileEx**](/windows/desktop/api/WinBase/nf-winbase-movefileexa) functions copy an existing file to a new location and deletes the original.

The [**MoveFileEx**](/windows/desktop/api/WinBase/nf-winbase-movefileexa) function also allows an application to specify how to move the file. The function can replace an existing file, move a file across volumes, and delay moving the file until the operating system is restarted.

 

 



