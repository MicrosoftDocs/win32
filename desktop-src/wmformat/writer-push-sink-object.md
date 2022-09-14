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
ms.date: 05/31/2018
---

# Writer Push Sink Object

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

 

 




