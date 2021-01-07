---
description: Sample Attributes
ms.assetid: 64aead5a-61c4-4e83-a556-af33e0aa82be
title: Sample Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Sample Attributes

The following attributes apply to [Media Samples](media-samples.md). To get the attributes from a media sample, use the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface.



| Attribute                                                                                                      | Description                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MFSampleExtension\_3DVideo](mfsampleextension-3dvideo.md)                                                    | Specifies whether a media sample contains a 3D video frame.                                                                                                                                                                                        |
| [MFSampleExtension\_3DVideo\_SampleFormat](mfsampleextension-3dvideo-sampleformat.md)                         | Specifies how a 3D video frame is stored in a media sample.                                                                                                                                                                                        |
| [**MFSampleExtension\_BottomFieldFirst**](mfsampleextension-bottomfieldfirst-attribute.md)                    | Specifies the field dominance for an interlaced video frame.                                                                                                                                                                                       |
| [MFSampleExtension\_CameraExtrinsics](mfsampleextension-cameraextrinsics.md)                                  | The camera extrinsics for the sample.                                                                                                                                                                                                              |
| [MFSampleExtension\_CaptureMetadata](mfsampleextension-capturemetadata.md)                                    | The [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) store for all the metadata related to the capture pipeline.                                                                                                                                             |
| [**MFSampleExtension\_CleanPoint**](mfsampleextension-cleanpoint-attribute.md)                                | Indicates whether a video sample is a key frame.                                                                                                                                                                                                   |
| [MFSampleExtension\_Content\_KeyID](mfsampleextension-content-keyid.md)                                       | Sets the Key ID for the sample.                                                                                                                                                                                                                    |
| [**MFSampleExtension\_DerivedFromTopField**](mfsampleextension-derivedfromtopfield-attribute.md)              | Specifies whether a deinterlaced video frame was derived from the upper field or the lower field.                                                                                                                                                  |
| [MFSampleExtension\_DeviceTimestamp](mfsampleextension-devicetimestamp.md)                                    | The time stamp from the device driver.                                                                                                                                                                                                             |
| [**MFSampleExtension\_Discontinuity**](mfsampleextension-discontinuity-attribute.md)                          | Specifies whether a media sample is the first sample after a gap in the stream.                                                                                                                                                                    |
| [MFSampleExtension\_Encryption\_CryptByteBlock](mfsampleextension-encryption-cryptbyteblock.md)               | Specifies the encrypted byte block size for sample-based pattern encryption.                                                                                                                                                                       |
| [MFSampleExtension\_Encryption\_ProtectionScheme](mfsampleextension-encryption-protectionscheme.md)           | Specifies the protection scheme for encrypted samples.                                                                                                                                                                                             |
| [MFSampleExtension\_Encryption\_SampleID](mfsampleextension-encryption-sampleid.md)                           | Specifies the ID of an encrypted sample.                                                                                                                                                                                                           |
| [MFSampleExtension\_Encryption\_SkipByteBlock](mfsampleextension-encryption-skipbyteblock.md)                 | Specifies the clear (non-encrypted) byte block size for sample-based pattern encryption.                                                                                                                                                           |
| [MFSampleExtension\_Encryption\_SubSampleMappingSplit](mfsampleextension-encryption-subsamplemappingsplit.md) | Sets the sub-sample mapping for the sample indicating the clear and encrypted bytes in the sample data.                                                                                                                                            |
| [MFSampleExtension\_FrameCorruption](mfsampleextension-framecorruption.md)                                    | Specifies whether a video frame is corrupted.                                                                                                                                                                                                      |
| [MFSampleExtension\_ForwardedDecodeUnits](mfsampleextension-forwardeddecodeunits.md)                          | Gets an object of type [**IMFCollection**](/windows/desktop/api/mfobjects/nn-mfobjects-imfcollection) containing [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) objects which contain network abstraction layer units (NALUs) and Supplemental Enhancement Information (SEI) units forwarded by a decoder. |
| [MFSampleExtension\_ForwardedDecodeUnitType](mfsampleextension-forwardeddecodeunittype.md)                    | Specifies the type, NALU or SEI, of a unit attached to an [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) in a [MFSampleExtension\_ForwardedDecodeUnits](mfsampleextension-forwardeddecodeunits.md) collection.                                                    |
| [**MFSampleExtension\_Interlaced**](mfsampleextension-interlaced-attribute.md)                                | Indicates whether a video frame is interlaced or progressive.                                                                                                                                                                                      |
| [MFSampleExtension\_LongTermReferenceFrameInfo](mfsampleextension-longtermreferenceframeinfo.md)              | Specifies Long Term Reference (LTR) frame info and is returned on the output sample.                                                                                                                                                               |
| [MFSampleExtension\_MeanAbsoluteDifference](mfsampleextension-meanabsolutedifference.md)                      | This attribute returns the mean absolute difference (MAD) across all macro-blocks in the Y plane.                                                                                                                                                  |
| [**MFSampleExtension\_PacketCrossOffsets**](mfsampleextension-packetcrossoffsets-attribute.md)                | Specifies the payload boundaries for a frame. This applies to encrypted samples.                                                                                                                                                                   |
| [MFSampleExtension\_PhotoThumbnail](mfsampleextension-photothumbnail.md)                                      | Contains the photo thumbnail of a [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample).                                                                                                                                                                                  |
| [MFSampleExtension\_PhotoThumbnailMediaType](mfsampleextension-photothumbnailmediatype.md)                    | Contains the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) which describes the image format type contained in the [MFSampleExtension\_PhotoThumbnail](mfsampleextension-photothumbnail.md) attribute.                                                      |
| [MFSampleExtension\_PinholeCameraIntrinsics](mfsampleextension-pinholecameraintrinsics.md)                    | The pinhole camera intrinsics for the sample.                                                                                                                                                                                                      |
| [**MFSampleExtension\_RepeatFirstField**](mfsampleextension-repeatfirstfield-attribute.md)                    | Specifies whether to repeat the first field in an interlaced frame.                                                                                                                                                                                |
| [MFSampleExtension\_ROIRectangle](mfsampleextension-roirectangle.md)                                          | Specifies the bounds of the region of interest which indicates the region of the frame that requires different quality.                                                                                                                            |
| [**MFSampleExtension\_SingleField**](mfsampleextension-singlefield-attribute.md)                              | Specifies whether a video sample contains a single field or two interleaved fields                                                                                                                                                                 |
| [MFSampleExtension\_TargetGlobalLuminance](mfsampleextension-targetgloballuminance.md)                        | The value in Nits that specifies the targeted global backlight luminance for the associated video frame.                                                                                                                                           |
| [**MFSampleExtension\_Token**](mfsampleextension-token-attribute.md)                                          | Contains a pointer to the token that was provided to the [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method.                                                                                                             |
| [MFSampleExtension\_VideoEncodePictureType](mfsampleextension-videoencodepicturetype.md)                      | Specifies the bounds of the region of interest which indicates the region of the frame that requires different quality.                                                                                                                            |
| [MFSampleExtension\_VideoEncodeQP](mfsampleextension-videoencodeqp.md)                                        | Specifies the quantization parameter (QP) that was used to encode a video sample.                                                                                                                                                                  |



 

Not every media sample contains every attribute listed here. In some cases, an attribute applies only to certain kinds of data. For example, some attributes apply only to video samples, and should not appear on audio samples. In other cases, the attribute has a default value which applies if the attribute is not set.

## Related topics

<dl> <dt>

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 



