---
title: WDS Transport Client Functions
description: This module defines the structures and functions that compose the interface between the content receiver and the transport client.
ms.assetid: 20c3116b-3a0d-4048-b6f2-81c03e0a80ef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WDS Transport Client Functions

This module defines the structures and functions that compose the interface between the content receiver and the transport client.



| Function                                                                              | Description                                                                                                                                                                 |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*PFN\_WdsTransportClientReceiveContents*](/windows/win32/Wdstci/nc-wdstci-pfn_wdstransportclientreceivecontents?branch=master) | Indicates that a block of data is ready to be used.                                                                                                                         |
| [*PFN\_WdsTransportClientReceiveMetadata*](/windows/win32/Wdstci/nc-wdstci-pfn_wdstransportclientreceivemetadata?branch=master) | Receives metadata information about a file.                                                                                                                                 |
| [*PFN\_WdsTransportClientSessionComplete*](/windows/win32/Wdstci/nc-wdstci-pfn_wdstransportclientsessioncomplete?branch=master) | Indicates that the session completed successfully or encountered an error.                                                                                                  |
| [*PFN\_WdsTransportClientSessionStart*](/windows/win32/Wdstci/nc-wdstci-pfn_wdstransportclientsessionstart?branch=master)       | Indicates the file size and other server side information about the file to the consumer.                                                                                   |
| [*PFN\_WdsTransportClientSessionStartEx*](/windows/win32/Wdstci/nc-wdstci-pfn_wdstransportclientsessionstartex?branch=master)   | Indicates the file size and other server side information about the file to the consumer.                                                                                   |
| [**WdsTransportClientAddRefBuffer**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientaddrefbuffer?branch=master)              | Increments the reference count on a buffer owned by the multicast client.                                                                                                   |
| [**WdsTransportClientCancelSession**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientcancelsession?branch=master)            | Releases the resources associated with a session in the client.                                                                                                             |
| [**WdsTransportClientCloseSession**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientclosesession?branch=master)              | Releases the resources associated with a session in the client.                                                                                                             |
| [**WdsTransportClientCompleteReceive**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientcompletereceive?branch=master)        | Indicates that all processing on a block of data is finished, and that the multicast client may remove this block of data from its cache to make room for further receives. |
| [**WdsTransportClientInitialize**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientinitialize?branch=master)                  | Initializes the multicast client.                                                                                                                                           |
| [**WdsTransportClientInitializeSession**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientinitializesession?branch=master)    | Initiates a multicast file transfer.                                                                                                                                        |
| [**WdsTransportClientQueryStatus**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientquerystatus?branch=master)                | Retrieves the current status of an ongoing or complete multicast transmission from the multicast client.                                                                    |
| [**WdsTransportClientRegisterCallback**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientregistercallback?branch=master)      | Registers a callback with the multicast client.                                                                                                                             |
| [**WdsTransportClientReleaseBuffer**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientreleasebuffer?branch=master)            | Decrements the reference count on a buffer owned by the multicast client.                                                                                                   |
| [**WdsTransportClientShutdown**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientshutdown?branch=master)                      | Shuts down the multicast client.                                                                                                                                            |
| [**WdsTransportClientStartSession**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientstartsession?branch=master)              | Initiates a multicast file transfer.                                                                                                                                        |
| [**WdsTransportClientWaitForCompletion**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientwaitforcompletion?branch=master)    | Blocks until either the multicast session is complete or the specified timeout is reached.                                                                                  |



 

 

 




