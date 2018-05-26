---
title: DMessengerEvents OnContactBlockChange event
description: Indicates that the block settings of a contact in the local clients Contact List have changed. Queries whether the contact is blocked by the local client user.
ms.assetid: f8e663d4-2186-4a01-a084-24efb89a3567
keywords:
- OnContactBlockChange event Windows Messenger
- OnContactBlockChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnContactBlockChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactBlockChange
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

# DMessengerEvents::OnContactBlockChange event

\[**OnContactBlockChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the block settings of a contact in the local client's Contact List have changed. Queries whether the contact is blocked by the local client user.

## Syntax


```C++
void OnContactBlockChange(
  [in] LONG         hr,
  [in] IDispatch    *pContact,
  [in] VARIANT_BOOL pBoolBlock
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. For a table of the MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

An error result for *hr* may result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.

Possible values are as follows:



| Value                                                                                                                                                                                               | Meaning                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <span id="S_OK"></span><span id="s_ok"></span><dl> <dt>**S\_OK**</dt> </dl>                                                                  | A user was successfully blocked or unblocked.<br/>                                      |
| <span id="MSGR_E_USER_NOT_FOUND"></span><span id="msgr_e_user_not_found"></span><dl> <dt>**MSGR\_E\_USER\_NOT\_FOUND**</dt> </dl>            | The user specified to be added does not exist.<br/>                                     |
| <span id="MSGR_E_UNEXPECTED"></span><span id="msgr_e_unexpected"></span><dl> <dt>**MSGR\_E\_UNEXPECTED**</dt> </dl>                          | The server has returned an unexpected error code.<br/>                                  |
| <span id="MSGR_E_SERVER_TOO_BUSY"></span><span id="msgr_e_server_too_busy"></span><dl> <dt>**MSGR\_E\_SERVER\_TOO\_BUSY**</dt> </dl>         | The server is not processing requests or not accepting new connections.<br/>            |
| <span id="MSGR_E_SERVER_UNAVAILABLE"></span><span id="msgr_e_server_unavailable"></span><dl> <dt>**MSGR\_E\_SERVER\_UNAVAILABLE**</dt> </dl> | The server was able to be contacted, but was unavailable for unspecified reasons. <br/> |



 

</dd> <dt>

*pContact* \[in\]
</dt> <dd>

Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object where a change in block value was attempted.

</dd> <dt>

*pBoolBlock* \[in\]
</dt> <dd>

One of two possible values of the **VARIANT\_BOOL** constant enumeration defined by the COM. **VARIANT\_TRUE** indicates that this contact is blocked. **VARIANT\_FALSE** indicates that this contact is not blocked. This value is potentially **NULL** or otherwise not useful if *hr* in the event returned any error code.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

To be used when writing custom ::Invoke methods to handle these events.



| Parameter  | vaArgs\[x\] | Variant Type |
|------------|-------------|--------------|
| pBoolBlock | 0           | VT\_BOOL     |
| pContact   | 1           | VT\_DISPATCH |
| hr         | 2           | VT\_I4       |



 

> [!Note]  
> This event is not available for scripting languages.

 

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

[**Blocked**](im-imessengercontact-blocked.md)
</dt> </dl>

 

 





