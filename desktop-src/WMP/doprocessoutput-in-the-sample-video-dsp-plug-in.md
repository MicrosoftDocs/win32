---
title: DoProcessOutput in the Sample Video DSP Plug-in
description: DoProcessOutput in the Sample Video DSP Plug-in
ms.assetid: 67536e35-a049-49c8-bd89-fad1fab37e6c
keywords:
- Windows Media Player plug-ins,video DSP
- plug-ins,video DSP
- digital signal processing plug-ins,DoProcessOutput
- DSP plug-ins,DoProcessOutput
- video DSP plug-ins,DoProcessOutput
ms.topic: article
ms.date: 05/31/2018
---

# DoProcessOutput in the Sample Video DSP Plug-in

Because a video DSP plug-in typically supports several video formats, it is convenient to separate the processing implementation code into a separate function for each format. This means that the implementation of **DoProcessOutput** for video DSP plug-ins is relatively simple.

The implementation in the sample plug-in first tests whether the user has enabled the plug-in. If the plug-in is disabled, the code copies the data provided in the input buffer to the output buffer without changing it, as the following code demonstrates:


```C++
// Test whether the plug-in has been disabled by the user.
if (!m_bEnabled)
{
    // Just copy the data without changing it. You should
    // also do any necessary format conversion here.
    memcpy(pbOutputData, pbInputData, m_dwBufferSize);
    *cbBytesProcessed = m_dwBufferSize;

    return S_OK;
}

```



If the plug-in is enabled, the code simply performs a series of checks on the input media type **subtype** member to determine the current video format. When a match is found, the code calls the appropriate processing function.

## Related topics

<dl> <dt>

[**Implementing a Video DSP Plug-in**](implementing-a-video-dsp-plug-in.md)
</dt> </dl>

 

 




