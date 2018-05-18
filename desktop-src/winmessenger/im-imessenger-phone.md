---
title: IMessenger Phone method
description: Launches the Phone Call dialog box.
ms.assetid: '99961081-1bdc-4311-8ca4-9eb1ed73c903'
keywords: ["Phone method Windows Messenger", "Phone method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , Phone method"]
topic_type:
- apiref
api_name:
- IMessenger.Phone
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::Phone method

\[**Phone** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the **Phone Call** dialog box.

## Syntax


```C++
HRESULT Phone(
  [in]          VARIANT     vContact,
  [in]          MPHONE_TYPE ePhoneNumber,
  [in]          BSTR        bstrNumber,
  [out, retval] IDispatch   **ppMWindow
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that can take as its value either a **VT\_BSTR** string or a **VT\_DISPATCH** pointer to an existing [**MessengerContact**](im-messengercontact.md) object. If the input value type is a string, this method creates a new **MessengerContact** object internally. The string should be the full sign-in name. For a Microsoft .NET Messenger Service contact, this should include the "at" sign (@) and domain name. If the input value type is a pointer to an existing **MessengerContact** object (should be type **VT\_DISPATCH**), the existing object is used.

</dd> <dt>

*ePhoneNumber* \[in\]
</dt> <dd>

Type: **MPHONE\_TYPE**

A value of the [**MPHONE\_TYPE**](im-mphone-type.md) enumeration that specifies the type of telephone number being called.

</dd> <dt>

*bstrNumber* \[in\]
</dt> <dd>

Type: **BSTR**

A **BSTR** that contains the telephone number that will be entered on the text field of the **Phone Call** dialog box. No validation is performed on this string. The string is expected to follow Telephony Application Programming Interface (TAPI) standards for phone numbers, which are as follows:


```
+[countrycode]SPACE[phonenumber]
```



where:

-   \+ is the plus character.
-   \[countrycode\] is any valid country/region code per international phone dialing conventions. An access code should not be supplied in this phone number string. The access code is added by the exchange that initiates the standard telephony portion of the call.
-   SPACE is the space character, CHR(20).
-   \[phonenumber\] is the phone number within the respective country's exchange, including area or regional codes, as appropriate.
-   Punctuation (except the + sign) should not be provided. Punctuation in \[countrycode\] or \[phonenumber\] will be ignored.

If the *bstrNumber* parameter is given as a **NULL** string, the text field of the new dialog box will be initially blank.

</dd> <dt>

*ppMWindow* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

A pointer to a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerWindow**](im-messengerwindow.md) object, which can be accessed through the [**IMessengerWindow**](im-imessengerwindow.md) interface that is used to call other automation-accessible properties, such as [**Height**](im-imessengerwindow-height.md), [**Width**](im-imessengerwindow-width.md), [**Top**](im-imessengerwindow-top.md), [**Left**](im-imessengerwindow-left.md), and [**Show**](im-imessengerwindow--show.md). This parameter cannot be **null**.

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of all MSGR\_E\_\* constants [**MSGRConstants**](im-msgrconstants.md), see.

Returns one of the following values.



| Return code                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                              | Success. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>                            | Could not create a **Phone Call** window. <br/> - or -<br/> Called this method against the local client user.<br/>                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>           | Client was not signed in the primary service at the time this method was called.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**S\_FALSE**</dt> </dl>                           | The **Phone Call** dialog box is already open.<br/>                                                                                                                                                                                                                                                                                                                                                                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                      | *vContact* is **NULL**, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or -<br/> *vContact* is a **VT\_BSTR** that exceeded 129 characters.<br/> - or -<br/> *vContact* is a **VT\_BSTR** and contains a carriage return or linefeed.<br/> - or -<br/> The phone type is out of range.<br/> - or -<br/> *bstrNumber* exceeds 256 characters.<br/> |
| <dl> <dt>**MSGR\_E\_PHONESERVICE\_UNAVAILABLE**</dt> </dl> | The service for the contact you are attempting to call does not support phone calls. <br/>                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**MSGR\_E\_PHONE\_INVALID\_NUMBER**</dt> </dl>    | The contact you are attempting to call does not have the given phone-type number set.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**MSGR\_E\_POLICY\_RESTRICTED**</dt> </dl>        | Windows Messenger 5.0 and later. The local computer or local user policy does not allow users to make phone calls. <br/>                                                                                                                                                                                                                                                                                                                              |



 

## Remarks

The Microsoft Exchange Instant Messaging Service (IM) cannot support this method. Calling this method on an Exchange service contact will fail.

*ppMWindow* should be released when it is no longer needed.

Only one **Phone Call** dialog box can be active at one time. Calling **Phone** multiple times returns S\_OK, not S\_FALSE. The phone number displayed in the dialog box will be the phone number entered as a parameter in the most recent method call.

In anticipation of numbers that exceed normal limits because of extensions, key sequences for private uses, and so on, there is no enforcement of string length for the *bstrNumber* parameter. There is a physical limit to the display of strings in the dialog box.

> [!Note]  
> This method is available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





