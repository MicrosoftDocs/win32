---
description: Deletes the proxy configuration for a specific proxy type from a named network connection.
title: WinHttpConnectionDeleteProxyInfo function
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WinHttpConnectionDeleteProxyInfo
api_type: 
- DllExport
api_location: 
- winhttp.dll
---

# WinHttpConnectionDeleteProxyInfo function

Deletes the proxy configuration for a specific proxy type from a named network connection.

## Syntax

```cpp
DWORD WINAPI WinHttpConnectionDeleteProxyInfo(
    _In_z_ PCWSTR                          pwszConnectionName,
    _In_   WINHTTP_CONNECTION_PROXY_TYPE    Type
);
```

## Parameters

### pwszConnectionName [in]

A null-terminated Unicode string identifying the network connection whose proxy configuration is to be removed.

### Type [in]

The proxy protocol type to delete. One of the following values.

| Value | Meaning |
|-------|---------|
| **WINHTTP_CONNECTION_PROXY_TYPE_HTTP** (1) | HTTP proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_WAP** (2) | WAP proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_SOCKS4** (4) | SOCKS4 proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_SOCKS5** (5) | SOCKS5 proxy. |

## Return value

Returns **ERROR_SUCCESS** (0) on success. Returns a [system error code](/windows/win32/debug/system-error-codes) on failure, including the following.

| Value | Description |
|-------|-------------|
| **ERROR_FILE_NOT_FOUND** | The proxy or connection does not exist. This can occur if the connection was already deleted (which auto-removes all associated proxies). This error can safely be ignored in cleanup scenarios. |
| **ERROR_ACCESS_DENIED** | Caller lacks required privileges. |

## Remarks

Before deleting the proxy entry, the function retrieves the current proxy configuration to identify stored credentials. Any credentials associated with the proxy server are removed from Windows Credential Manager on a best-effort basis.

This API requires elevated (administrator) privileges.

## Requirements

| Requirement | Value |
|---|---|
| Header | winhttp.h, winhttp_conn_proxy.h |
| Library | winhttp.lib |
| DLL | winhttp.dll |

## See also

- [WinHttpConnectionSetProxyInfo](winhttpconnectionsetproxyinfo.md)
