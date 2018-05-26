---
Description: Setting Audio Capture Properties
ms.assetid: 81400072-91d7-4db4-86d3-d072663e691f
title: Setting Audio Capture Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting Audio Capture Properties

Each input pin on the Audio Capture Filter exposes the [**IAMAudioInputMixer**](/windows/win32/Strmif/nn-strmif-iamaudioinputmixer?branch=master) interface. Use this interface to enable or disable a particular input, by calling the [**IAMAudioInputMixer::put\_Enable**](/windows/win32/Strmif/nf-strmif-iamaudioinputmixer-put_enable?branch=master) method on the pin. Also use this interface to set properties of an input, such as the bass, treble, and volume levels. If you are capturing multiple inputs at once, you can control the overall bass, treble, and volume levels through the **IAMAudioInputMixer** interface on the filter itself.

The available sampling rates and audio formats for capture are determined by the driver. Use the [**IAMStreamConfig**](/windows/win32/Strmif/nn-strmif-iamstreamconfig?branch=master) interface on the Audio Capture Filter's output pin to enumerate the available sampling rates and formats and set the desired format. The filter can connect downstream to any filter that accepts the output pin's media type.

The Audio Capture Filter also exposes the [**IAMBufferNegotiation**](/windows/win32/Strmif/nn-strmif-iambuffernegotiation?branch=master) interface. This interface is useful for controlling the amount of latency in audio preview. By default, the Audio Capture filter uses a half-second buffer size. This buffer size is optimal for capturing but causes a half-second preview delay. To reduce the latency, call the [**IAMBufferNegotiation::SuggestAllocatorProperties**](/windows/win32/Strmif/nf-strmif-iambuffernegotiation-suggestallocatorproperties?branch=master) method before you connect the Audio Capture Filter's output pin. This method takes a pointer to the [**ALLOCATOR\_PROPERTIES**](/windows/win32/strmif/ns-strmif-_allocatorproperties?branch=master) structure. Use the **cbBuffer** member to specify the buffer size, in bytes. An 80 millisecond buffer is generally safe, but buffers of 30 or 40 milliseconds might be sufficient. If the buffers are too small, the sound quality will be degraded.

 

 



