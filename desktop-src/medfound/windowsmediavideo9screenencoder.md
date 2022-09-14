---
description: The Windows Media Video 9 Screen encoder is optimized for encoding sequential screen shots from computer monitors.
ms.assetid: 22faebf8-40c0-47f9-b66b-c0a8b5ba7202
title: Windows Media Video 9 Screen Encoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Video 9 Screen Encoder

The Windows Media Video 9 Screen encoder is optimized for encoding sequential screen shots from computer monitors.

## Class Identifier

The class identifier (CLSID) for the Windows Media Video 9 Screen encoder is represented by the constant **CLSID\_CMSSCEncMediaObject2**. You can create an instance of the encoder by calling **CoCreateInstance**.

## Input Types

The following input types are supported by the Version 9 Screen encoder when it is being used as a DirectX Media Object (DMO).

-   MEDIASUBTYPE\_RGB24
-   MEDIASUBTYPE\_RGB32
-   MEDIASUBTYPE\_ARGB32
-   MEDIASUBTYPE\_RGB565
-   MEDIASUBTYPE\_RGB555
-   MEDIASUBTYPE\_RGB8

The following input types are supported by the Version 9 Screen encoder when it is being used as a Media Foundation Transform (MFT).

-   MFVideoFormat\_RGB24
-   MFVideoFormat\_RGB32
-   MFVideoFormat\_ARGB32
-   MFVideoFormat\_RGB565
-   MFVideoFormat\_RGB555
-   MFVideoFormat\_RGB8

## Output Types

The four-character code (FOURCC) for Windows Media Video Screen Version 9 encoded content is "MSS2".

The following output types are supported by the Version 9 Screen encoder.

-   MEDIASUBTYPE\_MSS2

## Encoder Properties

The Windows Media Video 9 Screen encoder supports the following properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mfpkey-asfoverheadperframeproperty.md">MFPKEY_ASFOVERHEADPERFRAME</a></td>
<td>Specifies the overhead, in bytes per packet, required for the container that is used to store the compressed content.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-bavgproperty.md">MFPKEY_BAVG</a></td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its average bit rate (specified by <a href="mfpkey-ravgproperty.md">MFPKEY_RAVG</a>).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-bmaxproperty.md">MFPKEY_BMAX</a></td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its peak bit rate (specified by <a href="mfpkey-rmaxproperty.md">MFPKEY_RMAX</a>).<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-bufferfullnessinfirstbyteproperty.md">MFPKEY_BUFFERFULLNESSINFIRSTBYTE</a></td>
<td>Specifies whether the encoded video bit stream contains a buffer fullness value with every key frame.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-codedframesproperty.md">MFPKEY_CODEDFRAMES</a></td>
<td>Specifies the number of video frames encoded by the codec.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-codednonzeroframesproperty.md">MFPKEY_CODEDNONZEROFRAMES</a></td>
<td>Specifies the number of video frames encoded by the codec that actually contain data.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-complexityproperty.md">MFPKEY_COMPLEXITY</a></td>
<td>This property is superseded by <a href="mfpkey-complexityexproperty.md">MFPKEY_COMPLEXITYEX</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="mfpkey-complexityexproperty.md">MFPKEY_COMPLEXITYEX</a></td>
<td>Specifies the complexity of the encoder algorithm.<br/> <dl> Windows Vista and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-crispproperty.md">MFPKEY_CRISP</a></td>
<td>Specifies a numeric representation of the tradeoff between motion smoothness and image quality in codec output.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-droppedframesproperty.md">MFPKEY_DROPPEDFRAMES</a></td>
<td>Specifies the number of video frames dropped during encoding.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-endofpassproperty.md">MFPKEY_ENDOFPASS</a></td>
<td>Specifies the end of an encoding pass.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-fourccproperty.md">MFPKEY_FOURCC</a></td>
<td>Specifies the FOURCC that identifies the encoder you want to use.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-keydistproperty.md">MFPKEY_KEYDIST</a></td>
<td>Specifies the maximum time, in milliseconds, between key frames in the codec output.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-liveencodeproperty.md">MFPKEY_LIVEENCODE</a></td>
<td>Obsolete.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-passesrecommendedproperty.md">MFPKEY_PASSESRECOMMENDED</a></td>
<td>Specifies the maximum number of passes supported by the codec.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-passesusedproperty.md">MFPKEY_PASSESUSED</a></td>
<td>Windows XP and later. Read/write.<br/> Specifies the number of passes that the codec will use to encode the content.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-qpperframeproperty.md">MFPKEY_QPPERFRAME</a></td>
<td>Specifies QP. Possible values are 1.0 through 31.0.<br/> <dl> Windows Vista and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-ravgproperty.md">MFPKEY_RAVG</a></td>
<td>Specifies the average bit rate, in bits per second, used for 2-pass variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-rmaxproperty.md">MFPKEY_RMAX</a></td>
<td>Specifies the peak bit rate, in bits per second, used for constrained 2-pass variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-totalframesproperty.md">MFPKEY_TOTALFRAMES</a></td>
<td>Specifies the number of video frames passed to the encoder during the encoding process.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-vbrenabledproperty.md">MFPKEY_VBRENABLED</a></td>
<td>Specifies whether the codec will use variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-vbrqualityproperty.md">MFPKEY_VBRQUALITY</a></td>
<td>Specifies the actual quality level for quality based (1-pass) variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-videowindowproperty.md">MFPKEY_VIDEOWINDOW</a></td>
<td>The amount of content, in milliseconds, that can fit into the model buffer.<br/> <dl> Windows XP and later,<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-zerobyteframesproperty.md">MFPKEY_ZEROBYTEFRAMES</a></td>
<td>Specifies the number of video frames that were skipped because they were duplicates of previous frames.<br/> <dl> Windows XP and later.<br />
Read-only.<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Remarks

A screen encoder object exposes the **IMediaObject** interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the **IMFTransform** interface so that the object can be used as a Media Foundation Transform (MFT).

A screen encoder behaves as a DMO or an MFT depending on which interfaces you obtain and which version of Windows is running. The following table shows the conditions under which a screen encoder behaves as a DMO or an MFT.



| Operating system            | Encoder behavior                                                                                                                                    |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows XP                  | A Windows Media Screen encoder always behaves as a DMO.                                                                                             |
| Windows Vista and Windows 7 | By default, a Windows Media Screen encoder behaves as a DMO. If you obtain an **IMFTransform** interface on a screen encoder, it behaves as an MFT. |



 

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmvsencd.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> <dt>

[Using the Windows Media Video 9 Screen Codec](usingthewindowsmediavideo9screencodec.md)
</dt> <dt>

[Windows Media Video 9 Screen Decoder](windowsmediavideo9screendecoder.md)
</dt> </dl>

 

 




