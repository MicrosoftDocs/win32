---
title: IMsgrSession User property
description: Retrieves a pointer to an IDispatch of a MessengerContact object.
ms.assetid: 1dc96a0a-50e8-459c-b801-68d0e3b9ec9b
keywords:
- User property Windows Messenger
- User property Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , User property
topic_type:
- apiref
api_name:
- IMsgrSession.User
- IMsgrSession.get_User
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMsgrSession::User property

\[**User** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) of a [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_User(
  [out, retval] IDispatch **ppUser
);
```



## Property value

A pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) of a [**MessengerContact**](im-messengercontact.md) object.

## Remarks

The [**MessengerContact**](im-messengercontact.md) object contains information about the contact associated with this object. For example, calling IMessengerContact::get\_FriendlyName returns the friendly name of the contact.

The following table lists the error codes returned by this property.



| Error Code            | Meaning                                           |
|-----------------------|---------------------------------------------------|
| E\_INVALIDARG         | The value passed into the property was not valid. |
| SR\_NO\_USER\_INVITED | No other user has been invited to this session.   |



 



| Error Code                         | Meaning                                         |
|------------------------------------|-------------------------------------------------|
| 0x80070057                         | One of the possible values is not valid.        |
| SR\_NO\_USER\_INVITED (0x81000612) | No other user has been invited to this session. |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.0<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMsgrSession**](im-imsgrsession.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





