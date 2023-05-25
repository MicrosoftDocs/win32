---
title: Writer Push Sink Object
description: Writer Push Sink Object
ms.assetid: 34e48f35-13d7-4649-a8b2-ed6510b16f88
keywords:
- Windows Media Format SDK,writer push sink objects
- Advanced Systems Format (ASF),writer push sink objects
- ASF (Advanced Systems Format),writer push sink objects
- objects,writer push sink objects
- writer push sink objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writer Push Sink Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer push sink object distributes digital media to publishing points. For example, a live concert can be encoded by a single server and then delivered, or *pushed*, to several other servers that will actually stream the content to users.

A writer push sink object is created by the function [**WMCreateWriterPushSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriterpushsink), which sets a pointer to an **IWMWriterPushSink** interface. The other interfaces supported by the object, listed in the following table, can be obtained by calling the **QueryInterface** method.



| Interface                                          | Description                                                                                                      |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**IWMRegisterCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmregistercallback) | Enables the application to get status messages from the object.                                                  |
| [**IWMWriterPushSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterpushsink)     | Manages a push distribution session.                                                                             |
| [**IWMWriterSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwritersink)             | Allocates memory, determines whether the sink is operating in real time, and exposes several callback functions. |



 

The following callback interface can be implemented by the application to track the progress of a writer push sink object.



| Interface                                      | Description                                                                    |
|------------------------------------------------|--------------------------------------------------------------------------------|
| [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) | Required when status information must be communicated to the host application. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Sending ASF Data to a Publishing Point**](sending-asf-data-to-a-publishing-point.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




