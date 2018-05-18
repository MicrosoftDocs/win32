---
title: Transport Security
description: Although this is not the preferred method, you can use the security settings that the named-pipe transport offers to add security features to your distributed application.
ms.assetid: 'faf48049-807c-4155-aa01-1947a0311a71'
---

# Transport Security

Although this is not the preferred method, you can use the security settings that the named-pipe transport offers to add security features to your distributed application. These security settings are used with the Microsoft RPC functions that start with the prefixes [**RpcServerUseProtseq**](rpcserveruseprotseq.md) and [**RpcServerUseAllProtseqs**](rpcserveruseallprotseqs.md), and the functions [**RpcImpersonateClient**](rpcimpersonateclient.md) and [**RpcRevertToSelf**](rpcreverttoself.md).

> [!Note]  
> If you are running an application that is a service and you are using NTLM for security, you must add an explicit service dependency for your application. The Secur32.dll will call the Service Control Manager (SCM) to begin the NTLM security package service. However, an RPC application that is a service and is running as a system, must also contact the SC unless it is connecting to another service on the same computer.

 

 

 




