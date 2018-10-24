---
title: WebSocket Protocol Component API Functions
description: The WebSocket Protocol Component API defines these functions.
ms.assetid: B833D18D-286C-4D32-A9C7-D5D5806EC306
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WebSocket Protocol Component API Functions

The WebSocket Protocol Component API defines these functions.

## In this section



| Topic                                                                             | Description                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WebSocketAbortHandle**](/windows/desktop/api/Websocket/nf-websocket-websocketaborthandle)<br/>                   | aborts a WebSocket session handle created by [**WebSocketCreateClientHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449325) or [**WebSocketCreateServerHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449327).<br/>   |
| [**WebSocketBeginClientHandshake**](/windows/desktop/api/Websocket/nf-websocket-websocketbeginclienthandshake)<br/> | begins the client-side handshake.<br/>                                                                                                                                                                |
| [**WebSocketBeginServerHandshake**](/windows/desktop/api/Websocket/nf-websocket-websocketbeginserverhandshake)<br/> | begins the server-side handshake.<br/>                                                                                                                                                                |
| [**WebSocketCompleteAction**](/windows/desktop/api/Websocket/nf-websocket-websocketcompleteaction)<br/>             | completes an action started by [**WebSocketGetAction**](https://msdn.microsoft.com/library/windows/desktop/hh449336).<br/>                                                                                                             |
| [**WebSocketCreateClientHandle**](/windows/desktop/api/Websocket/nf-websocket-websocketcreateclienthandle)<br/>     | creates a client-side WebSocket session handle.<br/>                                                                                                                                                  |
| [**WebSocketCreateServerHandle**](/windows/desktop/api/Websocket/nf-websocket-websocketcreateserverhandle)<br/>     | creates a server-side WebSocket session handle.<br/>                                                                                                                                                  |
| [**WebSocketDeleteHandle**](/windows/desktop/api/Websocket/nf-websocket-websocketdeletehandle)<br/>                 | deletes a WebSocket session handle created by [**WebSocketCreateClientHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449325) or [**WebSocketCreateServerHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449327).<br/>  |
| [**WebSocketEndClientHandshake**](/windows/desktop/api/Websocket/nf-websocket-websocketendclienthandshake)<br/>     | completes the client-side handshake.<br/>                                                                                                                                                             |
| [**WebSocketEndServerHandshake**](/windows/desktop/api/Websocket/nf-websocket-websocketendserverhandshake)<br/>     | completes the server-side handshake.<br/>                                                                                                                                                             |
| [**WebSocketGetAction**](/windows/desktop/api/Websocket/nf-websocket-websocketgetaction)<br/>                       | returns an action from a call to [**WebSocketSend**](https://msdn.microsoft.com/library/windows/desktop/hh449340), [**WebSocketReceive**](https://msdn.microsoft.com/library/windows/desktop/hh449338) or [**WebSocketCompleteAction**](https://msdn.microsoft.com/library/windows/desktop/hh449323).<br/> |
| [**WebSocketGetGlobalProperty**](/windows/desktop/api/Websocket/nf-websocket-websocketgetglobalproperty)<br/>       | gets a single WebSocket property.<br/>                                                                                                                                                                |
| [**WebSocketReceive**](/windows/desktop/api/Websocket/nf-websocket-websocketreceive)<br/>                           | adds a receive operation to the protocol component operation queue.<br/>                                                                                                                              |
| [**WebSocketSend**](/windows/desktop/api/Websocket/nf-websocket-websocketsend)<br/>                                 | adds a send operation to the protocol component operation queue.<br/>                                                                                                                                 |



 

 

 





