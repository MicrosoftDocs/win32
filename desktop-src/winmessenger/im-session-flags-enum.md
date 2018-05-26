---
title: SESSION\_FLAGS enumeration
description: Do not use. Provides the list of possible flag codes for the session invitation.
ms.assetid: 54cb8a58-2ddf-4662-b4b3-4c5e13c94a9d
keywords:
- SESSION_FLAGS enumeration Windows Messenger
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

# SESSION\_FLAGS enumeration

\[[**LockStatus**](im-lockstatus-enum.md) is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Provides the list of possible flag codes for the session invitation.

## Syntax


```C++
typedef enum  { 
  SF_NONE                   = 0x0000,
  SF_INVITER                = 0x0001,
  SF_INVITER                = 0x0002,
  SF_APP_INVITE_COMPATIBLE  = 0x0004
} LockError;
```



## Constants

<dl> <dt>

<span id="SF_NONE"></span><span id="sf_none"></span>**SF\_NONE**
</dt> <dd>

No such value.

</dd> <dt>

<span id="SF_INVITER"></span><span id="sf_inviter"></span>**SF\_INVITER**
</dt> <dd>

The party that holds the session object is the inviter.

</dd> <dt>

<span id="SF_INVITER"></span><span id="sf_inviter"></span>**SF\_INVITER**
</dt> <dd>

The party that holds the session object is the recipient.

</dd> <dt>

<span id="SF_APP_INVITE_COMPATIBLE"></span><span id="sf_app_invite_compatible"></span>**SF\_APP\_INVITE\_COMPATIBLE**
</dt> <dd>

The application shared between users is compatible.

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

 

 





