---
description: Represents a handle to an object identifier (OID) installable function.
ms.assetid: 06492b94-9717-40e0-be96-f97f42ac34af
title: HCRYPTOIDFUNCADDR (Wincrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# HCRYPTOIDFUNCADDR

The **HCRYPTOIDFUNCADDR** data type represents a handle to an [*object identifier*](../secgloss/o-gly.md) (OID) installable function. The [**CryptGetDefaultOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetdefaultoidfunctionaddress), [**CryptGetOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetoidfunctionaddress), and [**CryptFreeOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfreeoidfunctionaddress) functions, and the [**CERT\_STORE\_PROV\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_store_prov_info) structure use this data type.


```C++
typedef void* HCRYPTOIDFUNCADDR;
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 
