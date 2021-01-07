---
description: Frees a SIGNER\_CONTEXT structure allocated by a previous call to the SignerSignEx function.
ms.assetid: 190de302-50fe-488e-90ed-c9efd39dae70
title: SignerFreeSignerContext function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignerFreeSignerContext
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# SignerFreeSignerContext function

The **SignerFreeSignerContext** function frees a [**SIGNER\_CONTEXT**](signer-context.md) structure allocated by a previous call to the [**SignerSignEx**](signersignex.md) function.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
HRESULT WINAPI SignerFreeSignerContext(
  _In_ SIGNER_CONTEXT *pSignerContext
);
```



## Parameters

<dl> <dt>

*pSignerContext* \[in\]
</dt> <dd>

A pointer to the [**SIGNER\_CONTEXT**](signer-context.md) structure to free.

</dd> </dl>

## Return value

If the function succeeds, the function returns S\_OK.

If the function fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



## See also

<dl> <dt>

[**SIGNER\_CONTEXT**](signer-context.md)
</dt> <dt>

[**SignerSignEx**](signersignex.md)
</dt> </dl>

 

 
