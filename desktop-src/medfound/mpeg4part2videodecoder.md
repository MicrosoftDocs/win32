---
description: The MPEG4 Part 2 Video decoder decodes video streams that were encoded according to the MPEG4 Part 2 standard.
ms.assetid: 56e32d3c-9bd0-41fe-bb22-e4ff37b7cc5c
title: MPEG-4 Part 2 Video Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MPEG-4 Part 2 Video Decoder

The MPEG4 Part 2 Video decoder decodes video streams that were encoded according to the MPEG4 Part 2 standard.

You can create an instance of the MPEG4 Part 2 Video decoder by calling **CoCreateInstance**. To create an instance of the decoder that behaves as a DirectX Media Object (DMO), use the class identifier **CLSID\_CMpeg4sDecMediaObject**. To create an istance of the decoder that behaves as a Media Foundation Transform (MFT), use the class identifier **CLSID\_CMpeg4sDecMFT**.

## Input Types

The MPEG4 Part 2 Video decoder supports the following input media types.

-   MEDIASUBTYPE\_M4S2
-   MEDIASUBTYPE\_m4s2
-   MEDIASUBTYPE\_MP4V
-   MEDIASUBTYPE\_mp4v
-   MEDIASUBTYPE\_MP4S (deprecated)
-   MEDIASUBTYPE\_mp4s (deprecated)

## Output Types

The MPEG4 Part 2 Video decoder supports the following output media subtypes when it is acting as a DMO.

-   MEDIASUBTYPE\_YV12
-   MEDIASUBTYPE\_NV12
-   MEDIASUBTYPE\_YUY2
-   MEDIASUBTYPE\_UYVY
-   MEDIASUBTYPE\_YVYU
-   MEDIASUBTYPE\_NV11
-   MEDIASUBTYPE\_RGB32
-   MEDIASUBTYPE\_RGB24
-   MEDIASUBTYPE\_ RGB565
-   MEDIASUBTYPE\_RGB555
-   MEDIASUBTYPE\_RGB8

The MPEG4 Part 2 Video decoder supports the following output media subtypes when it is acting as an MFT.

-   MEDIASUBTYPE\_NV12
-   MEDIASUBTYPE\_YV12

## Formats

The MPEG4 Part 2 Video decoder accepts the following formats.

-   [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader)
-   [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) (VIH2)
-   [**MFVideoInfo**](/windows/desktop/api/mfobjects/ns-mfobjects-mfvideoinfo)
-   [**MPEG2VIDEOINFO**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-mpeg2videoinfo) (Only the VIH2 portion of the header is used.)

## Interfaces for the DMO

If you create an instance of the MPEG4 Part 2 Video decoder as a DMO, the decoder exposes the following interfaces.

-   [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject)
-   [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi)

You can obtain an [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject) interface by calling **CoCreateInstance**, and you can obtain an [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface by calling **QueryInterface**.

## Interfaces for the MFT

If you create an instance of the MPEG2 Part 2 Video decoder as an MFT, the decoder exposes the following interfaces.

-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
-   [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes)
-   [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)
-   [**IMFQualityAdvise2**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2)
-   [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol)
-   [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)

You can obtain a pointer to the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface by calling **CoCreateInstance**, and you can obtain a pointer to the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface by calling [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes). You can obtain a pointer to the [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise) or [**IMFQualityAdvise2**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2) interface by calling **QueryInterface** on the MFT. You can obtain a pointer to the [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol) or [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) interface by calling [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) and passing the service identifier **MF\_RATE\_CONTROL\_SERVICE**.

## Profiles and Levels

The MPEG4 specification defines several profiles, each of which specifies the tools that an encoder can use to generate an encoded stream. The MPEG4 Part2 Video Decoder supports two of those profiles: Simple Visual Profile and Advanced Simple Profile. In other words, the MPEG4 Part 2 Video decoder can decode streams that were encoded according to either the Simple Visual Profile or the Advanced Simple Profile.

The Simple Visual Profile supports basic transmission of low bit-rate video in progressive mode. It supports only Intra and Prediction pictures. It also supports the short header mode, which is backward compatible with the H.263 baseline profile. Starting with Windows 10, the MPEG-4 Part 2 Video Decoder also supports H.263v2 (H.263+) which supports custom picture sizes.

The Advanced Simple Profile supports all the tools of the Simple Visual Profile and, in addition, supports interlaced video, B-frames, quarter-pel motion compensation, additional quantization tables, and global motion compensation.

The MPEG4 specification also defines several levels, each of which specifies constraints on the output stream generated by an encoder.

The following table shows the profiles and levels, along with typical resolutions, supported by the MPEG4 Part 2 Video decoder.



| Profile         | Level | Typical Resolution |
|-----------------|-------|--------------------|
| Simple Visual   | 0     | 176 x 144          |
| Simple Visual   | 1     | 176 x 144          |
| Simple Visual   | 2     | 352 x 288          |
| Simple Visual   | 3     | 352 x 288          |
| SimpleVisual    | 4a    | 640 x 480          |
| Simple Visual   | 5     | 720 x 576          |
| Advanced Simple | 0     | 176 x 144          |
| Advanced Simple | 1     | 176 x 144          |
| Advanced Simple | 2     | 352 x 288          |
| Advanced Simple | 3     | 352 x 288          |
| Advanced Simple | 3b    | 352 x 288          |
| Advanced Simple | 4     | 352 x 756          |
| Advanced Simple | 5     | 720 x 576          |



 

For more information about profiles and levels, see the MPEG4 Part 2 specification (ISO/IEC 14496-2): Information technology -- Coding of audio-visual objects -- Part 2: Visual.

## Decoder Properties

To set properties on the MPEG4 Part 2 Video decoder, use the [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi) interface or the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface.

The MPEG4 Part 2 Video decoder supports the following properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
<th>Default Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/DirectShow/avdecvideoswpowerlevel-property"><strong>CODECAPI_AVDecVideoSWPowerLevel</strong></a></td>
<td>Specifies the power level.<br/> <dl> Windows 7.<br />
Write-only.<br />
</dl></td>
<td>100</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/DirectShow/avdecvideothumbnailgenerationmode-property"><strong>CODECAPI_AVDecVideoThumbnailGenerationMode</strong></a></td>
<td>Specifies the thumbnail generation mode.<br/> <dl> Windows 7.<br />
Write-only.<br />
</dl></td>
<td><strong>VARIANT_FALSE</strong></td>
</tr>
</tbody>
</table>



 

## Remarks

The globally unique identifiers (GUIDs) for RGB media subtypes differ depending on whether a decoder is acting as a DMO or an MFT. The GUIDs for non-RGB media subtypes are the same, regardless of whether a decoder is acting as a DMO or an MFT. For information about the GUIDs that represent media subtypes, see [Media Types](media-types.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MP4SDecd.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 
