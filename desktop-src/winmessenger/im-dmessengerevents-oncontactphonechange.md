---
title: DMessengerEvents OnContactPhoneChange event
description: Indicates that the phone information of a contact in the local clients Contact List has changed.
ms.assetid: 7623c10c-9c74-493e-aca0-bd6b5e3b6759
keywords:
- OnContactPhoneChange event Windows Messenger
- OnContactPhoneChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnContactPhoneChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactPhoneChange
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

# DMessengerEvents::OnContactPhoneChange event

\[**OnContactPhoneChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the phone information of a contact in the local client's Contact List has changed.

## Syntax


```C++
void OnContactPhoneChange(
  [in] LONG        hr,
  [in] IDispatch   *pContact,
  [in] MPHONE_TYPE PhoneType,
       BSTR        bstrNumber
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**.

An error result for *hr* might result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.

</dd> <dt>

*pContact* \[in\]
</dt> <dd>

Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object that corresponds to the contact. Using this pointer, clients can now code to its [**IMessengerContact**](im-imessengercontact.md) interface.

A [**MessengerContact**](im-messengercontact.md) object that corresponds to the contact. </dd> <dt>

*PhoneType* \[in\]
</dt> <dd>

A value in the [**MPHONE\_TYPE**](im-mphone-type.md) enumeration.

</dd> <dt>

*bstrNumber* 
</dt> <dd>

A **BSTR** that contains the string of the phone number.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Due to user input, the *bstrNumber* string might or might not contain punctuation. In general, punctuation is useful for display in the UI, but not for handling by APIs that handle telephony. Clients can strip or parse punctuation. However, punctuation cannot be added if none has been preserved because there are many possible punctuation conventions in various locales.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter  | vaArgs\[x\] | Variant Type |
|------------|-------------|--------------|
| bstrNumber | 0           | VT\_BSTR     |
| PhoneType  | 1           | VT\_I4       |
| pContact   | 2           | VT\_DISPATCH |
| hr         | 3           | VT\_I4       |



 

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

[**PhoneNumber**](im-imessengercontact-phonenumber.md)
</dt> </dl>

 

 





