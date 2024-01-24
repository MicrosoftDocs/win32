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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writer File Sink Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer file sink object is used when writing Windows Media output to a file.

The writer file sink object is created by the function [**WMCreateWriterFileSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriterfilesink), which sets a pointer to an **IWMWriterFileSink** interface. The other interfaces of the writer file sink object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the writer file sink object.



| Interface                                          | Description                                                                                                                     |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**IWMRegisterCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmregistercallback) | Enables the application to get status messages from the object.                                                                 |
| [**IWMWriterFileSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink)     | Opens a file to which the writer object can write data.                                                                         |
| [**IWMWriterFileSink2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink2)   | Provides extended management of a file sink object. Inherits all of the methods of **IWMWriterFileSink**.                       |
| [**IWMWriterFileSink3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink3)   | Provides additional options for writing files. Inherits all of the methods of **IWMWriterFileSink** and **IWMWriterFileSink2**. |
| [**IWMWriterSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwritersink)             | Allocates memory, determines whether the sink is operating in real time, and handles several callback functions.                |



 

The following callback interface should be implemented by the application to track the progress of a writer file sink object.



| Interface                                      | Description                                                                    |
|------------------------------------------------|--------------------------------------------------------------------------------|
| [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) | Required when status information must be communicated to the host application. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




