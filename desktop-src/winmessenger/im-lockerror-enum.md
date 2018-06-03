---
title: LockError enumeration
description: Do not use. Provides a list of Lock and Key error status codes.
ms.assetid: 1e18b522-11c9-4ab3-9e81-928affd323ea
keywords:
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrpriv.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# LockError enumeration

\[[**LockStatus**](im-lockstatus-enum.md) is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Provides a list of Lock and Key error status codes.

## Syntax


```C++
typedef enum  { 
  MSGR_E_API_NOTINITIALIZED    = 0x81000751,
  MSGR_E_API_LOCKED            = 0x81000752,
  MSGR_E_API_UNLOCK_FAILED     = 0x81000753,
  MSGR_E_API_ALREADY_UNLOCKED  = 0x81000754,
  MSGR_E_API_PENDING_UNLOCK    = 0x81000755,
  MSGR_E_API_DISABLED          = 0x81000756
} LockError;
```



## Constants

<dl> <dt>

<span id="MSGR_E_API_NOTINITIALIZED"></span><span id="msgr_e_api_notinitialized"></span>**MSGR\_E\_API\_NOTINITIALIZED**
</dt> <dd>

The restricted API is not initialized.

</dd> <dt>

<span id="MSGR_E_API_LOCKED"></span><span id="msgr_e_api_locked"></span>**MSGR\_E\_API\_LOCKED**
</dt> <dd>

The Messenger service API is locked.

</dd> <dt>

<span id="MSGR_E_API_UNLOCK_FAILED"></span><span id="msgr_e_api_unlock_failed"></span>**MSGR\_E\_API\_UNLOCK\_FAILED**
</dt> <dd>

The attempt to unlock the Messenger service API was unsuccessful.

</dd> <dt>

<span id="MSGR_E_API_ALREADY_UNLOCKED"></span><span id="msgr_e_api_already_unlocked"></span>**MSGR\_E\_API\_ALREADY\_UNLOCKED**
</dt> <dd>

The Messenger service API is already unlocked.

</dd> <dt>

<span id="MSGR_E_API_PENDING_UNLOCK"></span><span id="msgr_e_api_pending_unlock"></span>**MSGR\_E\_API\_PENDING\_UNLOCK**
</dt> <dd>

A challenge request has been made by the application and the Messenger client application is awaiting a response.

</dd> <dt>

<span id="MSGR_E_API_DISABLED"></span><span id="msgr_e_api_disabled"></span>**MSGR\_E\_API\_DISABLED**
</dt> <dd>

The Messenger service API is disabled.

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

 

 





