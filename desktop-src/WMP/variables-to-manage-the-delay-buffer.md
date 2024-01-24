---
title: Variables to Manage the Delay Buffer
description: Variables to Manage the Delay Buffer
ms.assetid: 2c5963a1-04e2-4421-8f56-14c1e059de4e
keywords:
- Windows Media Player plug-ins,Echo sample streaming resources
- plug-ins,Echo sample streaming resources
- digital signal processing plug-ins,Echo sample streaming resources
- DSP plug-ins,Echo sample streaming resources
- Echo DSP plug-in sample,streaming resources
- Echo DSP plug-in sample,delay buffer
- delay buffer
- buffers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Variables to Manage the Delay Buffer

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must add the declarations for the member variables you need to manage the delay buffer. Add the following declarations to Echo.h in the "private" section:


```C++
DWORD  m_cbDelayBuffer;   // Count of bytes in delay buffer size.
BYTE*  m_pbDelayPointer;  // Movable pointer to delay buffer.
BYTE*  m_pbDelayBuffer;   // Pointer to the head of the delay buffer.

```



Add the following code to the CEcho constructor to initialize the delay buffer variables:


```C++
m_pbDelayBuffer = NULL;
m_pbDelayPointer = NULL;
m_cbDelayBuffer = 0;

```



## Related topics

<dl> <dt>

[**Working with Streaming Resources**](working-with-streaming-resources.md)
</dt> </dl>

 

 




