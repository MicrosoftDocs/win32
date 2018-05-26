---
title: DMessengerEvents OnContactStatusChange event
description: Indicates that the status of a contact in the local clients Contact List has changed, and returns the current state of the contact.
ms.assetid: 7e6759aa-1d5b-439a-86d8-822fb502edf3
keywords:
- OnContactStatusChange event Windows Messenger
- OnContactStatusChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnContactStatusChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactStatusChange
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

# DMessengerEvents::OnContactStatusChange event

\[**OnContactStatusChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the status of a contact in the local client's Contact List has changed, and returns the current state of the contact.

## Syntax


```C++
void OnContactStatusChange(
  [in] IDispatch *pMContact,
  [in] MISTATUS  mStatus
);
```



## Parameters

<dl> <dt>*pMContact* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                                                                                  |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object that corresponds to the contact. Using this pointer, clients can now code to its [**IMessengerContact**](im-imessengercontact.md) interface. There is no *hr* in this event. Unless there is an error, *pMContact* will not be **NULL**. |
| **VB**  | A [**MessengerContact**](im-messengercontact.md) object that corresponds to the contact. There is no *hr* in this event. Unless there is an error, *pMContact* will not be **NULL**.                                                                                                                                                                                            |

 </dd> <dt>

*mStatus* \[in\]
</dt> <dd>

A member of the [**MISTATUS**](im-mistatus.md) enumerator that specifies the current state of the [**MessengerContact**](im-messengercontact.md) object.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

When the local client initially signs in to the service, events are distributed for those users on the local client's Contact List who are not offline. Otherwise, such events are distributed whenever status changes.

This event is received only for users in the client's Contact List.

All online [**MISTATUS**](im-mistatus.md) results are grouped by a common factor in the constant.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| mStatus   | 0           | VT\_14       |
| pMContact | 1           | VT\_DISPATCH |



 

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



## See also

<dl> <dt>

[**DMessengerEvents**](im-dmessengerevents.md)
</dt> <dt>

[**Status**](im-imessengercontact-status.md)
</dt> <dt>

[**OnMyStatusChange**](im-dmessengerevents-onmystatuschange.md)
</dt> </dl>

 

 





