---
title: Reader Object
description: Reader Object
ms.assetid: '70696ffc-2612-460d-b445-f200ba85d3c7'
keywords: ["Windows Media Format SDK,reader objects", "Advanced Systems Format (ASF),reader objects", "ASF (Advanced Systems Format),reader objects", "objects,reader objects", "reader objects,about"]
---

# Reader Object

The reader object reads data samples from media files. The reader object currently supports files using the advanced systems format (ASF) file structure as well as MP3 files. Data delivered by the reader object is uncompressed and ready for rendering by default, though samples can be delivered without being decompressed if desired. Samples are delivered asynchronously from the reader object; you must set up a callback function to receive them. For synchronous playback of ASF files, use the synchronous reader object. Neither the reader nor synchronous reader renders any data. You must provide your own rendering routines to display the media retrieved from a file.

When a file contains encoded media that can be decoded with a codec supported by the reader object, you can control the format of the uncompressed output. To change the format of decompressed output for a stream, you must retrieve the default output media properties object for that stream, make changes to it, and reassign it to the stream in the reader. Output media properties objects are subordinate to the reader object and should only be created by using the [**IWMReader::GetOutputProps**](iwmreader-getoutputprops.md) method.

The reader object is created by the function [**WMCreateReader**](wmcreatereader.md), which sets a pointer to an **IWMReader** interface. The other interfaces of the reader object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the reader object.



| Interface                                                    | Description                                                                                                                                                                     |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IReferenceClock**](ireferenceclock.md)                   | Provides access to the system clock used by the reader.                                                                                                                         |
| [**IWMDRMReader**](iwmdrmreader.md)                         | Manages license acquisition, [*DRM*](wmformat-glossary.md#wmformat-digital-rights-management--drm-) properties, and client individualization.                                  |
| [**IWMDRMReader2**](iwmdrmreader2.md)                       | Provides access to licenses that use output protection levels (OPL) to specify rights.                                                                                          |
| [**IWMHeaderInfo**](iwmheaderinfo.md)                       | Sets and retrieves header information, including metadata, [*markers*](wmformat-glossary.md#wmformat-marker), and script data.                                                 |
| [**IWMHeaderInfo2**](iwmheaderinfo2.md)                     | Retrieves information about the codecs that were used to encode the content in the file. Inherits all of the methods of **IWMHeaderInfo**.                                      |
| [**IWMHeaderInfo3**](iwmheaderinfo3.md)                     | Supports large attribute sizes, duplicate attribute names, and multiple language support. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**.              |
| [**IWMPacketSize**](iwmpacketsize.md)                       | Retrieves the size of the largest packet in the file loaded in the reader.                                                                                                      |
| [**IWMPacketSize2**](iwmpacketsize2.md)                     | Retrieves the size of the smallest packet in the file loaded in the reader.                                                                                                     |
| [**IWMProfile**](iwmprofile.md)                             | Provides access to the profile information of the file loaded in the reader.                                                                                                    |
| [**IWMProfile2**](iwmprofile2.md)                           | Retrieves the globally unique identifier (GUID), if any, associated with the profile. Inherits all of the methods of **IWMProfile**.                                            |
| [**IWMProfile3**](iwmprofile3.md)                           | Supports bandwidth sharing and stream prioritization information in the profile. Inherits all of the methods of **IWMProfile** and **IWMProfile2**.                             |
| [**IWMReader**](iwmreader.md)                               | Provides basic file reading capabilities, including operations such as open, close, start, pause, resume, stop, and getting and setting the output properties.                  |
| [**IWMReaderAccelerator**](iwmreaderaccelerator.md)         | Communicates with DirectX video acceleration.                                                                                                                                   |
| [**IWMReaderAdvanced**](iwmreaderadvanced.md)               | Provides advanced features of the reader, such as a user-provided clock, buffer allocation, return statistics, and stream selection notifications.                              |
| [**IWMReaderAdvanced2**](iwmreaderadvanced2.md)             | Provides an additional range of advanced methods for an existing reader object. Inherits all of the methods of **IWMReaderAdvanced**.                                           |
| [**IWMReaderAdvanced3**](iwmreaderadvanced3.md)             | Provides advanced seeking and streaming control. Inherits all of the methods of **IWMReaderAdvanced** and **IWMReaderAdvanced2**.                                               |
| [**IWMReaderAdvanced4**](iwmreaderadvanced4.md)             | Provides advanced reader options including multiple language support. Inherits all of the methods of **IWMReaderAdvanced**, **IWMReaderAdvanced2**, and **IWMReaderAdvanced3**. |
| [**IWMReaderNetworkConfig**](iwmreadernetworkconfig.md)     | Controls network configuration settings.                                                                                                                                        |
| [**IWMReaderNetworkConfig2**](iwmreadernetworkconfig2.md)   | Provides access to advanced network configuration settings. Inherits all of the methods of **IWMReaderNetworkConfig**.                                                          |
| [**IWMReaderStreamClock**](iwmreaderstreamclock.md)         | Sets and cancels timers on stream clocks, and retrieves the current value of a specified stream clock.                                                                          |
| [**IWMReaderTimecode**](iwmreadertimecode.md)               | Provides information about SMPTE time code ranges in the file loaded in the reader.                                                                                             |
| [**IWMReaderTypeNegotiation**](iwmreadertypenegotiation.md) | Tests whether changes to the output properties of a stream are working properly.                                                                                                |



 

The following callback interfaces can be implemented in the application to track the progress of a reader object.



| Interface                                                      | Description                                                                                                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMCredentialCallback**](iwmcredentialcallback.md)         | Acquires the credentials of users and checks that they have permission to access a remote site.                                               |
| [**IWMReaderAllocatorEx**](iwmreaderallocatorex.md)           | Provides expanded alternatives to the **AllocateForOutput** and **AllocateForStream** methods of the **IWMReaderCallbackAdvanced** interface. |
| [**IWMReaderCallback**](iwmreadercallback.md)                 | Provides callback methods for the **Start** and **Open** methods of **IWMReader**.                                                            |
| [**IWMReaderCallbackAdvanced**](iwmreadercallbackadvanced.md) | Provides callback methods for the methods of the [**IWMReaderAdvanced**](iwmreaderadvanced.md) interface.                                    |
| [**IWMStatusCallback**](iwmstatuscallback.md)                 | Required when status information must be communicated to the host application.                                                                |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> </dl>

 

 




