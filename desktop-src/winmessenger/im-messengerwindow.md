---
title: MessengerWindow object
description: Do not use.
ms.assetid: '3d34077d-79fa-4d14-a229-fa87c75e5ccf'
keywords: ["MessengerWindow object Windows Messenger", "MessengerWindow object Windows Messenger , described"]
topic_type:
- apiref
api_name:
- MessengerWindow
api_location:
- Msgrua.h
api_type:
- COM
---

# MessengerWindow object

\[**MessengerWindow** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **MessengerWindow** object corresponds to the [**IMessengerWindow**](im-imessengerwindow.md) interface. This object can represent either the main application window or a conversation window that contains one or more active sessions between contacts and the local client user.

## Remarks

MSMSGS.EXE implements this object.

A **MessengerWindow** object is not intended to be created separately through [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) or other Component Object Model (COM) object instantiation techniques. Client implementers should access existing **MessengerWindow** objects only after creating the [**Messenger**](im-messenger.md) object. After this object is created, a **MessengerWindow** object can be referenced through one of the following:

-   Using return values from several [**IMessenger**](im-imessenger.md) interface methods that create or access **MessengerWindow** objects.
-   Various [**DMessengerEvents**](im-dmessengerevents.md) events that return **MessengerWindow** object references.

### Interfaces Implemented



[**IMessengerWindow**](im-imessengerwindow.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





