---
title: Writer Network Sink Object
description: Writer Network Sink Object
ms.assetid: 'f7765b42-693a-4f48-b750-17579e860b6d'
keywords: ["Windows Media Format SDK,writer network sink objects", "Advanced Systems Format (ASF),writer network sink objects", "ASF (Advanced Systems Format),writer network sink objects", "objects,writer network sink objects", "writer network sink objects"]
---

# Writer Network Sink Object

The writer network sink object is used to write digital media to a network.

The writer network sink object is created by the function [**WMCreateWriterNetworkSink**](wmcreatewriternetworksink.md), which sets a pointer to an **IWMWriterNetworkSink** interface. The other interfaces of the writer network sink object can be obtained by calling the **QueryInterface** method.



| Interface                                              | Description                                                                                                                                                                                                     |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMClientConnections**](iwmclientconnections.md)   | Collects information on connected clients.                                                                                                                                                                      |
| [**IWMClientConnections2**](iwmclientconnections2.md) | Retrieves advanced client information.                                                                                                                                                                          |
| [**IWMRegisterCallback**](iwmregistercallback.md)     | Enables the application to get status messages from the object.                                                                                                                                                 |
| [**IWMWriterNetworkSink**](iwmwriternetworksink.md)   | Opens and closes ports, sets and retrieves the maximum number of clients that can connect to the sink object, sets the network protocol to be used by the writer object, and performs other advanced functions. |
| [**IWMWriterSink**](iwmwritersink.md)                 | Allocates memory, determines whether the sink is operating in real time, and handles several callback functions.                                                                                                |



 

The following callback interface can be implemented by the application to track the progress of a writer network sink object.



| Interface                                      | Description                                                                    |
|------------------------------------------------|--------------------------------------------------------------------------------|
| [**IWMStatusCallback**](iwmstatuscallback.md) | Required when status information must be communicated to the host application. |



 

## Related topics

<dl> <dt>

[**Broadcasting ASF Data**](broadcasting-asf-data.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




