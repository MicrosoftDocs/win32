---
title: Writer Network Sink Object
description: Writer Network Sink Object
ms.assetid: f7765b42-693a-4f48-b750-17579e860b6d
keywords:
- Windows Media Format SDK,writer network sink objects
- Advanced Systems Format (ASF),writer network sink objects
- ASF (Advanced Systems Format),writer network sink objects
- objects,writer network sink objects
- writer network sink objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writer Network Sink Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer network sink object is used to write digital media to a network.

The writer network sink object is created by the function [**WMCreateWriterNetworkSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriternetworksink), which sets a pointer to an **IWMWriterNetworkSink** interface. The other interfaces of the writer network sink object can be obtained by calling the **QueryInterface** method.



| Interface                                              | Description                                                                                                                                                                                                     |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMClientConnections**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmclientconnections)   | Collects information on connected clients.                                                                                                                                                                      |
| [**IWMClientConnections2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmclientconnections2) | Retrieves advanced client information.                                                                                                                                                                          |
| [**IWMRegisterCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmregistercallback)     | Enables the application to get status messages from the object.                                                                                                                                                 |
| [**IWMWriterNetworkSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriternetworksink)   | Opens and closes ports, sets and retrieves the maximum number of clients that can connect to the sink object, sets the network protocol to be used by the writer object, and performs other advanced functions. |
| [**IWMWriterSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwritersink)                 | Allocates memory, determines whether the sink is operating in real time, and handles several callback functions.                                                                                                |



 

The following callback interface can be implemented by the application to track the progress of a writer network sink object.



| Interface                                      | Description                                                                    |
|------------------------------------------------|--------------------------------------------------------------------------------|
| [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) | Required when status information must be communicated to the host application. |



 

## Related topics

<dl> <dt>

[**Broadcasting ASF Data**](broadcasting-asf-data.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




