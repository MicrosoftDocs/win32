---
title: Writer Object
description: Writer Object
ms.assetid: '8058b7fe-7d02-4572-ad43-6867d4ceb7e9'
keywords: ["Windows Media Format SDK,writer objects", "Advanced Systems Format (ASF),writer objects", "ASF (Advanced Systems Format),writer objects", "objects,writer objects", "writer objects"]
---

# Writer Object

The writer object is used to write digital media files using the advanced systems format (ASF) file structure. The process of writing a digital media file involves many steps internal to the writer, which coordinates compression, packetization, and multiplexing.

The writer object includes interfaces for output to files or a network, supports one callback interface, and can create one or more input media properties objects.

The writer object is created by the function [**WMCreateWriter**](wmcreatewriter.md), which sets a pointer to an **IWMWriter** interface. The other interfaces of the writer object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the writer object.



| Interface                                          | Description                                                                                                                                                                                               |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDRMWriter**](iwmdrmwriter.md)               | Provides methods to generate [*DRM*](wmformat-glossary.md#wmformat-digital-rights-management--drm-) keys.                                                                                                |
| [**IWMDRMWriter2**](iwmdrmwriter2.md)             | Configures the writer object to write a file containing a pre-encrypted stream that conforms to the Windows Media DRM 10 for Network Devices protocol.                                                    |
| [**IWMHeaderInfo**](iwmheaderinfo.md)             | Manages the specification and retrieval of header information, such as metadata, [*markers*](wmformat-glossary.md#wmformat-marker), and so on.                                                           |
| [**IWMHeaderInfo2**](iwmheaderinfo2.md)           | Manages enumerating through the available codec information. Inherits all of the methods of **IWMHeaderInfo**.                                                                                            |
| [**IWMHeaderInfo3**](iwmheaderinfo3.md)           | Manages enumerating through the available codec information. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**.                                                                     |
| [**IWMWatermarkInfo**](iwmwatermarkinfo.md)       | Provides access to information about watermarking systems present on the system.                                                                                                                          |
| [**IWMWriter**](iwmwriter.md)                     | Starts and stops the writing of ASF files; it includes methods for allocating buffers, setting and retrieving input properties, setting profiles and output file names, and unlocking the writer.         |
| [**IWMWriterAdvanced**](iwmwriteradvanced.md)     | Adds, gets, and removes specified sink objects; retrieves statistics, number of sinks, and the clock time the writer is working to; and performs other advanced functions.                                |
| [**IWMWriterAdvanced2**](iwmwriteradvanced2.md)   | Provides some advanced functionality, particularly for handling deinterlaced video. Inherits all of the methods of **IWMWriterAdvanced**.                                                                 |
| [**IWMWriterAdvanced3**](iwmwriteradvanced3.md)   | Provides additional writer functionality, including the ability to get detailed writer statistics. Inherits all of the methods of **IWMWriterAdvanced** and **IWMWriterAdvanced2**.                       |
| [**IWMWriterPostView**](iwmwriterpostview.md)     | Manages some advanced writing functionality related to postviewing samples. Postviewing is viewing the output, usually from an encoder, to check that the encoding/decoding process is working correctly. |
| [**IWMWriterPreprocess**](iwmwriterpreprocess.md) | Manages preprocessing passes made by the writer. Preprocessing passes are used to improve the quality of encoded output.                                                                                  |



 

The following callback interface must be implemented by the application to track the progress of postviewing.



| Interface                                                      | Description                                                                                              |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**IWMWriterPostViewCallback**](iwmwriterpostviewcallback.md) | Manages how uncompressed samples are received from the writer object to preview what the codec is doing. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




