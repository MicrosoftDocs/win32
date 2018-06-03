---
title: MessengerService object
description: Do not use. The MessengerService object corresponds to the IMessengerService interface. This object represents a single service.
ms.assetid: 0f5fdc52-a36f-4e59-b5f9-03737a881349
keywords:
- MessengerService object Windows Messenger
- MessengerService object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerService
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

# MessengerService object

\[**MessengerService** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerService** object corresponds to the [**IMessengerService**](im-imessengerservice.md) interface. This object represents a single service.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerService** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerService** objects only after creating the [**Messenger**](im-messenger.md) object. After this object is created, a **MessengerService** object can be referenced through one of the following:

-   Calling the [**Item**](im-imessengerservices-item.md) method on the **MessengerService** object representing the service list.
-   Various [**DMessengerEvents**](im-dmessengerevents.md) events that return **MessengerService** object references.

**MessengerService** objects will continue to exist after they are removed from the contact list programmatically or through user action until they are released. In most cases, a **MessengerService** object that is no longer in the service list should be released. All objects should be released as part of a cleanup or shutdown routine.

### Interfaces Implemented



[**IMessengerService**](im-imessengerservice.md)



 

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



 

 





