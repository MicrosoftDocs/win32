---
title: IMessengerContact ServiceID property
description: Retrieves the service ID, a GUID, for the contact associated with this MessengerContact object.
ms.assetid: 463378c3-ad57-43ea-b7ba-a4412584d84a
keywords:
- ServiceID property Windows Messenger
- ServiceID property Windows Messenger , IMessengerContact interface
- IMessengerContact interface Windows Messenger , ServiceID property
topic_type:
- apiref
api_name:
- IMessengerContact.ServiceID
- IMessengerContact.get_ServiceID
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

# IMessengerContact::ServiceID property

\[**ServiceID** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the service ID, a GUID, for the contact associated with this [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_ServiceID(
  [out, retval] BSTR *pbstrServiceID
);
```



## Property value

Pointer to a **BSTR** that contains a GUID that uniquely identifies the service used by this contact. This can be a secondary service contact and therefore may return an ID other than the one for the Microsoft .NET Messenger Service.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                            |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                               |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | General internal failure.<br/>               |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrServiceID* is a **NULL** pointer.<br/> |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                   |
|------------|---------------------------|
| 0x80004005 | General internal failure. |



 

Clients may wish to compare [**MyServiceId**](im-imessenger-myserviceid.md) (the client's service ID) to **ServiceID**. A match of services may allow service-specific functionality that is not possible if the local and remote users are on different services.

Stored service IDs for secondary services may also be useful if it is necessary to create [**MessengerContact**](im-messengercontact.md) objects that correspond to secondary service contacts (through [**GetContact**](im-imessenger-getcontact.md), which requires the service ID as a parameter).

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub btnServiceID_Click()
    On Error Resume Next
    Dim strSigninName As String
    Dim strServiceID As String
    'Get selected contact
    strSigninName = ListContact.SelectedItem.SubItems(2)
    strServiceID = ListContact.SelectedItem.SubItems(5)
    Set MsgrContact = Nothing
    Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
    ErrorTrap ("GetContact")    'Error handling routine
    MsgBox("Contact ServiceID: " & CStr(MsgrContact.ServiceId))
    ErrorTrap ("Contact.ServiceID") 'Error handling routine
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
</dt> <dt>

[**ServiceName**](im-imessengercontact-servicename.md)
</dt> </dl>

 

 





