---
title: IMessengerGroup RemoveContact method
description: Removes a contact from the group.
ms.assetid: 341b532c-8328-4ca0-bd3a-6a0fb3cf36f2
keywords:
- RemoveContact method Windows Messenger
- RemoveContact method Windows Messenger , IMessengerGroup interface
- IMessengerGroup interface Windows Messenger , RemoveContact method
topic_type:
- apiref
api_name:
- IMessengerGroup.RemoveContact
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

# IMessengerGroup::RemoveContact method

\[**RemoveContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Removes a contact from the group.

## Syntax


```C++
HRESULT RemoveContact(
  [in] VARIANT vContact
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

**VARIANT** that can take as its value either a VT\_BSTR string or a VT\_DISPATCH pointer to an existing [**MessengerContact**](im-messengercontact.md) object. If the input value type is a string, this method creates a new **MessengerContact** object internally. The string should be the full sign-in name. For a netmsgrsvc contact, this should include the "at" sign (@) and domain name. If the input value type is a pointer to an existing **MessengerContact** object (should be type VT\_DISPATCH), the existing object is used.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>             | *vContact* is **NULL**, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or - <br/> *vContact* is VT\_BStr that exceeded 129 characters (130 if the string terminator is included in the count. This allows for a 64-character sign-in name, @ symbol, and a 64-character domain name. This format does not have to be followed.)<br/> - or - <br/> *vContact* is VT\_BStr and contains a carriage return or linefeed.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                   | General failure.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>  | Client is offline.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <dl> <dt>**MSGR\_E\_USER\_NOT\_FOUND**</dt> </dl> | The user specified to be removed does not exist.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

## Remarks

The following table lists the error codes returned by this method.



|                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004005                | General failure.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 0x80070057                | *vContact* is a **NULL** string, or a string that has a space as the first character.<br/> - or - *vContact* is VT\_BStr that exceeded 129 characters (130 if the string terminator is included in the count. This allows for a 64-character sign-in name, @ symbol, and a 64-character domain name. This format does not have to be followed.)<br/> - or - *vContact* is VT\_BStr and contains a carriage return or linefeed.<br/> |
| MSGR\_E\_NOT\_LOGGED\_ON  | Client is offline.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| MSGR\_E\_USER\_NOT\_FOUND | The user specified to be removed does not exist                                                                                                                                                                                                                                                                                                                                                                                                       |



 

> [!Note]  
> This method is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrGroup As MessengerAPI.IMessengerGroup

Private Sub btnGroupRemoveContact_Click()
    On Error Resume Next
    FormAddRemoveContact_Group.Show vbModal 'Get user input
    If bDialogCancel = False Then
        MsgrGroup.RemoveContact strContactName
        populateListView    'Refresh contact list
    End If
    ErrorTrap ("MsgrGroup.RemoveContact")   'Error handling routine
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

[**IMessengerGroup**](im-imessengergroup.md)
</dt> </dl>

 

 





