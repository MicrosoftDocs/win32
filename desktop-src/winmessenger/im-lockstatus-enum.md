---
title: LockStatus enumeration
description: Do not use. Provides the list of possible status codes for the Messenger Lock and Key API.
ms.assetid: f31ddee9-3812-46b4-b844-582734e20337
keywords:
- LockStatus enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrpriv.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LockStatus enumeration

\[**LockStatus** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Provides the list of possible status codes for the Messenger Lock and Key API.

## Syntax


```C++
typedef enum  { 
  LOCK_NOTINITIALIZED  = 0x00000001,
  LOCK_INITIALIZED     = 0x00000002,
  LOCK_PENDINGRESULT   = 0x00000003,
  LOCK_UNLOCKED        = 0x00000004,
  LOCK_UNLOCKFAILED    = 0x00000005,
  LOCK_DISABLED        = 0x00000006
} LockError;
```



## Constants

<dl> <dt>

<span id="LOCK_NOTINITIALIZED"></span><span id="lock_notinitialized"></span>**LOCK\_NOTINITIALIZED**
</dt> <dd>

The Messenger client Lock and Key mechanism is not initialized.

</dd> <dt>

<span id="LOCK_INITIALIZED"></span><span id="lock_initialized"></span>**LOCK\_INITIALIZED**
</dt> <dd>

The Messenger service  API is locked.

</dd> <dt>

<span id="LOCK_PENDINGRESULT"></span><span id="lock_pendingresult"></span>**LOCK\_PENDINGRESULT**
</dt> <dd>

The application has successfully initiated a challenge request to the Messenger client and the Messenger client is awaiting the application response to its authentication challenge.

</dd> <dt>

<span id="LOCK_UNLOCKED"></span><span id="lock_unlocked"></span>**LOCK\_UNLOCKED**
</dt> <dd>

The Messenger service  API is unlocked.

</dd> <dt>

<span id="LOCK_UNLOCKFAILED"></span><span id="lock_unlockfailed"></span>**LOCK\_UNLOCKFAILED**
</dt> <dd>

The application response to the Messenger client authentication challenge failed.

</dd> <dt>

<span id="LOCK_DISABLED"></span><span id="lock_disabled"></span>**LOCK\_DISABLED**
</dt> <dd>

The Messenger client Lock and Key mechanism is disabled.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |



## See also

<dl> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





