---
title: Media Type Identifiers for Windows Media Format SDK
description: Learn about media type identifiers used to define the format of media used with the Windows Media Format SDK.
ms.assetid: 5d903953-cd6b-4fba-b877-8c7ad3aeb87d
keywords:
- Windows Media Format SDK,media type identifiers
- Advanced Systems Format (ASF),media type identifiers
- ASF (Advanced Systems Format),media type identifiers
- media types,identifiers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media Type Identifiers for the Windows Media Format SDK

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must use media types to define the format of media used with the Windows Media Format SDK. For descriptions of the various media types, see [Media Types](media-types.md).

The following table lists the global identifiers for all supported media types and their corresponding GUID values.



| Global media type identifier      | GUID                                 |
|-----------------------------------|--------------------------------------|
| MEDIASUBTYPE\_I420                | 30323449-0000-0010-8000-00AA00389B71 |
| MEDIASUBTYPE\_IYUV                | 56555949-0000-0010-8000-00AA00389B71 |
| MEDIASUBTYPE\_RGB1                | e436eb78-524f-11ce-9f53-0020af0ba770 |
| MEDIASUBTYPE\_RGB24               | e436eb7d-524f-11ce-9f53-0020af0ba770 |
| MEDIASUBTYPE\_RGB32               | e436eb7e-524f-11ce-9f53-0020af0ba770 |
| MEDIASUBTYPE\_RGB4                | e436eb79-524f-11ce-9f53-0020af0ba770 |
| MEDIASUBTYPE\_RGB555              | e436eb7c-524f-11ce-9f53-0020af0ba770 |
| MEDIASUBTYPE\_RGB565              | e436eb7b-524f-11ce-9f53-0020af0ba770 |
| MEDIASUBTYPE\_RGB8                | e436eb7a-524f-11ce-9f53-0020af0ba770 |
| MEDIASUBTYPE\_UYVY                | 59565955-0000-0010-8000-00AA00389B71 |
| MEDIASUBTYPE\_VIDEOIMAGE          | 1d4a45f2-e5f6-4b44-8388-f0ae5c0e0c37 |
| MEDIASUBTYPE\_YUY2                | 32595559-0000-0010-8000-00AA00389B71 |
| MEDIASUBTYPE\_YV12                | 31313259-0000-0010-8000-00AA00389B71 |
| MEDIASUBTYPE\_YVU9                | 39555659-0000-0010-8000-00AA00389B71 |
| MEDIASUBTYPE\_YVYU                | 55595659-0000-0010-8000-00AA00389B71 |
| WMFORMAT\_MPEG2Video              | e06d80e3-db46-11cf-b4d1-00805f6cbbea |
| WMFORMAT\_Script                  | 5C8510F2-DEBE-4ca7-BBA5-F07A104F8DFF |
| WMFORMAT\_VideoInfo               | 05589f80-c356-11ce-bf01-00aa0055595a |
| WMFORMAT\_WaveFormatEx            | 05589f81-c356-11ce-bf01-00aa0055595a |
| WMFORMAT\_WebStream               | da1e6b13-8359-4050-b398-388e965bf00c |
| WMMEDIASUBTYPE\_ACELPnet          | 00000130-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_Base              | 00000000-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_DRM               | 00000009-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_MP3               | 00000055-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_MP43              | 3334504D-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_MP4S              | 5334504D-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_M4S2              | 3253344D-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_P422              | 32323450-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_MPEG2\_VIDEO      | e06d8026-db46-11cf-b4d1-00805f6cbbea |
| WMMEDIASUBTYPE\_MSS1              | 3153534D-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_MSS2              | 3253534D-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_PCM               | 00000001-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WebStream         | 776257d4-c627-41cb-8f81-7ac7ff1c40cc |
| WMMEDIASUBTYPE\_WMAudio\_Lossless | 00000163-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMAudioV2         | 00000161-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMAudioV7         | 00000161-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMAudioV8         | 00000161-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMAudioV9         | 00000162-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMSP1             | 0000000A-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMV1              | 31564D57-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMV2              | 32564D57-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMV3              | 33564D57-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMVA              | 41564D57-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WMVP              | 50564D57-0000-0010-8000-00AA00389B71 |
| WMMEDIASUBTYPE\_WVP2              | 32505657-0000-0010-8000-00AA00389B71 |
| WMMEDIATYPE\_Audio                | 73647561-0000-0010-8000-00AA00389B71 |
| WMMEDIATYPE\_FileTransfer         | D9E47579-930E-4427-ADFC-AD80F290E470 |
| WMMEDIATYPE\_Image                | 34A50FD8-8AA5-4386-81FE-A0EFE0488E31 |
| WMMEDIATYPE\_Script               | 73636d64-0000-0010-8000-00AA00389B71 |
| WMMEDIATYPE\_Text                 | 9BBA1EA7-5AB2-4829-BA57-0940209BCF3E |
| WMMEDIATYPE\_Video                | 73646976-0000-0010-8000-00AA00389B71 |
| WMSCRIPTTYPE\_TwoStrings          | 82f38a70-c29f-11d1-97ad-00a0c95ea850 |



 

## Related topics

<dl> <dt>

[**GUID Values**](guid-values.md)
</dt> <dt>

[**Media Types**](media-types.md)
</dt> </dl>

 

 




