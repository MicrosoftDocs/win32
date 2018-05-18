---
title: Creating a RIFF Chunk
description: Creating a RIFF Chunk
ms.assetid: 'd17f6215-f04f-4776-826e-eedb245f549b'
keywords: ["multimedia file I/O,creating RIFF chunk", "file I/O,creating RIFF chunk", "input and output (I/O),creating RIFF chunk", "I/O (input and output),creating RIFF chunk", "creating RIFF chunk", "mmioCreateChunk function", "resource interchange file format (RIFF)", "RIFF (resource interchange file format)", "RIFF I/O", "RIFF chunk"]
---

# Creating a RIFF Chunk

The following example uses the [**mmioCreateChunk**](mmiocreatechunk.md) function to create a chunk with a chunk identifier of "RIFF" and a form type of "RDIB".


```C++
HMMIO    hmmio; 
MMCKINFO mmckinfo; 
. 
. 
. 
mmckinfo.fccType = mmioFOURCC('R', 'D', 'I', 'B'); 
mmioCreateChunk(hmmio, &amp;mmckinfo, MMIO_CREATERIFF); 
```



If you are creating a "RIFF" or "LIST" chunk, you must specify the form type or list type in the **fccType** member of the [**MMCKINFO**](mmckinfo.md) structure. In the previous example, "RDIB" is the form type.

If you know the size of the data field in a new chunk, you can set the **cksize** member of the **MMCKINFO** structure when you create the chunk. This value will be written to the data size field in the new chunk. If this value is not correct when you call [**mmioAscend**](mmioascend.md) to mark the end of the chunk, it will be automatically rewritten to reflect the correct size of the data field.

After you create a chunk by using the [**mmioCreateChunk**](mmiocreatechunk.md) function, the file position is set to the data field of the chunk (8 bytes from the beginning of the chunk). If the chunk is a "RIFF" or "LIST" chunk, the file position is set to the location following the form type or list type (12 bytes from the beginning of the chunk).

 

 




