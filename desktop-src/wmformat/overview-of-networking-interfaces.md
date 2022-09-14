---
title: Overview of Networking Interfaces
description: Overview of Networking Interfaces
ms.assetid: 7aa7ff1b-9c81-4fee-afa9-2a9eed457360
keywords:
- Windows Media Format SDK,networking interfaces
- Windows Media Format SDK,interfaces
- Advanced Systems Format (ASF),networking interfaces
- ASF (Advanced Systems Format),networking interfaces
- Advanced Systems Format (ASF),interface list for networking features
- ASF (Advanced Systems Format),interface list for networking features
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Networking Interfaces

The networking features of this SDK are supported through methods of the following interfaces.



| Interface                                                  | Description                                                                                                                                           |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMClientConnections**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmclientconnections)       | Gets information about the clients connected to a network sink.                                                                                       |
| [**IWMClientConnections2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmclientconnections2)     | Provides a method to get information about a client attached to a writer network sink. This interface extends the **IWMClientConnections** interface. |
| [**IWMCredentialCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback)     | Provides a callback method to acquire user credentials when accessing a remote site.                                                                  |
| [**IWMReaderAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2)           | Provides advanced methods on the reader object.                                                                                                       |
| [**IWMReaderAdvanced3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced3)           | Extends the **IWMReaderAdvanced2** interface.                                                                                                         |
| [**IWMReaderAdvanced4**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4)           | Extends the **IWMReaderAdvanced3** interface.                                                                                                         |
| [**IWMReaderNetworkConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig)   | Configures the network settings on the reader object.                                                                                                 |
| [**IWMReaderNetworkConfig2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig2) | Configures additional network settings on the reader object. This interface extends the **IWMReaderNetworkConfig** interface.                         |
| [**IWMWriterNetworkSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriternetworksink)       | Configures the network sink object, which is used to write digital media to a network.                                                                |
| [**IWMWriterPushSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterpushsink)             | Configures the push sink object, which is used to distribute digital media to publishing points.                                                      |



 

## Related topics

<dl> <dt>

[**Implementing Network Functionality**](implementing-network-functionality.md)
</dt> </dl>

 

 




