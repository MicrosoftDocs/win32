---
title: Reader Object
description: Reader Object
ms.assetid: 70696ffc-2612-460d-b445-f200ba85d3c7
keywords:
- Windows Media Format SDK,reader objects
- Advanced Systems Format (ASF),reader objects
- ASF (Advanced Systems Format),reader objects
- objects,reader objects
- reader objects,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reader Object

The reader object reads data samples from media files. The reader object currently supports files using the advanced systems format (ASF) file structure as well as MP3 files. Data delivered by the reader object is uncompressed and ready for rendering by default, though samples can be delivered without being decompressed if desired. Samples are delivered asynchronously from the reader object; you must set up a callback function to receive them. For synchronous playback of ASF files, use the synchronous reader object. Neither the reader nor synchronous reader renders any data. You must provide your own rendering routines to display the media retrieved from a file.

When a file contains encoded media that can be decoded with a codec supported by the reader object, you can control the format of the uncompressed output. To change the format of decompressed output for a stream, you must retrieve the default output media properties object for that stream, make changes to it, and reassign it to the stream in the reader. Output media properties objects are subordinate to the reader object and should only be created by using the [**IWMReader::GetOutputProps**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputprops?branch=master) method.

The reader object is created by the function [**WMCreateReader**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatereader?branch=master), which sets a pointer to an **IWMReader** interface. The other interfaces of the reader object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the reader object.



| Interface                                                    | Description                                                                                                                                                                     |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IReferenceClock**](ireferenceclock.md)                   | Provides access to the system clock used by the reader.                                                                                                                         |
| [**IWMDRMReader**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdrmreader?branch=master)                         | Manages license acquisition, [*DRM*](wmformat-glossary.md#wmformat-digital-rights-management--drm-) properties, and client individualization.                                  |
| [**IWMDRMReader2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdrmreader2?branch=master)                       | Provides access to licenses that use output protection levels (OPL) to specify rights.                                                                                          |
| [**IWMHeaderInfo**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo?branch=master)                       | Sets and retrieves header information, including metadata, [*markers*](wmformat-glossary.md#wmformat-marker), and script data.                                                 |
| [**IWMHeaderInfo2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2?branch=master)                     | Retrieves information about the codecs that were used to encode the content in the file. Inherits all of the methods of **IWMHeaderInfo**.                                      |
| [**IWMHeaderInfo3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3?branch=master)                     | Supports large attribute sizes, duplicate attribute names, and multiple language support. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**.              |
| [**IWMPacketSize**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmpacketsize?branch=master)                       | Retrieves the size of the largest packet in the file loaded in the reader.                                                                                                      |
| [**IWMPacketSize2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmpacketsize2?branch=master)                     | Retrieves the size of the smallest packet in the file loaded in the reader.                                                                                                     |
| [**IWMProfile**](iwmprofile.md)                             | Provides access to the profile information of the file loaded in the reader.                                                                                                    |
| [**IWMProfile2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofile2?branch=master)                           | Retrieves the globally unique identifier (GUID), if any, associated with the profile. Inherits all of the methods of **IWMProfile**.                                            |
| [**IWMProfile3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofile3?branch=master)                           | Supports bandwidth sharing and stream prioritization information in the profile. Inherits all of the methods of **IWMProfile** and **IWMProfile2**.                             |
| [**IWMReader**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreader?branch=master)                               | Provides basic file reading capabilities, including operations such as open, close, start, pause, resume, stop, and getting and setting the output properties.                  |
| [**IWMReaderAccelerator**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderaccelerator?branch=master)         | Communicates with DirectX video acceleration.                                                                                                                                   |
| [**IWMReaderAdvanced**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced?branch=master)               | Provides advanced features of the reader, such as a user-provided clock, buffer allocation, return statistics, and stream selection notifications.                              |
| [**IWMReaderAdvanced2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2?branch=master)             | Provides an additional range of advanced methods for an existing reader object. Inherits all of the methods of **IWMReaderAdvanced**.                                           |
| [**IWMReaderAdvanced3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced3?branch=master)             | Provides advanced seeking and streaming control. Inherits all of the methods of **IWMReaderAdvanced** and **IWMReaderAdvanced2**.                                               |
| [**IWMReaderAdvanced4**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4?branch=master)             | Provides advanced reader options including multiple language support. Inherits all of the methods of **IWMReaderAdvanced**, **IWMReaderAdvanced2**, and **IWMReaderAdvanced3**. |
| [**IWMReaderNetworkConfig**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig?branch=master)     | Controls network configuration settings.                                                                                                                                        |
| [**IWMReaderNetworkConfig2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig2?branch=master)   | Provides access to advanced network configuration settings. Inherits all of the methods of **IWMReaderNetworkConfig**.                                                          |
| [**IWMReaderStreamClock**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderstreamclock?branch=master)         | Sets and cancels timers on stream clocks, and retrieves the current value of a specified stream clock.                                                                          |
| [**IWMReaderTimecode**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadertimecode?branch=master)               | Provides information about SMPTE time code ranges in the file loaded in the reader.                                                                                             |
| [**IWMReaderTypeNegotiation**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadertypenegotiation?branch=master) | Tests whether changes to the output properties of a stream are working properly.                                                                                                |



 

The following callback interfaces can be implemented in the application to track the progress of a reader object.



| Interface                                                      | Description                                                                                                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMCredentialCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback?branch=master)         | Acquires the credentials of users and checks that they have permission to access a remote site.                                               |
| [**IWMReaderAllocatorEx**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderallocatorex?branch=master)           | Provides expanded alternatives to the **AllocateForOutput** and **AllocateForStream** methods of the **IWMReaderCallbackAdvanced** interface. |
| [**IWMReaderCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadercallback?branch=master)                 | Provides callback methods for the **Start** and **Open** methods of **IWMReader**.                                                            |
| [**IWMReaderCallbackAdvanced**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadercallbackadvanced?branch=master) | Provides callback methods for the methods of the [**IWMReaderAdvanced**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced?branch=master) interface.                                    |
| [**IWMStatusCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstatuscallback?branch=master)                 | Required when status information must be communicated to the host application.                                                                |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> </dl>

 

 




