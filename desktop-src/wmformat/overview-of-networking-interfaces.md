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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Overview of Networking Interfaces

The networking features of this SDK are supported through methods of the following interfaces.



| Interface                                                  | Description                                                                                                                                           |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMClientConnections**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmclientconnections?branch=master)       | Gets information about the clients connected to a network sink.                                                                                       |
| [**IWMClientConnections2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmclientconnections2?branch=master)     | Provides a method to get information about a client attached to a writer network sink. This interface extends the **IWMClientConnections** interface. |
| [**IWMCredentialCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback?branch=master)     | Provides a callback method to acquire user credentials when accessing a remote site.                                                                  |
| [**IWMReaderAdvanced2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2?branch=master)           | Provides advanced methods on the reader object.                                                                                                       |
| [**IWMReaderAdvanced3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced3?branch=master)           | Extends the **IWMReaderAdvanced2** interface.                                                                                                         |
| [**IWMReaderAdvanced4**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4?branch=master)           | Extends the **IWMReaderAdvanced3** interface.                                                                                                         |
| [**IWMReaderNetworkConfig**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig?branch=master)   | Configures the network settings on the reader object.                                                                                                 |
| [**IWMReaderNetworkConfig2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig2?branch=master) | Configures additional network settings on the reader object. This interface extends the **IWMReaderNetworkConfig** interface.                         |
| [**IWMWriterNetworkSink**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriternetworksink?branch=master)       | Configures the network sink object, which is used to write digital media to a network.                                                                |
| [**IWMWriterPushSink**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriterpushsink?branch=master)             | Configures the push sink object, which is used to distribute digital media to publishing points.                                                      |



 

## Related topics

<dl> <dt>

[**Implementing Network Functionality**](implementing-network-functionality.md)
</dt> </dl>

 

 




