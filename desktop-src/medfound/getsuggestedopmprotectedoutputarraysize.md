---
description: Gets the size of the array that should be allocated before calling CreateOPMProtectedOutputs.
ms.assetid: 65edce14-f225-4b7f-b953-32b085e1cabf
title: GetSuggestedOPMProtectedOutputArraySize function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetSuggestedOPMProtectedOutputArraySize
api_type: 
- DllExport
api_location: 
- gdi32.dll
---

# GetSuggestedOPMProtectedOutputArraySize function

> [!IMPORTANT]
> This function is used by [Output Protection Manager](output-protection-manager.md) (OPM) to access functionality in the display driver. Applications should not call this function.

 

Gets the size of the array that should be allocated before calling [**CreateOPMProtectedOutputs**](createopmprotectedoutputs.md).

## Syntax


```C++
NTSTATUS WINAPI GetSuggestedOPMProtectedOutputArraySize(
  _In_  PUNICODE_STRING pstrDeviceName,
  _Out_ DWORD           *pdwSuggestedOPMProtectedOutputArraySize
);
```



## Parameters

<dl> <dt>

*pstrDeviceName* \[in\]
</dt> <dd>

A pointer to a [**UNICODE\_STRING**](/windows/win32/api/subauth/ns-subauth-unicode_string) structure that contains the name of the display device, as returned by the [**GetMonitorInfo**](/windows/win32/api/winuser/nf-winuser-getmonitorinfoa) function.

</dd> <dt>

*pdwSuggestedOPMProtectedOutputArraySize* \[out\]
</dt> <dd>

Receives the size that should be allocated for the array, in number of array elements.

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

 

 
