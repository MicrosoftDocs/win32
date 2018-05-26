---
title: DMessengerEvents OnIMWindowCreated event
description: Indicates that a new conversation window has been opened.
ms.assetid: 1fc0e752-51e5-4785-95f0-e0f8c2413f5f
keywords:
- OnIMWindowCreated event Windows Messenger
- OnIMWindowCreated event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnIMWindowCreated event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnIMWindowCreated
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMessengerEvents::OnIMWindowCreated event

\[**OnIMWindowCreated** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a new conversation window has been opened.

## Syntax


```C++
void OnIMWindowCreated(
  [in] IDispatch *pIMWindow
);
```



## Parameters

<dl> <dt>*pIMWindow* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerConversationWnd**](im-messengerconversationwnd.md) object that corresponds to the added contact. Using this pointer, clients can now code to its [**IMessengerConversationWnd**](im-imessengerconversationwnd.md) interface. |
| **VB**  | A [**MessengerConversationWnd**](im-messengerconversationwnd.md) object that corresponds to the added contact.                                                                                                                                                                                                            |

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| pIMWindow | 0           | VT\_DISPATCH |



 

> [!Note]  
> This event is available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





