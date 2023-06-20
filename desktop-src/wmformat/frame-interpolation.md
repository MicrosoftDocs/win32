---
title: Frame Interpolation
description: Frame Interpolation
ms.assetid: 74dbe855-361c-42ba-b21b-322ccd1c91d0
keywords:
- Windows Media Format SDK,frame interpolation
- codecs,frame interpolation
- frame interpolation
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Frame Interpolation

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Frame interpolation is the process of creating intermediate video frames based on the data in two consecutive frames of encoded video. In effect, frame interpolation increases the [*frame rate*](wmformat-glossary.md) of encoded video at the time of decoding. You can use frame interpolation to improve the smoothness of playback for video streams with low frame rates.

Because this is a decoding feature, it does not involve any special encoding options and adds no overhead to the content. Frame interpolation is specified as an output setting in the reader object.

Only the Windows Media Video 9 codec supports frame interpolation.

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> <dt>

[**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting)
</dt> <dt>

[**Output Settings**](output-settings.md)
</dt> </dl>

 

 




