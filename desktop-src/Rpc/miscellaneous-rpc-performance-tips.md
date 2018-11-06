---
title: Miscellaneous RPC Performance Tips
description: This section discusses miscellaneous performance tips for developing high performance RPC servers. This section provides many tips that refer to the RPC client. Developing an RPC client properly enables the RPC server to perform less work.
ms.assetid: 82278f4b-1273-45e8-9078-ad919a4711f0
ms.topic: article
ms.date: 05/31/2018
---

# Miscellaneous RPC Performance Tips

This section discusses miscellaneous performance tips for developing high performance RPC servers. This section provides many tips that refer to the RPC client. Developing an RPC client properly enables the RPC server to perform less work.

## Use Kerberos

If security is used, use Kerberos. On the server side, Kerberos does not require access to the KDC. This moves the workload from the server to the client, which provides better performing servers.

## Use Static Identity Tracking

If security is used, try to use static identity tracking. Static identity tracking is cheaper in terms of resource usage than dynamic identity tracking. If the client identity changes, and the server should not be aware of the change, use dynamic tracking instead of creating a different binding handle for each identity. But if the identity is the same, ensure RPC is aware of that fact to avoid having RPC make checks for changed identity every time.

## Use the RpcGetAuthorizationContextForClient Function

If you need to check access in Windows XP, use the [**RpcGetAuthorizationContextForClient**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcgetauthorizationcontextforclient) function. The resulting Authz contexts enables very fast access checks, which are efficiently cached by the RPC run time.

## Do Not Modify the Token Unless Necessary

If dynamic identity tracking is used, do not modify the thread/process token unless absolutely necessary. Even if it is modified to settings it previously had, the token often is sufficiently different to the security system to trigger the establishment of a new security context.

## Consider Mixed Mode Serialization for Context Handles

The default serialization mode for context handle is serialized (exclusive). Consider making all calls that do not modify the state of the context handle in shared serialization mode. See [**RpcSsContextLockExclusive**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcsscontextlockexclusive) for more information.

 

 




