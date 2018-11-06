---
title: Client-side Asynchronous Pipe Handling
description: Before making an asynchronous remote call, the client must first initialize the asynchronous handle.
ms.assetid: 3d54b233-d8b0-45d1-b759-0d2d24c1e247
ms.topic: article
ms.date: 05/31/2018
---

# Client-side Asynchronous Pipe Handling

Before making an asynchronous remote call, the client must first initialize the asynchronous handle. As with nonpipe procedures, the client calls an asynchronous function with the asynchronous handle as the first parameter and uses the asynchronous handle to send and receive pipe data, query the status of the call, and receive the reply.

The client makes the asynchronous remote procedure call with the asynchronous handle as the first parameter. The client can use this handle to query the status of the call and to receive the reply. The asynchronous pipe model is symmetric. Both client and server applications send and receive pipe data actively (as opposed to synchronous RPC, where the pipe data is sent and received passively).

The client sends asynchronous pipe data by calling the **push** function on the appropriate asynchronous pipe, with the pipe's state variable as the first parameter. When the **push** function returns, the client can modify or free the send buffer.

If the RPC\_ASYNC\_NOTIFY\_ON\_SEND\_COMPLETE flag is set in the asynchronous handle, and if APCs are used as the notification mechanism, an APC is queued when the pipe send is actually complete. You can take advantage of this mechanism to implement flow control. Note, however, that if the client pushes another buffer before the previous push is complete, the client may, depending on the speed of the transfer operation, receive only one send-complete notification, rather than one notification for each buffer or each **push** operation. When the client has sent all of the pipe data, it makes one final **push** call with the number of elements set to 0.

The client program receives asynchronous pipe data by calling the **pull** function on the appropriate asynchronous pipe, with the pipe's state variable as the first parameter. If no pipe data is available, the **pull** function returns RPC\_S\_ASYNC\_CALL\_PENDING.

If the notification mechanism is APC, and the server returned RPC\_S\_ASYNC\_CALL\_PENDING, the client must wait until it receives the **RpcReceiveComplete** APC from run-time before calling **pull** again.

 

 




