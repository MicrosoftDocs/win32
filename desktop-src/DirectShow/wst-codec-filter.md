---
description: WST Codec Filter
ms.assetid: 0a06acbf-b842-4ab6-bcf9-d2d006301d83
title: WST Codec Filter
ms.topic: article
ms.date: 05/31/2018
---

# WST Codec Filter

> [!IMPORTANT]
> This component has been removed from Windows Vista and later operating systems. It is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems.

 

Starting in Windows Vista, this filter is replaced by the VBICodec filter, which is documented in the Microsoft TV Technologies documentation.

World Standard Teletext (WST) is the European standard for data transmission using VBI on PAL analog television signals. Both captioning and data services are provided using this standard. The WST Codec is a kernel-mode filter that receives raw VBI samples and, optionally, decoded Teletext samples from the Capture Filter via the [Tee/Sink-to-Sink Converter](tee-sink-to-sink-converter.md) filter. This codec decodes and/or duplicates the decoded and forward-error-corrected Teletext data for the [WST Decoder](wst-decoder-filter.md) filter. The WST Codec corresponds to the CC Decoder filter for NTSC transmissions. The WST Decoder corresponds to the [Line 21 Decoder](line-21-decoder-filter.md) for NTSC; these filters create the bitmaps that are sent to the Overlay Mixer or the Video Mixing Renderer.

This filter has two input pins, VBI and HWCC. The VBI pin is used for raw VBI data, and the HWCC pin is used when the VBI decoding is performed in hardware by the capture filter. When the data is received on the HWCC pin, the WST Codec operates in "pass-through" mode, and sends the data directly to the WST Decoder without processing it in any way. If the capture filter exposes an HWCC pin, it must be connected directly to the corresponding pin on the WST Codec.

The WST Codec filter appears in the "WDM Streaming VBI Codecs" filter category (**AM\_KSCATEGORY\_VBICODEC**).

Because this is a kernel-mode filter, applications cannot create it directly using **CoCreateInstance**. Instead, use the [System Device Enumerator](system-device-enumerator.md). For more information, see [Creating Kernel-Mode Filters](creating-kernel-mode-filters.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Viewing World Standard Teletext](viewing-world-standard-teletext.md)
</dt> </dl>

 

 



