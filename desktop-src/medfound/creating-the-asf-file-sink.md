---
Description: 'The ASF file sink is an implementation of IMFMediaSink provided by Media Foundation that an application can use to archive ASF media data to a file. For information about ASF Media Sinks' object model and general usage, see ASF Media Sinks.'
ms.assetid: '991f3345-a6b4-45c2-a89d-3c13c70b6bbc'
title: Creating the ASF File Sink
---

# Creating the ASF File Sink

The ASF file sink is an implementation of [**IMFMediaSink**](imfmediasink.md) provided by Media Foundation that an application can use to archive ASF media data to a file. For information about ASF Media Sinks' object model and general usage, see [ASF Media Sinks](asf-media-sinks.md).

There are two ways of creating an instance of the ASF file sink. You can call [**MFCreateASFMediaSink**](mfcreateasfmediasink.md) or [**MFCreateASFMediaSinkActivate**](mfcreateasfmediasinkactivate.md).

If you call [**MFCreateASFMediaSink**](mfcreateasfmediasink.md), you must specify a byte stream, for the output file, into which the sink will write the ASF content during an encoding session. The specified byte stream must have seekable and writable capabilities otherwise the **MFCreateASFMediaSink** call fails with the E\_FAIL error code. This call creates an in-process file sink object and returns a pointer to the [**IMFMediaSink**](imfmediasink.md) interface of the file sink.

If you call [**MFCreateASFMediaSinkActivate**](mfcreateasfmediasinkactivate.md), you must specify the URL of the output file into which the file sink will write media data. In this case, the file sink internally creates the byte stream. The function returns a pointer to the [**IMFActivate**](imfactivate.md) interface of the file sink. To

Consider [**MFCreateASFMediaSinkActivate**](mfcreateasfmediasinkactivate.md) instead of [**MFCreateASFMediaSink**](mfcreateasfmediasink.md), when your encoding topology is designed as follows:

-   The encoding topology is for the protected media path (PMP) and the file sink is used out-of-process.
-   The output node of the topology is created by using the returned pointer to the activate object of the file sink and your application is keeping track of the streams in the file sink by stream numbers.
    > [!Note]  
    > You can activate the file sink by calling [**IMFActivate::ActivateObject**](imfactivate-activateobject.md). However you do not need to activate the object explictly. The Media Session keeps track of the activation object and activates the file sink automatically during the encoding session.

     

-   The stream information is configured in the ContentInfo object. Disucssed in the next sub-section.

After creating the ASF file sink it must be configured before building the topology. The file sink needs to know the following information in order to generate the output file.

-   Basic stream information
-   Encoding mode information
-   Metadata

The file sink implements the [ASF ContentInfo Object](asf-contentinfo-object.md) and exposes the [**IMFASFContentInfo**](imfasfcontentinfo.md) interface so that an application can use it to set information related to the streams and encoding. Depending on the function you called to create the file sink, there are two ways of getting a reference to the **IMFASFContentInfo** interface.

-   If you call the [**MFCreateASFMediaSink**](mfcreateasfmediasink.md) function, the application must query for [**IMFASFContentInfo**](imfasfcontentinfo.md) interface by calling **IMFMediaSink::QueryInterface** on the returned file sink.
-   If you choose to call [**MFCreateASFMediaSinkActivate**](mfcreateasfmediasinkactivate.md), this function expects that you have a fully-configured ContentInfo object prior to the call. To do this, you need to create an empty ContentInfo object by calling [**MFCreateASFContentInfo**](mfcreateasfcontentinfo.md) and then configure it with all the required information. Pass the configured ContentInfo object to the **MFCreateASFMediaSinkActivate** to receive a pointer to the sink activate object. You cannot activate the file sink by using the returned activation object and then change any stream or encoding information.

For information about configuring sink streams and specific properties, see the following topics:

-   [Adding Stream Information to the ASF File Sink](adding-stream-information-to-the-asf-file-sink.md)
-   [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md)
-   [Adding Metadata to the File Sink](adding-metadata-to-the-file-sink.md)

## Related topics

<dl> <dt>

[ASF Media Sinks](asf-media-sinks.md)
</dt> <dt>

[Pipeline Layer ASF Components](pipeline-layer-asf-components.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 



