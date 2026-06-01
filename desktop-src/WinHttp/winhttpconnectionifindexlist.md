---
description: Contains a list of connection-to-interface-index mappings used to update the WinHTTP routing table.
title: WINHTTP_CONNECTION_IFINDEX_LIST structure
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINHTTP_CONNECTION_IFINDEX_LIST
api_type: 
- HeaderDef
api_location: 
- N/A
---

# WINHTTP_CONNECTION_IFINDEX_LIST structure

Contains a list of connection-to-interface-index mappings used to update the WinHTTP routing table.

## Syntax

```cpp
typedef struct _WINHTTP_CONNECTION_IFINDEX_LIST {
    WINHTTP_CONNECTION_IFINDEX_ENTRY *pConnectionIfIndexEntries;
    DWORD                             nEntries;
} WINHTTP_CONNECTION_IFINDEX_LIST;
```

## Members

### pConnectionIfIndexEntries

Pointer to an array of [WINHTTP_CONNECTION_IFINDEX_ENTRY](winhttpconnectionifindexentry.md) structures, each mapping a connection name to an interface index.

### nEntries

The number of entries in the **pConnectionIfIndexEntries** array. Set to 0 to clear all connection-interface mappings.

## Remarks

> [!NOTE]
> This type is not currently included in an SDK header file. You must declare it yourself in your code.

## Requirements

| Requirement | Value |
|---|---|
| Header | N/A |

## See also

- [WINHTTP_CONNECTION_IFINDEX_ENTRY](winhttpconnectionifindexentry.md)
- [WinHttpConnectionUpdateIfIndexTable](winhttpconnectionupdateifindextable.md)
