---
title: MessengerServices object
description: Do not use. The MessengerServices corresponds to the IMessengerServices interface. It represents a list of services in the Messenger object.
ms.assetid: ee3a63a7-974b-4d97-bb57-9b3eed0a4f5b
keywords:
- MessengerServices object Windows Messenger
- MessengerServices object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerServices
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

# MessengerServices object

\[**MessengerServices** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerServices** corresponds to the [**IMessengerServices**](im-imessengerservices.md) interface. It represents a list of services in the [**Messenger**](im-messenger.md) object.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerServices** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerServices** objects only after creating the [**Messenger**](im-messenger.md) object.

### Interfaces Implemented



[**IMessengerServices**](im-imessengerservices.md)



 

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



 

 





