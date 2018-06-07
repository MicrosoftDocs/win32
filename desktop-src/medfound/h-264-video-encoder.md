---
Description: 'The Microsoft Media Foundation H.264 video encoder is a Media Foundation transform that supports the following H.264 profiles:'
ms.assetid: 4d4c768f-b76a-40ca-8736-2f592a4f4cc4
title: H.264 Video Encoder
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# H.264 Video Encoder

The Microsoft Media Foundation H.264 video encoder is a [Media Foundation transform](media-foundation-transforms.md) that supports the following H.264 profiles:

-   Baseline Profile
-   Main Profile
-   High profile (requires Windows 8)

The H.264 video encoder exposes the following interfaces:

-   [**ICodecAPI**](https://msdn.microsoft.com/cc3f1bd9-1d36-45e6-94e2-07f2800fd073)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)

## Input Types

The input media type must have one of the following subtypes:

-   **MFVideoFormat\_I420**
-   **MFVideoFormat\_IYUV**
-   **MFVideoFormat\_NV12**
-   **MFVideoFormat\_YUY2**
-   **MFVideoFormat\_YV12**

For more information about these subtypes, see [Video Subtype GUIDs](video-subtype-guids.md).

The output type must be set before the input type. Until the output type is set, the encoder's [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) method returns **MF\_E\_TRANSFORM\_TYPE\_NOT\_SET**.

## Output Types

The encoder supports a single output subtype:

-   **MFVideoFormat\_H264**

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
<td>Video subtype. Must be <strong>MFVideoFormat_H264</strong>.</td>
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
<td>[<strong>MF_MT_MPEG2_PROFILE</strong>](mf-mt-mpeg2-profile-attribute.md)</td>
<td>H.264 encoding profile.<br/> The supported values are:<br/>
<ul>
<li><strong>eAVEncH264VProfile_Base</strong> (default)</li>
<li><strong>eAVEncH264VProfile_Main</strong></li>
<li><strong>eAVEncH264VProfile_High</strong> (requires Windows 8)</li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>MF_MT_MPEG2_LEVEL</strong>](mf-mt-mpeg2-level-attribute.md)</td>
<td>Optional. Specifies the H.264 encoding level.<br/> The default value is –1, indicating that the encoder will select the encoding level.<br/> It is recommended not to set the level in the media type, and allow the encoder to select the level. The encoder can derive the proper level for a given video stream, taking into account the format constraints and the characteristics of the video. For more information about profile and level constraints, refer to Annex A of ITU-T H.264.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MF_MT_PIXEL_ASPECT_RATIO</strong>](mf-mt-pixel-aspect-ratio-attribute.md)</td>
<td>Optional. Specifies the pixel aspect ratio. The default value is 1:1.</td>
</tr>
</tbody>
</table>



 

After the output type is set, the video encoder updates the type by adding the [**MF\_MT\_MPEG\_SEQUENCE\_HEADER**](mf-mt-mpeg-sequence-header-attribute.md) attribute. This attribute contains the sequence header.

## Codec Properties

