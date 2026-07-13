---
title: RpcNewHttpProxyChannel function
description: The RpcNewHttpProxyChannel function is used to both communicate RPC call attributes to the Redirector DLL and to receive a new server name or server port from the Redirector DLL.
ms.date: 03/20/2024
ms.keywords: RpcNewHttpProxyChannel
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
 - RpcNewHttpProxyChannel
---

# RpcNewHttpProxyChannel function

## Description

The **RpcNewHttpProxyChannel** function is used to both communicate RPC call attributes to the Redirector DLL and to receive a new server name or server port from the Redirector DLL.

## Syntax

```cpp
typedef RPC_STATUS
(__RPC_USER * RPC_NEW_HTTP_PROXY_CHANNEL) (
    _In_ RPC_HTTP_REDIRECTOR_STAGE RedirectorStage,
    _In_ RPC_WSTR ServerName, _In_ RPC_WSTR ServerPort,
    _In_opt_ RPC_WSTR RemoteUser,
    _In_opt_ RPC_WSTR AuthType,
    _Inout_ void __RPC_FAR * ResourceUuid,
    _Inout_ void __RPC_FAR * SessionId,
    _In_opt_ void __RPC_FAR * Interface,
    _In_opt_ void __RPC_FAR * Reserved,
    _In_ unsigned long Flags,
    _Outptr_opt_ RPC_WSTR __RPC_FAR * NewServerName,
    _Outptr_opt_ RPC_WSTR __RPC_FAR * NewServerPort
);
```

## Parameters

*RedirectorStage* \[in\]

The redirector stage at which the redirector implementation is being called. See the definition of [RPC_HTTP_REDIRECTOR_STAGE](rpc-http-redirector-stage.md) for more information on the redirector stages.

*ServerName* \[in\]

The name of the server as specified by the client or the previous redirector/filter DLL. See *NewServerName* to change the server name.

*ServerPort* \[in\]

The port of the server as specified by the client or the previous redirector/filter DLL. See *NewServerPort* to change the server port.

*RemoteUser* \[in\]

**Optional.** The user name as produced by the transport (HTTP) authentication. The user name is obtained by calling [GetServerVariable](/previous-versions/iis/6.0-sdk/ms525335(v=vs.90)) requesting the REMOTE_USER server variable

*AuthType* \[in\]

**Optional.** The authentication type used to authenticate the remote user. The authentication type is obtained by calling [GetServerVariable](/previous-versions/iis/6.0-sdk/ms525335(v=vs.90)) requesting the AUTH_TYPE server variable.

*ResourceUuid* \[in, out\]

**Optional.** The resource ID for this channel. The resource ID is used by RPC Load Balancing to identify the server farm which will service the connection. This Resource ID is the same UUID as the Resource UUID registry key stored under `HKLM\SOFTWARE\Microsoft\Rpc\RpcProxy\LBSConfiguration`.

A new ResourceType can be set only during the Redirect Stage. The use of a Resource ID is ignored unless the RPC Proxy is configured for RPC Load Balancing.

*SessionId* \[in, out\]

**Optional.** The Session ID as identified by the client or a previous redirector DLL. All connections which share a binding handle must share the same Session ID and all connections for a given Session ID must be serviced by the same target server.

A new Session ID can be set only during the Session Stage.

*Interface* \[in\]

**Optional.** The interface syntax identifier [RPC_SYNTAX_IDENTIFIER](/openspecs/windows_protocols/ms-rpcl/1831bd1c-738c-45dc-a2af-5d0b835af6f5) for the interface requested by the client.

*Reserved* \[in\]

**Optional.** This parameter should be ignored.

*Flags* \[in\]

This parameter should be ignored.

*NewServerName* \[out\]

**Optional.** The updated server name.

*NewServerPort* \[out\]

**Optional.** The updated server port.

## Remarks

This function is defined by RPC and must be implemented by a redirector DLL. If a redirector DLL fails to implement both the **RpcNewHttpProxyChannel** function and the [RpcHttpProxyFreeString](rpc-http-proxy-free-string.md) function, the Redirector DLL will be immediately unloaded and will not be called.

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

- [RpcHttpProxyFreeString](rpc-http-proxy-free-string.md)
- [RPC_HTTP_REDIRECTOR_STAGE](rpc-http-redirector-stage.md)
- [RPC_SYNTAX_IDENTIFIER](/openspecs/windows_protocols/ms-rpcl/1831bd1c-738c-45dc-a2af-5d0b835af6f5)
- [GetServerVariable](/previous-versions/iis/6.0-sdk/ms525335(v=vs.90))
- [RPC Functions](rpc-functions.md)
