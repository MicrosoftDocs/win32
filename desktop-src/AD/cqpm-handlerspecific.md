---
title: CQPM_HANDLERSPECIFIC message (Cmnquery.h)
description: Base value used for messages that are private to the query handler.
ms.assetid: c3badb89-ee4e-4317-97aa-15187b9bb3e8
ms.tgt_platform: multiple
keywords:
- CQPM_HANDLERSPECIFIC message Active Directory
topic_type:
- apiref
api_name:
- CQPM_HANDLERSPECIFIC
api_location:
- Cmnquery.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CQPM\_HANDLERSPECIFIC message

The **CQPM\_HANDLERSPECIFIC** message is the base value used for messages that are private to the query handler. The query handler should add this value to private messages to ensure that message collisions do not occur.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains additional message data. The content of this parameter is defined by the query handler.

</dd> <dt>

*lParam* 
</dt> <dd>

Contains additional message data. The content of this parameter is defined by the query handler.

</dd> </dl>

## Return value

The meaning of the return value is defined by the query handler.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cmnquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc)
</dt> </dl>

 

 





