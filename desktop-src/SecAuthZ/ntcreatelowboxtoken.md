---
description: Create a LowBox token object based on an existing access token.
ms.assetid: 37b14919-6bed-41dc-a9e7-bfa1ba44c6ff
title: NtCreateLowBoxToken function (Ntseapi.h)
ms.topic: reference
ms.date: 02/21/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtCreateLowBoxToken
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtCreateLowBoxToken function

The **NtCreateLowBoxToken** function creates a **LowBox ([AppContainer](/windows/win32/secauthz/appcontainer-isolation))** token object based on an existing [access token](/windows/win32/SecGloss/a-gly) and returns the handle opened for access to that token.

## Syntax

```C++
NTSTATUS NTAPI NtCreateLowBoxToken(
  _Out_ PHANDLE             TokenHandle,
  _In_  HANDLE              ExistingTokenHandle,
  _In_  ACCESS_MASK         DesiredAccess,
  _in_  POBJECT_ATTRIBUTES  ObjectAttributes,
  _in_  PSID                PackageSid,
  _in_  ULONG               CapabilityCount,
  _in_  PSID_AND_ATTRIBUTES Capabilities,
  _in_  ULONG               HandleCount,
  _in_  HANDLE*             Handles
);
```

## Parameters

`TokenHandle [out]`

Returns the handle of the newly created **LowBox** token.

`ExistingTokenHandle [in]`

The handle of the existing created token. The token must be open for **TOKEN\_QUERY** access.

`DesiredAccess [in]`

An [ACCESS_MASK](access-mask.md) indicating which access types the handle is to provide to the new object.

`ObjectAttributes [in, Optional]`

Points to the standard [OBJECT_ATTRIBUTES](/windows/win32/api/ntdef/ns-ntdef-_object_attributes) data structure.

`PackageSid [in]`

The _Package_ that this token will belong to. This must point to a valid [SID](/windows/win32/api/winnt/ns-winnt-sid) which must be a member of the LowBox Package SID group.

`CapabilityCount [in]`

The number of capabilities to include on the token.

`Capabilities [in, Optional]`

The [SID_AND_ATTRIBUTES](/windows/win32/api/winnt/ns-winnt-sid_and_attributes) structure containing the capability SIDs to include on the token.

`HandleCount [in]`

The number of handles to be included on the token.

`Handles [in, Optional]`

Handles to the named object directories for the AppContainer.

## Return value

If the function succeeds, the function returns **STATUS\_SUCCESS**.

If the function fails, it returns an **NTSTATUS** error code. See [NTSTATUS values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55) for a list of error codes and their values.

## Remarks

This API can only be called by medium or higher IL process.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Windows 8 \[desktop apps only\] |
| Minimum supported server | Windows Server 2012 \[desktop apps only\] |
| DLL | Ntdll.dll |

## See also

[NtCompareTokens](ntcomparetokens.md)
