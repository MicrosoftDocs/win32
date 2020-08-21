---
title: Basic Services
description: Basic Services
ms.assetid: 7b77ed5d-0bd9-4926-b73f-afc7070fe314
keywords:
- multimedia file I/O,basic services
- file I/O,basic services
- input and output (I/O),basic services
- I/O (input and output),basic services
- basic I/O
- mmioOpen function
ms.topic: article
ms.date: 05/31/2018
---

# Basic Services

Using the basic I/O services is similar to using the run-time file I/O services of the C run-time library. Files must be opened before they can be read or written. After reading or writing, the file must be closed. You can also change the current read or write location within an open file.

Before you begin any I/O operations to a file, you must open the file by using the [**mmioOpen**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioopen) function. This function returns a file handle of type **HMMIO**. You can use this file handle to identify the open file when calling other file I/O functions.

> [!Note]  
> An **HMMIO** file handle is not a standard file handle. Do not use **HMMIO** file handles with Win32 or C run-time file I/O functions.

 

When you use [**mmioOpen**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioopen) to open a file, you use a flag to specify whether you are opening it for reading, writing, or both. You can also specify flags that enable you to create or delete a file. Use the [**mmioClose**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioclose) function to close a file when you are finished reading or writing to it.

You can read and write files by using the [**mmioRead**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioread) and [**mmioWrite**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiowrite) functions respectively. The next read or write operation occurs at the current file position or file pointer in a file. The current file position is advanced each time a file is read or written.

You can also change the current file position by using the [**mmioSeek**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioseek) function. You should ensure that you specify a valid location in a file. If you specify an invalid location, such as past the end of the file, **mmioSeek** may not return an error, but subsequent I/O operations could fail.

There are flags you can use with the **mmioOpen** function for operations beyond basic file I/O. By specifying an [**MMIOINFO**](/previous-versions//dd757322(v=vs.85)) structure, for example, you can open memory files, specify a custom I/O procedure, or supply a buffer for buffered I/O.

 

 