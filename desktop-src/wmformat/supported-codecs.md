---
title: Supported Codecs
description: Supported Codecs
ms.assetid: d5907d38-2e26-442e-a0d1-1d7e267b9948
keywords:
- Windows Media Format SDK,codecs supported
- Windows Media Format SDK,IWMCodecInfo3 interface
- codecs,supported
- IWMCodecInfo3,about
- codecs,IWMCodecInfo3 interface
ms.topic: article
ms.date: 05/31/2018
---

# Supported Codecs

The Windows Media Format SDK provides support for the following codecs which are included when you install the SDK.




| Codec | Description | 
|-------|-------------|
| Windows Media Audio | Audio codec for general use in encoding complex audio, like music.The most recent versions of this codec are the Windows Media Audio 9 codec and the Windows Media Audio 9.1 codec.<br /> | 
| Windows Media Audio Professional | Audio codec for complex audio, like music. Supports multichannel and 24-bit encoding.There are two versions of this codec:<br /><ul><li>Windows Media Audio 9 Professional</li><li>Windows Media Audio 9.1 Professional</li></ul> | 
| Windows Media Audio Lossless | Audio codec for lossless encoding.There are two versions of this codec:<br /><ul><li>Windows Media Audio 9 Lossless</li><li>Windows Media Audio 9.1 Lossless</li></ul> | 
| Windows Media Audio 9 Voice | Audio codec optimized for encoding the human voice at high compression ratios. This is the preferred codec for streams consisting mostly of spoken words. For content that is mixed music and speech, this codec can dynamically change the encoding algorithm used to get optimal quality. | 
| Windows Media Video 9 | Video codec for general use in encoding complex video, such as movies. | 
| Windows Media Video 9 Advanced Profile | Video codec incorporating advanced encoding features, including interlaced encoding. | 
| Windows Media Video 9 Screen | Video codec optimized for encoding sequential screenshots. This codec is often used for software training or support by recording monitor images as computer applications are used. | 
| Windows Media Video Image | Video codec for converting bitmap images with deformation information into compressed video.There are two version of this codec:<br /><ul><li>Windows Media Video 9 Image</li><li>Windows Media Video 9 Image v2</li></ul> | 




 

Different versions of the Windows Media Audio and Video codecs are available for encoding depending on the version of the Windows Media Format SDK that you install. When you use the methods if the [**IWMCodecInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo3) interface to enumerate codecs and codec formats, only the latest supported versions are enumerated.

## Related topics

<dl> <dt>

[**Choosing an Encoding Method**](choosing-an-encoding-method.md)
</dt> <dt>

[**Codec Features**](codec-features.md)
</dt> </dl>

 

 





