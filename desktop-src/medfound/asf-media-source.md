---
description: Media Foundation provides the ASF media source that an application can use to represent an ASF file in the pipeline layer of the architecture.
ms.assetid: a2d2b382-d666-4a37-a6a9-0b839fbfbec3
title: ASF Media Source
ms.topic: article
ms.date: 05/31/2018
---

# ASF Media Source

Media Foundation provides the ASF media source that an application can use to represent an ASF file in the pipeline layer of the architecture.

In order to play an ASF file, an application can use the ASF media source to feed data into a playback pipeline. In an encoding scenario, application can use the ASF media source as the source to convert into another format or for converting a higher bit-rate file to a lower bit-rate file without changing formats. The ASF media source must be used in the pipeline layer, that is, an application must use the Media Session to control the operation. This level of access allows the applications to get events while the Media Session is in progress. To get lower-level access to the ASF content, an application must use the WMContainer Layer ASF components.

The ASF media source implements the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface, which is the generic interface for media sources in Media Foundation. Like any other media source, the ASF media source provides a presentation descriptor that primarily describes the ASF Header Object. In addition, the ASF media source provides stream descriptors that represent each stream in the media content. For more information, see [ASF File Structure](asf-file-structure.md).

-   [Creating the ASF Media Source](#creating-the-asf-media-source)
-   [Configuration Settings for the ASF Media Source](#configuration-settings-for-the-asf-media-source)
-   [ASF Media Source Object Model](#asf-media-source-object-model)
-   [ASF Media Source Services](#asf-media-source-services)
    -   [Timecode Translation](#timecode-translation)
-   [Related topics](#related-topics)

## Creating the ASF Media Source

To create the ASF media source, the application must use the [Source Resolver](source-resolver.md). In order to create the ASF media source, the application must provide the source for which the source resolver creates the ASF media source. The source information must be provided by either specifying the URL of the source file or the byte stream that contains the media. If the application chooses to create the ASF media source by specifying the URL, it must call either [**IMFSourceResolver::CreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-createobjectfromurl) for synchronous operation or **IMFSourceResolver::Begin…EndCreateObjectFromURL** for asynchronous operation. The process for creating the media source from a byte stream is similar. The application must call either [**IMFSourceResolver::CreateObjectFromByteStream**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-createobjectfrombytestream) for synchronous operation or **IMFSourceResolver::Begin…EndCreateObjectFromBytestream** for asynchronous operation. These calls must specify MF\_RESOLUTION\_MEDIASOURCE in *dwFlags* parameter. For more information about using this flag, see Using the Source Resolver.

If the application specifies a URL, for a local file, the URL string can contain the path of the media file or can be prefixed with the “file: “scheme. The file name extension must be ".asf", ".wm", L".wma", or ".wmv". For an ASF file on the network, the source resolver creates the [Network Source](network-source-features.md), which uses the ASF media source.

During the object creation process, the source resolver looks up the list of scheme handlers and the byte stream handlers in the system registry and loads the closest matching handler that can parse the media content and also create the media source object underneath. Irrespective of the method used to create the media source (URL and byte stream), the source resolver creates a byte stream and reads the contents of source media into the byte stream. For more information, see [Scheme Handlers and Byte-Stream Handlers](scheme-handlers-and-byte-stream-handlers.md).

For code example about how to create a media source, see [Using the Source Resolver](using-the-source-resolver.md).

## Configuration Settings for the ASF Media Source

The source resolver queries for the capabilities of the underlying byte stream and determines the operations are allowed on the newly created media source. One of such capabilities is seeking. If a seek operation is allowed, the application can specify the seeking mode that the media source uses while seeking to a particular point in the presentation.

An application can set the seek mode, for the media source to use, during object creation. After the ASF media source is created with the specified seek mode, it cannot be modified on the media source or dynamically changed during a presentation. Seeking preferences are specified as properties in the application’s call to the relevant source resolver methods that are used to create the media source. These set of properties are set in a property store and passed to the *pProps* parameter. If these properties are not passed, the media source functions with the default settings. For more information about setting these properties, see [Configuring a Media Source](configuring-a-media-source.md).

If seeking is allowed, the ASF media source supports the following seek modes:

-   Exact seeking: In this mode, the ASF media source relies on the ASF Index Object of the ASF file. If the file does not have the Index Object, exact seeking is disabled and one of the other modes are used depending on the application-specified properties that are set on the media source.
-   Approximate seeking: This mode is requested by the application by passing [**MFPKEY\_ASFMediaSource\_ApproxSeek**](mfpkey-asfmediasource-approxseek-property.md) in the property store to the relevant source resolver methods. However, approximate seeking is only used if the byte stream does not support time-based seeking. In this mode, the media source determine a start time that is relatively closer to the seek time. If the ASF file contains an ASF Index Object, it is used to calculate the start time. Approximate seeking is less accurate but faster than exact seeking because the time taken render the first sample at the predetermined start time is faster.
-   Iterative seeking: To set this mode, the application must set the [MFPKEY\_ASFMediaSource\_IterativeSeekIfNoIndex](mfpkey-asfmediasource-iterativeseekifnoindex.md) property. Iterative seeking is an algorithm to find a position in an ASF file that contains no ASF Index Object. In this mode, the media source determins a rough estimate of the seek point by reading the byte stream offset. It uses a series of approximations, based on the average bit rate, to get progressively closer to the target seek time. (The algorithm is similar to a binary search.) Iterative seeking can take longer than seeking by using the Index Object, so it is disabled by default. If you set this property, use the following properties to set the search parameters: [MFPKEY\_ASFMediaSource\_IterativeSeek\_Max\_Count](mfpkey-asfmediasource-iterativeseek-max-count.md)[MFPKEY\_ASFMediaSource\_IterativeSeek\_Tolerance\_In\_MilliSecond](mfpkey-asfmediasource-iterativeseek-tolerance-in-millisecond.md). These properties set the maximum number of iterations and the tolerance, respectively. The algorithm halts when it reaches the maximum number of iterations, or when it finds a packet whose distance from the seek time is within the specified tolerance.

In a nutshell, the application has the option of choosing approximate or iterative seeking when the ASF file does not contain an ASF Index Object.

## ASF Media Source Object Model

The ASF media source implements the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface and exposes the following interfaces. An application can get a reference to these interfaces by calling **IMFMediaSource::QueryInterface** on the ASF media source.



| Interface                                                | Description                                                                                                                                        |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)                 | Required for all media sources.                                                                                                                    |
| [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) | Required for all media sources. Allows applications to get events from the media source through the Media Session.                                 |
| [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)                   | Queries the media source for the specified service interface.                                                                                      |
| [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)               | Sets and gets properties on the media source. Each property contains a descriptive name and a value.                                               |
| [**IMFMetadata**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadata)                       | Describes the metadata for the ASF file.                                                                                                           |
| [**IMFMetadataProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadataprovider)       | Retrieves a collection of metadata, either for an entire presentation, or for one stream in the presentation.                                      |
| [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)                 | Queries the range of playback rates that are supported, including reverse playback.                                                                |
| [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol)                 | Gets or sets the playback rate.                                                                                                                    |
| [**IMFTrustedInput**](/windows/desktop/api/mfidl/nn-mfidl-imftrustedinput)               | Gets the ITA for each of the ASF streams contained in the source.                                                                                  |
| [**IMFPMPClient**](/windows/desktop/api/mfidl/nn-mfidl-imfpmpclient)                     | Enables a media source to receive a pointer to the [**IMFPMPHost**](/windows/desktop/api/mfidl/nn-mfidl-imfpmphost) interface, which is used to create objects in the PMP process. |
| [**IMFTimecodeTranslate**](/windows/desktop/api/mfidl/nn-mfidl-imftimecodetranslate)     | Converts between Society of Motion Picture and Television Engineers (SMPTE) time codes and 100-nanosecond time units.                              |



 

## ASF Media Source Services

The ASF media source provides various services that are scoped for ASF file. To get a pointer to a particular service, the application must use one of the following service identifiers in its call to [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice). For information, see [Service Interfaces](service-interfaces.md).



| Service Identifier               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MF\_RATE\_CONTROL\_SERVICE       | By using this identifier, an application can get a pointer to either [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) or [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol) interfaces. By using the rate support object implemented by the media source, the application can check if a particular rate is supported by the underlying ASF media file also get the fastest and the slowest rate. By using the rate control object the application can get and set the playback rate. If the application specifies a particular rate for playback, the ASF media source first checks if the requested rate is within the rate limits (determined by fasted and slowest rates) and then sets the rate. This does not check for variable conditions as the bitrate might change any moment depending on the network bandwidth. For more information, [Rate Control](rate-control.md). |
| MF\_METADATA\_PROVIDER\_SERVICE  | By using this identifier, the application can get a pointer to the [**IMFMetadataProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadataprovider) interface of the ASF media source. This interface provides access to information about ASF file specifically the ASF Header Objects and the streams contained within the media content. Header information is exposes through presentation descriptor attributes and stream information is provided through stream descriptor attributes. For more information about these attributes, see [Media Foundation Attributes for ASF Header Objects](media-foundation-attributes-for-asf-header-objects.md). In addition to information that is exposed through attributes, there also exists descriptive metadata, which are set as properties.                                                                                                 |
| MF\_PROPERTY\_HANDLER\_SERVICE   | By using this identifier, the application can get a pointer to the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) interface of the ASF media source. The property store contains all the metadata related to the ASF file. This identifier is new in Windows 7 and replaces MF\_METADATA\_PROVIDER\_SERVICE for getting metadata properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MFNETSOURCE\_STATISTICS\_SERVICE | For more information, see Retrieving Network Statistics in [Client Logging](client-logging.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MF\_TIMECODE\_SERVICE            | By using this identifier, the application can get a pointer to the media source’s [**IMFTimecodeTranslate**](/windows/desktop/api/mfidl/nn-mfidl-imftimecodetranslate) interface. This implementation can be used to perform time code translations such as converting SMPTE time code to 100-nano second units and back.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

### Timecode Translation

The ASF media source provides a time code translation service that allows your application to convert SMPTE time code to the closest presentation time (in 100-nanosecond unit). Conversely, the application can also get the time code for a requested presentation time. The service is available through the [**IMFTimecodeTranslate**](/windows/desktop/api/mfidl/nn-mfidl-imftimecodetranslate) interface, which the ASF media source implements. The method calls on this interface pointer are asynchronous that can run from your main application thread without blocking the user interface of your application.

The following steps summarize the procedure for time code translation:

1.  Get pointer to the [**IMFTimecodeTranslate**](/windows/desktop/api/mfidl/nn-mfidl-imftimecodetranslate) interface of the ASF media source by calling [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) and specifying the **MF\_TIMECODE\_SERVICE** identifier.
2.  Call [**IMFTimecodeTranslate::BeginConvertTimecodeToHNS**](/windows/desktop/api/mfidl/nf-mfidl-imftimecodetranslate-beginconverttimecodetohns) or [**IMFTimecodeTranslate::BeginConvertHNSToTimecode**](/windows/desktop/api/mfidl/nf-mfidl-imftimecodetranslate-beginconverthnstotimecode) and specify the time that is to be translated.. For **BeginConvertTimecodeToHNS** the time code must be specified as a [**PROPVARIANT**](/windows/win32/api/propidl/ns-propidl-propvariant) variable with **VT\_I8** data type. The **BeginConvertHNSToTimecode** method requires the time in 100-nanosecond units as the [**MFTIME**](mftime.md) type.
3.  Complete the asynchronous operation by calling [**IMFTimecodeTranslate::EndConvertTimecodeToHNS**](/windows/desktop/api/mfidl/nf-mfidl-imftimecodetranslate-endconverttimecodetohns) or **IMFTimecodeTranslate::EndConvertTimecodeToHNS** appropriately.

During the creation of the media source, the source resolver creates a byte stream for the file from which the media source reads the ASF content. In order for the time conversions to be successful, the byte stream associated with the ASF file must have seeking capabilities; otherwise, the application gets the MF\_E\_BYTESTREAM\_NOT\_SEEKABLE error from the **Begin...** call. Another requirement for time conversions is that the ASF file, represented by the ASF media source, must have ASF Index Objects. The presentation times and the time codes are extracted from the ASF Index Objects that maintain all the indexes and the corresponding seek- points for the ASF file. For presentation time-to-time code translation, the ASF file must contain a Simple Index Object; for time code-to-presentation time translation, the ASF file must have an Index Object. The conversion operations rely on the underlying *indexer* (WMContainer component) to parse and read the Index Object associated with the ASF file. If the file does not contain an Index Object, the application asynchronously receives the MF\_E\_NO\_INDEX error code.

To translate the time requested by the application, the media source enumerates the streams within the file and finds the stream that contains the appropriate ASF Index Object. If such a stream is found, the media source parses the stream’s ASF packets are parsed until the correct time code is reached. After it finds the correct sample it retrieves the corresponding presentation time or the time code from the sample, and returns it to the caller.

### Script Command Support

When you build an ASF topology that contains a script stream a Script Stream node is added to the topology. This node will send IMFSamples at the appropriate time. The IMFSample provided by the script source node stores the data in the IMFMediaBuffer associated with the sample. You can call CopyToBuffer on the sample to get an IMFMediaBuffer and then call Lock on the buffer to get the data. 

Script stream payloads are packed into the buffer as a type string, followed by NULL, followed by the command string, followed by NULL. Strings are Unicode in the ASF format.

For example, a payload might look like the following (where \0 indicates a NULL character):

*URL\0http://contoso.com\0*

*Text\0This is a caption\0*



## Related topics

<dl> <dt>

[Pipeline Layer ASF Components](pipeline-layer-asf-components.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 
