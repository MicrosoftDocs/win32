---
title: Variables to Perform Processing
description: Variables to Perform Processing
ms.assetid: 02f194ea-cac0-410f-886f-2894dd6971c8
keywords:
- Windows Media Player plug-ins,Echo sample DoProcessOutput method
- plug-ins,Echo sample DoProcessOutput method
- digital signal processing plug-ins,Echo sample DoProcessOutput method
- DSP plug-ins,Echo sample DoProcessOutput method
- Echo DSP plug-in sample,DoProcessOutput method
- Echo DSP plug-in sample,processing variables
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Variables to Perform Processing

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The member variables for handling the delay buffer deal with **BYTE** quantities; they are **BYTE** pointers and an integer that stores a count of bytes. This is ideal for processing 8-bit audio, since an 8-bit sample fits nicely into one byte of memory. When processing 16-bit audio, though, it is more convenient to convert these to **short** pointers, so the processing can occur two bytes at a time.

The following example code allocates the new 16-bit pointers, and adds a pointer variable that stores the address of the end of the delay buffer. Insert it in the "case 16" section just before the loop entry point:


```C++
// Store local pointers to the delay buffer.
short    *pwDelayPointer = (short *)m_pbDelayPointer;
short    *pwDelayBuffer = (short *) m_pbDelayBuffer;
// Store the address of the last word of the delay buffer.
short    *pwEOFDelayBuffer = (short *)(m_pbDelayBuffer + m_cbDelayBuffer - sizeof(short)); 

```



The code for 8-bit processing also allocates a variable that stores the address of the end of the delay buffer. Storing this value makes it easy to test whether the movable delay buffer pointer has reached the end of the delay buffer. The following example code calculates the value:


```C++
// Store the address of the end of the delay buffer.
BYTE * pbEOFDelayBuffer = (m_pbDelayBuffer + m_cbDelayBuffer - sizeof(BYTE));

```



## Related topics

<dl> <dt>

[**Implementing CEcho::DoProcessOutput**](implementing-cecho--doprocessoutput.md)
</dt> </dl>

 

 




