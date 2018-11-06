---
title: Propagating Error Information
description: Propagating extended error information allows servers that receive an RPC\_S\_\ error, or any other error code for that matter, to allow the RPC run time to propagate the information it received to its callers.
ms.assetid: f0395f19-ceb1-4249-892e-9b688464d0d2
ms.topic: article
ms.date: 05/31/2018
---

# Propagating Error Information

Propagating extended error information allows servers that receive an RPC\_S\_\* error, or any other error code for that matter, to allow the RPC run time to propagate the information it received to its callers. All the server must do is call the [**RpcRaiseException**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcraiseexception) or [**RpcAsyncAbortCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall) upon encountering a fatal error. The RPC run time takes care of chaining the extended error information, if any, causing the fatal error to report the fatal error itself, as long as the error code given to **RpcRaiseException** or **RpcAsyncAbortCall** is the same as the error code causing the fatal error.

 

 




