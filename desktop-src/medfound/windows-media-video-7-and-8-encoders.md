---
Description: 'The Windows Media Video 7/8 encoder implements previous versions of the Windows Media Video encoder.'
ms.assetid: 'c4165614-b9ec-4216-b36c-f57bc05e3a8e'
title: 'Windows Media Video 7/8 Encoder'
---

# Windows Media Video 7/8 Encoder

The Windows Media Video 7/8 encoder implements previous versions of the Windows Media Video encoder.

## Class Identifier

The class identifier (CLSID) for the Windows Media Video 7/8 encoder is **CLSID\_CWMVXEncMediaObject**. You can create an instance of the encoder by calling **CoCreateInstance**.

## Interfaces

A video encoder object exposes the [**IMediaObject**](dshow.imediaobject) interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the [**IMFTransform**](imftransform.md) interface so that the object can be used as a Media Foundation Transform (MFT).

A video encoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which a video encoder behaves as a DMO or an MFT.



| Operating system            | Encoder behavior                                                                                                                                                      |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP                  | A Windows Media video encoder always behaves as a DMO.                                                                                                                |
| Windows Vista and Windows 7 | By default, a Windows Media video encoder behaves as a DMO. If you obtain an [**IMFTransform**](imftransform.md) interface on a video encoder, it behaves as an MFT. |



 

## Input Formats

The Windows Media Video encoder supports the following input media subtypes when it is acting as a DMO.

-   MEDIASUBTYPE\_IYUV
-   MEDIASUBTYPE\_I420
-   MEDIASUBTYPE\_YV12
-   MEDIASUBTYPE\_NV11
-   MEDIASUBTYPE\_NV12
-   MEDIASUBTYPE\_YUY2
-   MEDIASUBTYPE\_UYVY
-   MEDIASUBTYPE\_YVYU
-   MEDIASUBTYPE\_RGB32
-   MEDIASUBTYPE\_RGB24
-   MEDIASUBTYPE\_RGB565
-   MEDIASUBTYPE\_RGB555
-   MEDIASUBTYPE\_RGB8
-   MEDIASUBTYPE\_PHOTOMOTION

The Windows Media Video encoder supports the following input media subtypes when it is acting as an MFT.

-   MFVideoFormat\_IYUV
-   MFVideoFormat\_I420
-   MFVideoFormat\_YV12
-   MFVideoFormat\_NV11
-   MFVideoFormat\_NV12
-   MFVideoFormat\_YUY2
-   MFVideoFormat\_UYVY
-   MFVideoFormat\_YVYU
-   MFVideoFormat\_RGB32
-   MFVideoFormat\_RGB24
-   MFVideoFormat\_RGB565
-   MFVideoFormat\_RGB555
-   MFVideoFormat\_RGB8
-   MEDIASUBTYPE\_PHOTOMOTION

## Output Formats

The following table shows the four-character codes (FOURCCs) for the output types supported by the Windows Media Video 7/8 encoder.



| Category              | FOURCC |
|-----------------------|--------|
| Windows Media Video 7 | "WMV1" |
| Windows Media Video 8 | "WMV2" |



 

## Properties

