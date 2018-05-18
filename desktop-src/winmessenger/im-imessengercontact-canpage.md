---
title: IMessengerContact CanPage property
description: Retrieves a Boolean value that declares whether the contact associated with this MessengerContact object has mobile preferences established or visible.
ms.assetid: '4b4071b7-23a9-4d20-87ea-5fa64fc15a30'
keywords: ["CanPage property Windows Messenger", "CanPage property Windows Messenger , IMessengerContact interface", "IMessengerContact interface Windows Messenger , CanPage property"]
topic_type:
- apiref
api_name:
- IMessengerContact.CanPage
- IMessengerContact.get_CanPage
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerContact::CanPage property

\[**CanPage** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a Boolean value that declares whether the contact associated with this [**MessengerContact**](im-messengercontact.md) object has mobile preferences established or visible.

This property is read-only.

## Syntax


```C++
HRESULT get_CanPage(
  [out, retval] VARIANT_BOOL *pBoolPage
);
```



## Property value

Pointer to a **VARIANT\_BOOL** that declares whether this user has a defined and accessible mobile device profile. VARIANT\_TRUE indicates that the user has mobile device information available. VARIANT\_FALSE indicates that the user has no mobile device information available.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                                                                                                |
| <dl> <dt>E\_FAIL</dt> </dl>                    | General internal failure.<br/>                                                                                                                                |
| <dl> <dt>DISP\_E\_BADVARTYPE</dt> </dl>        | Error returned by VARIANT handling library.<br/>                                                                                                              |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Error returned by VARIANT handling library.<br/>                                                                                                              |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | Requested an out-of-range property. This is not normally returned through this interface because the API calls a property that is known to be in range. <br/> |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pBoolPage* is a **NULL** pointer.<br/>                                                                                                                       |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                                 |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004005 | General internal failure.                                                                                                                               |
| 0x8007000E | Error returned by VARIANT handling library.                                                                                                             |
| 0x80070057 | Requested an out-of-range property. This is not normally returned through this interface because the API calls a property that is known to be in range. |



 

To use this method with Windows Messenger, you must install an add-in component that supports paging.

Actual values used for a mobile device contact must be retrieved through other means. This method determines at the top-level only whether mobile contact information exists.

Assuming the [**MessengerContact**](im-messengercontact.md) object can be successfully created (which can only be done with an online client), calling this method against a **MessengerContact** object while the client is offline will always return *pBoolPage*==FALSE, even if the contact can be paged. Property information cannot be determined while offline, but will not throw an error.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub mnuCanPage_Click()
    On Error Resume Next
    Dim strSigninName As String
    Dim strServiceID As String
    'Get selected contact
    strSigninName = ListContact.SelectedItem.SubItems(2)
    strServiceID = ListContact.SelectedItem.SubItems(5)
    Set MsgrContact = Nothing
    Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
    ErrorTrap ("GetContact")    'Error handling routine
    If MsgrContact.CanPage = True Then
        MsgBox("Contact: " & CStr(MsgrContact.SigninName) & " can be Paged")
    Else
        MsgBox("Contact: " & CStr(MsgrContact.SigninName) & " CANNOT be Paged")
    End If
    ErrorTrap ("Contact.CanPage")   'Error handling routine
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
</dt> </dl>

 

 





