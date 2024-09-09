---
title: To Use Dynamic Range Control
description: To Use Dynamic Range Control
ms.assetid: 719658c1-952f-4e8f-a3ea-bdf89a0a7268
keywords:
- Windows Media Format SDK,dynamic range control
- Windows Media Format SDK,Windows Media Audio 9 Professional codec
- Windows Media Format SDK,Windows Media Audio 9 Lossless codec
- Advanced Systems Format (ASF),Windows Media Audio 9 Professional codec
- ASF (Advanced Systems Format),Windows Media Audio 9 Professional codec
- Advanced Systems Format (ASF),Windows Media Audio 9 Lossless codec
- ASF (Advanced Systems Format),Windows Media Audio 9 Lossless codec
- Advanced Systems Format (ASF),dynamic range control
- ASF (Advanced Systems Format),dynamic range control
- dynamic range control
- codecs,Windows Media Audio 9 Lossless codec
- codecs,Windows Media Audio 9 Professional codec
- Windows Media Audio 9 Lossless codec,dynamic range control
- Windows Media Audio 9 Professional codec,dynamic range control
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Use Dynamic Range Control

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The dynamic range of a piece of audio content is basically the difference between the lowest volume and the maximum volume. If the dynamic range of the content is too high, users may find themselves adjusting the volume repeatedly during playback. For example, movies frequently have a high dynamic range. Often, when the volume is adjusted so that dialog can be understood during quiet scenes, other parts of the movie with music or sound effects are louder than desired.

The Windows Media Audio 9 Professional and Windows Media Audio 9 Lossless codecs support a feature called dynamic range control. At encode time, the codec calculates the peak and average amplitude values in the content, and the writer object stores these values in the metadata for the stream when encoding is finished. Optionally, an application can also write "target" values as metadata that player applications and the decoder can use as hints when playing back the file. At playback time, an application can specify the level of dynamic range control to apply to the audio stream.

Windows Media Player implements dynamic range control as the Quiet Mode feature.

## When to Use Dynamic Range Control

Dynamic range control can alter the sound of the content. For that reason, you should not configure your application to use dynamic range control automatically. Instead, provide users with the ability to turn dynamic range control on or off as needed.

## Using Dynamic Range Control

At playback time, dynamic range control is activated using the output setting g\_wszDynamicRangeControl. Use [**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting) to configure the setting. A value of zero (the default) indicates that the dynamic range should not be altered. A value of 1 or 2 signals the codec to perform dynamic range control, where 1 is a moderate level of dynamic range compression, and 2 is a high level of dynamic range compression.

At encoding time or playback time, you can give the codec target PCM values for the peak and average levels by setting the [**WM/WMADRCPeakTarget**](wm-wmadrcpeaktarget.md) and [**WM/WMADRCAverageTarget**](wm-wmadrcaveragetarget.md) attributes, respectively. These values are stored as metadata attributes and should be accessed using the methods of the [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) interface. When you encode an audio stream using the professional or lossless codec, the [**WM/WMADRCPeakReference**](wm-wmadrcpeakreference.md) and [**WM/WMADRCAverageReference**](wm-wmadrcaveragereference.md) attributes are set automatically to the peak and average levels of the original content. The target values are set to the same values as the references by default.

The decoder at playback time calculates the dynamic range based on the selected level of dynamic range control and the target values (if any are specified). The possible ranges are shown in the following table.



| Settings                                                                | Range of delivered audio                                                                                                     |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| g\_wszDynamicRangeControl = 0 (Any target values)                       | Same range as the original content.                                                                                          |
| g\_wszDynamicRangeControl = 1 (Target values equal to reference values) | Average level is maintained and peaks are confined to the average +12 dB.                                                    |
| g\_wszDynamicRangeControl = 2 (Target values equal to reference values) | Average level is maintained and peaks are confined to the average +6 dB.                                                     |
| g\_wszDynamicRangeControl = 1 (Target values specified)                 | Average level set to the target average value and peaks confined to the target peak value.                                   |
| g\_wszDynamicRangeControl = 2 (Target values specified)                 | Average level set to the target average value and peaks confined to the median of the target average and target peak values. |



 

Note that dynamic range control is a feature of decoding only and exists only as metadata in the file itself. These settings have no effect on the content stored in the file unless you specifically instruct the decoder to use them. The Windows Media Format SDK provides no methods for modifying the dynamic range of the audio data at encoding time.

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> </dl>

 

 




