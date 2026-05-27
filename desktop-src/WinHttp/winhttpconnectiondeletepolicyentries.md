---
description: Removes all connection routing policy entries associated with a specific policy tag from the WinHTTP Auto-Proxy Service.
title: WinHttpConnectionDeletePolicyEntries function
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WinHttpConnectionDeletePolicyEntries
api_type: 
- DllExport
api_location: 
- winhttp.dll
---

# WinHttpConnectionDeletePolicyEntries function

Removes all connection routing policy entries associated with a specific policy tag from the WinHTTP Auto-Proxy Service.

## Syntax

```cpp
DWORD WINAPI WinHttpConnectionDeletePolicyEntries(
    _In_ HINTERNET                      hSession,
    _In_ WINHTTP_CONNECTION_POLICY_TAG  PolicyEntryTag
);
```

## Parameters

### hSession [in]

A valid WinHTTP session handle created by [**WinHttpOpen**](/windows/win32/api/winhttp/nf-winhttp-winhttpopen). The handle must be a session-level handle.

### PolicyEntryTag [in]

Identifies which set of policy entries to remove. One of the following values.

| Value | Meaning |
|-------|---------|
| **TAG_WINHTTP_CONNECTION_POLICY_TAG_DEFAULT** (0) | Default/untagged policy entries. |
| **TAG_WINHTTP_CONNECTION_POLICY_TAG_CONNECTION_MANAGER** (1) | Entries managed by the system connection manager. |
| **TAG_WINHTTP_CONNECTION_POLICY_TAG_WWWPT** (2) | Entries managed by the WWWPT (Windows Web Platform Transport) component. |

## Return value

Returns **ERROR_SUCCESS** (0) on success. Returns a [system error code](/windows/win32/debug/system-error-codes) on failure, including the following.

| Value | Description |
|-------|-------------|
| **ERROR_WINHTTP_INCORRECT_HANDLE_TYPE** | *hSession* is not a session handle. |
| **ERROR_WINHTTP_NOT_INITIALIZED** | WinHTTP globals are not initialized. |
| **ERROR_ACCESS_DENIED** | Caller lacks required privileges. |

## Remarks

Removes all policy entries previously registered with the specified tag. Other tags' entries remain unaffected.

Typically called before [**WinHttpConnectionSetPolicyEntries**](winhttpconnectionsetpolicyentries.md) to ensure a clean slate when refreshing policy from the owning component.

This API requires elevated (administrator/SYSTEM) privileges.

## Requirements

| Requirement | Value |
|---|---|
| Header | winhttp.h, winhttp_conn_proxy.h |
| Library | winhttp.lib |
| DLL | winhttp.dll |

## See also

- [WinHttpConnectionSetPolicyEntries](winhttpconnectionsetpolicyentries.md)
- [WinHttpOpen](/windows/win32/api/winhttp/nf-winhttp-winhttpopen)
