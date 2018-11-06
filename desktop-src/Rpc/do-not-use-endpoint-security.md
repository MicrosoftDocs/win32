---
title: Do Not Use Endpoint Security
description: Endpoint security is a security model in which a security descriptor is given when an endpoint is created with the RpcServerUseProtseq\ group of RPC functions.
ms.assetid: 5b8841c4-5b65-417f-b790-e8c2dabb44a1
ms.topic: article
ms.date: 05/31/2018
---

# Do Not Use Endpoint Security

Endpoint security is a security model in which a security descriptor is given when an endpoint is created with the [**RpcServerUseProtseq**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseq)\* group of RPC functions. Do not use this security model. Do not give security descriptors to those functions. At best, this method is a waste of CPU resources. At worst, in many environments it is possible to circumvent the security descriptor, as the [Be Wary of Other RPC Endpoints Running In the Same Process](be-wary-of-other-rpc-endpoints-running-in-the-same-process.md) section exemplifies.

Endpoint security exists only for backward compatibility.

 

 




