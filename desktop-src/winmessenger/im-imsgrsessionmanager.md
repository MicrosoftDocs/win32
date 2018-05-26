---
title: IMsgrSessionManager interface
description: Do not use. The IMsgrSessionManager interface is a Messenger service API that provides programmatic access to the MsgrSessionManager object.
ms.assetid: b62cb956-943e-461f-ad8d-65214092ea54
keywords:
- IMsgrSessionManager interface Windows Messenger
- IMsgrSessionManager interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMsgrSessionManager
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

# IMsgrSessionManager interface

\[**IMsgrSessionManager** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMsgrSessionManager** interface is a Messenger service  API that provides programmatic access to the [**MsgrSessionManager**](im-msgrsessionmanager-object.md) object.

## Members

The **IMsgrSessionManager** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMsgrSessionManager** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsgrSessionManager** interface has these methods.



| Method                                                                               | Description                                                                    |
|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**CreateSession**](im-imsgrsessionmanager-createsession-method.md)                 | Creates a new [**MsgrSession**](im-msgrsession-object.md) object. <br/> |
| [**GetLaunchingSession**](im-imsgrsessionmanager-getlaunchingsession-method.md)     | Retrieves the session information that started the application.<br/>     |
| [**RegisterApplication**](im-imsgrsessionmanager-registerapplication-method.md)     | Registers an application for use with a Messenger client. <br/>          |
| [**UnRegisterApplication**](im-imsgrsessionmanager-unregisterapplication-method.md) | Removes an application from the Messenger client list.<br/>              |



 

### Properties

The **IMsgrSessionManager** interface has these properties.



| Property                                                                        | Access type           | Description                 |
|:--------------------------------------------------------------------------------|:----------------------|:----------------------------|
| [**Applications**](im-imsgrsessionmanager-applications-property.md)<br/> | Write-only<br/> | Not implemented.<br/> |



 

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
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IDispatch**](c1accca9-971c-4435-8a5e-e25404a3fb25)
</dt> <dt>

[**MsgrSessionManager**](im-msgrsessionmanager-object.md)
</dt> <dt>

[**MsgrSession**](im-msgrsession-object.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





