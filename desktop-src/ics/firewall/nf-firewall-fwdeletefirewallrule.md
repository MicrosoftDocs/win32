---
title: FWDeleteFirewallRule
description: Requests the server to delete the specified firewall rule in the policy contained in the specified policy store.
ms.topic: reference
ms.date: 11/12/2025
req.lib: 
req.dll: FirewallAPI.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- FirewallAPI.dll
api_name:
- FWDeleteFirewallRule
targetos: Windows
ms.localizationpriority: low
---

# FWDeleteFirewallRule function

Requests the server to delete the specified firewall rule in the policy contained in the specified policy store.

See **Remarks** for info about how to call the function.

## Syntax

```cpp
DWORD WINAPI FWDeleteFirewallRule(
  FW_POLICY_STORE_HANDLE hPolicyStore,
  PCWSTR                 wszRuleID
);
```

## Parameters

`hPolicyStore`

An opened policy store **HANDLE** that was successfully opened by using the [FWOpenPolicyStore](./nf-firewall-fwopenpolicystore.md) function. The handle must have read/write access rights.

`wszRuleID`

A pointer to a string that is the ID of the firewall rule the client wants to delete from the specified store.

## Return value

0 if successful. If it fails, it returns a nonzero error code, as specified in [MS-ERREF](/openspecs/windows_protocols/ms-erref/1bc92ddf-b79e-413c-bbaa-99a5281a6c90).

## Remarks

This function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`FirewallAPI.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11, version 23H2 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | FirewallAPI.dll |
