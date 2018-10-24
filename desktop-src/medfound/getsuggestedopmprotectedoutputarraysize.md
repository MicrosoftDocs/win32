---
Description: Gets the size of the array that should be allocated before calling CreateOPMProtectedOutputs.
ms.assetid: 65edce14-f225-4b7f-b953-32b085e1cabf
title: GetSuggestedOPMProtectedOutputArraySize function
ms.author: windowssdkdev
ms.topic: article
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

> \[!Important\]  
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

A pointer to a [**UNICODE\_STRING**](https://msdn.microsoft.com/en-us/library/Aa380518(v=VS.85).aspx) structure that contains the name of the display device, as returned by the [**GetMonitorInfo**](https://msdn.microsoft.com/en-us/library/Dd144901(v=VS.85).aspx) function.

</dd> <dt>

*pdwSuggestedOPMProtectedOutputArraySize* \[out\]
</dt> <dd>

Receives the size that should be allocated for the array, in number of array elements.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions to dynamically link to Gdi32.dll.

## Requirements



|                                     |                                                                                      |
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

 

 




