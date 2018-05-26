---
title: IMessengerGroup Service property
description: Retrieves the service object from the group.
ms.assetid: 6bdad54b-76a3-43b8-a37a-473f384494e9
keywords:
- Service property Windows Messenger
- Service property Windows Messenger , IMessengerGroup interface
- IMessengerGroup interface Windows Messenger , Service property
topic_type:
- apiref
api_name:
- IMessengerGroup.Service
- IMessengerGroup.get_Service
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

# IMessengerGroup::Service property

\[**Service** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the service object from the group.

This property is read-only.

## Syntax


```C++
HRESULT get_Service(
  [out, retval] IDispatch **pService
);
```



## Property value

Address of a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) on a [**MessengerService**](im-messengerservice.md) object.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                      |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success.<br/>                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pService* is a **NULL** pointer.<br/> |



## Remarks

This property returns no error codes.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
  Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrGroup As MessengerAPI.IMessengerGroup
Public MsgrService As MessengerAPI.IMessengerService

Private Sub btnGroupService_Click()
    On Error Resume Next
    Set MsgrService = Nothing
    Set MsgrService = MsgrGroup.Service
    ErrorTrap ("IMessengerGroup.Service")
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

 

 





