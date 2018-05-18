---
title: DMessengerEvents OnMyPhoneChange event
description: Indicates that the local client's phone contact information has been changed or that a change was attempted.
ms.assetid: 'dc224f0c-1dbc-41e6-9107-a72fb4f3471d'
keywords: ["OnMyPhoneChange event Windows Messenger", "OnMyPhoneChange event Windows Messenger , DMessengerEvents interface", "DMessengerEvents interface Windows Messenger , OnMyPhoneChange event"]
topic_type:
- apiref
api_name:
- DMessengerEvents.OnMyPhoneChange
api_location:
- Msgsc.dll
api_type:
- COM
---

# DMessengerEvents::OnMyPhoneChange event

\[**OnMyPhoneChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the local client's phone contact information has been changed or that a change was attempted.

## Syntax


```C++
void OnMyPhoneChange(
  [in] MPHONE_TYPE PhoneType,
  [in] BSTR        bstrNumber
);
```



## Parameters

<dl> <dt>

*PhoneType* \[in\]
</dt> <dd>

A value of the [**MPHONE\_TYPE**](im-mphone-type.md) enumeration.

</dd> <dt>

*bstrNumber* \[in\]
</dt> <dd>

A **BSTR** that contains the current client's new phone number. This might include punctuation, depending on how it is stored on the server.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The Windows Messenger API does not have a method to put or set the client's friendly name information. This event fires only if the friendly name is changed through internal APIs or user action on the UI. No *hr* is contained in this event.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter  | vaArgs\[x\] | Variant Type |
|------------|-------------|--------------|
| bstrNumber | 0           | VT\_BSTR     |
| PhoneType  | 1           | VT\_14       |



 

> [!Note]  
> This event is not available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**DMessengerEvents**](im-dmessengerevents.md)
</dt> <dt>

[**MyPhoneNumber**](im-imessenger-myphonenumber.md)
</dt> <dt>

[**PhoneNumber**](im-imessengercontact-phonenumber.md)
</dt> <dt>

[**OnContactPhoneChange**](im-dmessengerevents-oncontactphonechange.md)
</dt> </dl>

 

 





