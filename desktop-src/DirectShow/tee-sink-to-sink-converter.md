---
description: Tee/Sink-to-Sink Converter
ms.assetid: 8ee5e20c-f37a-4a9b-9382-2ed94333c6ec
title: Tee/Sink-to-Sink Converter
ms.topic: article
ms.date: 05/31/2018
---

# Tee/Sink-to-Sink Converter

The Tee/Sink-to-Sink Converter is a kernel-mode, KsProxy-based filter. It is used in analog video television filter graphs where VBI data is being rendered or captured. The filter is connected upstream to the [WDM Video Capture Filter](wdm-video-capture-filter.md) and provides an efficient means to duplicate streams of data within kernel mode without the expensive transitions between kernel and user mode. It delivers each received data block to all output pins, and the downstream codec is responsible for finding the specific VBI data to decode.

The Tee/Sink-to-Sink Converter appears in the "WDM Streaming Tee/Splitter Devices" filter category (AM\_KSCATEGORY\_SPLITTER).

Because this is a kernel-mode filter, applications cannot create it directly using [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance). Instead, use the [System Device Enumerator](system-device-enumerator.md). For more information, see [Creating Kernel-Mode Filters](creating-kernel-mode-filters.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 
