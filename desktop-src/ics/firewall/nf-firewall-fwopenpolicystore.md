---
title: FWOpenPolicyStore
description: Requests the server to open the specified policy store. The store can be opened for reading or for editing the firewall policy.
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
- FWOpenPolicyStore
targetos: Windows
ms.localizationpriority: low
---

# FWOpenPolicyStore function

Requests the server to open the specified policy store. The store can be opened for reading or for editing the firewall policy. Via this function, you also retrieve a handle to the opened store, with which you can then perform operations on the policy store. The server allocates a policy store connection object to track the policy store type and the binary version associated with the handle.

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

Specifies the RPC interface binary version. This implies versions of the methods and versions of the structures. This value must be a valid protocol version.

`wszMachineOrGPO`

The object to connect to. A machine name or a GPO path. **NULL** for local machine.

`StoreType`

The policy store type that the client wants to open.

`AccessRight`

The read or read/write access rights that the client is requesting on the store.

`dwFlags`

Not used. The server ignores this parameter; the client should pass a value of zero.

`phPolicyStore`

An output parameter that provides a pointer to an opened policy store **HANDLE**. If successful, this parameter contains a handle to the opened store.

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
