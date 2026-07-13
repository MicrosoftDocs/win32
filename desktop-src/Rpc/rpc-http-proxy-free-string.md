---
title: RpcHttpProxyFreeString function
description: The RpcHttpProxyFreeString function is used as a callback to the Redirector DLL to free the resources associated with a new server string.
ms.date: 03/20/2024
ms.keywords: RpcHttpProxyFreeString
ms.topic: reference
req.header: rpcdce.h
req.include-header: Rpc.h
req.target-type: Windows
req.lib: Rpcrt4.lib
req.dll: Rpcrt4.dll
targetos: Windows
topic_type:
 - APIRef
api_type:
 - DllExport
api_location:
 - Rpcrt4.dll
api_name:
 - RpcHttpProxyFreeString
---

# RpcHttpProxyFreeString function

## Description

The **RpcHttpProxyFreeString** function is used as a callback to the Redirector DLL to free the resources associated with a new server string. This is called after the RPC Proxy has completed the connection to the RPC server and it is used to free the resources associated with a *NewServerName* or *NewServerPort*.

## Syntax

```cpp
typedef void (__RPC_USER * RPC_HTTP_PROXY_FREE_STRING) (
    __in RPC_WSTR String
);
```

## Parameters

*String* \[in\]

The string for which the resource should be freed.

## Remarks

This function is defined by RPC and must be implemented by a redirector DLL. If a redirector DLL fails to implement both the [RpcNewHttpProxyChannel](rpc-new-http-proxy-channel.md) function and the **RpcHttpProxyFreeString** function, the Redirector DLL will be immediately unloaded and will not be called.

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows Vista [desktop apps \| UWP apps] |
| Minimum supported server | Windows Server 2003 [desktop apps \| UWP apps] |
| Target Platform | Windows |
| Header | rpcdce.h (include Rpc.h) |
| Library | Rpcrt4.lib |
| DLL | Rpcrt4.dll |

## See also

- [RpcNewHttpProxyChannel](rpc-new-http-proxy-channel.md)
- [RPC_HTTP_REDIRECTOR_STAGE](rpc-http-redirector-stage.md)
- [RPC Functions](rpc-functions.md)
