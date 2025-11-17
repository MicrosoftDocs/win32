---
title: FWFreeFirewallRules
description: Requests the server to free rules previously retrieved from the FWEnumFirewallRules function.
ms.topic: reference
ms.date: 11/17/2025
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
- FWFreeFirewallRules
targetos: Windows
ms.localizationpriority: low
---

# FWFreeFirewallRules function

Requests the server to free rules previously retrieved from the [FWEnumFirewallRules](./nf-firewall-fwfreefirewallrules.md) function.

See **Remarks** for info about how to call the function.

## Syntax

```cpp
DWORD WINAPI FWFreeFirewallRules(
  FW_RULE* pRules
);
```

## Parameters

`pRule`

A pointer to the linked list of [FW_RULE](./ns-firewall-fw_rule.md) previously retrieved from the [FWEnumFirewallRules](./nf-firewall-fwfreefirewallrules.md) function.

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

## See also

* [Windows Firewall with Advanced Security enums and structs](../firewall-enums-structs.md)
