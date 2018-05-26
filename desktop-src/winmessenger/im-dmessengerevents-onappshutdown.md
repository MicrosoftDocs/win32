---
title: DMessengerEvents OnAppShutdown event
description: Indicates that the client application is about to shut down for purposes of a client upgrade initiated either by the server or client user.
ms.assetid: d6c859a8-9fad-4313-a8f8-9e928718e237
keywords:
- OnAppShutdown event Windows Messenger
- OnAppShutdown event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnAppShutdown event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnAppShutdown
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

# DMessengerEvents::OnAppShutdown event

\[**OnAppShutdown** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the client application is about to shut down for purposes of a client upgrade initiated either by the server or client user.

## Syntax


```C++
void OnAppShutdown();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

After this event is issued, the application shuts down. Any references held will become invalid and, if not deallocated, might create memory leaks.

This event is generally sent only if the client is forced to shut down in order to complete a mandatory upgrade, as determined during a sign-in exchange sequence. Alternatively, the client user might have affirmed a dialog box for an optional upgrade. This event is not issued as a result of a standard application quit, minimize, or system shutdown without client upgrade involved. The event is issued only in upgrade path scenarios.

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



 

 





