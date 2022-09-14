---
title: ITsSbSession TargetName property
description: Retrieves the name of the target on which this session was created.
ms.assetid: 5ab4cdd6-9f5f-4253-9b80-6cc35cff8b79
ms.tgt_platform: multiple
keywords:
- TargetName property Remote Desktop Services
- TargetName property Remote Desktop Services , ITsSbSession interface
- ITsSbSession interface Remote Desktop Services , TargetName property
topic_type:
- apiref
api_name:
- ITsSbSession.TargetName
- ITsSbSession.get_TargetName
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbSession::TargetName property

Retrieves the name of the target on which this session was created.

This property is read-only.

## Syntax


```C++
HRESULT get_TargetName(
  [out, retval] BSTR *targetName
);
```



## Property value

A pointer to a **BSTR** variable that receives the name of the target on which this session was created.

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

 

 





