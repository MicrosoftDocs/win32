---
description: Specifies the type of proxy protocol for a per-connection proxy configuration.
title: WINHTTP_CONNECTION_PROXY_TYPE enumeration
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINHTTP_CONNECTION_PROXY_TYPE
api_type: 
- HeaderDef
api_location: 
- winhttp_conn_proxy.h
---

# WINHTTP_CONNECTION_PROXY_TYPE enumeration

Specifies the type of proxy protocol for a per-connection proxy configuration.

## Syntax

```cpp
typedef enum _WINHTTP_CONNECTION_PROXY_TYPE {
    WINHTTP_CONNECTION_PROXY_TYPE_NULL   = 0,
    WINHTTP_CONNECTION_PROXY_TYPE_HTTP   = 1,
    WINHTTP_CONNECTION_PROXY_TYPE_WAP    = 2,
    WINHTTP_CONNECTION_PROXY_TYPE_SOCKS4 = 4,
    WINHTTP_CONNECTION_PROXY_TYPE_SOCKS5 = 5
} WINHTTP_CONNECTION_PROXY_TYPE;
```

## Constants

| Constant | Value | Description |
|----------|-------|-------------|
| **WINHTTP_CONNECTION_PROXY_TYPE_NULL** | 0 | No proxy / placeholder. |
| **WINHTTP_CONNECTION_PROXY_TYPE_HTTP** | 1 | HTTP/HTTPS proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_WAP** | 2 | WAP gateway proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_SOCKS4** | 4 | SOCKS version 4 proxy. |
| **WINHTTP_CONNECTION_PROXY_TYPE_SOCKS5** | 5 | SOCKS version 5 proxy. |

## Requirements

| Requirement | Value |
|---|---|
| Header | winhttp_conn_proxy.h |

## See also

- [WinHttpConnectionSetProxyInfo](winhttpconnectionsetproxyinfo.md)
- [WinHttpConnectionDeleteProxyInfo](winhttpconnectiondeleteproxyinfo.md)
- [WINHTTP_CONNECTION_PROXY_INFO](winhttpconnectionproxyinfo.md)
