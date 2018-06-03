---
title: DMsgrSessionManagerEvents OnAppShutdown event
description: Fires when Windows Messenger is shutting down.
ms.assetid: 27c394fe-9048-455b-b639-97cf36cfd7c3
keywords:
- OnAppShutdown event Windows Messenger
- OnAppShutdown event Windows Messenger , DMsgrSessionManagerEvents interface
- DMsgrSessionManagerEvents interface Windows Messenger , OnAppShutdown event
topic_type:
- apiref
api_name:
- DMsgrSessionManagerEvents.OnAppShutdown
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DMsgrSessionManagerEvents::OnAppShutdown event

\[**OnAppShutdown** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Fires when Windows Messenger is shutting down.

## Syntax


```C++
void OnAppShutdown();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Msgrpriv.h (include Mdispid.h)</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md)
</dt> <dt>

[**OnAppRegistered**](im-dmsgrsessionmanagerevents-onappregistered.md)
</dt> <dt>

[**OnAppUnRegistered**](im-dmsgrsessionmanagerevents-onappunregistered.md)
</dt> <dt>

[**OnInvitation**](im-dmsgrsessionmanagerevents-oninvitation.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





