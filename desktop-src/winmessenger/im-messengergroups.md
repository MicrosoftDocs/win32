---
title: MessengerGroups object
description: Do not use. The MessengerGroups corresponds to the IMessengerGroups interface. It is a collection object of groups in the contact list.
ms.assetid: 8ca3a0f9-583a-4ffd-8e37-7f3a7920d5c3
keywords:
- MessengerGroups object Windows Messenger
- MessengerGroups object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerGroups
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

# MessengerGroups object

\[**MessengerGroups** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerGroups** corresponds to the [**IMessengerGroups**](im-imessengergroups.md) interface. It is a collection object of groups in the contact list.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerGroups** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerGroups** objects only after creating the [**Messenger**](im-messenger.md) object.

### Interfaces Implemented



[**IMessengerGroups**](im-imessengergroups.md)



 

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



 

 





