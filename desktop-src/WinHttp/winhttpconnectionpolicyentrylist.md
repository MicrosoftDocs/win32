---
description: Contains a list of connection routing policy entries to register with the WinHTTP Auto-Proxy Service.
title: WINHTTP_CONNECTION_POLICY_ENTRY_LIST structure
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINHTTP_CONNECTION_POLICY_ENTRY_LIST
api_type: 
- HeaderDef
api_location: 
- winhttp_conn_proxy.h
---

# WINHTTP_CONNECTION_POLICY_ENTRY_LIST structure

Contains a list of connection routing policy entries to register with the WinHTTP Auto-Proxy Service.

## Syntax

```cpp
typedef struct _WINHTTP_CONNECTION_POLICY_ENTRY_LIST {
    WINHTTP_CONNECTION_POLICY_ENTRY *pPolicyEntries;
    DWORD                            nEntries;
} WINHTTP_CONNECTION_POLICY_ENTRY_LIST;
```

## Members

### pPolicyEntries

Pointer to an array of [WINHTTP_CONNECTION_POLICY_ENTRY](winhttpconnectionpolicyentry.md) structures, each defining a host/application-to-connection routing rule.

### nEntries

The number of entries in the **pPolicyEntries** array.

## Requirements

| Requirement | Value |
|---|---|
| Header | winhttp_conn_proxy.h |

## See also

- [WINHTTP_CONNECTION_POLICY_ENTRY](winhttpconnectionpolicyentry.md)
- [WinHttpConnectionSetPolicyEntries](winhttpconnectionsetpolicyentries.md)
