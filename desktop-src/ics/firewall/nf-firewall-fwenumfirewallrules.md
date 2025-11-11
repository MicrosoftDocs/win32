---
title: FWEnumFirewallRules
description: TBD
ms.topic: reference
ms.date: 11/11/2025
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
- FWEnumFirewallRules
targetos: Windows
ms.localizationpriority: low
---

# FWEnumFirewallRules function

TBD

See **Remarks** for info about how to call the function.

## Syntax

```cpp
DWORD WINAPI FWEnumFirewallRules(
  FW_POLICY_STORE_HANDLE                         hPolicyStore,
  DWORD                                          dwFilteredByStatus,
  DWORD                                          dwProfileFilter,
  WORD                                           wFlags,
  __out  DWORD*                                  pdwNumRules,
  __deref_out_ecount_opt(*pdwNumRules) FW_RULE** ppRules
);
```

## Parameters

`hPolicyStore`

An opened policy store **HANDLE** that was successfully opened by using the [FWOpenPolicyStore](./nf-firewall-fwopenpolicystore.md) function. The handle must have read/write access rights.

`dwFilteredByStatus`

Bit-flags from **FW_RULE_STATUS_CLASS**.

`dwProfileFilter`

Bit-flags from **FW_PROFILE_TYPE**.

`wFlags`

Bit-flags from **FW_ENUM_RULES_FLAGS**.

`pdwNumRules`

TBD

`ppRules`

TBD

## Return value

TBD

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
