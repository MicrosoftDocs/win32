---
title: IMessengerGroup interface
description: Do not use. The IMessengerGroup interface provides methods and properties to handle a group's collection of users.
ms.assetid: d9c6b484-41d0-4a96-9e1d-db00ec2dfc18
keywords:
- IMessengerGroup interface Windows Messenger
- IMessengerGroup interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerGroup
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

# IMessengerGroup interface

\[**IMessengerGroup** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMessengerGroup** interface provides methods and properties to handle a group's collection of users.

## Members

The **IMessengerGroup** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerGroup** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessengerGroup** interface has these methods.



| Method                                                   | Description                                  |
|:---------------------------------------------------------|:---------------------------------------------|
| [**AddContact**](im-imessengergroup-addcontact.md)      | Adds a contact to the group.<br/>      |
| [**RemoveContact**](im-messengergroup-removecontact.md) | Removes a contact from the group.<br/> |



 

### Properties

The **IMessengerGroup** interface has these properties.



| Property                                                   | Access type          | Description                                                                   |
|:-----------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------|
| [**Contacts**](im-imessengergroup-contacts.md)<br/> | Read-only<br/> | Retrieves a list of contacts from the group's collection of users.<br/> |
| [**Name**](im-imessengergroup-name.md)<br/>         |                      | Sets the name of the group.<br/>                                        |
| [**Service**](im-imessengergroup-service.md)<br/>   | Read-only<br/> | Retrieves the service object from the group.<br/>                       |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





