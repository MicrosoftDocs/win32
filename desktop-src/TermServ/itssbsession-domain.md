---
title: ITsSbSession Domain property
description: Retrieves the domain name of the user.
ms.assetid: bbb9a805-7270-4555-8fee-130a46bc3903
ms.tgt_platform: multiple
keywords:
- Domain property Remote Desktop Services
- Domain property Remote Desktop Services , ITsSbSession interface
- ITsSbSession interface Remote Desktop Services , Domain property
topic_type:
- apiref
api_name:
- ITsSbSession.Domain
- ITsSbSession.get_Domain
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbSession::Domain property

Retrieves the domain name of the user.

This property is read-only.

## Syntax


```C++
HRESULT get_Domain(
  [out, retval] BSTR *domain
);
```



## Property value

A pointer to a **BSTR** variable that receives the domain name of the user.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbSession**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbsession)
</dt> </dl>

 

 





