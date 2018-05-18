---
title: MLIST enumeration
description: Do not use.
ms.assetid: '91361c98-08e9-429e-b2c0-04e400af304d'
keywords: ["MLIST enumeration Windows Messenger", "LockError enumeration Windows Messenger"]
topic_type:
- apiref
api_name:
- LockError
api_location:
- Mdisp.h
api_type:
- HeaderDef
---

# MLIST enumeration

\[**MLIST** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Used to retrieve information about contact lists.

> [!Note]  
> The **MLIST** enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.

 

## Syntax


```C++
typedef enum  { 
  MLIST_CONTACT,
  MLIST_ALLOW    = 1,
  MLIST_BLOCK    = 2,
  MLIST_REVERSE  = 3
} LockError;
```



## Constants

<dl> <dt>

<span id="MLIST_CONTACT"></span><span id="mlist_contact"></span>**MLIST\_CONTACT**
</dt> <dd>

Returns the collection of contacts in a contact list.

</dd> <dt>

<span id="MLIST_ALLOW"></span><span id="mlist_allow"></span>**MLIST\_ALLOW**
</dt> <dd>

Returns the collection of contacts that are allowed to send messages and see the user's presence information.

</dd> <dt>

<span id="MLIST_BLOCK"></span><span id="mlist_block"></span>**MLIST\_BLOCK**
</dt> <dd>

Returns the collection of contacts that are not allowed to send messages and see the user's presence information.

</dd> <dt>

<span id="MLIST_REVERSE"></span><span id="mlist_reverse"></span>**MLIST\_REVERSE**
</dt> <dd>

Returns the collection of contacts that have added the user to their contact list.

</dd> </dl>

## Requirements



|                                  |                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                |
| End of server support<br/> | Windows Server 2003<br/>                                                       |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl> |



 

 





