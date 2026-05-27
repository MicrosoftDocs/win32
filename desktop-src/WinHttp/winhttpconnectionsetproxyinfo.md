---
description: Sets or replaces proxy configuration for a specific proxy type on a named network connection.
title: WinHttpConnectionSetProxyInfo function
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WinHttpConnectionSetProxyInfo
api_type: 
- DllExport
api_location: 
- winhttp.dll
---

# WinHttpConnectionSetProxyInfo function

Sets or replaces proxy configuration for a specific proxy type on a named network connection.

## Syntax

```cpp
DWORD WINAPI WinHttpConnectionSetProxyInfo(
    _In_z_ PCWSTR                          pwszConnectionName,
    _In_   WINHTTP_CONNECTION_PROXY_TYPE    Type,
    _In_   const WINHTTP_CONNECTION_PROXY_INFO *pProxyInfo
);
```

## Parameters

### pwszConnectionName [in]

A null-terminated Unicode string identifying the network connection. Maximum length is **WINHTTP_CONNECTION_NAME_MAX_LENGTH** (64 characters). This typically corresponds to a cellular APN name or Wi-Fi profile name.

### Type [in]

The proxy protocol type to set. One of the following values.

| Value | Meaning |
|-------|---------|
| **WINHTTP_CONNECTION_PROXY_TYPE_HTTP** (1) | HTTP proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_WAP** (2) | WAP proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_SOCKS4** (4) | SOCKS4 proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_SOCKS5** (5) | SOCKS5 proxy. |

### pProxyInfo [in]

Pointer to a **WINHTTP_CONNECTION_PROXY_INFO** structure containing the proxy configuration. The **Version** field must be set to **WINHTTP_CONNECTION_PROXY_INFO_CURRENT_VERSION** (1).

The structure supports two modes via the **Switch** field:

- **WINHTTP_CONNECTION_PROXY_INFO_SWITCH_CONFIG** — Manual proxy configuration with server address, port, credentials, exception list, and extra info.
- **WINHTTP_CONNECTION_PROXY_INFO_SWITCH_SCRIPT** / **WINHTTP_CONNECTION_PROXY_INFO_SWITCH_WPAD** — Automatic proxy configuration via PAC script URL or WPAD, with optional credentials.

The **pwszFriendlyName** field should be unique or **NULL**/empty (a unique name is auto-generated if not specified).

The **Flags** field supports:

| Flag | Meaning |
|------|---------|
| **WINHTTP_CONNECTION_PROXY_INFO_FLAG_DISABLED** (0x1) | Proxy is disabled. |
| **WINHTTP_CONNECTION_PROXY_INFO_FLAG_BYPASSLOCAL** (0x2) | Bypass proxy for local addresses. |

## Return value

Returns **ERROR_SUCCESS** (0) on success. Returns a [system error code](/windows/win32/debug/system-error-codes) on failure, including the following.

| Value | Description |
|-------|-------------|
| **ERROR_INVALID_PARAMETER** | Invalid connection name or proxy info. |
| **ERROR_ACCESS_DENIED** | Caller lacks required privileges. |

## Remarks

If the specified proxy type does not exist for the connection, it is added. If it already exists, it is replaced.

For HTTP proxies, the function probes the proxy for authentication requirements. If the proxy requires authentication and credentials are supplied, they are stored in Windows Credential Manager.

This API requires elevated (administrator) privileges.

## Requirements

| Requirement | Value |
|---|---|
| Header | winhttp.h, winhttp_conn_proxy.h |
| Library | winhttp.lib |
| DLL | winhttp.dll |

## See also

- [WinHttpConnectionDeleteProxyInfo](winhttpconnectiondeleteproxyinfo.md)
- [WinHttpConnectionSetPolicyEntries](winhttpconnectionsetpolicyentries.md)
