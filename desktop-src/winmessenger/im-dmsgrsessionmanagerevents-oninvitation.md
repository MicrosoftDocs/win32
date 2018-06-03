---
title: DMsgrSessionManagerEvents OnInvitation event
description: Fires when a new session invitation has been received.
ms.assetid: 008344cd-3f2c-4ede-80aa-57e91db50dcd
keywords:
- OnInvitation event Windows Messenger
- OnInvitation event Windows Messenger , DMsgrSessionManagerEvents interface
- DMsgrSessionManagerEvents interface Windows Messenger , OnInvitation event
topic_type:
- apiref
api_name:
- DMsgrSessionManagerEvents.OnInvitation
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

# DMsgrSessionManagerEvents::OnInvitation event

\[**OnInvitation** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Fires when a new session invitation has been received.

## Syntax


```C++
void OnInvitation(
  [in]      IDispatch    *pSession,
  [in]      BSTR         bstrAppData,
  [in, out] VARIANT_BOOL *pfHandled = VARIANT_FALSE
);
```



## Parameters

<dl> <dt>

*pSession* \[in\]
</dt> <dd>

Pointer to an **IDispatch** interface that corresponds to the application session.

</dd> <dt>

*bstrAppData* \[in\]
</dt> <dd>

**BSTR** equal to the value defined by the application when the session invitation was made using the [**Invite**](im-imsgrsession-invite-method.md) method.

</dd> <dt>

*pfHandled* \[in, out\]
</dt> <dd>

Pointer to a **VARIANT\_BOOL** that defines one of the following possible values.



| Value                                                                                                                                                                                                                    | Meaning                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <span id="VARIANT_FALSE"></span><span id="variant_false"></span><dl> <dt>**VARIANT\_FALSE**</dt> <dt>false</dt> </dl> | An invitation was received and a Windows Messenger conversation window will be opened.<br/>      |
| <span id="VARIANT_TRUE"></span><span id="variant_true"></span><dl> <dt>**VARIANT\_TRUE**</dt> <dt>true</dt> </dl>     | An invitation was received, but a Windows Messenger conversation window will not be opened.<br/> |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

When the Messenger client receives an invitation, the default value of *pfHandled* will be VARIANT\_FALSE. If the user sets the value to VARIANT\_TRUE, then the Messenger client receiving the invitation will not have the conversation window open.

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

[**OnAppShutdown**](im-dmsgrsessionmanagerevents-onappshutdown.md)
</dt> <dt>

[**OnAppUnRegistered**](im-dmsgrsessionmanagerevents-onappunregistered.md)
</dt> <dt>

[**BeforeAppLaunch**](im-dmsgrsessionevents-beforeapplaunch.md)
</dt> <dt>

[**Invite**](im-imsgrsession-invite-method.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





