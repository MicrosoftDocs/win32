---
title: RPC_HTTP_REDIRECTOR_STAGE enumeration
description: The RPC_HTTP_REDIRECTOR_STAGE enumeration is used to identify the current stage at which the redirector implementation is being called.
ms.date: 03/20/2024
ms.keywords: RPC_HTTP_REDIRECTOR_STAGE
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
 - RPC_HTTP_REDIRECTOR_STAGE
---

# RPC_HTTP_REDIRECTOR_STAGE enumeration

## Description

The **RPC_HTTP_REDIRECTOR_STAGE** enumeration is used to identify the current stage at which the redirector implementation is being called. If a redirector implementation does not recognize or wish to process a stage, it must return **RPC_S_OK** with the exception of the interface stage. If a redirector implementation does not wish to process the interface stage, it must return **RPC_S_UNKNOWN_IF**.

## Syntax

```cpp
typedef enum _RPC_HTTP_REDIRECTOR_STAGE
{
    RPCHTTP_RS_REDIRECT = 1,
    RPCHTTP_RS_ACCESS_1,
    RPCHTTP_RS_SESSION,
    RPCHTTP_RS_ACCESS_2,
    RPCHTTP_RS_INTERFACE
} RPC_HTTP_REDIRECTOR_STAGE;
```

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
- [RpcHttpProxyFreeString](rpc-http-proxy-free-string.md)
- [RPC Enumerated Types](rpc-enumerated-types.md)
