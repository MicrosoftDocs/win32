---
description: The Windows Media Video 9 encoder encodes video streams.
ms.assetid: 1d0a41bc-7f7c-4e25-860c-1108ab292951
title: Windows Media Video 9 Encoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Video 9 Encoder

The Windows Media Video 9 encoder encodes video streams. The encoder supports the following four categories of encoded output.

-   Windows Media Video 9 Simple Profile
-   Windows Media Video 9 Main Profile
-   Windows Media Video 9 Advanced Profile
-   Windows Media Video 9.1 Image

## Class Identifier

The class identifier (CLSID) for the Windows Media Video encoder is represented by the constant **CLSID\_CWMV9EncMediaObject**. You can create an instance of the video encoder by calling **CoCreateInstance**.

## Interfaces

A video encoder object exposes the [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject) interface so that the object can be used as a DirectX Media Object (DMO), and it exposes the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface so that the object can be used as a Media Foundation Transform (MFT).

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

The following table shows the four-character codes (FOURCCs) that correspond to the categories of encoded output.



| Category                               | FOURCC                                   |
|----------------------------------------|------------------------------------------|
| Windows Media Video 9 Simple Profile   | "WMV3"                                   |
| Windows Media Video 9 Main Profile     | "WMV3"                                   |
| Windows Media Video 9 Advanced Profile | "WVC1"                                   |
| Windows Media Video 9.1 Image          | "WMVP" for 9.1, "WVP2" for 9.1 version 2 |



 

To distinguish between Simple Profile and Main Profile, set the [**MFPKEY\_DECODERCOMPLEXITYREQUESTED**](mfpkey-decodercomplexityrequestedproperty.md) property.

## Properties

