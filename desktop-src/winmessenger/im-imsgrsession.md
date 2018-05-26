---
title: IMsgrSession interface
description: Do not use. The IMsgrSession interface provides programmatic access to the MsgrSession object.
ms.assetid: 039b2e52-373d-4f06-9a95-057428a365db
keywords:
- IMsgrSession interface Windows Messenger
- IMsgrSession interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMsgrSession
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMsgrSession interface

\[**IMsgrSession** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMsgrSession** interface provides programmatic access to the [**MsgrSession**](im-msgrsession-object.md) object.

## Members

The **IMsgrSession** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMsgrSession** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsgrSession** interface has these methods.



| Method                                                            | Description                                         |
|:------------------------------------------------------------------|:----------------------------------------------------|
| [**Accept**](im-imsgrsession-accept-method.md)                   | Recipient accepts the invitation.<br/>        |
| [**Cancel**](im-imsgrsession-cancel-method.md)                   | Inviter cancels the invitation.<br/>          |
| [**Decline**](im-imsgrsession-decline-method.md)                 | Recipient declines the invitation.<br/>       |
| [**Invite**](im-imsgrsession-invite-method.md)                   | Invites a user to the current session.<br/>   |
| [**SendContextData**](im-imsgrsession-sendcontextdata-method.md) | Sends application-specific context data.<br/> |



 

### Properties

The **IMsgrSession** interface has these properties.



| Property                                                                       | Access type          | Description                                                                                                                                         |
|:-------------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Application**](im-imsgrsession-application-property.md)<br/>         |                      | Obtains the application's GUID set by the inviter for this session from the registry.<br/>                                                    |
| [**ApplicationName**](im-imsgrsession-applicationname-property.md)<br/> | Read-only<br/> | Retrieves a value that indicates the application name. <br/>                                                                                  |
| [**ApplicationURL**](im-imsgrsession-applicationurl-property.md)<br/>   | Read-only<br/> | Retrieves a value that indicates the application's URL from the registry.<br/>                                                                |
| [**ContextData**](im-imsgrsession-contextdata-property.md)<br/>         | Read-only<br/> | Retrieves a value that indicates the application-specific context data. <br/>                                                                 |
| [**Flags**](im-imsgrsession-flags-property.md)<br/>                     | Read-only<br/> | Retrieves a value that indicates the session flags. <br/>                                                                                     |
| [**LocalAddress**](im-imsgrsession-localaddress-property.md)<br/>       |                      | Sets or retrieves the IP address of the session.<br/>                                                                                         |
| [**RemoteAddress**](im-imsgrsession-remoteaddress-property.md)<br/>     | Read-only<br/> | Retrieves a value that indicates the IP address of the other party in the session.<br/>                                                       |
| [**SessionID**](im-imsgrsession-sessionid-property.md)<br/>             | Read-only<br/> | Retrieves a value that indicates the session ID. <br/>                                                                                        |
| [**State**](im-imsgrsession-state-property.md)<br/>                     | Read-only<br/> | Retrieves a value that indicates the current state of the session. <br/>                                                                      |
| [**User**](im-imsgrsession-user-property.md)<br/>                       | Read-only<br/> | Retrieves a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) of a [**MessengerContact**](im-messengercontact.md) object.<br/> |



 

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

[**IDispatch**](c1accca9-971c-4435-8a5e-e25404a3fb25)
</dt> <dt>

[**MsgrSession**](im-msgrsession-object.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





