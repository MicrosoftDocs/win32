---
Description: The Windows Media Video 7/8 encoder implements previous versions of the Windows Media Video encoder.
ms.assetid: c4165614-b9ec-4216-b36c-f57bc05e3a8e
title: Windows Media Video 7/8 Encoder
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Video 7/8 Encoder

The Windows Media Video 7/8 encoder implements previous versions of the Windows Media Video encoder.

## Class Identifier

The class identifier (CLSID) for the Windows Media Video 7/8 encoder is **CLSID\_CWMVXEncMediaObject**. You can create an instance of the encoder by calling **CoCreateInstance**.

## Interfaces

A video encoder object exposes the [**IMediaObject**](https://msdn.microsoft.com/en-us/library/Dd406926(v=VS.85).aspx) interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface so that the object can be used as a Media Foundation Transform (MFT).

A video encoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which a video encoder behaves as a DMO or an MFT.



| Operating system            | Encoder behavior                                                                                                                                                      |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP                  | A Windows Media video encoder always behaves as a DMO.                                                                                                                |
| Windows Vista and Windows 7 | By default, a Windows Media video encoder behaves as a DMO. If you obtain an [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface on a video encoder, it behaves as an MFT. |



 

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
<td><a href="mfpkey-asfoverheadperframeproperty"><strong>MFPKEY_ASFOVERHEADPERFRAME</strong></a></td>
<td>Specifies the overhead, in bytes per packet, required for the container used to store the compressed content.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-avgframerateproperty"><strong>MFPKEY_AVGFRAMERATE</strong></a></td>
<td>Specifies the average frame rate of video content, in frames per second.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-bavgproperty"><strong>MFPKEY_BAVG</strong></a></td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its average bit rate (specified by <a href="mfpkey-ravgproperty"><strong>MFPKEY_RAVG</strong></a>).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-bmaxproperty"><strong>MFPKEY_BMAX</strong></a></td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its peak bit rate (specified by <a href="mfpkey-rmaxproperty"><strong>MFPKEY_RMAX</strong></a>).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-bufferfullnessinfirstbyteproperty"><strong>MFPKEY_BUFFERFULLNESSINFIRSTBYTE</strong></a></td>
<td>Specifies whether the encoded video bit stream contains a buffer fullness value with every key frame.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-codedframesproperty"><strong>MFPKEY_CODEDFRAMES</strong></a></td>
<td>Specifies the number of video frames encoded by the codec.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-codednonzeroframesproperty"><strong>MFPKEY_CODEDNONZEROFRAMES</strong></a></td>
<td>Specifies the number of video frames encoded by the codec that actually contain data.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-complexityproperty"><strong>MFPKEY_COMPLEXITY</strong></a></td>
<td>This property is superseded by <a href="mfpkey-complexityexproperty"><strong>MFPKEY_COMPLEXITYEX</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-complexityexproperty"><strong>MFPKEY_COMPLEXITYEX</strong></a></td>
<td>Specifies the complexity of the encoder algorithm.<br/> <dl> Windows Vista and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-crispproperty"><strong>MFPKEY_CRISP</strong></a></td>
<td>Specifies a numeric representation of the tradeoff between motion smoothness and image quality in codec output.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-decodercomplexityprofileproperty"><strong>MFPKEY_DECODERCOMPLEXITYPROFILE</strong></a></td>
<td>Specifies the device conformance template to which the encoded content conforms.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-decodercomplexityrequestedproperty"><strong>MFPKEY_DECODERCOMPLEXITYREQUESTED</strong></a></td>
<td>Specifies the device conformance template that you want to use for video encoding.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-droppedframesproperty"><strong>MFPKEY_DROPPEDFRAMES</strong></a></td>
<td>Specifies the number of video frames dropped during encoding.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-endofpassproperty"><strong>MFPKEY_ENDOFPASS</strong></a></td>
<td>Specifies the end of an encoding pass.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-fourccproperty"><strong>MFPKEY_FOURCC</strong></a></td>
<td>Specifies the FOURCC that identifies the encoder you want to use.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-interlacedcodingenabledproperty"><strong>MFPKEY_INTERLACEDCODINGENABLED</strong></a></td>
<td>Specifies whether the codec output will be interlaced.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-keydistproperty"><strong>MFPKEY_KEYDIST</strong></a></td>
<td>Specifies the maximum time, in milliseconds, between key frames in the codec output.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-passesrecommendedproperty"><strong>MFPKEY_PASSESRECOMMENDED</strong></a></td>
<td>Specifies the maximum number of passes supported by the codec.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-passesusedproperty"><strong>MFPKEY_PASSESUSED</strong></a></td>
<td>Specifies the number of passes that the codec will use to encode the content.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-producedummyframesproperty"><strong>MFPKEY_PRODUCEDUMMYFRAMES</strong></a></td>
<td>Specifies whether the encoder produces dummy frame entries in the bit stream for duplicate frames.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-qpperframeproperty"><strong>MFPKEY_QPPERFRAME</strong></a></td>
<td>Specifies QP.<br/> <dl> Windows Vista and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-ravgproperty"><strong>MFPKEY_RAVG</strong></a></td>
<td>Specifies the average bit rate, in bits per second, used for 2-pass variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-rmaxproperty"><strong>MFPKEY_RMAX</strong></a></td>
<td>Specifies the peak bit rate, in bits per second, used for constrained 2-pass variable-bit-rate (VBR).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-totalframesproperty"><strong>MFPKEY_TOTALFRAMES</strong></a></td>
<td>Specifies the number of video frames passed to the encoder during the encoding process.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-vbrenabledproperty"><strong>MFPKEY_VBRENABLED</strong></a></td>
<td>Specifies whether the codec will use variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-vbrqualityproperty"><strong>MFPKEY_VBRQUALITY</strong></a></td>
<td>Specifies the actual quality level for quality based (1-pass) variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-videowindowproperty"><strong>MFPKEY_VIDEOWINDOW</strong></a></td>
<td>Specifies the amount of content, in milliseconds, that can fit into the model buffer.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-zerobyteframesproperty"><strong>MFPKEY_ZEROBYTEFRAMES</strong></a></td>
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

 

 