The Windows Media Video 9 encoder supports the following properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mfpkey-asfoverheadperframeproperty.md"><strong>MFPKEY_ASFOVERHEADPERFRAME</strong></a></td>
<td>Specifies the overhead, in bytes per packet, required for the container used to store the compressed content.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-avgframerateproperty.md"><strong>MFPKEY_AVGFRAMERATE</strong></a></td>
<td>Specifies the average frame rate of video content, in frames per second.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-bavgproperty.md"><strong>MFPKEY_BAVG</strong></a></td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its average bit rate (specified by <a href="mfpkey-ravgproperty.md"><strong>MFPKEY_RAVG</strong></a>).<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-bdeltaqpproperty.md"><strong>MFPKEY_BDELTAQP</strong></a></td>
<td>Specifies the delta increase between the picture quantizer of the anchor frame and the picture quantizer of the B-frame.<br/> <dl> Windows XP and later.<br />
Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-bmaxproperty.md"><strong>MFPKEY_BMAX</strong></a></td>
<td>Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its peak bit rate (specified by <a href="mfpkey-rmaxproperty.md"><strong>MFPKEY_RMAX</strong></a>).<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-bufferfullnessinfirstbyteproperty.md"><strong>MFPKEY_BUFFERFULLNESSINFIRSTBYTE</strong></a></td>
<td>Specifies whether the encoded video bit stream contains a buffer fullness value with every key frame.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-closedentrypointproperty.md"><strong>MFPKEY_CLOSEDENTRYPOINT</strong></a></td>
<td>Specifies the encoding pattern to use at the beginning of a group of pictures.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-codedframesproperty.md"><strong>MFPKEY_CODEDFRAMES</strong></a></td>
<td>Specifies the number of video frames encoded by the codec.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-codednonzeroframesproperty.md"><strong>MFPKEY_CODEDNONZEROFRAMES</strong></a></td>
<td>Specifies the number of video frames encoded by the codec that actually contain data.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-complexityproperty.md"><strong>MFPKEY_COMPLEXITY</strong></a></td>
<td>This property is superseded by <a href="mfpkey-complexityexproperty.md"><strong>MFPKEY_COMPLEXITYEX</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-complexityexproperty.md"><strong>MFPKEY_COMPLEXITYEX</strong></a></td>
<td>Specifies the complexity of the encoder algorithm.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile. Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-compressionoptimizationtypeproperty.md"><strong>MFPKEY_COMPRESSIONOPTIMIZATIONTYPE</strong></a></td>
<td>Specifies the type of optimization to use for the Windows Media Video 9 Advanced Profile codec.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-crispproperty.md"><strong>MFPKEY_CRISP</strong></a></td>
<td>Specifies a numeric representation of the tradeoff between motion smoothness and image quality in codec output.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-datarateproperty.md"><strong>MFPKEY_DATARATE</strong></a></td>
<td>Not used.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-decodercomplexityprofileproperty.md"><strong>MFPKEY_DECODERCOMPLEXITYPROFILE</strong></a></td>
<td>Specifies the device conformance template to which the encoded content conforms.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-decodercomplexityrequestedproperty.md"><strong>MFPKEY_DECODERCOMPLEXITYREQUESTED</strong></a></td>
<td>Specifies the device conformance template that you want to use for video encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-deltamvrangeindexproperty.md"><strong>MFPKEY_DELTAMVRANGEINDEX</strong></a></td>
<td>Specifies the method used to encode the motion vector information.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-denoiseoptionproperty.md"><strong>MFPKEY_DENOISEOPTION</strong></a></td>
<td>Specifies whether the codec will use the noise filter when encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-desired-vbrqualityproperty.md"><strong>MFPKEY_DESIRED_VBRQUALITY</strong></a></td>
<td>Specifies the desired quality level for quality based (1-pass) variable-bit-rate (VBR) encoding.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-droppedframesproperty.md"><strong>MFPKEY_DROPPEDFRAMES</strong></a></td>
<td>Specifies the number of video frames dropped during encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-endofpassproperty.md"><strong>MFPKEY_ENDOFPASS</strong></a></td>
<td>Specifies the end of an encoding pass.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-forceframeheightproperty.md"><strong>MFPKEY_FORCEFRAMEHEIGHT</strong></a></td>
<td>Specifies an intermediate frame height for encoded video.<br/> <dl> Windows XP and later.<br />
Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-forceframewidthproperty.md"><strong>MFPKEY_FORCEFRAMEWIDTH</strong></a></td>
<td>Specifies an intermediate frame width for encoded video.<br/> <dl> Windows XP and later.<br />
Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-forcemediansettingproperty.md"><strong>MFPKEY_FORCEMEDIANSETTING</strong></a></td>
<td>Specifies whether the codec should use median filtering during encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-fourccproperty.md"><strong>MFPKEY_FOURCC</strong></a></td>
<td>Specifies the FOURCC that identifies the encoder you want to use.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-framecountproperty.md"><strong>MFPKEY_FRAMECOUNT</strong></a></td>
<td>Obsolete.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-fullframerateproperty.md"><strong>MFPKEY_FULLFRAMERATE</strong></a></td>
<td>Specifies whether the encoder is allowed to drop frames.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-interlacedcodingenabledproperty.md"><strong>MFPKEY_INTERLACEDCODINGENABLED</strong></a></td>
<td>Specifies whether the codec output will be interlaced.<br/> <dl> Windows XP and later.<br />
Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-keydistproperty.md"><strong>MFPKEY_KEYDIST</strong></a></td>
<td>Specifies the maximum time, in milliseconds, between key frames in the codec output.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-liveencodeproperty.md"><strong>MFPKEY_LIVEENCODE</strong></a></td>
<td>Not used.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-lookaheadproperty.md"><strong>MFPKEY_LOOKAHEAD</strong></a></td>
<td>Specifies the number of frames after the current frame that the codec will evaluate before encoding the current frame.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-loopfilterproperty.md"><strong>MFPKEY_LOOPFILTER</strong></a></td>
<td>Specifies whether the codec should use the in-loop deblocking filter during encoding.<br/> <dl> Windows XP and later.<br />
Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-macroblockmodecostmethodproperty.md"><strong>MFPKEY_MACROBLOCKMODECOSTMETHOD</strong></a></td>
<td>Specifies the cost method used by the codec to determine which macroblock mode to use.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-motionmatchmethodproperty.md"><strong>MFPKEY_MOTIONMATCHMETHOD</strong></a></td>
<td>Specifies the method to use for motion matching.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-motionsearchlevelproperty.md"><strong>MFPKEY_MOTIONSEARCHLEVEL</strong></a></td>
<td>Specifies the types of video information that are used in motion search operations.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-motionsearchrangeproperty.md"><strong>MFPKEY_MOTIONSEARCHRANGE</strong></a></td>
<td>Specifies the range used in motion searches.<br/> <dl> Windows XP and later.<br />
Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-noiseedgeremovalproperty.md"><strong>MFPKEY_NOISEEDGEREMOVAL</strong></a></td>
<td>Specifies whether the codec should attempt to detect noisy frame edges and remove them.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-numbframesproperty.md"><strong>MFPKEY_NUMBFRAMES</strong></a></td>
<td>Specifies the number of bidirectional predictive frames (B-frames).<br/> <dl> Windows XP and later.<br />
Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-numthreadsproperty.md"><strong>MFPKEY_NUMTHREADS</strong></a></td>
<td>Specifies the number of threads that the codec will use for encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-passesrecommendedproperty.md"><strong>MFPKEY_PASSESRECOMMENDED</strong></a></td>
<td>Specifies the maximum number of passes supported by the codec.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-passesusedproperty.md"><strong>MFPKEY_PASSESUSED</strong></a></td>
<td>Specifies the number of passes that the codec will use to encode the content.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-perceptualoptlevelproperty.md"><strong>MFPKEY_PERCEPTUALOPTLEVEL</strong></a></td>
<td>Specifies whether the codec should use conservative perceptual optimization when encoding.<br/> <dl> Windows XP and later.<br />
Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-producedummyframesproperty.md"><strong>MFPKEY_PRODUCEDUMMYFRAMES</strong></a></td>
<td>Specifies whether the encoder produces dummy frame entries in the bit stream for duplicate frames.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-qpperframeproperty.md"><strong>MFPKEY_QPPERFRAME</strong></a></td>
<td>Specifies QP.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-rangereduxproperty.md"><strong>MFPKEY_RANGEREDUX</strong></a></td>
<td>Specifies the degree to which the codec should reduce the effective color range of the video.<br/> <dl> Windows XP and later.<br />
Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-ravgproperty.md"><strong>MFPKEY_RAVG</strong></a></td>
<td>Specifies the average bit rate, in bits per second, used for 2-pass variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-rdsubpixelsearchproperty.md"><strong>MFPKEY_RDSUBPIXELSEARCH</strong></a></td>
<td>Specifies whether the encoder uses RD-based sub-pixel MV search. <br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-reencendbuffersizeproperty.md"><strong>MFPKEY_REENCENDBUFFERSIZE</strong></a></td>
<td>For segment re-encoding, specifies the buffer size.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-reencdurationproperty.md"><strong>MFPKEY_REENCDURATION</strong></a></td>
<td>For segment re-encoding, specifies the duration of the segment to be re-encoded.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-reencqprefproperty.md"><strong>MFPKEY_REENCQPREF</strong></a></td>
<td>For segment re-encoding, specifies the quantizer of the frame prior to the starting segment.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-reencstartbuffersizeproperty.md"><strong>MFPKEY_REENCSTARTBUFFERSIZE</strong></a></td>
<td>For segment re-encoding, specifies the starting buffer fullness.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-rmaxproperty.md"><strong>MFPKEY_RMAX</strong></a></td>
<td>Specifies the peak bit rate, in bits per second, used for constrained 2-pass variable-bit-rate (VBR).<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-totalframesproperty.md"><strong>MFPKEY_TOTALFRAMES</strong></a></td>
<td>Specifies the number of video frames passed to the encoder during the encoding process.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Read-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-vbrenabledproperty.md"><strong>MFPKEY_VBRENABLED</strong></a></td>
<td>Specifies whether the codec will use variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Read/write.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-vbrqualityproperty.md"><strong>MFPKEY_VBRQUALITY</strong></a></td>
<td>Specifies the actual quality level for quality based (1-pass) variable-bit-rate (VBR) encoding.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-videoscalingproperty.md"><strong>MFPKEY_VIDEOSCALING</strong></a></td>
<td>Specifies whether the codec will use video scaling optimization.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-videowindowproperty.md"><strong>MFPKEY_VIDEOWINDOW</strong></a></td>
<td>Specifies the amount of content, in milliseconds, that can fit into the model buffer.<br/> <dl> Windows XP and later.<br />
Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-volheaderforreencodeproperty.md"><strong>MFPKEY_VOLHEADERFORREENCODE</strong></a></td>
<td>For segment re-encoding, specifies the codec private data of the file that is being re-encoded.<br/> <dl> Windows Vista and later.<br />
Simple Profile, Main Profile, Advanced Profile, Image.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="mfpkey-vtypeproperty.md"><strong>MFPKEY_VTYPE</strong></a></td>
<td>Specifies the type of logic that the codec will use to detect interlaced source video.<br/> <dl> Windows XP and later.<br />
Advanced Profile.<br />
Write-only.<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="mfpkey-zerobyteframesproperty.md"><strong>MFPKEY_ZEROBYTEFRAMES</strong></a></td>
<td>Specifies the number of video frames that were skipped because they were duplicates of previous frames.<br/> <dl> Windows XP and later.<br />
Simple Profile, Main Profile, Advanced Profile.<br />
Read-only<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmvencod.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Codec Implementation](codecimplementation.md)
</dt> </dl>

 

 
