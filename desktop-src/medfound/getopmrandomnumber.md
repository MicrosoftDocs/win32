---
description: Gets a 128-bit, cryptographically secure random number from a protected output object.
ms.assetid: d5adfa5c-ae61-43d5-916d-05085abea38b
title: GetOPMRandomNumber function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetOPMRandomNumber
api_type: 
- DllExport
api_location: 
- gdi32.dll
---

# GetOPMRandomNumber function

> [!IMPORTANT]
> This function is used by [Output Protection Manager](output-protection-manager.md) (OPM) to access functionality in the display driver. Applications should not call this function.

 

Gets a 128-bit, cryptographically secure random number from a protected output object.

## Syntax


```C++
NTSTATUS WINAPI GetOPMRandomNumber(
  _In_  OPM_PROTECTED_OUTPUT_HANDLE opoOPMProtectedOutput,
  _Out_ DXGKMDT_OPM_RANDOM_NUMBER   *prnRandomNumber
);
```



## Parameters

<dl> <dt>

*opoOPMProtectedOutput* \[in\]
</dt> <dd>

A handle to the protected output object. This handle is obtained by calling [**CreateOPMProtectedOutputs**](createopmprotectedoutputs.md).

</dd> <dt>

*prnRandomNumber* \[out\]
</dt> <dd>

A pointer to a **DXGKMDT\_OPM\_RANDOM\_NUMBER** structure that receives the random number.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Gdi32.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Gdi32.dll</dt> </dl> |



## See also

<dl> <dt>

[OPM Functions](opm-functions.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 
