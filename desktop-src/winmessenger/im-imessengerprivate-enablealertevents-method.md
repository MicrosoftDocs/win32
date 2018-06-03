---
title: IMessengerPrivate EnableAlertEvents method
description: Enables the Messenger client to be notified when the Messenger service fires events.
ms.assetid: 9d1d4e73-2099-4dcb-877a-1a27da145a25
keywords:
- EnableAlertEvents method Windows Messenger
- EnableAlertEvents method Windows Messenger , IMessengerPrivate interface
- IMessengerPrivate interface Windows Messenger , EnableAlertEvents method
topic_type:
- apiref
api_name:
- IMessengerPrivate.EnableAlertEvents
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

# IMessengerPrivate::EnableAlertEvents method

\[**EnableAlertEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Enables the Messenger client to be notified when the Messenger service fires events.

## Syntax


```VB
Function EnableAlertEvents( _
  ByRef ppsaSiteIds As SAFEARRAY (LONG) _
) As HRESULT
```



## Parameters

<dl> <dt>

*ppsaSiteIds* \[in, out\]
</dt> <dd>

Type: **SAFEARRAY (LONG)\***

Pointer to an array of type **LONG** that specifies the site IDs from which the object will receive notification events.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method call was completed successfully.<br/>                            |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | The method call failed because the service was locked.<br/>                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The parameter passed to this method is not valid for this method call.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The array *ppsaSiteIds* is too large.<br/>                                  |



 

## Remarks

This method passes a pointer to an array of site IDs, which have a **LONG** integer type. When a Messenger client application has called this method, it receives alert notifications from Messenger service sites with the [**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md) event.

The following table lists the error codes returned by this method.



| Error Code | Meaning                                                                |
|------------|------------------------------------------------------------------------|
| 0x80000002 | The array *ppsaSiteIds* is too large.                                  |
| 0x80000003 | The parameter passed to this method is not valid for this method call. |



 

> [!Note]  
> This method is not available for scripting languages.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMessengerPrivate**](im-imessengerprivate.md)
</dt> <dt>

[**AddContact**](im-imessengerprivate-addcontact-method.md)
</dt> <dt>

[**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





