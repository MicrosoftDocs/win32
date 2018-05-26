---
title: IMessengerContact IsSelf property
description: Retrieves a Boolean value that declares whether the contact associated with this MessengerContact object is actually the current client user.
ms.assetid: d4effff8-b80f-405f-a58c-98e3f7ebb018
keywords:
- IsSelf property Windows Messenger
- IsSelf property Windows Messenger , IMessengerContact interface
- IMessengerContact interface Windows Messenger , IsSelf property
topic_type:
- apiref
api_name:
- IMessengerContact.IsSelf
- IMessengerContact.get_IsSelf
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

# IMessengerContact::IsSelf property

\[**IsSelf** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a Boolean value that declares whether the contact associated with this [**MessengerContact**](im-messengercontact.md) object is actually the current client user.

This property is read-only.

## Syntax


```C++
HRESULT get_IsSelf(
  [out, retval] VARIANT_BOOL *pBoolSelf
);
```



## Property value

Pointer to a **VARIANT\_BOOL** that declares whether this [**MessengerContact**](im-messengercontact.md) object is the same user as the current client user (determined by a comparison of sign-in names, which are unique per service). VARIANT\_TRUE means the contact is the current client user. VARIANT\_FALSE means the contact is not the current client user.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                    |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                       |
| <dl> <dt>E\_FAIL</dt> </dl>                    | *pbstrFriendlyName* returned a **NULL** string.<br/> |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pBoolSelf* was a **NULL** pointer.<br/>             |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                                 |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004005 | General internal failure.                                                                                                                               |
| 0x8007000E | Error returned by VARIANT handling library.                                                                                                             |
| 0x80070057 | Requested an out-of-range property. This is not normally returned through this interface because the API calls a property that is known to be in range. |



 

The **IsSelf** property is scriptable.

Although users can add themselves as a contact, the Messenger client blocks users from sending instant messages to themselves. Other clients may duplicate this enforcement by checking this method's value before calling methods such as [**InstantMessage**](im-imessenger-instantmessage.md).

If this method is called while the client is offline, it will not fail, but will always return **FALSE**, even if the user represented by the [**MessengerContact**](im-messengercontact.md) object and the local client user are the same.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub mnuIsSelf_Click()
    On Error Resume Next
    Dim strSigninName As String
    Dim strServiceID As String
    'Get selected contact
    strSigninName = ListContact.SelectedItem.SubItems(2)
    strServiceID = ListContact.SelectedItem.SubItems(5)
    Set MsgrContact = Nothing
    Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
    ErrorTrap ("GetContact")    'Error handling routine
    If MsgrContact.IsSelf = True Then
        MsgBox("Contact: " & CStr(MsgrContact.SigninName) & " is self")
    Else
        MsgBox("Contact: " & CStr(MsgrContact.SigninName) & " is NOT self")
    End If
    ErrorTrap ("Contact.IsSelf")    'Error handling routine
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

[**MySigninName**](im-imessenger-mysigninname.md)
</dt> </dl>

 

 





