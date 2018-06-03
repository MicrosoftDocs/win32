---
title: MessengerContacts object
description: Do not use. The MessengerContacts object corresponds to the IMessengerContacts interface. It is a collection object of contacts in the contact list.
ms.assetid: 63eb71fc-1530-4e87-be6f-c03cc5c40c4a
keywords:
- MessengerContacts object Windows Messenger
- MessengerContacts object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerContacts
api_location:
- Msgrua.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# MessengerContacts object

\[**MessengerContacts** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerContacts** object corresponds to the [**IMessengerContacts**](im-imessengercontacts.md) interface. It is a collection object of contacts in the contact list.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerContacts** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerContacts** objects only after creating the [**Messenger**](im-messenger.md) object. After this object is created, a **MessengerContacts** object can be referenced by calling the [**MyContacts**](im-imessenger-mycontacts.md) property on the **Messenger** object.

### Interfaces Implemented



[**IMessengerContacts**](im-imessengercontacts.md)



 

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



 

 





