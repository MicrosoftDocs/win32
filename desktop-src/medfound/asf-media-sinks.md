---
description: The ASF media sink is the final component in the encoding pipeline that enables an application to write an ASF file.
ms.assetid: 65bb8822-5eb0-46a3-ab9e-c55ae466e982
title: ASF Media Sinks
ms.topic: article
ms.date: 05/31/2018
---

# ASF Media Sinks

The ASF media sink is the final component in the encoding pipeline that enables an application to write an ASF file.

Media Foundation provides two types of ASF media sinks:

-   *ASF file sink* is used to archive ASF media data to a file.
-   *ASF streaming sink* is used to write ASF content in a byte stream that can be streamed across the network.

ASF media sinks contain one or more stream sinks, which represents the data to write for each stream in the output ASF file. For encoding applications that run on Windows Vista, you must manually configure the encoding topology by creating and configuring the ASF media sink and then adding it to the topology. In Windows 7, if you are using the fast transcode objects to create the topology, you do not have create the media sink directly and the application does not call any methods on the media sink or any of the stream sinks. The fast transcode objects instantiate the required media sinks and add it to the topology before returning a reference to the caller application. However for fast transcode objects, there are some restrictions that apply depending on the type of encoding.

-   [ASF Media Sink Object Model](#asf-media-sink-object-model)
-   [ASF File Sink](#asf-file-sink)
-   [Related topics](#related-topics)

## ASF Media Sink Object Model

ASF media sinks implement the [**IMFMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasink) interface and exposes the following interfaces. An application can get a reference to these interfaces by calling [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the ASF media sink it is using for generating output samples.



| Interface                                                  | Description                                                                                                                                                                                            |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMFMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasink)                       | Required for all media sinks.                                                                                                                                                                          |
| [**IMFFinalizableMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imffinalizablemediasink) | Implemented by the ASF file sink that writes the generated media content to a file. You can use the methods on this interface to flush data and update the ASF Header Object of the final output file. |
| [**IMFClockStateSink**](/windows/desktop/api/mfidl/nn-mfidl-imfclockstatesink)             | Receives state-change notifications from the presentation clock.                                                                                                                                       |
| [**IMFASFContentInfo**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfcontentinfo)             | The ASF ContentInfo object is a WMContainer level object that mainly stores ASF Header Object information. This is used to create ASF media sinks.                                                     |
| [**IMFMetadata**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadata)                         | Used to describe the metadata for the ASF file.                                                                                                                                                        |
| [**IMFMetadataProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadataprovider)         | Retrieves a collection of metadata, either for an entire presentation, or for one stream in the presentation.                                                                                          |



 

## ASF File Sink

The ASF file sink is an implementation of [**IMFMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasink) provided by Media Foundation that an application can use to archive ASF media data to a file.

You need to create, configure, and call methods on the file sink or any of its stream sinks if you are using the pipeline layer objects to write a new ASF file. After configuring the file sink you can then add it to the encoding pipeline.

Here are the general steps for using the ASF file sink:

1.  Create the file sink in-process or out-of-process.
2.  Configure the file sink with all the streams, encoding properties, and metadata information.
3.  Associate the file sink with the output topology node either by enumerating the stream sinks or by keeping track of the stream numbers with in the sink.

The following topics contain detailed information about working with the ASF file sink:

-   [Creating the ASF File Sink](creating-the-asf-file-sink.md)
-   [Adding Stream Information to the ASF File Sink](adding-stream-information-to-the-asf-file-sink.md)
-   [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md)
-   [Adding Metadata to the File Sink](adding-metadata-to-the-file-sink.md)
-   [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md)

## Related topics

<dl> <dt>

[Pipeline Layer ASF Components](pipeline-layer-asf-components.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 
