---
title: IMSGPRIORITY enumeration
description: Do not use. Represents the priority of a message.
ms.assetid: '65fc1b25-e366-4a37-b2f3-fbfe7069642b'
keywords: ["IMSGPRIORITY enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# IMSGPRIORITY enumeration

Do not use. Represents the priority of a message.

## Syntax


```C++
typedef enum tagIMSGPRIORITY { 
  IMSG_PRI_LOW     = 5,
  IMSG_PRI_NORMAL  = 3,
  IMSG_PRI_HIGH    = 1
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IMSG_PRI_LOW"></span><span id="imsg_pri_low"></span>**IMSG\_PRI\_LOW**
</dt> <dd>

Indicates that the message is low priority.

</dd> <dt>

<span id="IMSG_PRI_NORMAL"></span><span id="imsg_pri_normal"></span>**IMSG\_PRI\_NORMAL**
</dt> <dd>

Indicates that the message is normal priority.

</dd> <dt>

<span id="IMSG_PRI_HIGH"></span><span id="imsg_pri_high"></span>**IMSG\_PRI\_HIGH**
</dt> <dd>

Indicates that the message is high priority.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





