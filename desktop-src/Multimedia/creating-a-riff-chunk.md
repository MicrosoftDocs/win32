---
title: Creating a RIFF Chunk
description: Creating a RIFF Chunk
ms.assetid: d17f6215-f04f-4776-826e-eedb245f549b
keywords:
- multimedia file I/O,creating RIFF chunk
- file I/O,creating RIFF chunk
- input and output (I/O),creating RIFF chunk
- I/O (input and output),creating RIFF chunk
- creating RIFF chunk
- mmioCreateChunk function
- resource interchange file format (RIFF)
- RIFF (resource interchange file format)
- RIFF I/O
- RIFF chunk
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating a RIFF Chunk

\[The feature associated with this page, [Multimedia File I/O](/windows/win32/multimedia/multimedia-file-i-o), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **Multimedia File I/O**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example uses the [**mmioCreateChunk**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiocreatechunk) function to create a chunk with a chunk identifier of "RIFF" and a form type of "RDIB".


```C++
HMMIO    hmmio; 
MMCKINFO mmckinfo; 
. 
. 
. 
mmckinfo.fccType = mmioFOURCC('R', 'D', 'I', 'B'); 
mmioCreateChunk(hmmio, &mmckinfo, MMIO_CREATERIFF); 
```



If you are creating a "RIFF" or "LIST" chunk, you must specify the form type or list type in the **fccType** member of the [**MMCKINFO**](/windows/win32/api/mmiscapi/ns-mmiscapi-mmckinfo) structure. In the previous example, "RDIB" is the form type.

If you know the size of the data field in a new chunk, you can set the **cksize** member of the **MMCKINFO** structure when you create the chunk. This value will be written to the data size field in the new chunk. If this value is not correct when you call [**mmioAscend**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioascend) to mark the end of the chunk, it will be automatically rewritten to reflect the correct size of the data field.

After you create a chunk by using the [**mmioCreateChunk**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiocreatechunk) function, the file position is set to the data field of the chunk (8 bytes from the beginning of the chunk). If the chunk is a "RIFF" or "LIST" chunk, the file position is set to the location following the form type or list type (12 bytes from the beginning of the chunk).

 

 