The Windows Media Video 7/8 encoder supports the following properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>MFPKEY_ASFOVERHEADPERFRAME</strong>](mfpkey-asfoverheadperframeproperty.md)</td>
<td>Specifies the overhead, in bytes per packet, required for the container used to store the compressed content.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_AVGFRAMERATE</strong>](mfpkey-avgframerateproperty.md)</td>
<td>Specifies the average frame rate of video content, in frames per second.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_BAVG</strong>](mfpkey-bavgproperty.md)</td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its average bit rate (specified by [<strong>MFPKEY_RAVG</strong>](mfpkey-ravgproperty.md)).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_BMAX</strong>](mfpkey-bmaxproperty.md)</td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its peak bit rate (specified by [<strong>MFPKEY_RMAX</strong>](mfpkey-rmaxproperty.md)).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_BUFFERFULLNESSINFIRSTBYTE</strong>](mfpkey-bufferfullnessinfirstbyteproperty.md)</td>
<td>Specifies whether the encoded video bit stream contains a buffer fullness value with every key frame.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_CODEDFRAMES</strong>](mfpkey-codedframesproperty.md)</td>
<td>Specifies the number of video frames encoded by the codec.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_CODEDNONZEROFRAMES</strong>](mfpkey-codednonzeroframesproperty.md)</td>
<td>Specifies the number of video frames encoded by the codec that actually contain data.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_COMPLEXITY</strong>](mfpkey-complexityproperty.md)</td>
<td>This property is superseded by [<strong>MFPKEY_COMPLEXITYEX</strong>](mfpkey-complexityexproperty.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_COMPLEXITYEX</strong>](mfpkey-complexityexproperty.md)</td>
<td>Specifies the complexity of the encoder algorithm.<br/> <dl> Windows Vista and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_CRISP</strong>](mfpkey-crispproperty.md)</td>
<td>Specifies a numeric representation of the tradeoff between motion smoothness and image quality in codec output.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_DECODERCOMPLEXITYPROFILE</strong>](mfpkey-decodercomplexityprofileproperty.md)</td>
<td>Specifies the device conformance template to which the encoded content conforms.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_DECODERCOMPLEXITYREQUESTED</strong>](mfpkey-decodercomplexityrequestedproperty.md)</td>
<td>Specifies the device conformance template that you want to use for video encoding.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_DROPPEDFRAMES</strong>](mfpkey-droppedframesproperty.md)</td>
<td>Specifies the number of video frames dropped during encoding.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_ENDOFPASS</strong>](mfpkey-endofpassproperty.md)</td>
<td>Specifies the end of an encoding pass.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_FOURCC</strong>](mfpkey-fourccproperty.md)</td>
<td>Specifies the FOURCC that identifies the encoder you want to use.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_INTERLACEDCODINGENABLED</strong>](mfpkey-interlacedcodingenabledproperty.md)</td>
<td>Specifies whether the codec output will be interlaced.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_KEYDIST</strong>](mfpkey-keydistproperty.md)</td>
<td>Specifies the maximum time, in milliseconds, between key frames in the codec output.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_PASSESRECOMMENDED</strong>](mfpkey-passesrecommendedproperty.md)</td>
<td>Specifies the maximum number of passes supported by the codec.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_PASSESUSED</strong>](mfpkey-passesusedproperty.md)</td>
<td>Specifies the number of passes that the codec will use to encode the content.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_PRODUCEDUMMYFRAMES</strong>](mfpkey-producedummyframesproperty.md)</td>
<td>Specifies whether the encoder produces dummy frame entries in the bit stream for duplicate frames.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_QPPERFRAME</strong>](mfpkey-qpperframeproperty.md)</td>
<td>Specifies QP.<br/> <dl> Windows Vista and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_RAVG</strong>](mfpkey-ravgproperty.md)</td>
<td>Specifies the average bit rate, in bits per second, used for 2-pass variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_RMAX</strong>](mfpkey-rmaxproperty.md)</td>
<td>Specifies the peak bit rate, in bits per second, used for constrained 2-pass variable-bit-rate (VBR).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_TOTALFRAMES</strong>](mfpkey-totalframesproperty.md)</td>
<td>Specifies the number of video frames passed to the encoder during the encoding process.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_VBRENABLED</strong>](mfpkey-vbrenabledproperty.md)</td>
<td>Specifies whether the codec will use variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_VBRQUALITY</strong>](mfpkey-vbrqualityproperty.md)</td>
<td>Specifies the actual quality level for quality based (1-pass) variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>MFPKEY_VIDEOWINDOW</strong>](mfpkey-videowindowproperty.md)</td>
<td>Specifies the amount of content, in milliseconds, that can fit into the model buffer.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>MFPKEY_ZEROBYTEFRAMES</strong>](mfpkey-zerobyteframesproperty.md)</td>
<td>Specifies the number of video frames that were skipped because they were duplicates of previous frames.<br/> <dl> Windows XP and later.<br />
Read-only<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmvxencd.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> <dt>

[Video Subtype GUIDs](video-subtype-guids.md)
</dt> </dl>

 

 




