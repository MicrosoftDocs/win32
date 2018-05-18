---
title: Writer File Sink Object
description: Writer File Sink Object
ms.assetid: '93f44579-fb2d-498e-a271-5bc91d6f0321'
keywords: ["Windows Media Format SDK,writer file sink objects", "Advanced Systems Format (ASF),writer file sink objects", "ASF (Advanced Systems Format),writer file sink objects", "objects,writer file sink objects", "writer file sink objects"]
---

# Writer File Sink Object

The writer file sink object is used when writing Windows Media output to a file.

The writer file sink object is created by the function [**WMCreateWriterFileSink**](wmcreatewriterfilesink.md), which sets a pointer to an **IWMWriterFileSink** interface. The other interfaces of the writer file sink object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the writer file sink object.



| Interface                                          | Description                                                                                                                     |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**IWMRegisterCallback**](iwmregistercallback.md) | Enables the application to get status messages from the object.                                                                 |
| [**IWMWriterFileSink**](iwmwriterfilesink.md)     | Opens a file to which the writer object can write data.                                                                         |
| [**IWMWriterFileSink2**](iwmwriterfilesink2.md)   | Provides extended management of a file sink object. Inherits all of the methods of **IWMWriterFileSink**.                       |
| [**IWMWriterFileSink3**](iwmwriterfilesink3.md)   | Provides additional options for writing files. Inherits all of the methods of **IWMWriterFileSink** and **IWMWriterFileSink2**. |
| [**IWMWriterSink**](iwmwritersink.md)             | Allocates memory, determines whether the sink is operating in real time, and handles several callback functions.                |



 

The following callback interface should be implemented by the application to track the progress of a writer file sink object.



| Interface                                      | Description                                                                    |
|------------------------------------------------|--------------------------------------------------------------------------------|
| [**IWMStatusCallback**](iwmstatuscallback.md) | Required when status information must be communicated to the host application. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




