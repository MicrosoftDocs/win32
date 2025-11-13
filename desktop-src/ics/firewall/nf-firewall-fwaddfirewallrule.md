---
title: FWAddFirewallRule
description: Requests the server to add the specified firewall rule in the policy contained in the specified policy store.
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
- FWAddFirewallRule
targetos: Windows
ms.localizationpriority: low
---

# FWAddFirewallRule function

Requests the server to add the specified firewall rule in the policy contained in the specified policy store.

See **Remarks** for info about how to call the function.

## Syntax

```cpp
DWORD WINAPI FWAddFirewallRule(
  FW_POLICY_STORE_HANDLE hPolicyStore,
  FW_RULE*               pRule,
);
```

## Parameters

`hPolicyStore`

An opened policy store **HANDLE** that was successfully opened by using the [FWOpenPolicyStore](./nf-firewall-fwopenpolicystore.md) function. The handle must have read/write access rights.

`pRule`

A pointer to an [FW_RULE](./ns-firewall-fw_rule.md) containing The firewall rule that the client wants to add to the store. The rule must be a valid rule, as specified in the definition of the [FW_RULE2_27](/openspecs/windows_protocols/ms-fasp/a6175371-a526-4e65-a14e-1929fd60dcec) data type.

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
