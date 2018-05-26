---
title: MessengerContact object
description: Do not use. The MessengerContact object corresponds to the IMessengerContact interface. This object provides a local representation of a remote contact. It represents a single user as stored in the Messenger objects internal contact list.
ms.assetid: f00b35ee-030e-4946-a954-2d0fd3e4193f
keywords:
- MessengerContact object Windows Messenger
- MessengerContact object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerContact
api_location:
- Msgrua.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MessengerContact object

\[**MessengerContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerContact** object corresponds to the [**IMessengerContact**](im-imessengercontact.md) interface. This object provides a local representation of a remote contact. It represents a single user as stored in the [**Messenger**](im-messenger.md) object's internal contact list.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerContact** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerContact** objects only after creating the [**Messenger**](im-messenger.md) object. After this object is created, a **MessengerContact** object can be referenced through one of the following:

-   Calling the [**Item**](im-imessengercontacts-item.md) method on the [**MessengerContacts**](im-messengercontacts.md) object representing the contact list.
-   Various [**DMessengerEvents**](im-dmessengerevents.md) events that return **MessengerContact** object references.

**MessengerContact** objects will continue to exist after they are removed from the contact list programmatically or through user action until they are released. In Microsoft Visual C++, you can determine whether **MessengerContact** objects are no longer in the contact list by monitoring [**OnContactListRemove**](im-dmessengerevents-oncontactlistremove.md) events. In most cases, a **MessengerContact** object that is no longer in the contact list should be released. All objects should be released as part of a cleanup or shutdown routine.

### Interfaces Implemented



**MessengerContact**



 

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



 

 





