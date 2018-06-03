---
title: MWINDOWPROPERTY enumeration
description: Do not use. Used to turn on or off the conversation window sidebar and toolbar.
ms.assetid: 2905456c-cd7f-4635-bcc9-aa8e2028940f
keywords:
- MWINDOWPROPERTY enumeration Windows Messenger
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

# MWINDOWPROPERTY enumeration

\[**MWINDOWPROPERTY** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Used to turn on or off the conversation window sidebar and toolbar.

## Syntax


```C++
typedef enum  { 
  MWINDOWPROP_INVALID_PROPERTY  = -1,
  MWINDOWPROP_VIEW_SIDEBAR,
  MWINDOWPROP_VIEW_TOOLBAR      = 1
} LockError;
```



## Constants

<dl> <dt>

<span id="MWINDOWPROP_INVALID_PROPERTY"></span><span id="mwindowprop_invalid_property"></span>**MWINDOWPROP\_INVALID\_PROPERTY**
</dt> <dd>

Not a valid property.

</dd> <dt>

<span id="MWINDOWPROP_VIEW_SIDEBAR"></span><span id="mwindowprop_view_sidebar"></span>**MWINDOWPROP\_VIEW\_SIDEBAR**
</dt> <dd>

Used for retrieving and adding or removing the conversation window sidebar.

</dd> <dt>

<span id="MWINDOWPROP_VIEW_TOOLBAR"></span><span id="mwindowprop_view_toolbar"></span>**MWINDOWPROP\_VIEW\_TOOLBAR**
</dt> <dd>

Used for retrieving and adding or removing the conversation window toolbar.

</dd> </dl>

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





