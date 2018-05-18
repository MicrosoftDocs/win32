---
title: DMsgrSessionEvents OnTermination event
description: Fires when the session has ended.
ms.assetid: 'fe2828fd-d842-4b52-903c-d5beef721881'
keywords: ["OnTermination event Windows Messenger", "OnTermination event Windows Messenger , DMsgrSessionEvents interface", "DMsgrSessionEvents interface Windows Messenger , OnTermination event"]
topic_type:
- apiref
api_name:
- DMsgrSessionEvents.OnTermination
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
---

# DMsgrSessionEvents::OnTermination event

\[**OnTermination** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Fires when the session has ended.

## Syntax


```C++
void OnTermination(
  [in] long hr,
  [in] BSTR bstrAppData
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

**HRESULT** that defines the return code for the operation.

</dd> <dt>

*bstrAppData* \[in\]
</dt> <dd>

**BSTR** that corresponds to a value provided by an application's invocation of the [**Decline**](im-imsgrsession-decline-method.md) method or [**Cancel**](im-imsgrsession-cancel-method.md) method.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>                                          |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMsgrSessionEvents**](im-dmsgrsessionevents.md)
</dt> <dt>

[**OnAccepted**](im-dmsgrsessionevents-onaccepted.md)
</dt> <dt>

[**OnAppNotPresent**](im-dmsgrsessionevents-onappnotpresent.md)
</dt> <dt>

[**OnCancelled**](im-dmsgrsessionevents-oncancelled.md)
</dt> <dt>

[**OnContextData**](im-dmsgrsessionevents-oncontextdata.md)
</dt> <dt>

[**OnDeclined**](im-dmsgrsessionevents-ondeclined.md)
</dt> <dt>

[**OnReadyToLaunch**](im-dmsgrsessionevents-onreadytolaunch.md)
</dt> <dt>

[**OnSendError**](im-dmsgrsessionevents-onsenderror.md)
</dt> <dt>

[**OnStateChanged**](im-dmsgrsessionevents-onstatechanged.md)
</dt> <dt>

[**Decline**](im-imsgrsession-decline-method.md)
</dt> <dt>

[**Cancel**](im-imsgrsession-cancel-method.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





