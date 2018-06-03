---
Description: The Media Foundation H.265 video encoder is a Media Foundation Transform that supports encoding content into the H.265/HEVC format.
ms.assetid: 790CFB39-6FC0-432D-A434-5262C30EABF4
title: H.265 / HEVC Video Encoder
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# H.265 / HEVC Video Encoder

The Media Foundation H.265 video encoder is a [Media Foundation Transform](media-foundation-transforms.md) that supports encoding content into the H.265/HEVC format. The encoder supports the following profiles:

-   Main Profile

The H.265 video encoder exposes the following interfaces:

-   [**ICodecAPI**](https://msdn.microsoft.com/windows/desktop/cc3f1bd9-1d36-45e6-94e2-07f2800fd073)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)

## Input Types

The input media type must have one of the following subtypes:

-   **MFVideoFormat\_IYUV**
-   **MFVideoFormat\_NV12**
-   **MFVideoFormat\_YUY2**
-   **MFVideoFormat\_YV12**

For more information about these subtypes, see [Video Subtype GUIDs](video-subtype-guids.md).

The output type must be set before the input type. Until the output type is set, the encoder's [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) method returns **MF\_E\_TRANSFORM\_TYPE\_NOT\_SET**.

## Output Types

The encoder supports a single output subtype:

-   **MFVideoFormat\_H265**

Set the following attributes on the output media type.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>MF_MT_MAJOR_TYPE</strong>](mf-mt-major-type-attribute.md)</td>
<td>Major type. Must be <strong>MFMediaType_Video</strong>.</td>
</tr>
<tr class="even">
<td>[<strong>MF_MT_SUBTYPE</strong>](mf-mt-subtype-attribute.md)</td>
<td>Video subtype. Must be <strong>MFVideoFormat_HEVC</strong>.</td>
</tr>
<tr class="odd">
<td>[<strong>MF_MT_AVG_BITRATE</strong>](mf-mt-avg-bitrate-attribute.md)</td>
<td>Average encoded bit rate, in bits per second. Must be greater than zero.</td>
</tr>
<tr class="even">
<td>[<strong>MF_MT_FRAME_RATE</strong>](mf-mt-frame-rate-attribute.md)</td>
<td>Frame rate.</td>
</tr>
<tr class="odd">
<td>[<strong>MF_MT_FRAME_SIZE</strong>](mf-mt-frame-size-attribute.md)</td>
<td>Frame size.</td>
</tr>
<tr class="even">
<td>[<strong>MF_MT_INTERLACE_MODE</strong>](mf-mt-interlace-mode-attribute.md)</td>
<td>Interlace mode.</td>
</tr>
<tr class="odd">
<td>[MF_MT_VIDEO_PROFILE](mf-mt-video-profile.md)</td>
<td>H.265 encoding profile.<br/> The supported values are: <br/>
<ul>
<li><strong>eAVEncH265VProfile_Main_420_8</strong></li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>MF_MT_MPEG2_LEVEL</strong>](mf-mt-mpeg2-level-attribute.md)</td>
<td>Specifies the level of the coded video. For more information about profile and level constraints, refer to Annex A of ITU-T H.265.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MF_MT_PIXEL_ASPECT_RATIO</strong>](mf-mt-pixel-aspect-ratio-attribute.md)</td>
<td>Optional. Specifies the pixel aspect ratio. The default value is 1:1.</td>
</tr>
</tbody>
</table>



 

After the output type is set, the video encoder updates the type by adding the [**MF\_MT\_MPEG\_SEQUENCE\_HEADER**](mf-mt-mpeg-sequence-header-attribute.md) attribute. This attribute contains the sequence header.

## Supported IMFTransform methods

The following methods of the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface are supported for the H.265/HEVC encoder:

