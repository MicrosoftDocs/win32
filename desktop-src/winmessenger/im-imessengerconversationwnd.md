---
title: IMessengerConversationWnd interface
description: Do not use. An interface that returns an IDispatch pointer to an IMessengerContacts collection that contains the participants of that conversation, excluding the local user. This is a read-only collection. Remove cannot be used on this collection.
ms.assetid: 8fc2c2d7-fe5d-4ab6-9cf7-e2cb099672a1
keywords:
- IMessengerConversationWnd interface Windows Messenger
- IMessengerConversationWnd interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerConversationWnd
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

# IMessengerConversationWnd interface

\[**IMessengerConversationWnd** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. An interface that returns an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) pointer to an [**IMessengerContacts**](im-imessengercontacts.md) collection that contains the participants of that conversation, excluding the local user. This is a read-only collection. [**Remove**](im-imessengergroups-remove.md) cannot be used on this collection.

## Members

The **IMessengerConversationWnd** interface inherits from [**IMessengerWindow**](im-imessengerwindow.md). **IMessengerConversationWnd** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessengerConversationWnd** interface has these methods.



| Method                                                        | Description                                                |
|:--------------------------------------------------------------|:-----------------------------------------------------------|
| [**AddContact**](im-imessengerconversationwnd-addcontact.md) | Adds another user to the current conversation. <br/> |



 

### Properties

The **IMessengerConversationWnd** interface has these properties.



| Property                                                             | Access type          | Description                                                                          |
|:---------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------|
| [**Contacts**](im-imessengerconversationwnd-contacts.md)<br/> | Read-only<br/> | Retrieves a read-only collection of contacts in the conversation window. <br/> |
| [**History**](im-imessengerconversationwnd-history.md)<br/>   | Read-only<br/> | Returns the text from the history of the conversation window.<br/>             |



 

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



 

 





