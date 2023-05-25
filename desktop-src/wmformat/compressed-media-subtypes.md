---
title: Compressed Media Subtypes
description: Compressed Media Subtypes
ms.assetid: 0ed6b4e8-6450-4484-90d6-efa2f9101782
keywords:
- Windows Media Format SDK,media types
- Advanced Systems Format (ASF),media types
- ASF (Advanced Systems Format),media types
- Windows Media Format SDK,compressed media subtypes
- Advanced Systems Format (ASF),compressed media subtypes
- ASF (Advanced Systems Format),compressed media subtypes
- media types,compressed media subtypes
- compressed media subtypes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Compressed Media Subtypes

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table lists the compressed media subtypes. These types are used to identify compressed streams in a file. When you configure a video or audio stream, you will usually use these types.



| Compressed media subtype          | Description                                                                                                                                                                                                                                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMMEDIASUBTYPE\_ACELPnet          | Audio encoded with the Sipro Labs ACELP codec. This audio is normally voice data. (No longer supported for encoding.)                                                                                                                                                                       |
| WMMEDIASUBTYPE\_MP43              | Video encoded by the Microsoft MPEG 4 codec version 3. This codec is no longer supported by the Windows Media Format SDK. If this codec is already installed on a computer, installing the Windows Media Format SDK or the redistribution package on a computer will not remove this codec. |
| WMMEDIASUBTYPE\_MP4S              | Video encoded using the ISO MPEG 4 codec version 1.                                                                                                                                                                                                                                         |
| WMMEDIASUBTYPE\_MPEG2\_VIDEO      | Video encoded to MPEG 2 specifications.                                                                                                                                                                                                                                                     |
| WMMEDIASUBTYPE\_MSS1              | Video encoded with the Windows Media Screen codec version 1.                                                                                                                                                                                                                                |
| WMMEDIASUBTYPE\_MSS2              | Video encoded with the Windows Media Video 9 Screen codec.                                                                                                                                                                                                                                  |
| WMMEDIASUBTYPE\_WMVP              | Video encoded with the Windows Media Video 9 Image codec to transform bitmaps and deformation data into a video stream.                                                                                                                                                                     |
| WMMEDIASUBTYPE\_WVP2              | Video encoded with the Windows Media Video 9 Image v2 codec.                                                                                                                                                                                                                                |
| WMMEDIASUBTYPE\_WMAudio\_Lossless | Audio encoded with the Windows Media Audio 9 Lossless codec or the Windows Media Audio 9.1 codec.                                                                                                                                                                                           |
| WMMEDIASUBTYPE\_WMAudioV2         | Audio encoded with the Windows Media Audio codec version 2. This value is identical to WMMEDIASUBTYPE\_WMAudioV7 and WMMEDIASUBTYPE\_WMAudioV8, because the bitstreams for these codec versions are compatible.                                                                             |
| WMMEDIASUBTYPE\_WMAudioV7         | Audio encoded with the Windows Media Audio codec version 7. This value is identical to WMMEDIASUBTYPE\_WMAudioV2 and WMMEDIASUBTYPE\_WMAudioV8, because the bitstreams for these codec versions are compatible.                                                                             |
| WMMEDIASUBTYPE\_WMAudioV8         | Audio encoded with the Windows Media Audio 8 codec, the Windows Media Audio 9 codec, or the Windows Media Audio 9.1 codec. This value is identical to WMMEDIASUBTYPE\_WMAudioV2 and WMMEDIASUBTYPE\_WMAudioV7, because the bitstreams for these codec versions are compatible.              |
| WMMEDIASUBTYPE\_WMAudioV9         | Audio encoded with the Windows Media Audio 9 Professional codec or the Windows Media Audio 9.1 Professional codec.                                                                                                                                                                          |
| WMMEDIASUBTYPE\_M4S2              | Video encoded with the ISO MPEG4 v1.1 codec.                                                                                                                                                                                                                                                |
| WMMEDIASUBTYPE\_WMSP1             | Audio encoded with the Windows Media Audio 9 Voice codec.                                                                                                                                                                                                                                   |
| WMMEDIASUBTYPE\_WMV1              | Video encoded using the Windows Media Video codec version 7.                                                                                                                                                                                                                                |
| WMMEDIASUBTYPE\_WMV2              | Video encoded using the Windows Media Video 8 codec.                                                                                                                                                                                                                                        |
| WMMEDIASUBTYPE\_WMV3              | Video encoded using the Windows Media Video 9 codec.                                                                                                                                                                                                                                        |
| WMMEDIASUBTYPE\_WMVA              | Video encoded using the version of the Windows Media Video 9 Advanced Profile codec that was released with the Windows Media Format 9 Series SDK.                                                                                                                                           |
| WMMEDIASUBTYPE\_WVC1              | Video encoded using the version of the Windows Media Video 9 Advanced Profile codec that was released with the Windows Media Format 11 SDK. This subtype identifies a bit stream that is compliant with the SMPTE VC-1 standard.                                                            |



 

## Related topics

<dl> <dt>

[**Media Type Identifiers**](media-type-identifiers.md)
</dt> <dt>

[**Media Types**](media-types.md)
</dt> <dt>

[**Uncompressed Media Subtypes**](uncompressed-media-subtypes.md)
</dt> </dl>

 

 




