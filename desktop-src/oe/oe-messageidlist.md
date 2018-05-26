---
title: MESSAGEIDLIST structure
description: Do not use. Specifies a list of messages.
ms.assetid: b9e9cbc3-5860-4475-a5f5-3942a5db91a2
keywords:
- MESSAGEIDLIST structure Windows Mail (formerly Outlook Express)
- LPMESSAGEIDLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MESSAGEIDLIST
api_location:
- Msoeapi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MESSAGEIDLIST structure

Do not use. Specifies a list of messages.

## Syntax


```C++
typedef struct tagMESSAGEIDLIST {
  DWORD       cbSize;
  DWORD       cMsgs;
  LPMESSAGEID prgdwMsgId;
} MESSAGEIDLIST, *LPMESSAGEIDLIST;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of the structure in bytes.

</dd> <dt>

**cMsgs**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Count of messages in the array specified by **prgdwMsgId**.

</dd> <dt>

**prgdwMsgId**
</dt> <dd>

Type: **LPMESSAGEID**

</dd> <dd>

Array of message ID values.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl> |



 

 





