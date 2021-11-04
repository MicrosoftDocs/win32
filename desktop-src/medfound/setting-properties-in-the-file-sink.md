---
description: Learn about setting properties in the ASF file sink, which an application can use to archive ASF media data to a file.
ms.assetid: a47caabd-23e3-4d22-b4b6-5fdb79d62ca1
title: Setting Properties in the File Sink
ms.topic: article
ms.date: 05/31/2018
---

# Setting Properties in the File Sink

The ASF file sink is an implementation of [**IMFMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasink) provided by Media Foundation that an application can use to archive ASF media data to a file. For information about ASF Media Sinks' object model and general usage, see [ASF Media Sinks](asf-media-sinks.md).

After [Creating the ASF file sink](creating-the-asf-file-sink.md), it must be configured with information about the streams in the output file. This procedure is described in [Adding Stream Information to the ASF File Sink](adding-stream-information-to-the-asf-file-sink.md). You can set additional properties on the file sink depending on the type of encoding; leaky buckets; general file properties. These settings are not written in the final ASF Header Object. This topic describes process of adding these properties in the file sink's property store.

The ContentInfo object maintains the global file properties and individual stream properties for the file sink. For information about getting a reference to the file sink's ASF ContentInfo object, see [Creating the ASF File Sink](creating-the-asf-file-sink.md).

To get a reference to the file sink's property store ([**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)), call [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore) on the file sink's ContentInfo object's reference.

## Stream Encoding Properties

To encode content properly the file needs to know certain encoding information such as type of encoding and the related encoding parameters. These values are set on the file sink as property values in a property store that is maintained by the ASF ContentInfo object. If you are configuring the file sink before instantiating the relevant encoders, you can use the ContentInfo object with all the populated properties to create the Windows Media encoders. In this case, the properties are automatically set on the instantiated encoders. Conversely, if you are creating the encoders before the sink, make sure that the properties that you set on the encoders are copied into the file sink's property store.

To set encoding properties, you need access to the file sink's stream-level property store. Pass the stream number in the *wStreamNumber* parameter of the [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore) method. The stream numbers must match the values set while configuring each stream in the profile. Property values are set by calling [**IPropertyStore::SetValue**](/windows/win32/api/propsys/nn-propsys-ipropertystore). The following table describes the supported properties.

The properties depend on the type of encoding. For information about the properties and the respective values that you must set, see [Encoding Properties](configuring-the-encoder.md).

## Leaky Bucket Property

Leaky bucket parameters determine the actual buffer window used by the encoder for the stream. The file sink's [**MFPKEY\_ASFSTREAMSINK\_CORRECTED\_LEAKYBUCKET**](mfpkey-asfstreamsink-corrected-leakybucket-property.md) property contains the leaky bucket parameters, bit rate, buffer window, and initial buffer fullness.This property is set in the stream-level property property store for the file sink and must be set after encoders have been created and configured. This value is set in the . During the media type negotiation, the encoder decides the buffer window and the bit rate to use. You can get these values by using the **IWMCodecLeakyBucket** interface, which is defined in wmcodecifaces.h and you must link to wmcodecdspuuid.lib to call its methods.

The retrieved values can be set for this property for each stream in the ASF file sink.

## Global File Sink Properties

To get the file sink's global property store, pass 0 in the *wStreamNumber* parameter of the [**IMFASFContentInfo::GetEncodingConfigurationPropertyStore**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getencodingconfigurationpropertystore) method. Property values are set by calling [**IPropertyStore::SetValue**](/windows/win32/api/propsys/nn-propsys-ipropertystore). The following table describes the supported properties.

| File-level Properties                                                                                | Description                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MFPKEY\_ASFMEDIASINK\_BASE\_SENDTIME**](mfpkey-asfmediasink-base-sendtime-property.md)           | The send time indicates when the payload inside the leaky bucket will be released. This property value indicates the first send time. The multiplexer uses this value to calculate the subsequent send times for the generated packets and ensures that data flows steadily through the leaky bucket. |
| [**MFPKEY\_ASFMEDIASINK\_AUTOADJUST\_BITRATE**](mfpkey-asfmediasink-autoadjust-bitrate-property.md) | This BOOL value indicates whether the multiplexer needs to adjust the bit rate automatically to ensure that data does not overflow the leaky bucket.                                                                                                                                                  |
| [**MFPKEY\_ASFMEDIASINK\_DRMACTION**](mfpkey-asfmediasink-drmaction-property.md)                    | This indicates the ASF media sink DRM action for file generation. In this release, only DRM transcode is supported.                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[ASF Media Sinks](asf-media-sinks.md)
</dt> <dt>

[Pipeline Layer ASF Components](pipeline-layer-asf-components.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 
