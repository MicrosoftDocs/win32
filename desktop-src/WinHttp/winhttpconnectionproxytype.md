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
- N/A
---

# WINHTTP_CONNECTION_PROXY_TYPE enumeration

Specifies the type of proxy protocol for a per-connection proxy configuration.

## Syntax

```cpp
typedef enum _WINHTTP_CONNECTION_PROXY_TYPE {
    WINHTTP_CONNECTION_PROXY_TYPE_NULL   = 0,
    WINHTTP_CONNECTION_PROXY_TYPE_HTTP   = 1
} WINHTTP_CONNECTION_PROXY_TYPE;
```

## Constants

| Constant | Value | Description |
|----------|-------|-------------|
| **WINHTTP_CONNECTION_PROXY_TYPE_NULL** | 0 | No proxy / placeholder. |
| **WINHTTP_CONNECTION_PROXY_TYPE_HTTP** | 1 | HTTP/HTTPS proxy. |

## Remarks

> [!NOTE]
> This type is not currently included in an SDK header file. You must declare it yourself in your code.

## Requirements

| Requirement | Value |
|---|---|
| Header | N/A |

## See also

- [WinHttpConnectionSetProxyInfo](winhttpconnectionsetproxyinfo.md)
- [WinHttpConnectionDeleteProxyInfo](winhttpconnectiondeleteproxyinfo.md)
- [WINHTTP_CONNECTION_PROXY_INFO](winhttpconnectionproxyinfo.md)
