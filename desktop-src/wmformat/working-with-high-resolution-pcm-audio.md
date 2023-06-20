---
title: Working with High-Resolution PCM Audio
description: Working with High-Resolution PCM Audio
ms.assetid: 422a78f9-0f43-4edb-acaf-7f6e3f4a1cb8
keywords:
- Advanced Systems Format (ASF),high-resolution PCM audio
- ASF (Advanced Systems Format),high-resolution PCM audio
- profiles,high-resolution PCM audio
- codecs,high-resolution PCM audio
- Advanced Systems Format (ASF),PCM audio
- ASF (Advanced Systems Format),PCM audio
- profiles,PCM audio
- codecs,PCM audio
- high-resolution PCM audio
- PCM audio
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with High-Resolution PCM Audio

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some of the input formats for the Windows Media Audio 9 Professional codec and the Windows Media Audio 9 Lossless codec are high-resolution PCM formats. These are PCM formats that have more than two channels, or more than 16 bits per sample (audio with more than two channels is also called multichannel audio).

These formats are configured by using a structured extension of the [**WAVEFORMATEX**](/previous-versions/windows/desktop/legacy/dd757720(v=vs.85)) structure, called [**WAVEFORMATEXTENSIBLE**](/previous-versions/windows/desktop/legacy/dd757721(v=vs.85)). The **WAVEFORMATEXTENSIBLE** structure includes information about the channels included in the audio. This structure is required when using high-resolution PCM audio, because some Windows APIs will not accept **WAVEFORMATEX** structures that contain high-resolution values.

High-resolution PCM formats have 22 bytes of extended data, which is specified in the **cbSize** member of the **WAVEFORMATEX** structure. High-resolution Windows Media audio formats do not use the **WAVEFORMATEXTENSIBLE** structure, but do have extended data appended to the **WAVEFORMATEX** structure.

The Windows Media audio codecs only support decoding to high-resolution PCM formats when the application is running on Windows XP or later. On previous versions of Microsoft Windows, the codecs decode to a format with a maximum of 16 bits per sample and 2 channels. In addition, you must specify that you want the codec to decode to high-definition PCM by setting the g\_wszEnableDiscreteOutput output setting to **TRUE** using the [**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting) method. After making this call, the outputs enumerated by the reader will include high-definition formats.

Multichannel audio requires more configuration. For more information, see [Reading Multichannel Audio](reading-multichannel-audio.md).

## Related topics

<dl> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> </dl>

 

 