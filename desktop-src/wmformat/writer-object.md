---
title: Writer Object
description: Writer Object
ms.assetid: 8058b7fe-7d02-4572-ad43-6867d4ceb7e9
keywords:
- Windows Media Format SDK,writer objects
- Advanced Systems Format (ASF),writer objects
- ASF (Advanced Systems Format),writer objects
- objects,writer objects
- writer objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Writer Object

The writer object is used to write digital media files using the advanced systems format (ASF) file structure. The process of writing a digital media file involves many steps internal to the writer, which coordinates compression, packetization, and multiplexing.

The writer object includes interfaces for output to files or a network, supports one callback interface, and can create one or more input media properties objects.

The writer object is created by the function [**WMCreateWriter**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriter?branch=master), which sets a pointer to an **IWMWriter** interface. The other interfaces of the writer object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the writer object.



| Interface                                          | Description                                                                                                                                                                                               |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDRMWriter**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdrmwriter?branch=master)               | Provides methods to generate [*DRM*](wmformat-glossary.md#wmformat-digital-rights-management--drm-) keys.                                                                                                |
| [**IWMDRMWriter2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmdrmwriter2?branch=master)             | Configures the writer object to write a file containing a pre-encrypted stream that conforms to the Windows Media DRM 10 for Network Devices protocol.                                                    |
| [**IWMHeaderInfo**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo?branch=master)             | Manages the specification and retrieval of header information, such as metadata, [*markers*](wmformat-glossary.md#wmformat-marker), and so on.                                                           |
| [**IWMHeaderInfo2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2?branch=master)           | Manages enumerating through the available codec information. Inherits all of the methods of **IWMHeaderInfo**.                                                                                            |
| [**IWMHeaderInfo3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3?branch=master)           | Manages enumerating through the available codec information. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**.                                                                     |
| [**IWMWatermarkInfo**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwatermarkinfo?branch=master)       | Provides access to information about watermarking systems present on the system.                                                                                                                          |
| [**IWMWriter**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriter?branch=master)                     | Starts and stops the writing of ASF files; it includes methods for allocating buffers, setting and retrieving input properties, setting profiles and output file names, and unlocking the writer.         |
| [**IWMWriterAdvanced**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced?branch=master)     | Adds, gets, and removes specified sink objects; retrieves statistics, number of sinks, and the clock time the writer is working to; and performs other advanced functions.                                |
| [**IWMWriterAdvanced2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced2?branch=master)   | Provides some advanced functionality, particularly for handling deinterlaced video. Inherits all of the methods of **IWMWriterAdvanced**.                                                                 |
| [**IWMWriterAdvanced3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced3?branch=master)   | Provides additional writer functionality, including the ability to get detailed writer statistics. Inherits all of the methods of **IWMWriterAdvanced** and **IWMWriterAdvanced2**.                       |
| [**IWMWriterPostView**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriterpostview?branch=master)     | Manages some advanced writing functionality related to postviewing samples. Postviewing is viewing the output, usually from an encoder, to check that the encoding/decoding process is working correctly. |
| [**IWMWriterPreprocess**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriterpreprocess?branch=master) | Manages preprocessing passes made by the writer. Preprocessing passes are used to improve the quality of encoded output.                                                                                  |



 

The following callback interface must be implemented by the application to track the progress of postviewing.



| Interface                                                      | Description                                                                                              |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**IWMWriterPostViewCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriterpostviewcallback?branch=master) | Manages how uncompressed samples are received from the writer object to preview what the codec is doing. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




