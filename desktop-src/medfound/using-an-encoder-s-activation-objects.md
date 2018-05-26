---
Description: For converting media files into ASF format, you can use Windows Media encoders. To use these encoders, they must be registered with the system.
ms.assetid: 18c26619-6047-4f7f-bb65-ca418f02e5b1
title: Using an Encoders Activation Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using an Encoder's Activation Objects

For converting media files into ASF format, you can use Windows Media encoders. To use these encoders, they must be registered with the system.

For information about encoder registration, see [Instantiating an Encoder MFT](instantiating-the-encoder-mft.md).

-   [Using an Encoder's Activation Objects](#using-an-encoders-activation-objects)
-   [Encoder Enumeration in Windows 7 and Later](#encoder-enumeration-in-windows-7-and-later)
-   [Related topics](#related-topics)

## Using an Encoder's Activation Objects

As an alternative to using an encoder's [**IMFTransform**](/windows/win32/mftransform/nn-mftransform-imftransform?branch=master) interface (described in [Creating an Encoder by Using CoCreateInstance](using-an-encoder-s-imftransform--interface.md)), you can create an instance of the activation object for the encoder. Activation objects facilitates encoder creation and Media Foundation provides the following two functions for this approach:

-   [**MFCreateWMAEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate?branch=master) for instantiating the Windows Media audio encoder.
-   [**MFCreateWMVEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmvencoderactivate?branch=master) for instantiating the Windows Media video encoder.

Both these functions require that you create the target media type and set the encoding properties before calling these functions. If your application is using [Pipeline Layer ASF Components](pipeline-layer-asf-components.md) to encode a file to ASF format, and have already created and configured the [ASF Media Sinks](asf-media-sinks.md), you can get this set of information from the ASF media sink.

[**MFCreateWMAEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate?branch=master) and [**MFCreateWMVEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmvencoderactivate?branch=master) set the output type of the encoder to the media type specified by the application.

**Note**  If you are using [**MFCreateWMAEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate?branch=master) and [**MFCreateWMVEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmvencoderactivate?branch=master) you can activate the encoder by calling [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master) but you cannot change the input and the output media types of the encoder nor can you change any of the encoding properties.

For more information about creating Media Foundation objects by using activation objects, see [Activation Objects](activation-objects.md).

**To get the target media type from the ASF media sink**

1.  Get a pointer to the [**IMFASFContentInfo**](/windows/win32/wmcontainer/nn-wmcontainer-imfasfcontentinfo?branch=master) pointer of the ASF media sink by calling **IMFMediaSink::QueryInterface** on the ASF media sink and passing **IID\_IMFASFContentInfo** as the interface identifier.
2.  Get the ASF profile object associated with the ContentInfo object.
3.  Enumerate the streams in the profile to get the stream's media type.

**To get the encoding properties from the ASF media sink**

1.  If you have configured the [Encoding Properties](configuring-the-encoder.md) in the media sink (described in [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md)), you can a reference to the sink's property store by calling **IMFMediaSink::QueryInterface** on the ASF media sink and passing **IID\_IPropertyStore** as the interface identifier.
2.  If you have a pointer to the sink's ContentInfo object, you can call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore?branch=master) to get a reference to the media sink's property store.

    Make sure that all of encoding properties that are set on the ASF media sink are reflected in the property store passed to [**MFCreateWMAEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate?branch=master) and [**MFCreateWMVEncoderActivate**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreatewmvencoderactivate?branch=master). The encoder is configured automatically based on the settings specified by the application.

While creating the transform node in the encoding topology, you can set the object type as an [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointer received in these two calls. When the topology is resolved, the Media Session uses the activation object to create an instance of the encoder MFT.

## Encoder Enumeration in Windows 7 and Later

For applications that are running on Windows 7, in addition to [**MFTEnum**](/windows/win32/mfapi/nf-mfapi-mftenum?branch=master) you can enumerate the encoder MFTs by calling [**MFTEnumEx**](/windows/win32/mfapi/nf-mfapi-mftenumex?branch=master). This function returns a pointer to the activation object of the encoder MFT. The structure of the function is very similar to **MFTEnum** described above except **MFTEnumEx**returns an array of [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointers for the encoder MFTs that match the search criteria.

## Related topics

<dl> <dt>

[Instantiating an Encoder MFT](instantiating-the-encoder-mft.md)
</dt> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 



