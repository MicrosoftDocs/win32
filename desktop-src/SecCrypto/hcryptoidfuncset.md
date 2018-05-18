---
Description: 'Represents a handle to a set of object identifier (OID) installable functions.'
ms.assetid: '83b76466-dc55-4269-91a3-17c2e6102126'
title: HCRYPTOIDFUNCSET
---

# HCRYPTOIDFUNCSET

The **HCRYPTOIDFUNCSET** data type represents a handle to a set of [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) installable functions. The [**CryptGetDefaultOIDFunctionAddress**](cryptgetdefaultoidfunctionaddress.md), [**CryptGetOIDFunctionAddress**](cryptgetoidfunctionaddress.md), [**CryptFreeOIDFunctionAddress**](cryptfreeoidfunctionaddress.md), and [**CryptInitOIDFunctionSet**](cryptinitoidfunctionset.md) functions use this data type.


```C++
typedef void* HCRYPTOIDFUNCSET;
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 




