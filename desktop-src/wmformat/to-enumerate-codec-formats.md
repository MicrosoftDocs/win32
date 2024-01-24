---
title: To Enumerate Codec Formats
description: To Enumerate Codec Formats
ms.assetid: 4441b3f8-3edd-441f-8df8-6281937903e0
keywords:
- streams,enumerating codec formats
- codecs,enumerations
- streams,codec formats
- codecs,formats
- codecs,IWMCodecInfo interface
- IWMCodecInfo,codec formats
- codecs,IWMCodecInfo3 interface
- IWMCodecInfo3,codec formats
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Enumerate Codec Formats

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A codec format is a stream configuration object populated with data from a codec. Each codec format contains a media configuration supported by the codec. Most audio codecs support a finite number of formats, each of which is enumerated by the codec and can be accessed using the methods of [**IWMCodecInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo). Video codecs, on the other hand, provide only a single format. This is because video streams have variables, like frame size, that are more flexible than the settings of an audio stream. With a video stream, you must fill in some of the stream configuration values; audio stream configurations should only be edited to assign a name, connection name, and stream number. For more information, see [Configuration Common to All Streams](configuration-common-to-all-streams.md).

The codec formats enumerated depend upon the current codec enumeration settings, which are set using [**IWMCodecInfo3::SetCodecEnumerationSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcodecinfo3-setcodecenumerationsetting). Currently, only two codec properties are supported: g\_wszNumPasses, which specifies the number of encoding passes that the codec will perform, and g\_wszVBREnabled, which specifies whether the codec will use variable bit rate encoding. The maximum number of encoding passes supported by any of the codecs is two, so there are four distinct configurations for which you can retrieve codecs, as shown in the following table.



|    &nbsp;    | Constant bit rate (CBR) stream | 2-pass CBR stream | Quality-based variable bit rate (VBR) stream | Bit-rate-based VBR stream (constrained or unconstrained) |
|------------------|--------------------------------|-------------------|----------------------------------------------|----------------------------------------------------------|
| g\_wszVBREnabled | FALSE                          | FALSE             | TRUE                                         | TRUE                                                     |
| g\_wszNumPasses  | 1                              | 2                 | 1                                            | 2                                                        |



 

To enumerate the formats supported for a codec, use [**IWMCodecInfo::GetCodecFormatCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmcodecinfo-getcodecformatcount) to find the number of supported codecs. Then call [**IWMCodecInfo::GetCodecFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcodecinfo-getcodecformat) for each format. The format indexes range from zero, to one less than the total number of supported formats. You can retrieve a description of the format by calling [**IWMCodecInfo2::GetCodecFormatDesc**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcodecinfo2-getcodecformatdesc). When using **GetCodecFormatDesc**, you do not need to use **GetCodecFormat**, because the stream configuration object is retrieved by both methods. Video codec formats do not include a description. Each video codec has only one format that is used for all streams of that type.

When you retrieve a codec format, you get the [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig) interface of a stream configuration object containing the format settings.

## Related topics

<dl> <dt>

[**Getting Stream Configuration Information from Codecs**](getting-stream-configuration-information-from-codecs.md)
</dt> </dl>

 

 




