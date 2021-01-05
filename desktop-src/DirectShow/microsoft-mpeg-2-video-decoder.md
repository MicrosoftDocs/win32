---
description: This filter decodes MPEG-1, MPEG-2, H.264 video.
ms.assetid: d8195c3a-97ac-4ad1-a097-18878c8fda6f
title: Microsoft MPEG-2 Video Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Microsoft MPEG-2 Video Decoder

This filter decodes MPEG-1, MPEG-2, H.264 video.

> [!Note]  
> Decoding of H.264 video requires Windows 7.

 

> [!Note]  
> This filter is not supported on IA-64-based platforms.

 

In the registry, the friendly name of this filter is "Microsoft DTV-DVD Video Decoder".



Filter Information

Filter Interfaces

[**IAMDecoderCaps**](/windows/desktop/api/Strmif/nn-strmif-iamdecodercaps)<br/> [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)<br/> [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)<br/>

Input Pin Media Types

Video input pin:

-   MEDIATYPE\_DVD\_ENCRYPTED\_PACK, MEDIASUBTYPE\_MPEG2\_VIDEO
-   MEDIATYPE\_MPEG2\_PES, MEDIASUBTYPE\_MPEG2\_VIDEO
-   MEDIATYPE\_Video, MEDIASUBTYPE\_MPEG1Packet
-   MEDIATYPE\_Video, MEDIASUBTYPE\_MPEG1Payload
-   MEDIATYPE\_Video, MEDIASUBTYPE\_MPEG2\_VIDEO

Subpicture input pin:<br/>

-   MEDIATYPE\_DVD\_ENCRYPTED\_PACK, MEDIASUBTYPE\_DVD\_SUBPICTURE

Starting in Windows 7, the video input pin also supports the following input types:<br/>

-   **MEDIATYPE\_Video**, **MEDIASUBTYPE\_AVC1**
-   **MEDIATYPE\_Video**, **MEDIASUBTYPE\_H264**
-   **MEDIATYPE\_Video**, **MEDIASUBTYPE\_h264**
-   **MEDIATYPE\_Video**, **MEDIASUBTYPE\_X264**
-   **MEDIATYPE\_Video**, **MEDIASUBTYPE\_x264**

See [H.264 Video Types](h-264-video-types.md) for more information. The input media type can change dynamically between MPEG2 and H.264 types.<br/>

Input Pin Interfaces

[**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)<br/> [**IKsPropertySet**](ikspropertyset.md)<br/> [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)<br/> [**IMFSampleProtection**](/windows/win32/api/mfidl/nn-mfidl-imfsampleprotection)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/>

Output Pin Media Types

Video output pin:

-   MEDIATYPE\_Video, DXVA\_ModeMPEG2\_A (DXVA 1.0)
-   MEDIATYPE\_Video, DXVA\_ModeMPEG2\_C (DXVA 1.0)
-   MEDIATYPE\_Video, MEDIASUBTYPE\_I420 (Software decode or DXVA2.0)
-   MEDIATYPE\_Video, MEDIASUBTYPE\_NV12 (Software decode or DXVA2.0)
-   MEDIATYPE\_Video, MEDIASUBTYPE\_YUY2 (Software decode or DXVA2.0)
-   MEDIATYPE\_Video, MEDIASUBTYPE\_IMC3 (DXVA2.0 only)
-   MEDIATYPE\_Video, MEDIASUBTYPE\_IMC4 (DXVA2.0 only)
-   MEDIATYPE\_Video, MEDIASUBTYPE\_S340 (DXVA2.0 only)
-   MEDIATYPE\_Video, MEDIASUBTYPE\_YV12 (DXVA2.0 only)

Line-21 output pin:<br/>

-   MEDIATYPE\_AUXLine21Data, MEDIASUBTYPE\_Line21\_GOPPacket

Subpicture output pin:<br/>

-   MEDIATYPE\_Video, MEDIASUBTYPE\_AI44
-   MEDIATYPE\_Video, MEDIASUBTYPE\_ARGB32
-   MEDIATYPE\_Video, MEDIASUBTYPE\_ARGB4444
-   MEDIATYPE\_Video, MEDIASUBTYPE\_AYUV

Output Pin Interfaces

