---
title: IMessengerContact interface
description: Do not use. The primary interface for an individual MessengerContact object (the local representation of a remote user). Each contact in the contact list exists as its own MessengerContact object.
ms.assetid: 7854cfd9-5a56-4643-ba98-c9e30110ab89
keywords:
- IMessengerContact interface Windows Messenger
- IMessengerContact interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerContact
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMessengerContact interface

\[**IMessengerContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The primary interface for an individual [**MessengerContact**](im-messengercontact.md) object (the local representation of a remote user). Each contact in the contact list exists as its own **MessengerContact** object.

## Members

The **IMessengerContact** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerContact** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMessengerContact** interface has these properties.



| Property                                                             | Access type          | Description                                                                                                                                                                                        |
|:---------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Blocked**](im-imessengercontact-blocked.md)<br/>           |                      | Sets or retrieves a Boolean value that declares whether the contact associated with this [**MessengerContact**](im-messengercontact.md) object is blocked by the current client user. <br/> |
| [**CanPage**](im-imessengercontact-canpage.md)<br/>           | Read-only<br/> | Retrieves a Boolean value that declares whether the contact associated with this [**MessengerContact**](im-messengercontact.md) object has mobile preferences established or visible. <br/> |
| [**FriendlyName**](im-imessengercontact-friendlyname.md)<br/> | Read-only<br/> | Retrieves the friendly name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.<br/>                                                                 |
| [**IsSelf**](im-imessengercontact-isself.md)<br/>             | Read-only<br/> | Retrieves a Boolean value that declares whether the contact associated with this [**MessengerContact**](im-messengercontact.md) object is actually the current client user.<br/>            |
| [**PhoneNumber**](im-imessengercontact-phonenumber.md)<br/>   | Read-only<br/> | Retrieves the phone number information for the contact associated with this [**MessengerContact**](im-messengercontact.md) object.<br/>                                                     |
| [**Property**](im-imessengercontact-property.md)<br/>         |                      | Reserved.<br/>                                                                                                                                                                               |
| [**ServiceID**](im-imessengercontact-serviceid.md)<br/>       | Read-only<br/> | Retrieves the service ID, a GUID, for the contact associated with this [**MessengerContact**](im-messengercontact.md) object. <br/>                                                         |
| [**ServiceName**](im-imessengercontact-servicename.md)<br/>   | Read-only<br/> | Retrieves the service name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.<br/>                                                                  |
| [**SigninName**](im-imessengercontact-signinname.md)<br/>     | Read-only<br/> | Retrieves the sign-in name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.<br/>                                                                  |
| [**Status**](im-imessengercontact-status.md)<br/>             | Read-only<br/> | Retrieves the connection status of the contact associated with the [**MessengerContact**](im-messengercontact.md) object.<br/>                                                              |



 

## Remarks

[**MessengerContact**](im-messengercontact.md) objects are also occasionally created or used for other purposes. For example, a **MessengerContact** object can be used as the parameter input for the [**InstantMessage**](im-imessenger-instantmessage.md) method even if that contact does not exist in the local contact list.

To create a [**MessengerContact**](im-messengercontact.md) object, use the [**GetContact**](im-imessenger-getcontact.md) method. You create new **MessengerContact** objects by sign-in name. When you are creating a **MessengerContact** object, you are not necessarily creating a new contact until you place the new **MessengerContact** object into the contact list. If a **MessengerContact** object already exists for that sign-in name, this method will reference the existing object instead of creating a new one.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





