---
description: Compares two access tokens and determines whether they are equivalent with respect to a call to the AccessCheck function.
ms.assetid: 3a07ddc6-9748-4f96-a597-2af6b4282e56
title: NtCompareTokens function (Ntseapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtCompareTokens
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtCompareTokens function

The **NtCompareTokens** function compares two [*access tokens*](/windows/desktop/SecGloss/a-gly) and determines whether they are equivalent with respect to a call to the [**AccessCheck**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-accesscheck) function.

## Syntax


```C++
NTSTATUS NTAPI NtCompareTokens(
  _In_  HANDLE   FirstTokenHandle,
  _In_  HANDLE   SecondTokenHandle,
  _Out_ PBOOLEAN Equal
);
```



## Parameters

<dl> <dt>

*FirstTokenHandle* \[in\]
</dt> <dd>

A handle to the first access token to compare. The token must be open for **TOKEN\_QUERY** access.

</dd> <dt>

*SecondTokenHandle* \[in\]
</dt> <dd>

A handle to the second access token to compare. The token must be open for **TOKEN\_QUERY** access.

</dd> <dt>

*Equal* \[out\]
</dt> <dd>

A pointer to a variable that receives a value that indicates whether the tokens represented by the *FirstTokenHandle* and *SecondTokenHandle* parameters are equivalent.

</dd> </dl>

## Return value

If the function succeeds, the function returns STATUS\_SUCCESS.

If the function fails, it returns an **NTSTATUS** error code.

## Remarks

Two access control tokens are considered to be equivalent if all of the following conditions are true:

-   Every [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) that is present in either token is also present in the other token.
-   Neither or both of the tokens are restricted.
-   If both tokens are restricted, every SID that is restricted in one token is also restricted in the other token.
-   Every privilege present in either token is also present in the other token.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Ntseapi.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl> |



 

