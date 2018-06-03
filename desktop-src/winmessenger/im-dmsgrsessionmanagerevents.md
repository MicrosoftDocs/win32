---
title: DMsgrSessionManagerEvents interface
description: Do not use. The DMsgrSessionManagerEvents dispinterface fires events in the Messenger client when notifications from IMsgrSessionManager are received.
ms.assetid: 2fd8e32e-3171-48f1-9470-21e3bc9966b8
keywords:
- DMsgrSessionManagerEvents interface Windows Messenger
- DMsgrSessionManagerEvents interface Windows Messenger , described
topic_type:
- apiref
api_name:
- DMsgrSessionManagerEvents
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# DMsgrSessionManagerEvents interface

\[**DMsgrSessionManagerEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **DMsgrSessionManagerEvents** dispinterface fires events in the Messenger client when notifications from [**IMsgrSessionManager**](im-imsgrsessionmanager.md) are received.

## Members

The **DMsgrSessionManagerEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **DMsgrSessionManagerEvents** also has these types of members:

-   [Events](#events)

### Events

The **DMsgrSessionManagerEvents** interface has these events.



| Event                                                                           | Description                                                                                                                                      |
|:--------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnAppRegistered**](im-dmsgrsessionmanagerevents-onappregistered.md)         | Fires when a new application has been registered.<br/>                                                                                     |
| [**OnAppShutdown**](im-dmsgrsessionmanagerevents-onappshutdown.md)             | Fires when Windows Messenger is shutting down.<br/>                                                                                        |
| [**OnAppUnRegistered**](im-dmsgrsessionmanagerevents-onappunregistered.md)     | Fires when an application has been unregistered.<br/>                                                                                      |
| [**OnInvitation**](im-dmsgrsessionmanagerevents-oninvitation.md)               | Fires when a new session invitation has been received.<br/>                                                                                |
| [**OnLockChallenge**](im-dmsgrsessionmanagerevents-onlockchallenge.md)         | Notifies a Messenger client that an authentication challenge from a Messenger service has been received.<br/>                              |
| [**OnLockEnable**](im-dmsgrsessionmanagerevents-onlockenable.md)               | Notifies a Messenger client with the status of the Messenger Lock and Key APIs. <br/>                                                      |
| [**OnLockResult**](im-dmsgrsessionmanagerevents-onlockresult.md)               | Returns the result of a Lock and Key authentication transaction between a Messenger client and the Microsoft .NET Messenger Service. <br/> |
| [**OnLockStatusChanged**](im-dmsgrsessionmanagerevents-onlockstatuschanged.md) | Fires when the lock status changes. <br/>                                                                                                  |



 

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

[**IMsgrSessionManager**](im-imsgrsessionmanager.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





