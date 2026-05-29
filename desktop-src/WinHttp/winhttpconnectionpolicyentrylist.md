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
- N/A
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

## Remarks

> [!NOTE]
> This type is not currently included in an SDK header file. You must declare it yourself in your code.

## Requirements

| Requirement | Value |
|---|---|
| Header | N/A |

## See also

- [WINHTTP_CONNECTION_POLICY_ENTRY](winhttpconnectionpolicyentry.md)
- [WinHttpConnectionSetPolicyEntries](winhttpconnectionsetpolicyentries.md)
