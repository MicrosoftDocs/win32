---
description: Tee/Sink-to-Sink Converter
ms.assetid: 8ee5e20c-f37a-4a9b-9382-2ed94333c6ec
title: Tee/Sink-to-Sink Converter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Tee/Sink-to-Sink Converter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Tee/Sink-to-Sink Converter is a kernel-mode, KsProxy-based filter. It is used in analog video television filter graphs where VBI data is being rendered or captured. The filter is connected upstream to the [WDM Video Capture Filter](wdm-video-capture-filter.md) and provides an efficient means to duplicate streams of data within kernel mode without the expensive transitions between kernel and user mode. It delivers each received data block to all output pins, and the downstream codec is responsible for finding the specific VBI data to decode.

The Tee/Sink-to-Sink Converter appears in the "WDM Streaming Tee/Splitter Devices" filter category (AM\_KSCATEGORY\_SPLITTER).

Because this is a kernel-mode filter, applications cannot create it directly using [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance). Instead, use the [System Device Enumerator](system-device-enumerator.md). For more information, see [Creating Kernel-Mode Filters](creating-kernel-mode-filters.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 
