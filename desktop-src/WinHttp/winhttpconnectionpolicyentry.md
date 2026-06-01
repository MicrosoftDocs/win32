---
description: Defines a connection routing policy entry that associates a host and application with eligible network connections.
title: WINHTTP_CONNECTION_POLICY_ENTRY structure
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINHTTP_CONNECTION_POLICY_ENTRY
api_type: 
- HeaderDef
api_location: 
- N/A
---

# WINHTTP_CONNECTION_POLICY_ENTRY structure

Defines a connection routing policy entry that associates a host and application with eligible network connections.

## Syntax

```cpp
typedef struct _WINHTTP_CONNECTION_POLICY_ENTRY {
    PCWSTR  pwszHost;
    PCWSTR  pwszAppId;
    DWORD   cbAppSid;
    PBYTE   pbAppSid;
    DWORD   nConnections;
    PCWSTR *ppwszConnections;
    DWORD   dwPolicyEntryFlags;
} WINHTTP_CONNECTION_POLICY_ENTRY;
```

## Members

### pwszHost

Target hostname pattern this policy applies to (for example, "\*.contoso.com").

### pwszAppId

Application identifier. This is typically a package family name, or "\*" to match all applications.

### cbAppSid

Size, in bytes, of the app container SID pointed to by **pbAppSid**. Set to 0 if not applicable.

### pbAppSid

Pointer to the app container SID bytes for the application, derived from **pwszAppId** via **DeriveAppContainerSidFromAppContainerName**. Set to **NULL** if not applicable.

### nConnections

Number of connection name strings in the **ppwszConnections** array.

### ppwszConnections

Pointer to an array of null-terminated Unicode strings, each specifying a connection name eligible to carry traffic matching this policy entry.

### dwPolicyEntryFlags

Policy entry flags. The following value is supported.

| Flag | Value | Description |
|------|-------|-------------|
| **WINHTTP_CONNECTION_POLICY_ENTRY_ONDEMAND** | 0x1 | Indicates the connection should be activated on-demand when traffic matches this policy entry. |

## Remarks

> [!NOTE]
> This type is not currently included in an SDK header file. You must declare it yourself in your code.

## Requirements

| Requirement | Value |
|---|---|
| Header | N/A |

## See also

- [WINHTTP_CONNECTION_POLICY_ENTRY_LIST](winhttpconnectionpolicyentrylist.md)
- [WINHTTP_CONNECTION_POLICY_TAG](winhttpconnectionpolicytag.md)
- [WinHttpConnectionSetPolicyEntries](winhttpconnectionsetpolicyentries.md)
