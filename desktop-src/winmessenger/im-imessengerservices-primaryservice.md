---
title: IMessengerServices PrimaryService property
description: Returns the MessengerService object for the primary service for the primary client.
ms.assetid: b15e9e97-00f8-46b3-b2b3-004768879197
keywords:
- PrimaryService property Windows Messenger
- PrimaryService property Windows Messenger , IMessengerServices interface
- IMessengerServices interface Windows Messenger , PrimaryService property
topic_type:
- apiref
api_name:
- IMessengerServices.PrimaryService
- IMessengerServices.get_PrimaryService
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

# IMessengerServices::PrimaryService property

\[**PrimaryService** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Returns the [**MessengerService**](im-messengerservice.md) object for the primary service for the primary client.

This property is read-only.

## Syntax


```C++
HRESULT get_PrimaryService(
  [out, retval] IDispatch **ppService
);
```



## Property value

Address of a pointer to a [**IMessengerService**](im-imessengerservice.md) interface that represents the primary service.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                       |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *ppService* is a **NULL** pointer.<br/> |



## Remarks

This property does not return any error codes.

The primary service is the service used when the [**AutoSignin**](im-imessenger-autosignin.md) method is called.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrServices As MessengerAPI.IMessengerServices
Public MsgrService As MessengerAPI.IMessengerService

Private Sub btnServicesPrimaryService_Click()
    On Error Resume Next
    Set MsgrService = Nothing
    Set MsgrService = MsgrServices.PrimaryService
    MsgBox("Primary service : " & MsgrService.ServiceName)
    ErrorTrap ("MsgrServices.PrimaryService")   'Error handling routine
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

[**IMessengerServices**](im-imessengerservices.md)
</dt> <dt>

[Using the Registration Mechanism](im-registration-mechanism.md)
</dt> </dl>

 

 





