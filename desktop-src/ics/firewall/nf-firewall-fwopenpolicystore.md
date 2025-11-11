---
title: FWOpenPolicyStore
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
- FWOpenPolicyStore
targetos: Windows
ms.localizationpriority: low
---

# FWOpenPolicyStore function

TBD

See **Remarks** for info about how to call the function.

## Syntax

```cpp
DWORD WINAPI FWOpenPolicyStore(
  WORD                          wBinaryVersion,
  __in_opt PCWSTR               wszMachineOrGPO,
  FW_STORE_TYPE                 StoreType,
  FW_POLICY_ACCESS_RIGHT        AccessRight,
  DWORD                         dwFlags,
  __out FW_POLICY_STORE_HANDLE* phPolicyStore
);
```

## Parameters

`wBinaryVersion`

TBD

`wszMachineOrGPO`

The object to connect to. A machine name or a GPO path. **NULL** for local machine.

`StoreType`

TBD

`AccessRight`

TBD

`dwFlags`

TBD

`phPolicyStore`

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
