---
title: ITsSbTaskInfo Identifier property
description: Retrieves a GUID that is used as a unique identifier by the task agent.
ms.assetid: 96b41588-d634-4cdd-aacc-0456b8e47c3b
ms.tgt_platform: multiple
keywords:
- Identifier property Remote Desktop Services
- Identifier property Remote Desktop Services , ITsSbTaskInfo interface
- ITsSbTaskInfo interface Remote Desktop Services , Identifier property
topic_type:
- apiref
api_name:
- ITsSbTaskInfo.Identifier
- ITsSbTaskInfo.get_Identifier
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbTaskInfo::Identifier property

Retrieves a GUID that is used as a unique identifier by the task agent.

This property is read-only.

## Syntax


```C++
HRESULT get_Identifier(
  [out, retval] BSTR *pIdentifier
);
```



## Property value

A pointer to a **BSTR** value that receives the GUID.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbTaskInfo**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtaskinfo)
</dt> </dl>

 

 





