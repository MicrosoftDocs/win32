---
description: Setting Audio Capture Properties
ms.assetid: 81400072-91d7-4db4-86d3-d072663e691f
title: Setting Audio Capture Properties
ms.topic: article
ms.date: 05/31/2018
---

# Setting Audio Capture Properties

Each input pin on the Audio Capture Filter exposes the [**IAMAudioInputMixer**](/windows/desktop/api/Strmif/nn-strmif-iamaudioinputmixer) interface. Use this interface to enable or disable a particular input, by calling the [**IAMAudioInputMixer::put\_Enable**](/windows/desktop/api/Strmif/nf-strmif-iamaudioinputmixer-put_enable) method on the pin. Also use this interface to set properties of an input, such as the bass, treble, and volume levels. If you are capturing multiple inputs at once, you can control the overall bass, treble, and volume levels through the **IAMAudioInputMixer** interface on the filter itself.

The available sampling rates and audio formats for capture are determined by the driver. Use the [**IAMStreamConfig**](/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig) interface on the Audio Capture Filter's output pin to enumerate the available sampling rates and formats and set the desired format. The filter can connect downstream to any filter that accepts the output pin's media type.

The Audio Capture Filter also exposes the [**IAMBufferNegotiation**](/windows/desktop/api/Strmif/nn-strmif-iambuffernegotiation) interface. This interface is useful for controlling the amount of latency in audio preview. By default, the Audio Capture filter uses a half-second buffer size. This buffer size is optimal for capturing but causes a half-second preview delay. To reduce the latency, call the [**IAMBufferNegotiation::SuggestAllocatorProperties**](/windows/desktop/api/Strmif/nf-strmif-iambuffernegotiation-suggestallocatorproperties) method before you connect the Audio Capture Filter's output pin. This method takes a pointer to the [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure. Use the **cbBuffer** member to specify the buffer size, in bytes. An 80 millisecond buffer is generally safe, but buffers of 30 or 40 milliseconds might be sufficient. If the buffers are too small, the sound quality will be degraded.

 

 



