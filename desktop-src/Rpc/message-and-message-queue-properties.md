---
title: Message and Message Queue Properties
description: A message has properties, which specify a label, a message body, and a number of options.
ms.assetid: d0c9126e-a2c6-4d70-b87a-154a570899fc
ms.topic: article
ms.date: 05/31/2018
---

# Message and Message Queue Properties

A message has properties, which specify a label, a message body, and a number of options. Message property options can include quality of service, priority, journaling, privacy and authentication levels, and the lifetime of the message. In conventional (non-RPC) message-queuing applications, you specify these properties by calling the MSMQ API functions or COM object methods, which are described in the MSMQ SDK documentation. RPC client applications can set certain properties for remote procedure calls by calling [**RpcBindingSetOption**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetoption) and [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo). Once set, the properties remain in effect for each message until the client application resets them.

A message queue has its own set of properties, apart from those of the messages. These properties uniquely identify a queue and define the class of service that the queue provides, the privacy and authentication levels required for messages in this queue, and whether the messages are to be part of a distributed transaction. As with message properties, you specify the properties of a message queue by calling the MSMQ API functions or COM object methods, which are described in the MSMQ documentation. However, an RPC server application can specify properties of its own receive queue when it calls [**RpcServerUseProtseqEpEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex) to establish the binding.

 

 