-   [**GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes)
-   [**GetInputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputavailabletype)
-   [**GetInputCurrentType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputcurrenttype)
-   [**GetInputStatus**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstatus)
-   [**GetInputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreaminfo)
-   [**GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype)
-   [**GetOutputCurrentType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputcurrenttype)
-   [**GetOutputStatus**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstatus)
-   [**GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo)
-   [**GetStreamCount**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamcount)
-   [**GetStreamLimits**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamlimits)
-   [**ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent)
-   [**ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage)
-   [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput)
-   [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput)
-   [**SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype)
-   [**SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype)
-   [**SetOutputBounds**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputbounds)

All other [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) methods will return the error E\_NOTIMPL.

## Supported ICodecAPI methods

The following methods of the [**ICodecAPI**](https://msdn.microsoft.com/windows/desktop/cc3f1bd9-1d36-45e6-94e2-07f2800fd073) interface are supported for the H.265/HEVC encoder:

-   [**IsSupported**](https://msdn.microsoft.com/windows/desktop/6f556532-1a49-45c1-b446-89c05e8a8237)
-   [**SetValue**](https://msdn.microsoft.com/windows/desktop/e78a310a-3605-4cb3-a0c3-7864c890c1fa)
-   [**GetValue**](https://msdn.microsoft.com/windows/desktop/863ba518-c3c6-47d8-96d8-445a7e4d02aa)
-   [**GetParameterRange**](https://msdn.microsoft.com/windows/desktop/35bf758f-0ce3-4b3a-aae5-9d4326089743)
-   [**GetParameterValues**](https://msdn.microsoft.com/windows/desktop/7f6c7db8-f71f-4ea7-8584-0df6e28c0fc9)

All other [**ICodecAPI**](https://msdn.microsoft.com/windows/desktop/cc3f1bd9-1d36-45e6-94e2-07f2800fd073) methods will return the error E\_NOTIMPL.

## Codec Properties

The H.265 encoder implements the [**ICodecAPI**](https://msdn.microsoft.com/windows/desktop/cc3f1bd9-1d36-45e6-94e2-07f2800fd073) interface for setting encoding parameters. It supports the following properties.

For the codec requirements for HCK encoder certification, see the **Certified Hardware Encoder** section below.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CODECAPI_AVEncCommonRateControlMode</strong>](https://msdn.microsoft.com/windows/desktop/4a0d49b1-30da-4ebe-abff-3fceef6dd94a)</td>
<td>Sets the rate control mode. The supported modes are:<br/>
<ul>
<li><strong>eAVEncCommonRateControlMode_CBR</strong></li>
<li><strong>eAVEncCommonRateControlMode_Quality</strong></li>
</ul>
If other modes are specified, the <strong>eAVEncCommonRateControlMode_CBR</strong> rate control will be used.<br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncCommonMeanBitRate](https://msdn.microsoft.com/windows/desktop/8519685a-4f5b-44af-ad46-09eba7a198c6)</td>
<td>Sets the average bit rate for the encoded bit stream, in bits per second. <br/> The valid range is [1 ... 2³²–1]. <br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncCommonBufferSize](https://msdn.microsoft.com/windows/desktop/3315785e-306f-44d6-ac39-796025a2da3a)</td>
<td>Sets the buffer size, in bytes, for constant bit rate (CBR) encoding.<br/> The valid range is [1 ... 2³²–1]. <br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncCommonMaxBitRate](https://msdn.microsoft.com/windows/desktop/053fdad0-dc5f-4af1-84a6-bb7c0dac7e79)</td>
<td>Sets the maximum bitrate for rate control modes that allow a peak bitrate. <br/> The valid range is [1 ... 2³²–1]. <br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncMPVGOPSize](https://msdn.microsoft.com/windows/desktop/90433df4-5a96-4bc2-a780-93306abcb0a4)</td>
<td>Sets the number of pictures from one GOP header to the next, including the leading anchor but not the following one. <br/> The valid range is [0 ... 2³²–1]. If zero, the encoder selects the GOP size. The default value is zero. <br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVLowLatencyMode](codecapi-avlowlatencymode.md)</td>
<td>Enables or disables low-latency mode. <br/> This is a VT_BOOL value.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncCommonQualityVsSpeed](https://msdn.microsoft.com/windows/desktop/d721a50d-dec9-4e2d-bda5-25913f225d68)</td>
<td>Sets the quality/speed tradeoff. This value affects how the encoder performs various encoding operations, such as motion compensation. At higher complexity levels, the encoder runs more slowly but produces better quality at the same bit rate. <br/> The valid range is 0 – 100. Internally, this value is mapped to a smaller set of quality/speed levels supported by the encoder.<br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncVideoForceKeyFrame](codecapi-avencvideoforcekeyframe.md)</td>
<td>Forces the encoder to code the next frame as a key frame.<br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md)</td>
<td>When this property is set it will cause the encoder to use the specified QP to encode the next frame and all subsequent frames until a new QP is specified. <br/> Valid range: 0–51, inclusive <br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncVideoMinQP](codecapi-avencvideominqp.md)</td>
<td>This property will set a limit on the minimum QP that the encoder can use during CBR ratecontrol.<br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncVideoMaxQP](codecapi-avencvideomaxqp.md)</td>
<td>This property will set a limit on the maximum QP that the encoder can use during CBR ratecontrol.<br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_VideoEncoderDisplayContentType](codecapi-videoencoderdisplaycontenttype.md)</td>
<td>Sets whether the content is full-screen video, as opposed to screen content that might have a smaller window of video or have no video at all.<br/> This is a VT_UI4 value.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncNumWorkerThreads](codecapi-avencnumworkerthreads.md)</td>
<td>Sets the number of threads used to perform the compression operation. The encoder will divide the frame into tiles such that the number of threads equals the number of tiles.<br/>
<ul>
<li>The number of logical processors. The number of threads must be less than or equal to the number of logical processors.</li>
<li>The size of the frame. The size of a tile must bigger than or equal to 265x64 pixels.</li>
<li>Parity. The number of threads must be an even value. If the specified value is odd then the next lower even value will be used.</li>
</ul>
This is a VT_UI4 value.<br/></td>
</tr>
</tbody>
</table>



 

## Certified Hardware Encoder

If a certified hardware encoder is present, it will generally be used instead of the inbox system encoder for Media Foundation related scenarios. Certified encoders are required to support a certain set of **ICodecAPI** properties and can optionally support another set of properties. The certification process should guarantee that the required properties are properly supported and, if an optional property is supported, that it is also properly supported.

The following is the set of required and optional **ICodecAPI** properties for encoders to pass the HCK encoder certification.

-   [CODECAPI\_AVEncCommonRateControlMode](https://msdn.microsoft.com/windows/desktop/4a0d49b1-30da-4ebe-abff-3fceef6dd94a)
-   [CODECAPI\_AVEncCommonQuality](https://msdn.microsoft.com/windows/desktop/2c7f3836-2392-47c6-9a56-d5a9b52560ff)
-   [CODECAPI\_AVEncCommonMeanBitRate](https://msdn.microsoft.com/windows/desktop/8519685a-4f5b-44af-ad46-09eba7a198c6)
-   [CODECAPI\_AVEncCommonBufferSize](https://msdn.microsoft.com/windows/desktop/3315785e-306f-44d6-ac39-796025a2da3a)
-   [CODECAPI\_AVEncMPVGOPSize](https://msdn.microsoft.com/windows/desktop/90433df4-5a96-4bc2-a780-93306abcb0a4)
-   [CODECAPI\_AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md)
-   [CODECAPI\_AVEncVideoForceKeyFrame](codecapi-avencvideoforcekeyframe.md)

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | None supported<br/>                                                                |
| DLL<br/>                      | <dl> <dt>Mfh265enc.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> </dl>

 

 




