---
title: SESSION\_STATE enumeration
description: Do not use. Provides the list of possible state codes of the session invitation.
ms.assetid: 1619d750-ffb6-4d99-8f3b-b94184b47fba
keywords:
- SESSION_STATE enumeration Windows Messenger
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

# SESSION\_STATE enumeration

\[[**LockStatus**](im-lockstatus-enum.md) is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Provides the list of possible state codes of the session invitation.

## Syntax


```C++
typedef enum  { 
  SS_UNKNOWN,
  SS_READY,
  SS_INVITATION,
  SS_ACCEPTED,
  SS_CONNECTED,
  SS_CANCELLED,
  SS_DECLINED,
  SS_TERMINATED
} LockError;
```



## Constants

<dl> <dt>

<span id="SS_UNKNOWN"></span><span id="ss_unknown"></span>**SS\_UNKNOWN**
</dt> <dd>

Unknown response.

</dd> <dt>

<span id="SS_READY"></span><span id="ss_ready"></span>**SS\_READY**
</dt> <dd>

The session is ready.

</dd> <dt>

<span id="SS_INVITATION"></span><span id="ss_invitation"></span>**SS\_INVITATION**
</dt> <dd>

The session is an invitation.

</dd> <dt>

<span id="SS_ACCEPTED"></span><span id="ss_accepted"></span>**SS\_ACCEPTED**
</dt> <dd>

The session is accepted.

</dd> <dt>

<span id="SS_CONNECTED"></span><span id="ss_connected"></span>**SS\_CONNECTED**
</dt> <dd>

The session is not ready.

</dd> <dt>

<span id="SS_CANCELLED"></span><span id="ss_cancelled"></span>**SS\_CANCELLED**
</dt> <dd>

The local session canceled.

</dd> <dt>

<span id="SS_DECLINED"></span><span id="ss_declined"></span>**SS\_DECLINED**
</dt> <dd>

The session is remotely canceled.

</dd> <dt>

<span id="SS_TERMINATED"></span><span id="ss_terminated"></span>**SS\_TERMINATED**
</dt> <dd>

Protocol error.

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

 

 





