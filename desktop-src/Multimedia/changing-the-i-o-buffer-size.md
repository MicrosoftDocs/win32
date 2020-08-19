---
title: Changing the I/O Buffer Size
description: Changing the I/O Buffer Size
ms.assetid: eff97399-143e-477b-bb16-7305e83a2317
keywords:
- multimedia file I/O,changing buffer size
- file I/O,changing buffer size
- input and output (I/O),changing buffer size
- I/O (input and output),changing buffer size
- changing I/O buffer size
- unbuffered I/O
- buffered I/O
- mmioSetBuffer function
ms.topic: article
ms.date: 05/31/2018
---

# Changing the I/O Buffer Size

The following example opens a file named SAMPLE.TXT for unbuffered I/O, and then enables buffered I/O with an internal 16K buffer using the [**mmioSetBuffer**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiosetbuffer) function.


```C++
HMMIO hFile; 

if ((hFile = mmioOpen("SAMPLE.TXT", NULL, MMIO_READ)) != NULL) 
{ 
    // File opened successfully; request an I/O buffer. 
    if (mmioSetBuffer(hFile, NULL, 16384L, 0)) 
        // Buffer cannot be allocated. 
    else 
        // Buffer allocated successfully. 
} 
else 
    // File cannot be opened. 
```



 

 