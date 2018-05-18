---
title: DMsgrSessionEvents interface
description: Do not use. The DMessengerPrivateEvents dispinterface fires events in the Messenger client when notifications from IMsgrSession are received.
ms.assetid: 'cee7fed0-df2a-44ea-829a-068969d0f5ed'
keywords: ["DMsgrSessionEvents interface Windows Messenger", "DMsgrSessionEvents interface Windows Messenger , described"]
topic_type:
- apiref
api_name:
- DMsgrSessionEvents
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
---

# DMsgrSessionEvents interface

\[**DMsgrSessionEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md) dispinterface fires events in the Messenger client when notifications from [**IMsgrSession**](im-imsgrsession.md) are received.

## Members

The **DMsgrSessionEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **DMsgrSessionEvents** also has these types of members:

-   [Events](#events)

### Events

The **DMsgrSessionEvents** interface has these events.



| Event                                                            | Description                                                                        |
|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**BeforeAppLaunch**](im-dmsgrsessionevents-beforeapplaunch.md) | Fires when the session's application is about to be launched. <br/>          |
| [**OnAccepted**](im-dmsgrsessionevents-onaccepted.md)           | Fires when the recipient has accepted the invitation. <br/>                  |
| [**OnAppNotPresent**](im-dmsgrsessionevents-onappnotpresent.md) | Fires when the application requested by the invitation is not present. <br/> |
| [**OnCancelled**](im-dmsgrsessionevents-oncancelled.md)         | Fires when the session has been canceled by the inviter. <br/>               |
| [**OnContextData**](im-dmsgrsessionevents-oncontextdata.md)     | Fires when new context data has arrived.<br/>                                |
| [**OnDeclined**](im-dmsgrsessionevents-ondeclined.md)           | Fires when the recipient has declined the invitation.<br/>                   |
| [**OnReadyToLaunch**](im-dmsgrsessionevents-onreadytolaunch.md) | Fires when the session is approved to start.<br/>                            |
| [**OnSendError**](im-dmsgrsessionevents-onsenderror.md)         | Fires when the last operation fails when sending.<br/>                       |
| [**OnStateChanged**](im-dmsgrsessionevents-onstatechanged.md)   | Fires when the session state has changed from the previous state.<br/>       |
| [**OnTermination**](im-dmsgrsessionevents-ontermination.md)     | Fires when the session has ended.<br/>                                       |



 

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>                                          |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMessengerPrivateEvents**](im-dmessengerprivateevents.md)
</dt> <dt>

[**IMsgrSession**](im-imsgrsession.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





