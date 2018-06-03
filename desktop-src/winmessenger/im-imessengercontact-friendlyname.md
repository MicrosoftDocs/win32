---
title: IMessengerContact FriendlyName property
description: Retrieves the friendly name of the contact associated with this MessengerContact object.
ms.assetid: 74ca5edc-27ca-441e-b9ca-223c06a85cb9
keywords:
- FriendlyName property Windows Messenger
- FriendlyName property Windows Messenger , IMessengerContact interface
- IMessengerContact interface Windows Messenger , FriendlyName property
topic_type:
- apiref
api_name:
- IMessengerContact.FriendlyName
- IMessengerContact.get_FriendlyName
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

# IMessengerContact::FriendlyName property

\[**FriendlyName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the friendly name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_FriendlyName(
  [out, retval] BSTR *pbstrFriendlyName
);
```



## Property value

Pointer to a **BSTR** that contains the friendly name of this user.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                    |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                       |
| <dl> <dt>E\_FAIL</dt> </dl>                    | *pbstrFriendlyName* returned a **NULL** string.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Error returned by VARIANT handling library.<br/>     |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrFriendlyName* was a **NULL** pointer.<br/>     |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                         |
|------------|-------------------------------------------------|
| 0x80004005 | *pbstrFriendlyName* returned a **NULL** string. |
| 0x8007000E | String comparison failed.                       |



 

The friendly name is used in conjunction with the sign-in name primarily for UI display. Because a friendly name is not guaranteed to be unique, it is good practice to display both the sign-in and friendly names for any contact viewed within a client.

> [!Note]  
> This property is available for scripting languages only in a trusted zone.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub btnFriendlyName_Click()
    On Error Resume Next
    Dim strSigninName As String
    Dim strServiceID As String
    'Get selected contact
    strSigninName = ListContact.SelectedItem.SubItems(2)
    strServiceID = ListContact.SelectedItem.SubItems(5)
    sbStatus.Panels.Item(1).Text = "Selected: " & strSigninName & " : " & strServiceID
    Set MsgrContact = Nothing
    Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
    ErrorTrap ("GetContact")    'Error handling routine
    MsgBox("Contact FriendlyName: " & CStr(MsgrContact.FriendlyName))
    ErrorTrap ("Contact.FriendlyName")  'Error handling routine
End Sub
```



## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessengerContact**](im-imessengercontact.md)
</dt> <dt>

[**SigninName**](im-imessengercontact-signinname.md)
</dt> <dt>

[**OnContactFriendlyNameChange**](im-dmessengerevents-oncontactfriendlynamechange.md)
</dt> </dl>

 

 





