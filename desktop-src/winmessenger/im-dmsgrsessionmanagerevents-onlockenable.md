---
title: DMsgrSessionManagerEvents OnLockEnable event
description: Notifies a Messenger client with the status of the Messenger Lock and Key APIs.
ms.assetid: 'ae1d2abf-1aa9-4b8f-a135-01fcc80730d0'
keywords: ["OnLockEnable event Windows Messenger", "OnLockEnable event Windows Messenger , DMsgrSessionManagerEvents interface", "DMsgrSessionManagerEvents interface Windows Messenger , OnLockEnable event"]
topic_type:
- apiref
api_name:
- DMsgrSessionManagerEvents.OnLockEnable
api_location:
- Msnmsgrexe.adeb440d_7847_4f65_80bd_899870ed2ec9
api_type:
- COM
---

# DMsgrSessionManagerEvents::OnLockEnable event

\[**OnLockEnable** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Notifies a Messenger client with the status of the Messenger Lock and Key APIs.

## Syntax


```C++
void OnLockEnable(
  [in] VARIANT_BOOL fEnable = VARIANT_TRUE
);
```



## Parameters

<dl> <dt>

*fEnable* \[in\]
</dt> <dd>

**VARIANT\_BOOL** that defines one of the following possible values.



| Value                                                                                                                                                                                                                    | Meaning                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| <span id="VARIANT_FALSE"></span><span id="variant_false"></span><dl> <dt>**VARIANT\_FALSE**</dt> <dt>false</dt> </dl> | Lock and Key is disabled.<br/> |
| <span id="VARIANT_TRUE"></span><span id="variant_true"></span><dl> <dt>**VARIANT\_TRUE**</dt> <dt>true</dt> </dl>     | Lock and Key is enabled.<br/>  |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event fires shortly after a user signs in to Windows Messenger and indicates whether the Messenger client can proceed to request an authentication challenge from the Messenger service . Until this event notification is received, a Messenger client cannot unlock the Messenger service  APIs and requests for an authentication challenge will fail.

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Sessions.h (include Mdispid.h)</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Sessions.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md)
</dt> <dt>

[**OnLockChallenge**](im-dmsgrsessionmanagerevents-onlockchallenge.md)
</dt> <dt>

[**OnLockResult**](im-dmsgrsessionmanagerevents-onlockresult.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





