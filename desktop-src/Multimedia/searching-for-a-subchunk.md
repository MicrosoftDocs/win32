---
title: Searching for a Subchunk
description: Searching for a Subchunk
ms.assetid: c494a57f-6395-40a4-a4f2-d200d7ad6223
keywords:
- multimedia file I/O,searching for RIFF chunk
- file I/O,searching for RIFF chunk
- input and output (I/O),searching for RIFF chunk
- I/O (input and output),searching for RIFF chunk
- searching for RIFF chunk
- resource interchange file format (RIFF)
- RIFF (resource interchange file format)
- RIFF I/O
- RIFF chunk
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Searching for a Subchunk

\[The feature associated with this page, [Multimedia File I/O](/windows/win32/multimedia/multimedia-file-i-o), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **Multimedia File I/O**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example uses the [**mmioDescend**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiodescend) function to search for the "FMT" chunk in the "RIFF" chunk of the previous example.


```C++
// Find the format chunk (form type "FMT"); it should be 
// a subchunk of the "RIFF" parent chunk. 
mmckinfoSubchunk.ckid = mmioFOURCC('f', 'm', 't', ' '); 
if (mmioDescend(hmmio, &mmckinfoSubchunk, &mmckinfoParent, 
    MMIO_FINDCHUNK)) 
    // Error, cannot find the "FMT" chunk. 
else 
    // "FMT" chunk found. 
```



To search for a subchunk (that is, any chunk other than a "RIFF" or "LIST" chunk), identify its parent chunk in the *lpckParent* parameter of the [**mmioDescend**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiodescend) function.

If you do not specify a parent chunk, the current file position should be at the beginning of a chunk before you call the **mmioDescend** function. If you do specify a parent chunk, the current file position can be anywhere in that chunk.

If the search for a subchunk fails, the current file position is undefined. You can use the [**mmioSeek**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioseek) function and the **dwDataOffset** member of the [**MMCKINFO**](/windows/win32/api/mmiscapi/ns-mmiscapi-mmckinfo) structure describing the parent chunk to seek back to the beginning of the parent chunk, as in the following example:


```C++
mmioSeek(hmmio, mmckinfoParent.dwDataOffset + 4, SEEK_SET); 
```



Because **dwDataOffset** specifies the offset to the beginning of the data portion of the chunk, you must seek 4 bytes past **dwDataOffset** to set the file position after the form type.

 

 