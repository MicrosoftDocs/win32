---
title: IMessengerGroups Remove method
description: Removes a MessengerGroup object from a collection.
ms.assetid: '49e6513e-ad60-4533-85f6-6c492963066a'
keywords: ["Remove method Windows Messenger", "Remove method Windows Messenger , IMessengerGroups interface", "IMessengerGroups interface Windows Messenger , Remove method"]
topic_type:
- apiref
api_name:
- IMessengerGroups.Remove
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerGroups::Remove method

\[**Remove** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Removes a [**MessengerGroup**](im-messengergroup.md) object from a collection.

## Syntax


```C++
HRESULT Remove(
  [in] IDispatch *pMGroup
);
```



## Parameters

<dl> <dt>

*pMGroup* \[in\]
</dt> <dd>

Type: **IDispatch\***

Pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerGroup**](im-messengergroup.md) object to be removed from the collection.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                              |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success<br/>                                                                                       |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Object pointed to by *pGroup* is not in the collection (as determined locally by the client).<br/> |
| <dl> <dt>**E\_POINTER** </dt> </dl>              | *pGroup* is a **NULL** pointer.<br/>                                                               |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>               | Cannot be accessed through scripting.<br/>                                                         |
| <dl> <dt>**MSGR\_E\_CANNOT\_DELETE** </dt> </dl> | The group "Other Contacts" is read-only and cannot be deleted.<br/>                                |
| <dl> <dt>**MSGR\_E\_CONNECT**</dt> </dl>         | The client was not logged on.<br/>                                                                 |



 

## Remarks

The following table lists the error codes returned by this method.



| Error Code              | Meaning                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------|
| 0x80004001              | Cannot be accessed through scripting.                                                         |
| 0x80004005              | Object pointed to by *pGroup* is not in the collection (as determined locally by the client). |
| MSGR\_E\_CANNOT\_DELETE | The group "Other Contacts" is read-only and cannot be deleted.                                |
| MSGR\_E\_CONNECT        | The client was not logged on.                                                                 |



 

> [!Note]  
> This method is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrGroups As MessengerAPI.IMessengerGroups

Private Sub btnGroupsRemove_Click()
    On Error Resume Next
    FormRemoveGroup.Show vbModal    'Get user input
    If bDialogCancel = False Then   
    Dim found As Long 
        found = FindGroupbyName(strGroupName)   'function to get group by name 
        If found &amp;lt;&amp;gt;  -1 Then
            Set MsgrGroups = Nothing
            Set MsgrGroups = MsgrUIA.MyGroups
            MsgrGroups.Remove MsgrGroups.Item(found)
        Else
            MsgBox("Remove Group: " & strGroupName & "NOTFOUND")
        End If
        populateListView    'Refresh contact list
    End If
    ErrorTrap ("Groups.Remove") 'Error handling routine
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

[**IMessengerGroups**](im-imessengergroups.md)
</dt> </dl>

 

 





