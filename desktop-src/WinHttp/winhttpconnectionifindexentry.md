---
description: Maps a named network connection to its active network interface index.
title: WINHTTP_CONNECTION_IFINDEX_ENTRY structure
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINHTTP_CONNECTION_IFINDEX_ENTRY
api_type: 
- HeaderDef
api_location: 
- winhttp_conn_proxy.h
---

# WINHTTP_CONNECTION_IFINDEX_ENTRY structure

Maps a named network connection to its active network interface index.

## Syntax

```cpp
typedef struct _WINHTTP_CONNECTION_IFINDEX_ENTRY {
    PCWSTR pwszConnectionName;
    DWORD  dwIfIndex;
} WINHTTP_CONNECTION_IFINDEX_ENTRY;
```

## Members

### pwszConnectionName

A null-terminated Unicode string containing the network connection name (for example, "Cellular" or "Wi-Fi").

### dwIfIndex

The active network interface index (**IF_INDEX**) associated with this connection.

## Requirements

| Requirement | Value |
|---|---|
| Header | winhttp_conn_proxy.h |

## See also

- [WINHTTP_CONNECTION_IFINDEX_LIST](winhttpconnectionifindexlist.md)
- [WinHttpConnectionUpdateIfIndexTable](winhttpconnectionupdateifindextable.md)
