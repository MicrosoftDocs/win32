---
title: Writer File Sink Object
description: Writer File Sink Object
ms.assetid: 93f44579-fb2d-498e-a271-5bc91d6f0321
keywords:
- Windows Media Format SDK,writer file sink objects
- Advanced Systems Format (ASF),writer file sink objects
- ASF (Advanced Systems Format),writer file sink objects
- objects,writer file sink objects
- writer file sink objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Writer File Sink Object

The writer file sink object is used when writing Windows Media output to a file.

The writer file sink object is created by the function [**WMCreateWriterFileSink**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatewriterfilesink?branch=master), which sets a pointer to an **IWMWriterFileSink** interface. The other interfaces of the writer file sink object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the writer file sink object.



| Interface                                          | Description                                                                                                                     |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**IWMRegisterCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmregistercallback?branch=master) | Enables the application to get status messages from the object.                                                                 |
| [**IWMWriterFileSink**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink?branch=master)     | Opens a file to which the writer object can write data.                                                                         |
| [**IWMWriterFileSink2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink2?branch=master)   | Provides extended management of a file sink object. Inherits all of the methods of **IWMWriterFileSink**.                       |
| [**IWMWriterFileSink3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink3?branch=master)   | Provides additional options for writing files. Inherits all of the methods of **IWMWriterFileSink** and **IWMWriterFileSink2**. |
| [**IWMWriterSink**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwritersink?branch=master)             | Allocates memory, determines whether the sink is operating in real time, and handles several callback functions.                |



 

The following callback interface should be implemented by the application to track the progress of a writer file sink object.



| Interface                                      | Description                                                                    |
|------------------------------------------------|--------------------------------------------------------------------------------|
| [**IWMStatusCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstatuscallback?branch=master) | Required when status information must be communicated to the host application. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




