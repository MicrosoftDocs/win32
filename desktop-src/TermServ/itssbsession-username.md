---
title: ITsSbSession Username property
description: Retrieves the user name for this session.
ms.assetid: 0034e8cc-b67b-4e30-a059-47a269bab0fd
ms.tgt_platform: multiple
keywords:
- Username property Remote Desktop Services
- Username property Remote Desktop Services , ITsSbSession interface
- ITsSbSession interface Remote Desktop Services , Username property
topic_type:
- apiref
api_name:
- ITsSbSession.Username
- ITsSbSession.get_Username
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbSession::Username property

Retrieves the user name for this session.

This property is read-only.

## Syntax


```C++
HRESULT get_Username(
  [out, retval] BSTR *userName
);
```



## Property value

A pointer to a **BSTR** variable that receives the user name for this session.

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

 

 





