---
title: Opening a File with mmioOpen
description: Opening a File with mmioOpen
ms.assetid: 947d1b1c-ec00-4bd9-948a-4b8e3bfb84f6
keywords:
- multimedia file I/O,opening files
- file I/O,opening files
- input and output (I/O),opening files
- I/O (input and output),opening files
- multimedia file I/O,mmioOpen function
- file I/O,mmioOpen function
- input and output (I/O),mmioOpen function
- I/O (input and output),mmioOpen function
- mmioOpen function
- opening I/O files
ms.topic: article
ms.date: 05/31/2018
---

# Opening a File with mmioOpen

To open a file for basic I/O operations, set the *lpmmioinfo* parameter of the [**mmioOpen**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioopen) function to **NULL**. The following example opens a file named "C:\\SAMPLES\\SAMPLE1.TXT" for reading, and checks the return value for error.


```C++
HMMIO hFile; 

if ((hFile = mmioOpen("C:\\SAMPLES\\SAMPLE1.TXT", NULL, 
    MMIO_READ)) != NULL) 
    // File opened successfully. 
else 
    // File cannot be opened. 
```



Use the *dwFlags* parameter of **mmioOpen** to specify flags for opening a file.

 

 