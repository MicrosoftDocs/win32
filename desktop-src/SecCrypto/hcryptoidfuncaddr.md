---
Description: 'Represents a handle to an object identifier (OID) installable function.'
ms.assetid: '06492b94-9717-40e0-be96-f97f42ac34af'
title: HCRYPTOIDFUNCADDR
---

# HCRYPTOIDFUNCADDR

The **HCRYPTOIDFUNCADDR** data type represents a handle to an [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) installable function. The [**CryptGetDefaultOIDFunctionAddress**](cryptgetdefaultoidfunctionaddress.md), [**CryptGetOIDFunctionAddress**](cryptgetoidfunctionaddress.md), and [**CryptFreeOIDFunctionAddress**](cryptfreeoidfunctionaddress.md) functions, and the [**CERT\_STORE\_PROV\_INFO**](cert-store-prov-info.md) structure use this data type.


```C++
typedef void* HCRYPTOIDFUNCADDR;
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 




