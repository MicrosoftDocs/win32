---
description: Updates the WinHTTP internal mapping table that associates named network connections with their active network interface indices.
title: WinHttpConnectionUpdateIfIndexTable function
ms.topic: reference
ms.date: 05/27/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WinHttpConnectionUpdateIfIndexTable
api_type: 
- DllExport
api_location: 
- winhttp.dll
---

# WinHttpConnectionUpdateIfIndexTable function

Updates the WinHTTP internal mapping table that associates named network connections with their active network interface indices. This enables WinHTTP to route HTTP requests through the correct network interface based on connection-aware policy decisions.

## Syntax

```cpp
DWORD WINAPI WinHttpConnectionUpdateIfIndexTable(
    _In_ HINTERNET                          hSession,
    _In_ WINHTTP_CONNECTION_IFINDEX_LIST   *pConnectionIfIndexEntries
);
```

## Parameters

### hSession [in]

A valid WinHTTP session handle created by [**WinHttpOpen**](/windows/win32/api/winhttp/nf-winhttp-winhttpopen). The handle must be a session-level handle.

### pConnectionIfIndexEntries [in]

Pointer to a **WINHTTP_CONNECTION_IFINDEX_LIST** structure containing an array of connection-to-interface-index mappings.

The **WINHTTP_CONNECTION_IFINDEX_LIST** structure contains:

- **nEntries** — Number of entries in the array. Can be 0 to clear the table.
- **pConnectionIfIndexEntries** — Array of **WINHTTP_CONNECTION_IFINDEX_ENTRY** structures, each containing:
  - **pwszConnectionName** — Name of the connection (for example, "Cellular").
  - **dwIfIndex** — Active network interface index (**IF_INDEX**).

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

This function communicates with the WinHTTP Auto-Proxy Service to update the connection-to-interface mapping table.

The table enables WinHTTP to bind HTTP connections to specific network interfaces, which is critical for multi-homed devices (for example, devices with both Wi-Fi and cellular connections active simultaneously).

Typically called by system networking components, like Windows Connection Manager, whenever connection states change (connect/disconnect events) to keep WinHTTP's routing table synchronized with the current network state.

Passing an empty list (**nEntries** = 0, **pConnectionIfIndexEntries** = **nullptr**) effectively clears all connection-interface mappings.

### Example

The following example updates the interface index table with mappings for both a Wi-Fi and a cellular connection.

```cpp
WINHTTP_CONNECTION_IFINDEX_ENTRY entries[2] = {};
entries[0].pwszConnectionName = L"Wi-Fi";
entries[0].dwIfIndex = 4;
entries[1].pwszConnectionName = L"Cellular";
entries[1].dwIfIndex = 7;

WINHTTP_CONNECTION_IFINDEX_LIST ifList = {};
ifList.pConnectionIfIndexEntries = entries;
ifList.nEntries = 2;

WinHttpConnectionUpdateIfIndexTable(hSession, &ifList);
```

## Requirements

| Requirement | Value |
|---|---|
| Header | N/A |
| Library | winhttp.lib |
| DLL | winhttp.dll |

## See also

- [WinHttpConnectionSetPolicyEntries](winhttpconnectionsetpolicyentries.md)
- [WinHttpOpen](/windows/win32/api/winhttp/nf-winhttp-winhttpopen)
