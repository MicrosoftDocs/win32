---
title: DMessengerPrivateEvents OnAlertReceived event
description: Fires when an alert notification is sent from a Messenger service to a Messenger client application.
ms.assetid: 6e03cb90-91dc-4982-a84b-677f86093772
keywords:
- OnAlertReceived event Windows Messenger
- OnAlertReceived event Windows Messenger , DMessengerPrivateEvents interface
- DMessengerPrivateEvents interface Windows Messenger , OnAlertReceived event
topic_type:
- apiref
api_name:
- DMessengerPrivateEvents.OnAlertReceived
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

# DMessengerPrivateEvents::OnAlertReceived event

\[**OnAlertReceived** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Fires when an alert notification is sent from a Messenger service to a Messenger client application.

## Syntax


```C++
void OnAlertReceived(
  [in]      BSTR         bstrAlert,
  [in, out] VARIANT_BOOL *pBoolfEnableDefault = VARIANT_TRUE
);
```



## Parameters

<dl> <dt>

*bstrAlert* \[in\]
</dt> <dd>

**BSTR** containing the alert notification message.

</dd> <dt>

*pBoolfEnableDefault* \[in, out\]
</dt> <dd>

Pointer to a **VARIANT\_BOOL** that defines one of the following possible values.



| Value                                                                                                                                                                                                                    | Meaning                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| <span id="VARIANT_FALSE"></span><span id="variant_false"></span><dl> <dt>**VARIANT\_FALSE**</dt> <dt>false</dt> </dl> | Alerts are disabled.<br/> |
| <span id="VARIANT_TRUE"></span><span id="variant_true"></span><dl> <dt>**VARIANT\_TRUE**</dt> <dt>true</dt> </dl>     | Alerts are enabled.<br/>  |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

A Messenger client receives this event if it has called the [**EnableAlertEvents**](im-imessengerprivate-enablealertevents-method.md) method and one of the Messenger service sites that the application is connected to fires an alert.

The value of *pBoolfEnableDefault* indicates whether a popup window is displayed when this event is received. You must set this value to **VARIANT\_FALSE** to specify that Windows Messenger must not display a popup window for this alert; otherwise a popup window is displayed.

## Requirements



|                                     |                                                                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                                 |
| Product<br/>                  | Messenger 4.5<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>                                          |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl>                                        |
| DLL<br/>                      | <dl> <dt>Msnmsgrexe.adeb440d\_7847\_4f65\_80bd\_899870ed2ec9</dt> </dl> |



## See also

<dl> <dt>

[**DMessengerPrivateEvents**](im-dmessengerprivateevents.md)
</dt> <dt>

[**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md)
</dt> <dt>

[**OnLockEnable**](im-dmessengerprivateevents-onlockenable.md)
</dt> <dt>

[**OnLockResult**](im-dmessengerprivateevents-onlockresult.md)
</dt> <dt>

[**RequestChallenge**](im-imsgrlock-requestchallenge-method.md)
</dt> <dt>

[**SendResponse**](im-imsgrlock-sendresponse-method.md)
</dt> <dt>

[**EnableAlertEvents**](im-imessengerprivate-enablealertevents-method.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





