---
title: IMessengerGroup AddContact method
description: Adds a contact to the group.
ms.assetid: f42a2052-5cfa-46ef-b204-e4a759da8db0
keywords:
- AddContact method Windows Messenger
- AddContact method Windows Messenger , IMessengerGroup interface
- IMessengerGroup interface Windows Messenger , AddContact method
topic_type:
- apiref
api_name:
- IMessengerGroup.AddContact
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

# IMessengerGroup::AddContact method

\[**AddContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Adds a contact to the group.

## Syntax


```C++
HRESULT AddContact(
  [in] VARIANT vContact
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

**VARIANT** that defines the contact to add to the group.

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
| <dl> <dt>**MSGR\_E\_USER\_NOT\_FOUND**</dt> </dl> | The user specified to be added does not exist.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

## Remarks

The following table lists the error codes returned by this method.



|                           |                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004005                | General failure.                                                                                                                                                                                                                                                                                                                                                                                                     |
| 0x80070057                | *vContact* is a **NULL** string, or a string that has a space as the first character. - or - *vContact* is VT\_BStr that exceeded 129 characters (130 if the string terminator is included in the count. This allows for a 64-character sign-in name, @ symbol, and a 64-character domain name. This format does not have to be followed.) - or - *vContact* is VT\_BStr and contains a carriage return or linefeed. |
| MSGR\_E\_NOT\_LOGGED\_ON  | Client is offline.                                                                                                                                                                                                                                                                                                                                                                                                   |
| MSGR\_E\_USER\_NOT\_FOUND | The user specified to be added does not exist.                                                                                                                                                                                                                                                                                                                                                                       |



 

> [!Note]  
> This method is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```
  Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrGroup As MessengerAPI.IMessengerGroup

Private Sub btnGroupAddContact_Click()
    On Error Resume Next
    FormAddContact_Group.Show vbModal   'Get user input
    If bDialogCancel = False Then
        MsgrGroup.AddContact strContactName
        populateListView    'Refresh contact list
    End If
    ErrorTrap ("MsgrGroup.AddContact")  'Error handling routine
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

 

 





