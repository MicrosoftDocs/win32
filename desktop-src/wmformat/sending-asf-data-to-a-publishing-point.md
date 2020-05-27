---
title: Sending ASF Data to a Publishing Point
description: Sending ASF Data to a Publishing Point
ms.assetid: 8f01beae-4270-4cf5-afff-3f7014cae90f
keywords:
- Windows Media Format SDK,sending ASF data
- Windows Media Format SDK,publishing points
- Advanced Systems Format (ASF),sending data
- ASF (Advanced Systems Format),sending data
- Advanced Systems Format (ASF),publishing points
- ASF (Advanced Systems Format),publishing points
- publishing points
ms.topic: article
ms.date: 05/31/2018
---

# Sending ASF Data to a Publishing Point

You can use the Windows Media Format SDK to push ASF data to a publishing point on a Windows Media server. The server then broadcasts the data from that publishing point. This scenario is useful if you are capturing or re-encoding content on one computer, and wish to distribute the content from another computer (or several computers). It is also useful if you need to move content from a computer inside a firewall to a Windows Media server outside the firewall, because push distribution uses the HTTP protocol.

> [!Note]  
> A *publishing point* acts essentially like a redirector. The client specifies the publishing point in the URL (for example, mms://MyServer/MyPublishingPoint) and the server translates this into a request for content.

 

To push data to the publishing point, attach the push sink object to the writer object. The push sink is used to open the connection to the server and manage the push session. The writer object handles all the other aspects of creating the file.

Perform the following steps:

1.  Create the writer object by calling the [**WMCreateWriter**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter) function, which returns an [**IWMWriter**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter) pointer.
2.  Create the push sink object by calling the [**WMCreateWriterPushSink**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-wmcreatewriterpushsink) function, which returns an [**IWMWriterPushSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterpushsink) pointer.
3.  Attach the network sink to the writer by calling [**IWMWriterAdvanced::AddSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-addsink) on the writer, with a pointer to the network sink's **IWMWriterPushSink** interface.
4.  Connect to the server by calling [**IWMWriterPushSink::Connect**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterpushsink-connect).
5.  Write the stream. This step involves setting the profile on the writer object, sending samples to the writer, and possibly other tasks. For more information, see [Writing ASF Files](writing-asf-files.md). Additional tasks might include setting metadata attributes (as described in [Working with Metadata](working-with-metadata.md)) or setting live-DRM on the stream (as described in [Enabling DRM Support](enabling-drm-support.md)). These tasks are performed exactly as they are for ASF file writing.
6.  After you are done writing, call [**IWMWriterAdvanced::RemoveSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-removesink) on the writer to detach the push sink object.
7.  Call [**IWMWriterPushSink::EndSession**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterpushsink-endsession) on the push sink to end the session with the server.

These steps are illustrated in the WMVNetWrite sample application.

> [!Note]  
> If you are sending a very-low-bit-rate video-only file, it might not start playing on the publishing point for several seconds. This can happen in various cases, for example when a single packet contains many small video frames and no audio, or when there is a long time gap between the first packet and the second packet in a low-bit-rate video-only file. To avoid this problem, insert a silent audio stream into the file.

 

## Authentication

Authentication to the server is automatically handled by the push sink object. However, the application may need to supply credentials. This is done through the **IWMCredentialCallback** callback interface, as follows:

1.  Implement the [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) and [**IWMCredentialCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback) interface in your application.
2.  Query the push sink object for the [**IWMRegisterCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmregistercallback) interface.
3.  Call [**IWMRegisterCallback::Advise**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistercallback-advise) with a pointer to your application's **IWMStatusCallback** interface.
4.  If the push sink needs to get credentials from the application, it queries the **IWMStatusCallback** pointer for the **IWMCredentialCallback** interface and calls [**IWMCredentialCallback::AcquireCredentials**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcredentialcallback-acquirecredentials). For information about this method, see [Authentication](authentication.md).
5.  When you are done, call [**IWMRegisterCallback::Unadvise**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmregistercallback-unadvise) to stop getting event notifications from the push sink.

## Related topics

<dl> <dt>

[**Sending ASF Data Over a Network**](sending-asf-data-over-a-network.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> <dt>

[**Writer Push Sink Object**](writer-push-sink-object.md)
</dt> </dl>

 

 




