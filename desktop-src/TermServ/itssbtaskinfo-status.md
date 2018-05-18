---
title: ITsSbTaskInfo Status property
description: Retrieves an RDV\_TASK\_STATUS enumeration value that represents the state of the task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '779af127-133c-47ff-8fca-bfd2c96c9768'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["Status property Remote Desktop Services", "Status property Remote Desktop Services , ITsSbTaskInfo interface", "ITsSbTaskInfo interface Remote Desktop Services , Status property"]
topic_type:
- apiref
api_name:
- ITsSbTaskInfo.Status
- ITsSbTaskInfo.get_Status
api_location:
- Sbtsv.idl
api_type:
- COM
---

# ITsSbTaskInfo::Status property

Retrieves an [**RDV\_TASK\_STATUS**](rdv-task-status.md) enumeration value that represents the state of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_Status(
  [out, retval] RDV_TASK_STATUS *pStatus
);
```



## Property value

An [**RDV\_TASK\_STATUS**](rdv-task-status.md) enumeration value that represents the state of the task.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbTaskInfo**](itssbtaskinfo.md)
</dt> </dl>

 

 





