---
title: DMessengerPrivateEvents OnContactListAdd event
description: Notifies a Messenger client that a contact has been added to the contact list.
ms.assetid: aea5e1f5-ca0e-46aa-9013-f76be397fec4
keywords:
- OnContactListAdd event Windows Messenger
- OnContactListAdd event Windows Messenger , DMessengerPrivateEvents interface
- DMessengerPrivateEvents interface Windows Messenger , OnContactListAdd event
topic_type:
- apiref
api_name:
- DMessengerPrivateEvents.OnContactListAdd
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DMessengerPrivateEvents::OnContactListAdd event

\[**OnContactListAdd** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Notifies a Messenger client that a contact has been added to the contact list.

## Syntax


```C++
HRESULT OnContactListAdd(
  [in] long      hr,
  [in] IDispatch *pMContact
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

**LONG** that defines the error code for the operation.

</dd> <dt>

*pMContact* \[in\]
</dt> <dd>

Pointer to an [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface of a [**MessengerContact**](im-messengercontact.md) object representing the user that has been added to the contact list.

</dd> </dl>

## Return value

If this event succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The same DISPID is defined on [**DMessengerEvents**](im-dmessengerevents.md), and so the event also occurs on the [**Messenger**](im-messenger.md) object.

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>                                          |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMessengerPrivateEvents**](im-dmessengerprivateevents.md)
</dt> <dt>

[**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md)
</dt> <dt>

[**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md)
</dt> <dt>

[**OnLockEnable**](im-dmessengerprivateevents-onlockenable.md)
</dt> <dt>

[**RequestChallenge**](im-imsgrlock-requestchallenge-method.md)
</dt> <dt>

[**SendResponse**](im-imsgrlock-sendresponse-method.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





