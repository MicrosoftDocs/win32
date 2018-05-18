---
title: IMessengerContact SigninName property
description: Retrieves the sign-in name of the contact associated with this MessengerContact object.
ms.assetid: '9dc784b1-ab71-42bd-880c-f5623f71b95a'
keywords: ["SigninName property Windows Messenger", "SigninName property Windows Messenger , IMessengerContact interface", "IMessengerContact interface Windows Messenger , SigninName property"]
topic_type:
- apiref
api_name:
- IMessengerContact.SigninName
- IMessengerContact.get_SigninName
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerContact::SigninName property

\[**SigninName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the sign-in name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_SigninName(
  [out, retval] BSTR *pbstrSigninName
);
```



## Property value

Pointer to a **BSTR** that uniquely identifies the contact.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                 |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                    |
| <dl> <dt>E\_FAIL</dt> </dl>                    | *pbstrSigninName* returns a **NULL** string.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | String comparison failed.<br/>                    |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrSigninName* is a **NULL** pointer.<br/>     |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be accessed through scripting.<br/>        |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                      |
|------------|----------------------------------------------|
| 0x80004001 | Cannot be accessed through scripting.        |
| 0x80004005 | *pbstrSigninName* returns a **NULL** string. |
| 0x8007000E | String comparison failed.                    |



 

To get the sign-in name of the local client user rather than a remote user, use [**MySigninName**](im-imessenger-mysigninname.md).

> [!Note]  
> This property is available to scripting languages only in a trusted zone.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub btnSigninName_Click()
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
    MsgBox("Contact SigninName: " & CStr(MsgrContact.SigninName))
    ErrorTrap ("Contact.SigninName")    'Error handling routine
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

[**FriendlyName**](im-imessengercontact-friendlyname.md)
</dt> </dl>

 

 





