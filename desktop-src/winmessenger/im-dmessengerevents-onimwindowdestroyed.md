---
title: DMessengerEvents OnIMWindowDestroyed event
description: Indicates that a new conversation window has been closed.
ms.assetid: 7c2e4d31-cbe4-43a1-9a40-48258c32bfe8
keywords:
- OnIMWindowDestroyed event Windows Messenger
- OnIMWindowDestroyed event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnIMWindowDestroyed event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnIMWindowDestroyed
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DMessengerEvents::OnIMWindowDestroyed event

\[**OnIMWindowDestroyed** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a new conversation window has been closed.

## Syntax


```C++
void OnIMWindowDestroyed(
  [in] IDispatch *pIMWindow
);
```



## Parameters

<dl> <dt>*pIMWindow* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerConversationWnd**](im-messengerconversationwnd.md) object that corresponds to the added contact. Using this pointer, clients can now code to its [**IMessengerConversationWnd**](im-imessengerconversationwnd.md) interface. |
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



 

 





