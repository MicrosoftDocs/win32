---
title: REGISTERNOTIFYFLAGS enumeration
description: Do not use. Flags for registering notification.
ms.assetid: '90a6ee56-2db1-4201-8b52-a047190469b2'
keywords: ["REGISTERNOTIFYFLAGS enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# REGISTERNOTIFYFLAGS enumeration

Do not use. Flags for registering notification.

## Syntax


```C++
typedef enum  { 
  REGISTER_NOTIFY_NOADDREF       = 0x00000001,
  REGISTER_NOTIFY_ORDINALSONLY   = 0x00000002
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="REGISTER_NOTIFY_NOADDREF"></span><span id="register_notify_noaddref"></span>**REGISTER\_NOTIFY\_NOADDREF**
</dt> <dd>

Do not add ref to the notification object when registering notification.

</dd> <dt>

<span id="REGISTER_NOTIFY_ORDINALSONLY_"></span><span id="register_notify_ordinalsonly_"></span>**REGISTER\_NOTIFY\_ORDINALSONLY** 
</dt> <dd>

Only notify with the updated record index ordinals (as oppose to notify with the all the data members).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