The H.264 encoder implements the [**ICodecAPI**](https://msdn.microsoft.com/cc3f1bd9-1d36-45e6-94e2-07f2800fd073) interface for setting encoding parameters. It supports the following properties.

For the codec requirements for HCK encoder certification, see the **Certified Hardware Encoder** section below.

The following properties are supported in Windows 7.



| Property                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CODECAPI\_AVEncCommonRateControlMode**](https://msdn.microsoft.com/4a0d49b1-30da-4ebe-abff-3fceef6dd94a) | Sets the rate control mode. See Remarks. The default mode is unconstrained variable bit rate (VBR).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**CODECAPI\_AVEncCommonQuality**](https://msdn.microsoft.com/2c7f3836-2392-47c6-9a56-d5a9b52560ff)                 | Sets the quality level. This property applies when the rate control mode is quality-based VBR (**eAVEncCommonRateControlMode\_Quality**). The valid range is 1–100. The default value is 70. <br/> To set this parameter, set the property before calling [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype). <br/> To set this parameter in Windows 7, set the property before calling [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype). The encoder ignores changes after the output type is set. <br/> In Windows 8, this property can be set at any time during encoding. Changes are applied starting at the next input frame. <br/> Internally, the encoder converts this property to an [AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md) value. <br/> |



 

The following properties require Windows 8.



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
<td>[CODECAPI_AVEncAdaptiveMode](codecapi-avencadaptivemode.md)</td>
<td>Sets the adaptive encoding mode. The H.264 encoder supports the following modes in Windows 8:
<ul>
<li><strong>eAVEncAdaptiveMode_None</strong>. No adaptive encoding. (Default.)</li>
<li><strong>eAVEncAdaptiveMode_FrameRate</strong>. Adaptively change the frame rate.</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncCommonBufferSize](https://msdn.microsoft.com/3315785e-306f-44d6-ac39-796025a2da3a)</td>
<td>Sets the buffer size, in bytes, for constant bit rate (CBR) encoding.<br/> The valid range is [1 ... 2³²–1]. <br/> Requires Windows 8. <br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncCommonMaxBitRate](https://msdn.microsoft.com/053fdad0-dc5f-4af1-84a6-bb7c0dac7e79)</td>
<td>For constrained VBR encoding, specifies the rate at which the &quot;leaky bucket&quot; is drained, in bits per second. This property applies when the rate control mode is <strong>eAVEncCommonRateControlMode_PeakConstrainedVBR</strong>. <br/> The valid range is [1 ... 2³²–1]. <br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncCommonMeanBitRate](https://msdn.microsoft.com/8519685a-4f5b-44af-ad46-09eba7a198c6)</td>
<td>Sets the average bit rate for the encoded bit stream, in bits per second. This property is ignored if the rate control mode is <strong>eAVEncCommonRateControlMode_Quality</strong>. <br/> The valid range is [1 ... 2³²–1]. <br/> In CBR and unconstrained VBR modes, the average bit rate determines the final size of the file. In CBR mode, the average bit rate is also the rate at which compressed bits are drained from the &quot;leaky bucket.&quot; (For more information, see [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md).) <br/> In Windows 7, the average bit rate is specified by the [MF_MT_AVG_BITRATE](mf-mt-avg-bitrate-attribute.md) attribute on the media type. <br/> In Windows 8, you can set the average bit rate using either the [MF_MT_AVG_BITRATE](mf-mt-avg-bitrate-attribute.md) attribute or the [CODECAPI_AVEncCommonMeanBitRate](https://msdn.microsoft.com/8519685a-4f5b-44af-ad46-09eba7a198c6) property. If both are set, CODECAPI_AVEncCommonMeanBitRate overrides. In Windows 8, you can set the average bit rate during encoding. If the bit rate changes, the encoder uses adaptive encoding.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncCommonQualityVsSpeed](https://msdn.microsoft.com/d721a50d-dec9-4e2d-bda5-25913f225d68)</td>
<td>Sets the quality/speed tradeoff. Valid range:
<ul>
<li>0–33: Low complexity</li>
<li>34–66: Medium complexity (default)</li>
<li>67–100: High complexity</li>
</ul>
<br/> This value affects how the encoder performs various encoding operations, such as motion compensation. At higher complexity levels, the encoder runs more slowly but produces better quality at the same bit rate.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncH264CABACEnable](codecapi-avench264cabacenable.md)</td>
<td>Enables or disables CABAC (context-adaptive binary arithmetic coding) for H.264 entropy coding. The default value is <strong>VARIANT_FALSE</strong>. <br/> CABAC is not used for Baseline profile.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncH264SPSID](codecapi-avench264spsid.md)</td>
<td>Sets the value of <strong>seq_parameter_set_id</strong> in the SPS NAL unit of the H.264 bitstream. <br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncMPVDefaultBPictureCount](https://msdn.microsoft.com/d41ed713-0159-4325-bc44-f4a3eea10aa2)</td>
<td>Sets the maximum number of consecutive B frames in the output bitstream. Valid values are:
<ul>
<li>0: Do not use B frames (default).</li>
<li>1: Use one B frame.</li>
<li>2: Use two B frames.</li>
</ul>
To set this parameter, set the property before calling [<strong>IMFTransform::SetOutputType</strong>](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype). <br/> For Baseline profile, the number of B frames is always zero. The encoder will override nonzero values.<br/> For other H.264 profiles, if this property is nonzero, the encoding pattern is IBBPBBP, where the maximum number of consecutive B frames is equal to [CODECAPI_AVEncMPVDefaultBPictureCount](https://msdn.microsoft.com/d41ed713-0159-4325-bc44-f4a3eea10aa2). <br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncMPVGOPSize](https://msdn.microsoft.com/90433df4-5a96-4bc2-a780-93306abcb0a4)</td>
<td>Sets the number of pictures from one GOP header to the next, including the leading anchor but not the following one. <br/> The valid range is [0 ... 2³²–1]. If zero, the encoder selects the GOP size. The default value is zero. <br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncNumWorkerThreads](codecapi-avencnumworkerthreads.md)</td>
<td>Sets the number of worker threads used by a encoder.<br/> The valid range is 0–16. If zero, the encoder selects the number of threads. <br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncVideoContentType](codecapi-avencvideocontenttype.md)</td>
<td>Indicates the type of video content.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md)</td>
<td>Valid range: 16–51. The default value is 24. <br/> This property applies when the rate control mode is <strong>eAVEncCommonRateControlMode_Quality</strong>. <br/> This property configures the same encoding setting as [<strong>AVEncCommonQuality</strong>](https://msdn.microsoft.com/2c7f3836-2392-47c6-9a56-d5a9b52560ff). However, [AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md) enables the application to specify the value of QP directly. If both properties are set, AVEncVideoEncodeQP overrides. <br/> The default value of 24 corresponds to the default value of 70 for the [<strong>AVEncCommonQuality</strong>](https://msdn.microsoft.com/2c7f3836-2392-47c6-9a56-d5a9b52560ff) setting.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVEncVideoForceKeyFrame](codecapi-avencvideoforcekeyframe.md)</td>
<td>Forces the encoder to code the next frame as a key frame.<br/></td>
</tr>
<tr class="even">
<td>[CODECAPI_AVEncVideoMinQP](codecapi-avencvideominqp.md)</td>
<td>Valid range: 0–51. The default value is 0. <br/> This property applies to all rate control modes. The encoder should not produce a QP value lower than what is specified by the [CODECAPI_AVEncVideoMinQP](codecapi-avencvideominqp.md) property.<br/></td>
</tr>
<tr class="odd">
<td>[CODECAPI_AVLowLatencyMode](codecapi-avlowlatencymode.md)</td>
<td>Enables or disables low-latency mode. See &quot;Multithreading&quot; in the Remarks section.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

The encoder supports the following rate control modes.



| Mode                                  | Constant                                            | Description                                                                                                                                                                                                                                         |
|---------------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constant bit rate (CBR)               | **eAVEncCommonRateControlMode\_CBR**                | The encoder tries to achieve a constant bit rate, using a "leaky bucket" model. The target bit rate is given by the [CODECAPI\_AVEncCommonMeanBitRate](https://msdn.microsoft.com/8519685a-4f5b-44af-ad46-09eba7a198c6) property. <br/> Requires Windows 8. <br/> |
| Constrained variable bit rate (VBR)   | **eAVEncCommonRateControlMode\_PeakConstrainedVBR** | The encoder uses a "leaky bucket" model with a peak bit rate. The drain rate for the leaky bucket is given by the [CODECAPI\_AVEncCommonMaxBitRate](https://msdn.microsoft.com/053fdad0-dc5f-4af1-84a6-bb7c0dac7e79) property. <br/> Requires Windows 8. <br/>     |
| Quality-based variable bit rate (VBR) | **eAVEncCommonRateControlMode\_Quality**            | The encoder tries to achieve a constant quality level, given by the [**AVEncCommonQuality**](https://msdn.microsoft.com/2c7f3836-2392-47c6-9a56-d5a9b52560ff) property.                                                                                                           |
| Unconstrained VBR                     | **eAVEncCommonRateControlMode\_UnconstrainedVBR**   | The encoder tries to achieve the target bitrate given by the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute in the output media type. This is the default mode.                                                              |



 

CBR and constrained VBR modes require Windows 8.

In Windows 8, the encoder sets the following attributes on the output samples:

-   [MFSampleExtension\_DecodeTimestamp](mfsampleextension-decodetimestamp.md)
-   [MFSampleExtension\_VideoEncodePictureType](mfsampleextension-videoencodepicturetype.md)
-   [MFSampleExtension\_VideoEncodeQP](mfsampleextension-videoencodeqp.md)

> [!Note]  
> A previous version of the documentation incorrectly stated that the encoder is supported on Windows Server 2008 R2.

 

### Multithreading

In Windows 8, the encoder supports two encoding modes:

-   **Slice encoding.** In this mode, slices are encoded in parallel. Each slice is encoded on a different thread. This mode has low latency, because a single picture is encoded in parallel. However, this approach does not scale as the number of cores increases, because the number of slices is bounded by the number of macroblock rows in the input picture.
-   **Multi-frame encoding.** In this mode, the encoder accepts multiple frames of input and encodes them in parallel. This mode scales better in a multicore environment, but introduces more latency.

The encoder defaults to slice encoding, to minimize latency. To enable multi-frame encoding, set the [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md) property to **VARIANT\_FALSE**.

To set the number of worker threads used by the encoder, set the [CODECAPI\_AVEncNumWorkerThreads](codecapi-avencnumworkerthreads.md) property.

In Windows 7, the encoder always uses slice encoding.

### Certified Hardware Encoder

If a certified hardware encoder is present, it will generally be used instead of the inbox system encoder for Media Foundation related scenarios. Certified encoders are required to support a certain set of **ICodecAPI** properties and can optionally support another set of properties. The certification process should guarantee that the required properties are properly supported and, if an optional property is supported, that it is also properly supported.

The following is the set of required and optional **ICodecAPI** properties for encoders to pass the HCK encoder certification.

The following Windows 8 and Windows 8.1 **ICodecAPI** properties are required:

-   [CODECAPI\_AVEncCommonRateControlMode](https://msdn.microsoft.com/4a0d49b1-30da-4ebe-abff-3fceef6dd94a)
-   [CODECAPI\_AVEncCommonQuality](https://msdn.microsoft.com/2c7f3836-2392-47c6-9a56-d5a9b52560ff)
-   [CODECAPI\_AVEncCommonQualityVsSpeed](https://msdn.microsoft.com/d721a50d-dec9-4e2d-bda5-25913f225d68)
-   [CODECAPI\_AVEncCommonMeanBitRate](https://msdn.microsoft.com/8519685a-4f5b-44af-ad46-09eba7a198c6)
-   [CODECAPI\_AVEncCommonMaxBitRate](https://msdn.microsoft.com/053fdad0-dc5f-4af1-84a6-bb7c0dac7e79)
-   [CODECAPI\_AVEncCommonBufferSize](https://msdn.microsoft.com/3315785e-306f-44d6-ac39-796025a2da3a)
-   [CODECAPI\_AVEncMPVGOPSize](https://msdn.microsoft.com/90433df4-5a96-4bc2-a780-93306abcb0a4)
-   [CODECAPI\_AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md)
-   [CODECAPI\_AVEncVideoForceKeyFrame](codecapi-avencvideoforcekeyframe.md)

The following Windows 8.1 **ICodecAPI** properties are optional, but are tested in HCK if supported.

-   [CODECAPI\_AVEncVideoMinQP](codecapi-avencvideominqp.md)
-   [CODECAPI\_AVEncVideoLTRBufferControl](codecapi-avencvideoltrbuffercontrol.md)
-   [CODECAPI\_AVEncVideoMarkLTRFrame](codecapi-avencvideomarkltrframe.md)
-   [CODECAPI\_AVEncVideoUseLTRFrame](codecapi-avencvideouseltrframe.md)
-   [CODECAPI\_AVEncVideoEncodeFrameTypeQP](codecapi-avencvideoencodeframetypeqp.md)
-   [CODECAPI\_AVEncSliceControlMode](codecapi-avencslicecontrolmode.md)
-   [CODECAPI\_AVEncSliceControlSize](codecapi-avencslicecontrolsize.md)
-   [CODECAPI\_AVEncVideoMaxNumRefFrame](codecapi-avencvideomaxnumrefframe.md)
-   [CODECAPI\_AVEncVideoMeanAbsoluteDifference](codecapi-avencvideomeanabsolutedifference.md)
-   [CODECAPI\_AVEncVideoMaxQP](codecapi-avencvideomaxqp.md)
-   [CODECAPI\_AVEncVideoROIEnabled](codecapi-avencvideoroienabled.md)
-   [CODECAPI\_AVEncVideoTemporalLayerCount](codecapi-avencvideotemporallayercount.md) (Dynamic)
-   [CODECAPI\_AVEncH264CABACEnable](codecapi-avench264cabacenable.md)

The following Windows 8 and Windows 8.1 **ICodecAPI** properties are optional, but are tested in HCK if supported.

-   [CODECAPI\_AVEncVideoTemporalLayerCount](codecapi-avencvideotemporallayercount.md) (Static)
-   [CODECAPI\_AVLowLatencyMode](codecapi-avlowlatencymode.md)

The following **ICodecAPI** properties are optional. They are not tested in HCK.

-   [CODECAPI\_AVEncMPVDefaultBPictureCount](https://msdn.microsoft.com/d41ed713-0159-4325-bc44-f4a3eea10aa2)

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | None supported<br/>                                                                |
| DLL<br/>                      | <dl> <dt>Mfh264enc.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[MPEG-4 Support in Media Foundation](mpeg-4-support-in-media-foundation.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> </dl>

 

 




