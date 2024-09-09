---
title: Reader Object
description: Reader Object
ms.assetid: 'b5edbf8b-820f-4e09-a482-8efc2283360e'
keywords:
- Windows Media Format SDK,reader objects
- Advanced Systems Format (ASF),reader objects
- ASF (Advanced Systems Format),reader objects
- objects,reader objects
- reader objects,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reader Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The reader object reads data samples from media files. The reader object currently supports files using the advanced systems format (ASF) file structure as well as MP3 files. Data delivered by the reader object is uncompressed and ready for rendering by default, though samples can be delivered without being decompressed if desired. Samples are delivered asynchronously from the reader object; you must set up a callback function to receive them. For synchronous playback of ASF files, use the synchronous reader object. Neither the reader nor synchronous reader renders any data. You must provide your own rendering routines to display the media retrieved from a file.

When a file contains encoded media that can be decoded with a codec supported by the reader object, you can control the format of the uncompressed output. To change the format of decompressed output for a stream, you must retrieve the default output media properties object for that stream, make changes to it, and reassign it to the stream in the reader. Output media properties objects are subordinate to the reader object and should only be created by using the [**IWMReader::GetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputprops) method.

The reader object is created by the function [**WMCreateReader**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatereader), which sets a pointer to an **IWMReader** interface. The other interfaces of the reader object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the reader object.



| Interface                                                    | Description                                                                                                                                                                     |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IReferenceClock**](ireferenceclock.md)                   | Provides access to the system clock used by the reader.                                                                                                                         |
| [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader)                         | Manages license acquisition, [*DRM*](wmformat-glossary.md) properties, and client individualization.                                  |
| [**IWMDRMReader2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader2)                       | Provides access to licenses that use output protection levels (OPL) to specify rights.                                                                                          |
| [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)                       | Sets and retrieves header information, including metadata, [*markers*](wmformat-glossary.md), and script data.                                                 |
| [**IWMHeaderInfo2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2)                     | Retrieves information about the codecs that were used to encode the content in the file. Inherits all of the methods of **IWMHeaderInfo**.                                      |
| [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3)                     | Supports large attribute sizes, duplicate attribute names, and multiple language support. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**.              |
| [**IWMPacketSize**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpacketsize)                       | Retrieves the size of the largest packet in the file loaded in the reader.                                                                                                      |
| [**IWMPacketSize2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpacketsize2)                     | Retrieves the size of the smallest packet in the file loaded in the reader.                                                                                                     |
| [**IWMProfile**](iwmprofile.md)                             | Provides access to the profile information of the file loaded in the reader.                                                                                                    |
| [**IWMProfile2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofile2)                           | Retrieves the globally unique identifier (GUID), if any, associated with the profile. Inherits all of the methods of **IWMProfile**.                                            |
| [**IWMProfile3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofile3)                           | Supports bandwidth sharing and stream prioritization information in the profile. Inherits all of the methods of **IWMProfile** and **IWMProfile2**.                             |
| [**IWMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)                               | Provides basic file reading capabilities, including operations such as open, close, start, pause, resume, stop, and getting and setting the output properties.                  |
| [**IWMReaderAccelerator**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderaccelerator)         | Communicates with DirectX video acceleration.                                                                                                                                   |
| [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced)               | Provides advanced features of the reader, such as a user-provided clock, buffer allocation, return statistics, and stream selection notifications.                              |
| [**IWMReaderAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2)             | Provides an additional range of advanced methods for an existing reader object. Inherits all of the methods of **IWMReaderAdvanced**.                                           |
| [**IWMReaderAdvanced3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced3)             | Provides advanced seeking and streaming control. Inherits all of the methods of **IWMReaderAdvanced** and **IWMReaderAdvanced2**.                                               |
| [**IWMReaderAdvanced4**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4)             | Provides advanced reader options including multiple language support. Inherits all of the methods of **IWMReaderAdvanced**, **IWMReaderAdvanced2**, and **IWMReaderAdvanced3**. |
| [**IWMReaderNetworkConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig)     | Controls network configuration settings.                                                                                                                                        |
| [**IWMReaderNetworkConfig2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig2)   | Provides access to advanced network configuration settings. Inherits all of the methods of **IWMReaderNetworkConfig**.                                                          |
| [**IWMReaderStreamClock**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderstreamclock)         | Sets and cancels timers on stream clocks, and retrieves the current value of a specified stream clock.                                                                          |
| [**IWMReaderTimecode**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadertimecode)               | Provides information about SMPTE time code ranges in the file loaded in the reader.                                                                                             |
| [**IWMReaderTypeNegotiation**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadertypenegotiation) | Tests whether changes to the output properties of a stream are working properly.                                                                                                |



 

The following callback interfaces can be implemented in the application to track the progress of a reader object.



| Interface                                                      | Description                                                                                                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMCredentialCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback)         | Acquires the credentials of users and checks that they have permission to access a remote site.                                               |
| [**IWMReaderAllocatorEx**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderallocatorex)           | Provides expanded alternatives to the **AllocateForOutput** and **AllocateForStream** methods of the **IWMReaderCallbackAdvanced** interface. |
| [**IWMReaderCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadercallback)                 | Provides callback methods for the **Start** and **Open** methods of **IWMReader**.                                                            |
| [**IWMReaderCallbackAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadercallbackadvanced) | Provides callback methods for the methods of the [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced) interface.                                    |
| [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback)                 | Required when status information must be communicated to the host application.                                                                |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> </dl>

 

 




