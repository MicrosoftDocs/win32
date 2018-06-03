---
title: MessengerConversationWnd object
description: Do not use. The MessengerConversationWnd object corresponds to the IMessengerConversationWnd interface.
ms.assetid: 03ec74d1-3860-454e-9db2-558cc8d69c5c
keywords:
- MessengerConversationWnd object Windows Messenger
- MessengerConversationWnd object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerConversationWnd
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

# MessengerConversationWnd object

\[**MessengerConversationWnd** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerConversationWnd** object corresponds to the [**IMessengerConversationWnd**](im-imessengerconversationwnd.md) interface.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerConversationWnd** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerConversationWnd** objects only after creating the [**Messenger**](im-messenger.md) object.

### Interfaces Implemented



[**IMessengerConversationWnd**](im-imessengerconversationwnd.md)



 

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



 

 





