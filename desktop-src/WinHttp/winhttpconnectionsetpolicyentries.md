---
description: Registers a set of connection routing policy entries with the WinHTTP Auto-Proxy Service.
title: WinHttpConnectionSetPolicyEntries function
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WinHttpConnectionSetPolicyEntries
api_type: 
- DllExport
api_location: 
- winhttp.dll
---

# WinHttpConnectionSetPolicyEntries function

Registers a set of connection routing policy entries with the WinHTTP Auto-Proxy Service. Policy entries define which network connections should be used for specific host/application combinations, enabling connection-aware HTTP routing.

## Syntax

```cpp
DWORD WINAPI WinHttpConnectionSetPolicyEntries(
    _In_ HINTERNET                              hSession,
    _In_ WINHTTP_CONNECTION_POLICY_TAG          PolicyEntryTag,
    _In_ WINHTTP_CONNECTION_POLICY_ENTRY_LIST  *pPolicyEntryList
);
```

## Parameters

### hSession [in]

A valid WinHTTP session handle created by [**WinHttpOpen**](/windows/win32/api/winhttp/nf-winhttp-winhttpopen). The handle must be a session-level handle.

### PolicyEntryTag [in]

Identifies the owner/source of the policy entries. One of the following values.

| Value | Meaning |
|-------|---------|
| **TAG_WINHTTP_CONNECTION_POLICY_TAG_DEFAULT** (0) | Default/untagged policy entries. |
| **TAG_WINHTTP_CONNECTION_POLICY_TAG_CONNECTION_MANAGER** (1) | Reserved for entries managed by the system connection manager. Third-party applications should use TAG_WINHTTP_CONNECTION_POLICY_TAG_WWWPT to avoid conflicts with system entries. |
| **TAG_WINHTTP_CONNECTION_POLICY_TAG_WWWPT** (2) | Entries managed by the WWWPT (Windows Web Platform Transport) component. |

Tags allow multiple components to independently manage their policy sets without overwriting each other.
 
### pPolicyEntryList [in]

Pointer to a **WINHTTP_CONNECTION_POLICY_ENTRY_LIST** structure containing an array of policy entries.

Each **WINHTTP_CONNECTION_POLICY_ENTRY** in the list contains:

- **pwszHost** — Target hostname pattern this policy applies to.
- **pwszAppId** — Application identifier (package family name or "\*" for all apps).
- **cbAppSid** / **pbAppSid** — Optional app container SID for the application. Set **cbAppSid** to 0 and **pbAppSid** to **NULL** if not applicable.
- **nConnections** — Number of connection names in **ppwszConnections**.
- **ppwszConnections** — Array of connection name strings that may carry traffic for this host/app combination.
- **dwPolicyEntryFlags** — Currently, no flags are supported.

## Return value

Returns **ERROR_SUCCESS** (0) on success. Returns a [system error code](/windows/win32/debug/system-error-codes) on failure, including the following.

| Value | Description |
|-------|-------------|
| **ERROR_WINHTTP_INCORRECT_HANDLE_TYPE** | *hSession* is not a session handle. |
| **ERROR_WINHTTP_NOT_INITIALIZED** | WinHTTP globals are not initialized. |
| **ERROR_ACCESS_DENIED** | Caller lacks required privileges. |

## Remarks

> [!NOTE]
> This API is not currently included in an SDK header file. You must declare the function yourself in your code.

Policy entries instruct WinHTTP which named connections are eligible to carry traffic destined for specific hosts or originating from specific applications. This is central to connection-aware networking on devices with multiple simultaneous network connections.

Calling this function replaces any previously set entries for the same *PolicyEntryTag*. The typical pattern is:

1. Call [**WinHttpConnectionDeletePolicyEntries**](winhttpconnectiondeletepolicyentries.md) to clear stale entries.
2. Call **WinHttpConnectionSetPolicyEntries** with the full updated set.

The Windows Connection Manager uses **TAG_WINHTTP_CONNECTION_POLICY_TAG_CONNECTION_MANAGER** to push host-to-connection routing rules derived from connection selection logic.

This API requires elevated (administrator/SYSTEM) privileges.

### Example

The following example deletes existing connection manager policy entries and then registers a new on-demand policy for all apps connecting to hosts matching `*.contoso.com`.

```cpp
// First delete existing connection manager policies
WinHttpConnectionDeletePolicyEntries(
    hSession,
    TAG_WINHTTP_CONNECTION_POLICY_TAG_WWWPT);

// Then set new policies
WINHTTP_CONNECTION_POLICY_ENTRY entry = {};
entry.pwszHost = L"*.contoso.com";
entry.pwszAppId = L"*";

PCWSTR connectionName = L"Contoso Cellular";
entry.nConnections = 1;
entry.ppwszConnections = &connectionName;

WINHTTP_CONNECTION_POLICY_ENTRY_LIST list = {};
list.pPolicyEntries = &entry;
list.nEntries = 1;

WinHttpConnectionSetPolicyEntries(
    hSession,
    TAG_WINHTTP_CONNECTION_POLICY_TAG_WWWPT,
    &list);
```

## Requirements

| Requirement | Value |
|---|---|
| Header | N/A |
| Library | winhttp.lib |
| DLL | winhttp.dll |

## See also

- [WinHttpConnectionDeletePolicyEntries](winhttpconnectiondeletepolicyentries.md)
- [WinHttpConnectionUpdateIfIndexTable](winhttpconnectionupdateifindextable.md)
- [WinHttpOpen](/windows/win32/api/winhttp/nf-winhttp-winhttpopen)
