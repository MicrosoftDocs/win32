---
title: MPHONE\_TYPE enumeration
description: Do not use. Specifies which phone number of a given contact is used.
ms.assetid: c43925f7-1c43-43f2-860f-b41773bae378
keywords:
- MPHONE_TYPE enumeration Windows Messenger
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

# MPHONE\_TYPE enumeration

\[**MPHONE\_TYPE** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Specifies which phone number of a given contact is used.

## Syntax


```C++
typedef enum  { 
  MPHONE_TYPE_ALL     = -1,
  MPHONE_TYPE_HOME,
  MPHONE_TYPE_WORK    = 1,
  MPHONE_TYPE_MOBILE  = 2,
  MPHONE_TYPE_CUSTOM  = 3
} LockError;
```



## Constants

<dl> <dt>

<span id="MPHONE_TYPE_ALL"></span><span id="mphone_type_all"></span>**MPHONE\_TYPE\_ALL**
</dt> <dd>

Valid with [**Phone**](im-imessenger-phone.md) method only.

</dd> <dt>

<span id="MPHONE_TYPE_HOME"></span><span id="mphone_type_home"></span>**MPHONE\_TYPE\_HOME**
</dt> <dd>

Use home phone number.

</dd> <dt>

<span id="MPHONE_TYPE_WORK"></span><span id="mphone_type_work"></span>**MPHONE\_TYPE\_WORK**
</dt> <dd>

Use work phone number.

</dd> <dt>

<span id="MPHONE_TYPE_MOBILE"></span><span id="mphone_type_mobile"></span>**MPHONE\_TYPE\_MOBILE**
</dt> <dd>

Use mobile phone number.

</dd> <dt>

<span id="MPHONE_TYPE_CUSTOM"></span><span id="mphone_type_custom"></span>**MPHONE\_TYPE\_CUSTOM**
</dt> <dd>

Valid with [**Phone**](im-imessenger-phone.md) method only. Specifies that the contact information should be ignored and that the phone number specified in the method call should be used.

</dd> </dl>

## Remarks

This constant is used as an index for APIs that get or set phone number information stored in the properties of a contact or current client user.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





