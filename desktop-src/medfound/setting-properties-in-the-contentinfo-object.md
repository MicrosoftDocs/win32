---
description: While creating an ASF file, the ContentInfo object needs to know the characteristics of the media content so that the various header objects are populated with the correct values.
ms.assetid: 30e3c10b-1310-4194-8b83-221dfe73b03c
title: Setting Properties in the ContentInfo Object
ms.topic: article
ms.date: 05/31/2018
---

# Setting Properties in the ContentInfo Object

While creating an ASF file, the ContentInfo object needs to know the characteristics of the media content so that the various header objects are populated with the correct values.

-   [Content-Related Settings in the ContentInfo Object](#content-related-settings-in-the-contentinfo-object)
-   [Configuring the ContentInfo Object with Encoder Settings](#configuring-the-contentinfo-object-with-encoder-settings)
-   [Related topics](#related-topics)

## Content-Related Settings in the ContentInfo Object

Content configuration settings are stream settings, which are contained within the profile and specify the stream identifier, the media type, and the leaky bucket parameters for the media sink. After the profile is set on the ContentInfo object by calling [**IMFASFContentInfo::SetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-setprofile), these values are reflected in the ASF Header Object that was generated. For information about these settings, see [Creating and Configuring ASF Streams](creating-and-configuring-asf-streams.md).

## Configuring the ContentInfo Object with Encoder Settings

Digital media audio or video data is complex and takes up large amounts of memory. Under most circumstances, both audio and video are compressed by using encoders before being added to an ASF file. In Media Foundation, encoders are implemented as [Media Foundation Transforms](media-foundation-transforms.md) (MFTs) with one input and one output. You must select the output media type depending on the media type of the input stream and the encoding type you choose for compressing the stream.

Before the encoding session, the encoder must be configured by setting the relevant properties depending on the type of encoding.

After configuring the encoder, you must configure the ContentInfo object with the encoder values because the [ASF Multiplexer](asf-multiplexer.md) and the ASF Media Sink, which are initialized with the populated ContentInfo object, use settings such as the leaky bucket values, to generate ASF data packets. The values are not saved in the final ASF Header Object. The encoding settings are exposed as properties. To configure the ContentInfo object with the encoder properties, do the following:

1.  Get a pointer to the encoder's property store by querying the encoder ([**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface) directly for the **IPropertyStore** interface.
2.  Call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore). To set stream-specific properties, specify the stream identifier in the *wStreamNumber* parameter; for file-level properties, pass 0. The *ppIStore* parameter receives a pointer to the **IPropertyStore** interface. The received property store is empty.
3.  Call **IPropertyStore::GetValue** on the encoder and get the property value by specifying the property key constants. For a complete list of encoding properties, see the [Codec Programming Reference](/previous-versions//aa384554(v=vs.85)).
4.  Call **IPropertyStore::SetValue** on the ContentInfo object to set the required property in the property store.
5.  Repeat steps 3 and 4 for each property that you want to set.

The ASF media sink can be created by using an activation object by calling [**MFCreateASFMediaSinkActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfmediasinkactivate). The new media sink object is configured based on media sink-specific settings that can be set in the ContentInfo object's property store. The following table shows the ASF media sink property constants.



| Property                                                                                                     | Description                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MFPKEY\_ASFMEDIASINK\_BASE\_SENDTIME**](mfpkey-asfmediasink-base-sendtime-property.md)                   | The send time indicates when the payload inside the leaky bucket will be released. This property value indicates the first send time. The multiplexer uses this value to calculate the subsequent send times for the generated packets and ensures that data flows steadily through the leaky bucket. |
| [**MFPKEY\_ASFMEDIASINK\_AUTOADJUST\_BITRATE**](mfpkey-asfmediasink-autoadjust-bitrate-property.md)         | This **BOOL** value indicates whether the multiplexer needs to adjust the bit rate automatically to ensure that data does not overflow the leaky bucket.                                                                                                                                              |
| [**MFPKEY\_ASFMEDIASINK\_DRMACTION**](mfpkey-asfmediasink-drmaction-property.md)                            | This indicates the ASF media sink DRM action for file generation. In this release, only DRM transcode is supported.                                                                                                                                                                                   |
| [**MFPKEY\_ASFSTREAMSINK\_CORRECTED\_LEAKYBUCKET**](mfpkey-asfstreamsink-corrected-leakybucket-property.md) | This property must be set when the encoder decides which buffer window and bit rate to use. To set these values, use the [**IWMCodecLeakyBucket**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecleakybucket) interface. This must be set for each stream in the ASF file.                                                     |



 

## Related topics

<dl> <dt>

[Writing an ASF Header Object for a New File](writing-an-asf-header-object-for-a-new-file.md)
</dt> </dl>

 

 
