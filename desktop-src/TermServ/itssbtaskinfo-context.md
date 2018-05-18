---
title: ITsSbTaskInfo Context property
description: Retrieves the context bytes associated with the task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ce55ce2a-957f-4b50-b632-42079277102b'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["Context property Remote Desktop Services", "Context property Remote Desktop Services , ITsSbTaskInfo interface", "ITsSbTaskInfo interface Remote Desktop Services , Context property"]
topic_type:
- apiref
api_name:
- ITsSbTaskInfo.Context
- ITsSbTaskInfo.get_Context
api_location:
- Sbtsv.idl
api_type:
- COM
---

# ITsSbTaskInfo::Context property

Retrieves the context bytes associated with the task.

This property is read-only.

## Syntax


```C++
HRESULT get_Context(
  [out, retval] SAFEARRAY(BYTE) *pContext
);
```



## Property value

The context of the task.

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

 

 





