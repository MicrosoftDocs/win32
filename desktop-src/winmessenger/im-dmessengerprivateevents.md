---
title: DMessengerPrivateEvents interface
description: Do not use. The DMessengerPrivateEvents dispinterface fires events in the Messenger client when notifications from IMessengerPrivate are received.
ms.assetid: 96185ddd-63f1-4cd7-85c9-3e7be96ef3a7
keywords:
- DMessengerPrivateEvents interface Windows Messenger
- DMessengerPrivateEvents interface Windows Messenger , described
topic_type:
- apiref
api_name:
- DMessengerPrivateEvents
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMessengerPrivateEvents interface

\[**DMessengerPrivateEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **DMessengerPrivateEvents** dispinterface fires events in the Messenger client when notifications from [**IMessengerPrivate**](im-imessengerprivate.md) are received.

## Members

The **DMessengerPrivateEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **DMessengerPrivateEvents** also has these types of members:

-   [Events](#events)

### Events

The **DMessengerPrivateEvents** interface has these events.



| Event                                                                   | Description                                                                                                                                     |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md)   | Fires when an alert notification is sent from a Messenger service to a Messenger client application. <br/>                                |
| [**OnContactListAdd**](im-dmessengerprivateevents-oncontactlistadd.md) | Notifies a Messenger client that a contact has been added to the contact list.<br/>                                                       |
| [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md)   | Notifies a Messenger client that an authentication challenge from a Messenger service has been received. <br/>                            |
| [**OnLockEnable**](im-dmessengerprivateevents-onlockenable.md)         | Notifies a Messenger client with the status of the Messenger Lock and Key APIs.<br/>                                                      |
| [**OnLockResult**](im-dmessengerprivateevents-onlockresult.md)         | Returns the result of a Lock and Key authentication transaction between a Messenger client and the Microsoft .NET Messenger Service.<br/> |



 

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>                                          |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**IMessengerPrivate**](im-imessengerprivate.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





