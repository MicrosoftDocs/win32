---
title: IMessengerContact ServiceName property
description: Retrieves the service name of the contact associated with this MessengerContact object.
ms.assetid: 0c2692a7-152e-4b6c-9d13-549620cb206f
keywords:
- ServiceName property Windows Messenger
- ServiceName property Windows Messenger , IMessengerContact interface
- IMessengerContact interface Windows Messenger , ServiceName property
topic_type:
- apiref
api_name:
- IMessengerContact.ServiceName
- IMessengerContact.get_ServiceName
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

# IMessengerContact::ServiceName property

\[**ServiceName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the service name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_ServiceName(
  [out, retval] BSTR *pbstrServiceName
);
```



## Property value

Pointer to a **BSTR** that contains a string that identifies the service used by this contact.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                              |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                 |
| <dl> <dt>E\_FAIL</dt> </dl>                    | General internal failure.<br/>                 |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Internal string copy failed.<br/>              |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrServiceName* is a **NULL** pointer.<br/> |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be accessed through scripting.<br/>     |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                      |
|------------|------------------------------|
| 0x80004005 | General internal failure.    |
| 0x8007000E | Internal string copy failed. |



 

This method is useful for obtaining human-readable, service-identifying strings to be used in the user interface (UI). The service ID (obtained through [**ServiceID**](im-imessengercontact-serviceid.md)) will be more useful in the Windows Messenger APIs.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub btnServiceName_Click()
    On Error Resume Next
    Dim strSigninName As String
    Dim strServiceID As String
    'Get selected contact
    strSigninName = ListContact.SelectedItem.SubItems(2)
    strServiceID = ListContact.SelectedItem.SubItems(5)
    Set MsgrContact = Nothing
    Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
    ErrorTrap ("GetContact")    'Error handling routine
    MsgBox("Contact ServiceName: " & CStr(MsgrContact.ServiceName))
    ErrorTrap ("Contact.ServiceName")   'Error handling routine
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

[**MyServiceName**](im-imessenger-myservicename.md)
</dt> </dl>

 

 





