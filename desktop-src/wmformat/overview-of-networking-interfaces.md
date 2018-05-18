---
title: Overview of Networking Interfaces
description: Overview of Networking Interfaces
ms.assetid: '7aa7ff1b-9c81-4fee-afa9-2a9eed457360'
keywords: ["Windows Media Format SDK,networking interfaces", "Windows Media Format SDK,interfaces", "Advanced Systems Format (ASF),networking interfaces", "ASF (Advanced Systems Format),networking interfaces", "Advanced Systems Format (ASF),interface list for networking features", "ASF (Advanced Systems Format),interface list for networking features"]
---

# Overview of Networking Interfaces

The networking features of this SDK are supported through methods of the following interfaces.



| Interface                                                  | Description                                                                                                                                           |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMClientConnections**](iwmclientconnections.md)       | Gets information about the clients connected to a network sink.                                                                                       |
| [**IWMClientConnections2**](iwmclientconnections2.md)     | Provides a method to get information about a client attached to a writer network sink. This interface extends the **IWMClientConnections** interface. |
| [**IWMCredentialCallback**](iwmcredentialcallback.md)     | Provides a callback method to acquire user credentials when accessing a remote site.                                                                  |
| [**IWMReaderAdvanced2**](iwmreaderadvanced2.md)           | Provides advanced methods on the reader object.                                                                                                       |
| [**IWMReaderAdvanced3**](iwmreaderadvanced3.md)           | Extends the **IWMReaderAdvanced2** interface.                                                                                                         |
| [**IWMReaderAdvanced4**](iwmreaderadvanced4.md)           | Extends the **IWMReaderAdvanced3** interface.                                                                                                         |
| [**IWMReaderNetworkConfig**](iwmreadernetworkconfig.md)   | Configures the network settings on the reader object.                                                                                                 |
| [**IWMReaderNetworkConfig2**](iwmreadernetworkconfig2.md) | Configures additional network settings on the reader object. This interface extends the **IWMReaderNetworkConfig** interface.                         |
| [**IWMWriterNetworkSink**](iwmwriternetworksink.md)       | Configures the network sink object, which is used to write digital media to a network.                                                                |
| [**IWMWriterPushSink**](iwmwriterpushsink.md)             | Configures the push sink object, which is used to distribute digital media to publishing points.                                                      |



 

## Related topics

<dl> <dt>

[**Implementing Network Functionality**](implementing-network-functionality.md)
</dt> </dl>

 

 




