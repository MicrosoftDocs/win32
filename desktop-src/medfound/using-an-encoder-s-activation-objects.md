---
Description: 'For converting media files into ASF format, you can use Windows Media encoders. To use these encoders, they must be registered with the system.'
ms.assetid: '18c26619-6047-4f7f-bb65-ca418f02e5b1'
title: 'Using an Encoder''s Activation Objects'
---

# Using an Encoder's Activation Objects

For converting media files into ASF format, you can use Windows Media encoders. To use these encoders, they must be registered with the system.

For information about encoder registration, see [Instantiating an Encoder MFT](instantiating-the-encoder-mft.md).

-   [Using an Encoder's Activation Objects](#using-an-encoders-activation-objects)
-   [Encoder Enumeration in Windows 7 and Later](#encoder-enumeration-in-windows-7-and-later)
-   [Related topics](#related-topics)

## Using an Encoder's Activation Objects

As an alternative to using an encoder's [**IMFTransform**](imftransform.md) interface (described in [Creating an Encoder by Using CoCreateInstance](using-an-encoder-s-imftransform--interface.md)), you can create an instance of the activation object for the encoder. Activation objects facilitates encoder creation and Media Foundation provides the following two functions for this approach:

-   [**MFCreateWMAEncoderActivate**](mfcreatewmaencoderactivate.md) for instantiating the Windows Media audio encoder.
-   [**MFCreateWMVEncoderActivate**](mfcreatewmvencoderactivate.md) for instantiating the Windows Media video encoder.

Both these functions require that you create the target media type and set the encoding properties before calling these functions. If your application is using [Pipeline Layer ASF Components](pipeline-layer-asf-components.md) to encode a file to ASF format, and have already created and configured the [ASF Media Sinks](asf-media-sinks.md), you can get this set of information from the ASF media sink.

[**MFCreateWMAEncoderActivate**](mfcreatewmaencoderactivate.md) and [**MFCreateWMVEncoderActivate**](mfcreatewmvencoderactivate.md) set the output type of the encoder to the media type specified by the application.

**Note**  If you are using [**MFCreateWMAEncoderActivate**](mfcreatewmaencoderactivate.md) and [**MFCreateWMVEncoderActivate**](mfcreatewmvencoderactivate.md) you can activate the encoder by calling [**IMFActivate::ActivateObject**](imfactivate-activateobject.md) but you cannot change the input and the output media types of the encoder nor can you change any of the encoding properties.

For more information about creating Media Foundation objects by using activation objects, see [Activation Objects](activation-objects.md).

**To get the target media type from the ASF media sink**

1.  Get a pointer to the [**IMFASFContentInfo**](imfasfcontentinfo.md) pointer of the ASF media sink by calling **IMFMediaSink::QueryInterface** on the ASF media sink and passing **IID\_IMFASFContentInfo** as the interface identifier.
2.  Get the ASF profile object associated with the ContentInfo object.
3.  Enumerate the streams in the profile to get the stream's media type.

**To get the encoding properties from the ASF media sink**

1.  If you have configured the [Encoding Properties](configuring-the-encoder.md) in the media sink (described in [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md)), you can a reference to the sink's property store by calling **IMFMediaSink::QueryInterface** on the ASF media sink and passing **IID\_IPropertyStore** as the interface identifier.
2.  If you have a pointer to the sink's ContentInfo object, you can call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](imfasfcontentinfo-getencodingconfigurationpropertystore.md) to get a reference to the media sink's property store.

    Make sure that all of encoding properties that are set on the ASF media sink are reflected in the property store passed to [**MFCreateWMAEncoderActivate**](mfcreatewmaencoderactivate.md) and [**MFCreateWMVEncoderActivate**](mfcreatewmvencoderactivate.md). The encoder is configured automatically based on the settings specified by the application.

While creating the transform node in the encoding topology, you can set the object type as an [**IMFActivate**](imfactivate.md) pointer received in these two calls. When the topology is resolved, the Media Session uses the activation object to create an instance of the encoder MFT.

## Encoder Enumeration in Windows 7 and Later

For applications that are running on Windows 7, in addition to [**MFTEnum**](mftenum.md) you can enumerate the encoder MFTs by calling [**MFTEnumEx**](mftenumex.md). This function returns a pointer to the activation object of the encoder MFT. The structure of the function is very similar to **MFTEnum** described above except **MFTEnumEx**returns an array of [**IMFActivate**](imfactivate.md) pointers for the encoder MFTs that match the search criteria.

## Related topics

<dl> <dt>

[Instantiating an Encoder MFT](instantiating-the-encoder-mft.md)
</dt> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 



