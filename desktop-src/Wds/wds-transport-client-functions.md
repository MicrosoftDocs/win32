---
title: WDS Transport Client Functions
description: This module defines the structures and functions that compose the interface between the content receiver and the transport client.
ms.assetid: '20c3116b-3a0d-4048-b6f2-81c03e0a80ef'
---

# WDS Transport Client Functions

This module defines the structures and functions that compose the interface between the content receiver and the transport client.



| Function                                                                              | Description                                                                                                                                                                 |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*PFN\_WdsTransportClientReceiveContents*](pfn-wdstransportclientreceivecontents.md) | Indicates that a block of data is ready to be used.                                                                                                                         |
| [*PFN\_WdsTransportClientReceiveMetadata*](pfn-wdstransportclientreceivemetadata.md) | Receives metadata information about a file.                                                                                                                                 |
| [*PFN\_WdsTransportClientSessionComplete*](pfn-wdstransportclientsessioncomplete.md) | Indicates that the session completed successfully or encountered an error.                                                                                                  |
| [*PFN\_WdsTransportClientSessionStart*](pfn-wdstransportclientsessionstart.md)       | Indicates the file size and other server side information about the file to the consumer.                                                                                   |
| [*PFN\_WdsTransportClientSessionStartEx*](pfn-wdstransportclientsessionstartex.md)   | Indicates the file size and other server side information about the file to the consumer.                                                                                   |
| [**WdsTransportClientAddRefBuffer**](wdstransportclientaddrefbuffer.md)              | Increments the reference count on a buffer owned by the multicast client.                                                                                                   |
| [**WdsTransportClientCancelSession**](wdstransportclientcancelsession.md)            | Releases the resources associated with a session in the client.                                                                                                             |
| [**WdsTransportClientCloseSession**](wdstransportclientclosesession.md)              | Releases the resources associated with a session in the client.                                                                                                             |
| [**WdsTransportClientCompleteReceive**](wdstransportclientcompletereceive.md)        | Indicates that all processing on a block of data is finished, and that the multicast client may remove this block of data from its cache to make room for further receives. |
| [**WdsTransportClientInitialize**](wdstransportclientinitialize.md)                  | Initializes the multicast client.                                                                                                                                           |
| [**WdsTransportClientInitializeSession**](wdstransportclientinitializesession.md)    | Initiates a multicast file transfer.                                                                                                                                        |
| [**WdsTransportClientQueryStatus**](wdstransportclientquerystatus.md)                | Retrieves the current status of an ongoing or complete multicast transmission from the multicast client.                                                                    |
| [**WdsTransportClientRegisterCallback**](wdstransportclientregistercallback.md)      | Registers a callback with the multicast client.                                                                                                                             |
| [**WdsTransportClientReleaseBuffer**](wdstransportclientreleasebuffer.md)            | Decrements the reference count on a buffer owned by the multicast client.                                                                                                   |
| [**WdsTransportClientShutdown**](wdstransportclientshutdown.md)                      | Shuts down the multicast client.                                                                                                                                            |
| [**WdsTransportClientStartSession**](wdstransportclientstartsession.md)              | Initiates a multicast file transfer.                                                                                                                                        |
| [**WdsTransportClientWaitForCompletion**](wdstransportclientwaitforcompletion.md)    | Blocks until either the multicast session is complete or the specified timeout is reached.                                                                                  |



 

 

 




