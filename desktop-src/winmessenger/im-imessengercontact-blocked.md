---
title: IMessengerContact Blocked property
description: Sets or retrieves a Boolean value that declares whether the contact associated with this MessengerContact object is blocked by the current client user.
ms.assetid: 819af259-e1ec-44d4-bb31-fe6905e650bf
keywords:
- Blocked property Windows Messenger
- Blocked property Windows Messenger , IMessengerContact interface
- IMessengerContact interface Windows Messenger , Blocked property
topic_type:
- apiref
api_name:
- IMessengerContact.Blocked
- IMessengerContact.get_Blocked
- IMessengerContact.put_Blocked
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

# IMessengerContact::Blocked property

\[**Blocked** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves a Boolean value that declares whether the contact associated with this [**MessengerContact**](im-messengercontact.md) object is blocked by the current client user.

This property is read/write.

## Syntax


```C++
HRESULT put_Blocked(
           VARIANT_BOOL vBoolBlock
);

HRESULT get_Blocked(
  [retval] VARIANT_BOOL *pBoolBlock
);
```



## Property value

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                                                                                                |
| <dl> <dt>S\_FALSE</dt> </dl>                   | Attempted to block an already blocked user or unblock a user who was not blocked.<br/>                                                                        |
| <dl> <dt>E\_FAIL</dt> </dl>                    | General internal failure.<br/>                                                                                                                                |
| <dl> <dt>DISP\_E\_BADVARTYPE</dt> </dl>        | Error returned by VARIANT handling library.<br/>                                                                                                              |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Error returned by VARIANT handling library.<br/>                                                                                                              |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | Requested an out-of-range property. This is not normally returned through this interface because the API calls a property that is known to be in range. <br/> |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pBoolBlock* is a **NULL** pointer.<br/>                                                                                                                      |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                                 |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004005 | General internal failure.                                                                                                                               |
| 0x8007000E | Error returned by VARIANT handling library.                                                                                                             |
| 0x80070057 | Requested an out-of-range property. This is not normally returned through this interface because the API calls a property that is known to be in range. |



 

Blocking is not necessarily reciprocal. User A may have blocked User B, but if User B hasn't blocked User A, then User A can still receive status updates about User B (if User B is on User A's contact list). Blocking a user does not remove the user from the **Contact List** or the [**MessengerContacts**](im-messengercontacts.md) collection. Clients should decide how to enforce a logical relationship between blocking users and getting blocked users out of the **Contact List**.

Assuming the [**MessengerContact**](im-messengercontact.md) object can be successfully created (which can only be done with an online client), calling this method against a **MessengerContact** object while the client is offline will always return *pBoolBlock*==**FALSE**, even if the contact in question really is blocked. Property information cannot be determined while offline, but will not throw an error.

Blocking is not necessarily reciprocal. User A may have blocked User B, but if User B has not blocked User A, then User A can still receive status updates about User B (if User B is on User A's contact list). Blocking a user does not remove the user from the contact list or the [**MessengerContacts**](im-messengercontacts.md) collection. Clients should decide how to enforce a logical relationship between blocking users and getting blocked users out of the Contact List.

Assuming the [**MessengerContacts**](im-messengercontacts.md) object can be successfully created (which can only be done with an online client), calling this method against a MessengerContact object while the client is offline will always return **FALSE**, even if the contact in question really is blocked. Property information cannot be determined while offline, but will not throw an error.

> [!Note]  
> This property is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub btnBlocked_Click()
    On Error Resume Next
    Dim strSigninName As String
    Dim strServiceID As String
    'Get selected contact
    strSigninName = ListContact.SelectedItem.SubItems(2)
    strServiceID = ListContact.SelectedItem.SubItems(5)
    Set MsgrContact = Nothing
    Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
    ErrorTrap ("GetContact")    'Error handling routine
    If MsgrContact.Blocked = True Then
        MsgrContact.Blocked = False
        MsgBox("Contact: " & CStr(MsgrContact.SigninName) & " is now Unblocked")
    Else
        MsgrContact.Blocked = True
        MsgBox("Contact: " & CStr(MsgrContact.SigninName) & " is now Blocked")
    End If
    ErrorTrap ("Contact.Blocked")   'Error handling routine
    populateListView    'Refresh contact list
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
</dt> </dl>

 

 





