---
title: IMessengerService ServiceName property
description: Retrieves the service name of the contact associated with this MessengerContact object.
ms.assetid: '6ab463a4-d4fd-4665-9caa-a48401e9cc7d'
keywords: ["ServiceName property Windows Messenger", "ServiceName property Windows Messenger , IMessengerService interface", "IMessengerService interface Windows Messenger , ServiceName property"]
topic_type:
- apiref
api_name:
- IMessengerService.ServiceName
- IMessengerService.get_ServiceName
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerService::ServiceName property

\[**ServiceName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the service name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_ServiceName(
  [out, retval] BSTR *pbstrServiceName
);
```



## Property value

Pointer to a **BSTR** containing a string that identifies the service used by this contact.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                              |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                 |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrServiceName* is a **NULL** pointer.<br/> |
| <dl> <dt>E\_FAIL</dt> </dl>                    | General failure.<br/>                          |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Internal string copy failed.<br/>              |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                      |
|------------|------------------------------|
| 0x80004005 | General internal failure.    |
| 0x8007000E | Internal string copy failed. |



 

This method is useful for obtaining human-readable, service-identifying strings to be used in the UI.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrService As MessengerAPI.IMessengerService

Private Sub btnServiceServiceName_Click()
    On Error Resume Next
    MsgBox("Service Name: " & MsgrService.ServiceName)
    ErrorTrap ("MsgrService.Name")  'Error handling routine
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

[**IMessengerService**](im-imessengerservice.md)
</dt> <dt>

[**ServiceID**](im-imessengerservice-serviceid.md)
</dt> </dl>

 

 





