---
description: CC Decoder Filter
ms.assetid: 57ef75f6-411c-4b1f-b0dc-ac293ebc0b9c
title: CC Decoder Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CC Decoder Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!IMPORTANT]
> This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

 

The CC VBI Decoder is a kernel-mode stream class filter. It appears in GraphEdit under the "WDM Streaming VBI Codecs" category. It accepts sample waveforms delivered by a capture filter and delivers decoded closed-captioning data to the [Line 21 Decoder](line-21-decoder-filter.md) and/or to interested applications.

This filter has two input pins, VBI and HWCC. The VBI pin is used for raw VBI data, and the HWCC pin is used when the VBI decoding is performed in hardware by the capture filter. When the data is received on the HWCC pin, the CC Decoder operates in "pass-through" mode, and sends the data directly to the Line 21 Decoder without processing it in any way. If the capture filter exposes an HWCC pin, it must be connected directly to the corresponding pin on the CC Decoder. The pin category is **PINNAME\_VIDEO\_CC\_CAPTURE**.

The CC Decoder has up to eight output pins, each of which can select their own lines and substreams. The first output pin is connected to the Line-21 Decoder.

The CC Decoder filter appears in the "WDM Streaming VBI Codecs" filter category (**AM\_KSCATEGORY\_VBICODEC**).

Because this is a kernel-mode filter, applications cannot create it directly using **CoCreateInstance**. Instead, use the [System Device Enumerator](system-device-enumerator.md). For more information, see [Creating Kernel-Mode Filters](creating-kernel-mode-filters.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Viewing Closed Captions](viewing-closed-captions.md)
</dt> </dl>

 

 



