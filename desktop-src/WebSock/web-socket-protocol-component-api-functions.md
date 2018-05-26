---
title: WebSocket Protocol Component API Functions
description: The WebSocket Protocol Component API defines these functions.
ms.assetid: B833D18D-286C-4D32-A9C7-D5D5806EC306
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WebSocket Protocol Component API Functions

The WebSocket Protocol Component API defines these functions.

## In this section



| Topic                                                                             | Description                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WebSocketAbortHandle**](/windows/win32/Websocket/nf-websocket-websocketaborthandle?branch=master)<br/>                   | aborts a WebSocket session handle created by [**WebSocketCreateClientHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449325) or [**WebSocketCreateServerHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449327).<br/>   |
| [**WebSocketBeginClientHandshake**](/windows/win32/Websocket/nf-websocket-websocketbeginclienthandshake?branch=master)<br/> | begins the client-side handshake.<br/>                                                                                                                                                                |
| [**WebSocketBeginServerHandshake**](/windows/win32/Websocket/nf-websocket-websocketbeginserverhandshake?branch=master)<br/> | begins the server-side handshake.<br/>                                                                                                                                                                |
| [**WebSocketCompleteAction**](/windows/win32/Websocket/nf-websocket-websocketcompleteaction?branch=master)<br/>             | completes an action started by [**WebSocketGetAction**](https://msdn.microsoft.com/library/windows/desktop/hh449336).<br/>                                                                                                             |
| [**WebSocketCreateClientHandle**](/windows/win32/Websocket/nf-websocket-websocketcreateclienthandle?branch=master)<br/>     | creates a client-side WebSocket session handle.<br/>                                                                                                                                                  |
| [**WebSocketCreateServerHandle**](/windows/win32/Websocket/nf-websocket-websocketcreateserverhandle?branch=master)<br/>     | creates a server-side WebSocket session handle.<br/>                                                                                                                                                  |
| [**WebSocketDeleteHandle**](/windows/win32/Websocket/nf-websocket-websocketdeletehandle?branch=master)<br/>                 | deletes a WebSocket session handle created by [**WebSocketCreateClientHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449325) or [**WebSocketCreateServerHandle**](https://msdn.microsoft.com/library/windows/desktop/hh449327).<br/>  |
| [**WebSocketEndClientHandshake**](/windows/win32/Websocket/nf-websocket-websocketendclienthandshake?branch=master)<br/>     | completes the client-side handshake.<br/>                                                                                                                                                             |
| [**WebSocketEndServerHandshake**](/windows/win32/Websocket/nf-websocket-websocketendserverhandshake?branch=master)<br/>     | completes the server-side handshake.<br/>                                                                                                                                                             |
| [**WebSocketGetAction**](/windows/win32/Websocket/nf-websocket-websocketgetaction?branch=master)<br/>                       | returns an action from a call to [**WebSocketSend**](https://msdn.microsoft.com/library/windows/desktop/hh449340), [**WebSocketReceive**](https://msdn.microsoft.com/library/windows/desktop/hh449338) or [**WebSocketCompleteAction**](https://msdn.microsoft.com/library/windows/desktop/hh449323).<br/> |
| [**WebSocketGetGlobalProperty**](/windows/win32/Websocket/nf-websocket-websocketgetglobalproperty?branch=master)<br/>       | gets a single WebSocket property.<br/>                                                                                                                                                                |
| [**WebSocketReceive**](/windows/win32/Websocket/nf-websocket-websocketreceive?branch=master)<br/>                           | adds a receive operation to the protocol component operation queue.<br/>                                                                                                                              |
| [**WebSocketSend**](/windows/win32/Websocket/nf-websocket-websocketsend?branch=master)<br/>                                 | adds a send operation to the protocol component operation queue.<br/>                                                                                                                                 |



 

 

 





