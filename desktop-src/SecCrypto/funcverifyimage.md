---
description: Used by a cryptographic service provider (CSP) to verify the signature of a DLL.
ms.assetid: 477a6c9f-05ac-485a-8b27-5605fc11c1d6
title: CRYPT_VERIFY_IMAGE function pointer (Cspdk.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRYPT_VERIFY_IMAGE
- CRYPT_VERIFY_IMAGE_A
- CRYPT_VERIFY_IMAGE_W
api_type: 
- UserDefined
api_location: 
- Cspdk.h
---

# CRYPT\_VERIFY\_IMAGE function pointer

The **FuncVerifyImage** callback function is used by a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) to verify the signature of a DLL.

All auxiliary DLLs into which a CSP makes function calls must be signed in the same manner (and with the same key) as the primary CSP DLL. To ensure this signature, the auxiliary DLLs must be loaded dynamically by using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) function. But before the DLL is loaded, the signature of the DLL must be verified. The CSP performs this verification by calling the **FuncVerifyImage** function, as shown in the example below.

## Syntax


```C++
typedef BOOL ( WINAPI *CRYPT_VERIFY_IMAGE)(
  _In_       LPCTSTR lpszImage,
  _In_ const BYTE    *pbSigData
);
```



## Parameters

<dl> <dt>

*lpszImage* \[in\]
</dt> <dd>

The address of a null-terminated string that contains the path and file name of the DLL to verify the signature for.

</dd> <dt>

*pbSigData* \[in\]
</dt> <dd>

The address of a buffer that contains the signature.

</dd> </dl>

## Return value

Returns **TRUE** if the function succeeds, **FALSE** if it fails.

## Examples

The following example shows how to use the **FuncVerifyImage** callback function to verify the signature of a DLL before it is loaded by a CSP.


```C++
BOOL (FARPROC *ProvVerifyImage)(LPCSTR lpszImage, BYTE *pSigData);


//  "ProvVerifyImage" has been set to "pVTable->FuncVerifyImage"
//  within the CPAcquireContext function.

//  bSignature is a previously assigned BYTE array that contains the
//  signature that is stored in the C:\Winnt40\System32\signature.sig
//  file. During development, this file is created with the 
//  Sign.exe tool.
...


//  Verify the signature in the
//  C:\Winnt40\System32\Signature.dll file.
if(RCRYPT_FAILED(ProvVerifyImage
    ("c:\\winnt40\\system32\\signature.dll",
        bSignature)) {
    SetLastError(NTE_BAD_SIGNATURE);
    return CRYPT_FAILED;
}

//  Load the DLL with the LoadLibrary function, then acquire pointers 
//  to the functions with the GetProcAddress function.
//...
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Cspdk.h</dt> </dl> |



## See also

<dl> <dt>

[**CPAcquireContext**](https://www.bing.com/search?q=**CPAcquireContext**)
</dt> <dt>

[**VTableProvStruc**](vtableprovstruc.md)
</dt> </dl>

 

 
