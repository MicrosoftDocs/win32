---
title: MessengerGroup object
description: Do not use. The MessengerGroup object corresponds to the IMessengerGroup interface. It represents a single group as stored in the Messenger objects internal group list.
ms.assetid: 74c4ffca-ee4b-4347-bfd9-16c481edf953
keywords:
- MessengerGroup object Windows Messenger
- MessengerGroup object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerGroup
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

# MessengerGroup object

\[**MessengerGroup** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerGroup** object corresponds to the [**IMessengerGroup**](im-imessengergroup.md) interface. It represents a single group as stored in the [**Messenger**](im-messenger.md) object's internal group list.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerGroup** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerGroup** objects only after creating the [**Messenger**](im-messenger.md) object. After this object is created, a **MessengerGroup** object can be referenced through one of the following:

-   Calling the [**Item**](im-imessengergroups-item.md) method on the **MessengerGroup** object representing the group list.
-   Various [**DMessengerEvents**](im-dmessengerevents.md) events that return **MessengerGroup** object references.

**MessengerGroup** objects will continue to exist after they are removed from the contact list programmatically or through user action until they are released. In Microsoft Visual C++, you can determine whether **MessengerGroup** objects are no longer in the group list by monitoring [**OnGroupRemoved**](im-dmessengerevents-ongroupremoved.md) events. In most cases, a **MessengerGroup** object that is no longer in the group list should be released. All objects should be released as part of a cleanup or shutdown routine.

### Interfaces Implemented



[**IMessengerGroup**](im-imessengergroup.md)



 

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



 

 





