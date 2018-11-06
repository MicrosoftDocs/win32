---
title: Function Call Attributes
description: Programs can use these attributes on individual functions within the interface, and affect only that function.
ms.assetid: c54dbcd9-46c9-4755-b4a8-0f78068920b7
keywords:
- IDL MIDL , attributes, function call
ms.topic: article
ms.date: 05/31/2018
---

# Function Call Attributes

Programs can use these attributes on individual functions within the interface, and affect only that function.



| Attribute                        | Usage                                                                                                                                                                                                                                                      |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**message**](message.md)       | The remote procedure call is to be treated as an asynchronous message from the client to the server. The client makes the call and returns immediately, while the actual call is handled by the message-queuing transport ([**ncadg\_mq**](ncadg-mq.md)). |
| [**maybe**](maybe.md)           | The client making this remote procedure call does not expect any response indicating delivery or completion of the call. This is in contrast to [**message**](message.md) operations where no response is expected but the delivery is guaranteed.        |
| [**broadcast**](broadcast.md)   | The remote procedure call is to be sent to all of the servers on the network. The client accepts the first return, subsequent replies from other servers are discarded.                                                                                    |
| [**idempotent**](idempotent.md) | The call does not change state and returns the same information each time it is called with the same input parameters.                                                                                                                                     |
| [**callback**](callback.md)     | Designates a function that resides in the client application, which the server can call to obtain information from the client.                                                                                                                             |
| [**call\_as**](call-as.md)      | Maps a nonremotable function to a remote procedure call.                                                                                                                                                                                                   |
| [**local**](local.md)           | Designates a local procedure for which MIDL does not generate stub code.                                                                                                                                                                                   |



 

On non-[**object**](object.md) interfaces, you can also apply the [**context\_handle**](context-handle.md) attribute to a function to specify characteristics of the return value.

 

 




