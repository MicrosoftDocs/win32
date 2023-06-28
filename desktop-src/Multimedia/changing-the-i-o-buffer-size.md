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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Changing the I/O Buffer Size

\[The feature associated with this page, [Multimedia File I/O](/windows/win32/multimedia/multimedia-file-i-o), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **Multimedia File I/O**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 