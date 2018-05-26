---
title: DMsgrSessionManagerEvents OnAppRegistered event
description: Fires when a new application has been registered.
ms.assetid: c75e70d1-07e9-4ae5-b24e-3779a3c77852
keywords:
- OnAppRegistered event Windows Messenger
- OnAppRegistered event Windows Messenger , DMsgrSessionManagerEvents interface
- DMsgrSessionManagerEvents interface Windows Messenger , OnAppRegistered event
topic_type:
- apiref
api_name:
- DMsgrSessionManagerEvents.OnAppRegistered
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMsgrSessionManagerEvents::OnAppRegistered event

\[**OnAppRegistered** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Fires when a new application has been registered.

## Syntax


```C++
void OnAppRegistered(
  [in] BSTR bstrAppGUID
);
```



## Parameters

<dl> <dt>

*bstrAppGUID* \[in\]
</dt> <dd>

**BSTR** that defines the application's GUID.

</dd> </dl>

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

[**OnAppShutdown**](im-dmsgrsessionmanagerevents-onappshutdown.md)
</dt> <dt>

[**OnAppUnRegistered**](im-dmsgrsessionmanagerevents-onappunregistered.md)
</dt> <dt>

[**OnInvitation**](im-dmsgrsessionmanagerevents-oninvitation.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





