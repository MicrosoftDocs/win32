---
Description: Is used as a handle to a CryptoAPI cryptographic service provider (CSP) or CNG CSP.
ms.assetid: 1ad77adb-5960-4965-bddb-5967b982b034
title: HCRYPTPROV\_OR\_NCRYPT\_KEY\_HANDLE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HCRYPTPROV\_OR\_NCRYPT\_KEY\_HANDLE

The **HCRYPTPROV\_OR\_NCRYPT\_KEY\_HANDLE** data type is used as a handle to a CryptoAPI [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) or CNG CSP. This handle must be an [**HCRYPTPROV**](hcryptprov.md) handle that has been created by using the [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) function or an **NCRYPT\_KEY\_HANDLE** handle that has been created by using the [**NCryptOpenKey**](https://msdn.microsoft.com/581c5d89-730d-4d8c-b3bb-a28edec25910) function. New applications should always pass in the **NCRYPT\_KEY\_HANDLE** handle to a CNG CSP.


```C++
typedef ULONG_PTR HCRYPTPROV_OR_NCRYPT_KEY_HANDLE;
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 




