---
title: Searching for a RIFF Chunk
description: Searching for a RIFF Chunk
ms.assetid: ce974fb3-3af0-4400-8f55-65d63627592a
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
ms.date: 05/31/2018
---

# Searching for a RIFF Chunk

The following example uses the [**mmioDescend**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiodescend) function to search for a "RIFF" chunk with a form type of "WAVE" to verify that the file that has just been opened is a waveform-audio file.


```C++
HMMIO    hmmio; 
MMCKINFO mmckinfoParent; 
MMCKINFO mmckinfoSubchunk; 
. 
. 
. 
// Locate a "RIFF" chunk with a "WAVE" form type to make 
// sure the file is a waveform-audio file. 
mmckinfoParent.fccType = mmioFOURCC('W', 'A', 'V', 'E'); 
if (mmioDescend(hmmio, (LPMMCKINFO) &mmckinfoParent, NULL, 
    MMIO_FINDRIFF)) 
    // The file is not a waveform-audio file. 
else 
    // The file is a waveform-audio file 

```



 

 