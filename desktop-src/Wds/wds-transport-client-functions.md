---
title: WDS Transport Client Functions
description: This module defines the structures and functions that compose the interface between the content receiver and the transport client.
ms.assetid: 20c3116b-3a0d-4048-b6f2-81c03e0a80ef
ms.topic: article
ms.date: 05/31/2018
---

# WDS Transport Client Functions

This module defines the structures and functions that compose the interface between the content receiver and the transport client.



| Function                                                                              | Description                                                                                                                                                                 |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*PFN\_WdsTransportClientReceiveContents*](/windows/desktop/api/Wdstci/nc-wdstci-pfn_wdstransportclientreceivecontents) | Indicates that a block of data is ready to be used.                                                                                                                         |
| [*PFN\_WdsTransportClientReceiveMetadata*](/windows/desktop/api/Wdstci/nc-wdstci-pfn_wdstransportclientreceivemetadata) | Receives metadata information about a file.                                                                                                                                 |
| [*PFN\_WdsTransportClientSessionComplete*](/windows/desktop/api/Wdstci/nc-wdstci-pfn_wdstransportclientsessioncomplete) | Indicates that the session completed successfully or encountered an error.                                                                                                  |
| [*PFN\_WdsTransportClientSessionStart*](/windows/desktop/api/Wdstci/nc-wdstci-pfn_wdstransportclientsessionstart)       | Indicates the file size and other server side information about the file to the consumer.                                                                                   |
| [*PFN\_WdsTransportClientSessionStartEx*](/windows/desktop/api/Wdstci/nc-wdstci-pfn_wdstransportclientsessionstartex)   | Indicates the file size and other server side information about the file to the consumer.                                                                                   |
| [**WdsTransportClientAddRefBuffer**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientaddrefbuffer)              | Increments the reference count on a buffer owned by the multicast client.                                                                                                   |
| [**WdsTransportClientCancelSession**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientcancelsession)            | Releases the resources associated with a session in the client.                                                                                                             |
| [**WdsTransportClientCloseSession**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientclosesession)              | Releases the resources associated with a session in the client.                                                                                                             |
| [**WdsTransportClientCompleteReceive**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientcompletereceive)        | Indicates that all processing on a block of data is finished, and that the multicast client may remove this block of data from its cache to make room for further receives. |
| [**WdsTransportClientInitialize**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientinitialize)                  | Initializes the multicast client.                                                                                                                                           |
| [**WdsTransportClientInitializeSession**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientinitializesession)    | Initiates a multicast file transfer.                                                                                                                                        |
| [**WdsTransportClientQueryStatus**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientquerystatus)                | Retrieves the current status of an ongoing or complete multicast transmission from the multicast client.                                                                    |
| [**WdsTransportClientRegisterCallback**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientregistercallback)      | Registers a callback with the multicast client.                                                                                                                             |
| [**WdsTransportClientReleaseBuffer**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientreleasebuffer)            | Decrements the reference count on a buffer owned by the multicast client.                                                                                                   |
| [**WdsTransportClientShutdown**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientshutdown)                      | Shuts down the multicast client.                                                                                                                                            |
| [**WdsTransportClientStartSession**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientstartsession)              | Initiates a multicast file transfer.                                                                                                                                        |
| [**WdsTransportClientWaitForCompletion**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientwaitforcompletion)    | Blocks until either the multicast session is complete or the specified timeout is reached.                                                                                  |



 

 

 




