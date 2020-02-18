---
title: Frame Interpolation
description: Frame Interpolation
ms.assetid: 74dbe855-361c-42ba-b21b-322ccd1c91d0
keywords:
- Windows Media Format SDK,frame interpolation
- codecs,frame interpolation
- frame interpolation
ms.topic: article
ms.date: 05/31/2018
---

# Frame Interpolation

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

 

 




