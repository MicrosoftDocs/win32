---
title: Accessing a File I/O Buffer
description: Accessing a File I/O Buffer
ms.assetid: 'b829d8ef-8e0b-4c30-b8cf-e9feccc63bbf'
keywords: ["multimedia file I/O,accessing buffers", "file I/O,accessing buffers", "input and output (I/O),accessing buffers", "I/O (input and output),accessing buffers", "accessing I/O buffers", "buffered I/O", "mmioSetInfo function"]
---

# Accessing a File I/O Buffer

The following example accesses an I/O buffer directly to read data from a waveform-audio file.


```C++
HMMIO    hmmio; 
MMIOINFO mmioinfo; 
DWORD    dwDataSize; 
DWORD    dwCount; 
HPSTR    hptr; 

// Get information about the file I/O buffer. 
if (mmioGetInfo(hmmio, &amp;mmioinfo, 0)) 
{ 
    Error("Failed to get I/O buffer info."); 
    . 
    . 
    . 
    mmioClose(hmmio, 0); 
    return; 
} 
 
// Read the entire file by directly reading the file I/O buffer. 
// When the end of the I/O buffer is reached, advance the buffer. 

for (dwCount = dwDataSize, hptr = lpData; dwCount  0; dwCount--) 
{ 
    // Check to see if the I/O buffer must be advanced. 
    if (mmioinfo.pchNext == mmioinfo.pchEndRead) 
    { 
        if(mmioAdvance(hmmio, &amp;mmioinfo, MMIO_READ)) 
        { 
            Error("Failed to advance buffer."); 
            . 
            . 
            . 
            mmioClose(hmmio, 0); 
            return; 
        } 
    } 
 
    // Get a character from the buffer. 
    *hptr++ = *mmioinfo.pchNext++; 
} 
 
// End direct buffer access and close the file. 
mmioSetInfo(hmmio, &amp;mmioinfo, 0); 
mmioClose(hmmio, 0); 

```



When you finish accessing a file I/O buffer, call the [**mmioSetInfo**](mmiosetinfo.md) function, passing an address of the [**MMIOINFO**](mmioinfo.md) structure filled by the [**mmioGetInfo**](mmiogetinfo.md) function. If you wrote to the buffer, set the MMIO\_DIRTY flag in the **dwFlags** member of the **MMIOINFO** structure before calling **mmioSetInfo**. Otherwise, the buffer will not be flushed to disk.

 

 




