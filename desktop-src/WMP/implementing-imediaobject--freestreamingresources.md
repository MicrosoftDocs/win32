---
title: Implementing IMediaObject FreeStreamingResources
description: Implementing IMediaObject FreeStreamingResources
ms.assetid: 970dd10b-a7a0-4ba0-97e3-725d5c914500
keywords:
- Windows Media Player plug-ins,Echo sample streaming resources
- plug-ins,Echo sample streaming resources
- digital signal processing plug-ins,Echo sample streaming resources
- DSP plug-ins,Echo sample streaming resources
- Echo DSP plug-in sample,streaming resources
- Echo DSP plug-in sample,releasing memory
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Implementing IMediaObject::FreeStreamingResources

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

It is important that your code releases any allocated memory before the plug-in object is destroyed. Windows Media Player calls **FreeStreamingResources** to allow you to do this. For safety, the sample created by the plug-in wizard includes a call to **FreeStreamingResources** in the **FinalRelease** method to ensure that the memory is freed. You must add the following code to **FreeStreamingResources** for the Echo sample:


```
// Test whether a buffer exists.
if (m_pbDelayBuffer)
{
    delete m_pbDelayBuffer;
    m_pbDelayBuffer = NULL;
    m_pbDelayPointer = NULL;
    m_cbDelayBuffer = 0;
}
```



## Related topics

<dl> <dt>

[**Working with Streaming Resources**](working-with-streaming-resources.md)
</dt> </dl>

 

 




