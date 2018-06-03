---
title: MCONTACTPROPERTY enumeration
description: Do not use. Used to ask for the property that indicates which groups a user belongs to, or the contact's e-mail address.
ms.assetid: 2711e95b-d73c-41c8-870d-99f0ca48f05a
keywords:
- MCONTACTPROPERTY enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrua.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MCONTACTPROPERTY enumeration

\[**MCONTACTPROPERTY** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Used to ask for the property that indicates which groups a user belongs to, or the contact's e-mail address.

## Syntax


```C++
typedef enum  { 
  MCONTACTPROP_INVALID_PROPERTY  = -1,
  MCONTACTPROP_GROUPS_PROPERTY,
  MCONTACTPROP_EMAIL             = 1
} LockError;
```



## Constants

<dl> <dt>

<span id="MCONTACTPROP_INVALID_PROPERTY"></span><span id="mcontactprop_invalid_property"></span>**MCONTACTPROP\_INVALID\_PROPERTY**
</dt> <dd>

Not a valid property.

</dd> <dt>

<span id="MCONTACTPROP_GROUPS_PROPERTY"></span><span id="mcontactprop_groups_property"></span>**MCONTACTPROP\_GROUPS\_PROPERTY**
</dt> <dd>

Used to ask for the property that indicates which groups a user belongs to.

</dd> <dt>

<span id="MCONTACTPROP_EMAIL"></span><span id="mcontactprop_email"></span>**MCONTACTPROP\_EMAIL**
</dt> <dd>

Used to ask for the property that indicates the contact's e-mail address.

</dd> </dl>

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





