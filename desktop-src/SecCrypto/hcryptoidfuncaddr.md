---
Description: Represents a handle to an object identifier (OID) installable function.
ms.assetid: 06492b94-9717-40e0-be96-f97f42ac34af
title: HCRYPTOIDFUNCADDR
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HCRYPTOIDFUNCADDR

The **HCRYPTOIDFUNCADDR** data type represents a handle to an [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) installable function. The [**CryptGetDefaultOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetdefaultoidfunctionaddress?branch=master), [**CryptGetOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetoidfunctionaddress?branch=master), and [**CryptFreeOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptfreeoidfunctionaddress?branch=master) functions, and the [**CERT\_STORE\_PROV\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cert_store_prov_info?branch=master) structure use this data type.


```C++
typedef void* HCRYPTOIDFUNCADDR;
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 




