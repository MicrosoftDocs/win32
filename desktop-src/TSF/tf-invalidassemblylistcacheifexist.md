---
title: TF_InvalidAssemblyListCacheIfExist function
description: The TF\_InvalidAssemblyListCacheIfExist function invalidates the text input processor's description cache.
ms.assetid: a0f61b25-598c-417c-8679-7523c041f9ef
keywords:
- TF_InvalidAssemblyListCacheIfExist function Text Services Framework
topic_type:
- apiref
api_name:
- TF_InvalidAssemblyListCacheIfExist
api_location:
- msctf.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_InvalidAssemblyListCacheIfExist function

The **TF\_InvalidAssemblyListCacheIfExist** function invalidates the text input processor's description cache. It is not necessary to call this function if the input processor setup program requires you to restart or log on. The cache is valid until the user logs off.

## Syntax


```C++
HRESULT TF_InvalidAssemblyListCacheIfExist(void);
```



## Parameters

This function has no parameters.

## Return value

This function can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The function was successful.<br/>   |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Examples

There is no import library available that defines this function, so it is necessary to obtain a pointer to this function using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress). The following example demonstrates how to obtain a pointer to this function.

> [!Note]  
> Using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) incorrectly can compromise the security of your application by loading the wrong DLL. Refer to [Dynamic-Link Library Search Order](/windows/desktop/Dlls/dynamic-link-library-search-order) for information on how to correctly load DLLs with different versions of Microsoft Windows.

 


```C++
typedef HRESULT (WINAPI *pTF_InvalidAssemblyListCacheIfExist )(void);

HMODULE hMSCTF = LoadLibrary(TEXT("msctf.dll"));

if(hMSCTF == NULL)
{
    //Error loading module -- fail as securely as possible 
}

else
{
    pTF_InvalidAssemblyListCacheIfExist pfnInvalidAssemblyListCacheIfExist;
    
    pfnInvalidAssemblyListCacheIfExist = (pTF_InvalidAssemblyListCacheIfExist )GetProcAddress(hMSCTF, "TF_InvalidAssemblyListCacheIfExist");

    if(pfnInvalidAssemblyListCacheIfExist)
    {
        (*pfnInvalidAssemblyListCacheIfExist)();
       
    }

    FreeLibrary(hMSCTF);
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| DLL<br/>                      | <dl> <dt>Msctf.dll</dt> </dl> |



 

