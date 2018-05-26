---
title: IMessengerService ServiceID property
description: Retrieves the service ID of the contact associated with the selected service.
ms.assetid: 9acbb2de-1c5d-4f49-83c8-54d2eb0c4f80
keywords:
- ServiceID property Windows Messenger
- ServiceID property Windows Messenger , IMessengerService interface
- IMessengerService interface Windows Messenger , ServiceID property
topic_type:
- apiref
api_name:
- IMessengerService.ServiceID
- IMessengerService.get_ServiceID
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

# IMessengerService::ServiceID property

\[**ServiceID** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the service ID of the contact associated with the selected service.

This property is read-only.

## Syntax


```C++
HRESULT get_ServiceID(
  [out, retval] BSTR *pbstrID
);
```



## Property value

Pointer to a **BSTR** that contains a string that identifies the service ID used by this contact.

## Error codes

Returns one of the following values. 



| Name                                                                                     | Meaning                                     |
|------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | Success. <br/>                        |
| <dl> <dt>E\_FAIL</dt> </dl>       | General failure.<br/>                 |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | *pbstrID* is a **NULL** pointer.<br/> |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning          |
|------------|------------------|
| 0x80004005 | General failure. |



 

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrService As MessengerAPI.IMessengerService

Private Sub btnServiceServiceID_Click()
    On Error Resume Next
    MsgBox("Service ID: " & MsgrService.ServiceID)
    ErrorTrap ("MsgrService.Name")  'Error handling routine
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

[**IMessengerService**](im-imessengerservice.md)
</dt> <dt>

[**ServiceName**](im-imessengerservice-servicename.md)
</dt> </dl>

 

 





