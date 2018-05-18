---
title: IMessengerContact PhoneNumber property
description: Retrieves the phone number information for the contact associated with this MessengerContact object.
ms.assetid: 'e48b5229-4b4f-493e-9c0c-753ab5af653b'
keywords: ["PhoneNumber property Windows Messenger", "PhoneNumber property Windows Messenger , IMessengerContact interface", "IMessengerContact interface Windows Messenger , PhoneNumber property"]
topic_type:
- apiref
api_name:
- IMessengerContact.PhoneNumber
- IMessengerContact.get_PhoneNumber
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerContact::PhoneNumber property

\[**PhoneNumber** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the phone number information for the contact associated with this [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_PhoneNumber(
  [in]          MPHONE_TYPE PhoneType,
  [out, retval] BSTR        *bstrNumber
);
```



## Property value

Pointer to a **BSTR** that contains the returned phone number as a string.

## Error codes

Returns one of the following values.



| Name                                                                                  | Meaning                                                                                                                                     |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>      | Success. <br/>                                                                                                                        |
| <dl> <dt>E\_FAIL</dt> </dl>    | [**MessengerContact**](im-messengercontact.md) object not valid; or, [**MPHONE\_TYPE**](im-mphone-type.md) parameter invalid. <br/> |
| <dl> <dt>E\_NOTIMPL</dt> </dl> | Cannot be accessed through scripting.<br/>                                                                                            |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                                 |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004005 | General internal failure.                                                                                                                               |
| 0x8007000E | Error returned by VARIANT handling library.                                                                                                             |
| 0x80070057 | Requested an out-of-range property. This is not normally returned through this interface because the API calls a property that is known to be in range. |



 

The *bstrNumber* return value may contain punctuation. Most APIs used for Internet telephony will either ignore or strip punctuation.

E\_FAIL HRESULT will be returned for a contact who does not have phone information for the specified *PhoneType* parameter.

> [!Note]  
> This property is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub btnPhoneNumber_Click()
    On Error Resume Next
    FormPPType.Show vbModal 'Dialog to select phone type
    If bDialogCancel = False Then
        Dim strSigninName As String
        Dim strServiceID As String
        'Get selected contact
        strSigninName = ListContact.SelectedItem.SubItems(2)
        strServiceID = ListContact.SelectedItem.SubItems(5)
        Set MsgrContact = Nothing
        Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
        ErrorTrap ("GetContact")    'Error handling routine
        MsgBox("Contact Phone = " & CStr(MsgrContact.PhoneNumber(lppType)))
    End If
    ErrorTrap ("Contact.PhoneNumber")   'Error handling routine
End Sub
```



## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessengerContact**](im-imessengercontact.md)
</dt> <dt>

[**OnContactPagerChange**](im-dmessengerevents-oncontactpagerchange.md)
</dt> <dt>

[**MyPhoneNumber**](im-imessenger-myphonenumber.md)
</dt> </dl>

 

 