[**IAMVideoAcceleratorNotify**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoacceleratornotify) (video output pin only)<br/> [**IKsPropertySet**](ikspropertyset.md)<br/> [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/> [**IVPConfig**](/previous-versions/windows/desktop/api/Vpconfig/nn-vpconfig-ivpconfig)<br/>

Filter CLSID

**CLSID\_CMPEG2VidDecoderDS** (defined in wmcodecdsp.h)

Executable

msmpeg2vdec.dll

[Merit](merit.md)

**MERIT\_NORMAL** - 1

[Filter Category](filter-categories.md)

**CLSID\_LegacyAmFilterCategory**



 

## Remarks

This filter has two input pins and three output pins.

Input pins:

-   Video input
-   Subpicture input

Output pins:

-   Video output
-   Line-21 output
-   Subpicture output

The filter does not create the subpicture output pin unless the video input pin is connected with a **MEDIATYPE\_DVD\_ENCRYPTED\_PACK** media type.

### MPEG-1/2 Support

For MPEG-1 and MPEG-2, the decoder supports the following formats:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Profiles/Levels</td>
<td>Any combination of the following profiles and levels:<br/>
<ul>
<li>Profiles: Simple, Main</li>
<li>Levels: Low, Main, High, High 1440</li>
</ul></td>
</tr>
<tr class="even">
<td>Chroma Formats</td>
<td>4:2:0 chroma</td>
</tr>
<tr class="odd">
<td>Maximum Resolution</td>
<td>1920 × 1088 pixels</td>
</tr>
<tr class="even">
<td>DXVA</td>
<td>The decoder supports DirectX Video Acceleration (DXVA) version 1 and version 2.</td>
</tr>
</tbody>
</table>



 

The decoder does not support scalable bitstreams. The input must be an elementary video stream.

The decoder does not support 4:2:2 chroma formats.

### H.264 Support

For H.264, the decoder supports the following formats:



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Profiles/Levels    | Baseline, Main, and High profiles, up to level 5.1. (See ITU-T H.264 specification for details.)                                                                                                                                                                          |
| Chroma Formats     | 4:2:0 chroma or monochrome                                                                                                                                                                                                                                                |
| Minimum Resolution | 48 × 48 pixels                                                                                                                                                                                                                                                            |
| Maximum Resolution | 1920 × 1088 pixels                                                                                                                                                                                                                                                        |
| DXVA               | The decoder supports DXVA version 2, but not DXVA version 1. DXVA decoding is supported only for Main-compatible Baseline, Main, and High profile bitstreams. (Main-compatible Baseline bitstreams are defined as **profile\_idc**=66 and **constrained\_set1\_flag**=1.) |



 

The decoder does not support Film Grain Technology.

For information about the H.264 media types, see [H.264 Video Types](h-264-video-types.md).

### Codec Properties

The input pins support the following property sets through [**IKsPropertySet**](ikspropertyset.md):

-   [**DVD Copy Protection Property Set**](dvd-copy-protection-property-set.md)
-   [**DVD Subpicture Property Set**](dvd-subpicture-property-set.md) (subpicture pin only)

The input pins support the following properties through [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi):



| Property                                                                  | Requires      |
|---------------------------------------------------------------------------|---------------|
| [**AVDecCommonInputFormat**](avdeccommoninputformat-property.md)         | Windows Vista |
| [**AVDecVideoInputScanType**](avdecvideoinputscantype-property.md)       | Windows Vista |
| [**AVDecVideoPixelAspectRatio**](avdecvideopixelaspectratio-property.md) | Windows Vista |



 

The filter supports the following properties through [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi):



| Property                                                                                | Requires      |
|-----------------------------------------------------------------------------------------|---------------|
| [**AVDecMmcssClass**](avdecmmcss-property.md)                                          | Windows Vista |
| [**AVDecVideoAcceleration\_H264**](avdecvideoacceleration-h264-property.md)            | Windows 7     |
| [**AVDecVideoAcceleration\_MPEG2**](avdecvideoacceleration-mpeg2-property.md)          | Windows 7     |
| [**AVDecVideoDropPicWithMissingRef**](avdecvideodroppicwithmissingref-property.md)     | Windows 7     |
| [**AVDecVideoFastDecodeMode**](avdecvideofastdecodemode.md)                            | Windows 7     |
| [**AVDecVideoImageSize**](avdecvideoimagesize.md)                                      | Windows 7     |
| [**AVDecVideoSoftwareDeinterlaceMode**](avdecvideosoftwaredeinterlacemode-property.md) | Windows 7     |
| [**AVDecVideoThumbnailGenerationMode**](avdecvideothumbnailgenerationmode-property.md) | Windows 7     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Home Premium, Windows Vista Ultimate, Windows 7 Home Premium, Windows 7 Professional, Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                                     |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl>                                                                                       |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[**DVD Media Types**](dvd-media-types.md)
</dt> <dt>

[H.264 Video Types](h-264-video-types.md)
</dt> </dl>

 

 
