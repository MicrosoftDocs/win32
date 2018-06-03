---
title: IMessengerContacts interface
description: Do not use. An interface that manipulates the contact list, which maintains a collection of users in a Messenger object.
ms.assetid: 6e08d2e2-cc75-441b-b2c2-755668429f48
keywords:
- IMessengerContacts interface Windows Messenger
- IMessengerContacts interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerContacts
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

# IMessengerContacts interface

\[**IMessengerContacts** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. An interface that manipulates the contact list, which maintains a collection of users in a [**Messenger**](im-messenger.md) object.

Any [**MessengerContacts**](im-messengercontacts.md) collection object can have zero members in its collection.

List collection objects are not explicitly created or destroyed. They already exist and were created by the [**Messenger**](im-messenger.md) object. To create a pointer to the existing object that represents the Contact List, use the [**GetContact**](im-imessenger-getcontact.md) method.

## Members

The **IMessengerContacts** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerContacts** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessengerContacts** interface has these methods.



| Method                                         | Description                                                                                    |
|:-----------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**Item**](im-imessengercontacts-item.md)     | Retrieves a specific service by index.<br/>                                              |
| [**Remove**](im-imessengercontacts-remove.md) | Removes a [**MessengerContact**](im-messengercontact.md) object from a collection.<br/> |



 

### Properties

The **IMessengerContacts** interface has these properties.



| Property                                                       | Access type          | Description                                                                                                     |
|:---------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](im-imessengercontacts--newenum.md)<br/> | Read-only<br/> | Enumerates the [**MessengerContact**](im-messengercontact.md) objects in a collection.<br/>              |
| [**Count**](im-imessengercontacts-count.md)<br/>        | Read-only<br/> | Retrieves the number of [**MessengerContacts**](im-messengercontacts.md) objects in the collection.<br/> |



 

## Remarks

The Messenger client contains other lists of users and contacts internally, but only the contact list is accessible through the Windows Messenger API.

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



 

 





