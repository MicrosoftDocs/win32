---
Description: Configuring Video Encoding
ms.assetid: '917600f5-5580-4ca5-bce9-70eadec40df7'
title: Configuring Video Encoding
---

# Configuring Video Encoding

To configure the video encoder, perform the following steps:

1.  Set any properties on the encoder DMO by using **IPropertyBag::Write**. The following list summarizes the minimum set of properties that are required to encode a CBR video stream (all of these values have defaults that can be used):

    -   The[MFPKEY\_VIDEOWINDOW](mfpkey-videowindowproperty.md) property specifies the buffer window to use for the stream. For more information about the buffer windows setting and how it affects content, see [Encoding Methods](encodingmethods.md). The default buffer window is three seconds, which is appropriate for many scenarios.
    -   Video complexity is set to determine the tradeoff between the quality of the encoded content and the time that is required to encode. If you do not set a value, the default value is used. However, you can find the recommended modes for a specific codec by calling [IWMCodecProps::GetCodecProp](iwmcodecpropsgetcodecprop.md) to retrieve g\_wszWMVCComplexityExLive, g\_wszWMVCComplexityExOffline, and g\_wszWMVCComplexityExMax. Then you can set [MFPKEY\_COMPLEXITYEX](mfpkey-complexityexproperty.md) to a value between 0 and the reported maximum complexity.
    -   [MFPKEY\_CRISP](mfpkey-crispproperty.md) specifies the relative importance of video smoothness and the image quality of encoded frames. In most cases, the default value works fine.
    -   For video content stored in a container other than ASF, the [MFPKEY\_ASFOVERHEADPERFRAME](mfpkey-asfoverheadperframeproperty.md) property must be set to 0. This is not the default value.

    For information about configuring VBR streams, see [Using VBR Encoding](usingvbrencoding.md).

2.  Configure the [**DMO\_MEDIA\_TYPE**](dshow.dmo_media_type) structure for the input type, or if you are using the Media Foundation SDK, use the [**MFInitMediaTypeFromVideoInfoHeader**](mfinitmediatypefromvideoinfoheader.md) function. Use a [**VIDEOINFOHEADER**](dshow.videoinfoheader) structure describing the uncompressed input content. The codec does not resize video or convert the color space.
3.  Set the input type using [**IMediaObject::SetInputType**](dshow.imediaobject_setinputtype) or [**IMFTransform::SetInputType**](imftransform-setinputtype.md).
4.  Configure the output type for the encoder. After the input type is set, the encoder enumerates output types that are complete except for the **dwBitrate** member of the [**VIDEOINFOHEADER**](dshow.videoinfoheader) structure, or the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute of the [**IMFMediaType**](imfmediatype.md) interface. If you retrieve an output type before setting an input type, the delivered [**DMO\_MEDIA\_TYPE**](dshow.dmo_media_type) structure will not have an associated **VIDEOINFOHEADER**.
5.  Retrieve the codec private data and append it to the [**VIDEOINFOHEADER**](dshow.videoinfoheader) structure that you pass to the [**DMO\_MEDIA\_TYPE**](dshow.dmo_media_type) structure or to [**IMFMediaType**](imfmediatype.md). For more information, see [Using Video Codec Private Data](usingvideocodecprivatedata.md).
6.  Set the output type by calling the [**IMediaObject::SetOutputType**](dshow.imediaobject_setoutputtype) or [**IMFTransform::SetOutputType**](imftransform-setoutputtype.md) method. Either pass the [**DMO\_MEDIA\_TYPE**](dshow.dmo_media_type) structure with the completed [**VIDEOINFOHEADER**](dshow.videoinfoheader) structure (including appended private data) referenced in the **pbFormat** member, or construct an [**IMFMediaType**](imfmediatype.md) by calling [**MFInitMediaTypeFromVideoInfoHeader**](mfinitmediatypefromvideoinfoheader.md).

> [!Note]  
> The video encoder object supports two outputs. The second output is for encoder "post view". It delivers the uncompressed samples as they will be delivered from the decoder. This enables you to monitor the quality of the encoding without having to wait until the entire stream is processed. This output is optional. If you want to use it, configure its type following the same process used to set the encoder input type.

 

## Related topics

<dl> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



