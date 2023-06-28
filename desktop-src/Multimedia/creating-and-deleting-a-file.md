---
title: Creating and Deleting a File
description: Creating and Deleting a File
ms.assetid: a4b4a310-7230-4f1d-b084-c47db39adaac
keywords:
- multimedia file I/O,creating files
- file I/O,creating files
- input and output (I/O),creating files
- I/O (input and output),creating files
- creating I/O files
- multimedia file I/O,deleting files
- file I/O,deleting files
- input and output (I/O),deleting files
- I/O (input and output),deleting files
- deleting I/O files
- mmioOpen function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating and Deleting a File

\[The feature associated with this page, [Multimedia File I/O](/windows/win32/multimedia/multimedia-file-i-o), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **Multimedia File I/O**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To create a file, set the *dwOpenFlags* parameter of the [**mmioOpen**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioopen) function to MMIO\_CREATE. The following example creates a file and opens it for reading and writing.


```C++
HMMIO hFile; 

hFile = mmioOpen("NEWFILE.TXT", NULL, MMIO_CREATE | MMIO_READWRITE); 
if (hFile != NULL) 
    // File created successfully. 
else 
    // File cannot be created. 
```



If the file you are creating already exists, it will be truncated to zero length.

To delete a file, set the *dwOpenFlags* parameter of the **mmioOpen** function to MMIO\_DELETE. After you delete a file, it cannot be recovered by any standard means. If your application is deleting a file at the request of a user, query the user before deleting the file to make sure the user wants to delete it.

 

 