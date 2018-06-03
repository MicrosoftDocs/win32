---
title: DMsgrSessionEvents BeforeAppLaunch event
description: Fires when the session's application is about to be launched.
ms.assetid: f619a9e8-9bd6-4853-9161-08429216fcef
keywords:
- BeforeAppLaunch event Windows Messenger
- BeforeAppLaunch event Windows Messenger , DMsgrSessionEvents interface
- DMsgrSessionEvents interface Windows Messenger , BeforeAppLaunch event
topic_type:
- apiref
api_name:
- DMsgrSessionEvents.BeforeAppLaunch
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

# DMsgrSessionEvents::BeforeAppLaunch event

\[**BeforeAppLaunch** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Fires when the session's application is about to be launched.

## Syntax


```C++
void BeforeAppLaunch(
  [in, out] VARIANT_BOOL *pBoolfEnableDefault = VARIANT_TRUE
);
```



## Parameters

<dl> <dt>

*pBoolfEnableDefault* \[in, out\]
</dt> <dd>

Pointer to a **VARIANT\_BOOL** that defines one of the following possible values.



| Value                                                                                                                                                                                                                    | Meaning                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <span id="VARIANT_FALSE"></span><span id="variant_false"></span><dl> <dt>**VARIANT\_FALSE**</dt> <dt>false</dt> </dl> | Application launch disabled.<br/> |
| <span id="VARIANT_TRUE"></span><span id="variant_true"></span><dl> <dt>**VARIANT\_TRUE**</dt> <dt>true</dt> </dl>     | Application launch enabled.<br/>  |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of *pBoolfEnableDefault* indicates whether a Messenger client will launch the session's application when this event is received. To disable a Messenger client from launching the session's application, the application must set this value to VARIANT\_FALSE.

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>                                          |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMsgrSessionEvents**](im-dmsgrsessionevents.md)
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

[**OnTermination**](im-dmsgrsessionevents-ontermination.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





