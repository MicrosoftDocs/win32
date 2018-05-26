---
title: IMessengerService MyStatus property
description: Retrieves the status of the local user in a service.
ms.assetid: 4fa1c7a4-63aa-40ad-bbb9-9b693e4a5634
keywords:
- MyStatus property Windows Messenger
- MyStatus property Windows Messenger , IMessengerService interface
- IMessengerService interface Windows Messenger , MyStatus property
topic_type:
- apiref
api_name:
- IMessengerService.MyStatus
- IMessengerService.get_MyStatus
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

# IMessengerService::MyStatus property

\[**MyStatus** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the status of the local user in a service.

This property is read-only.

## Syntax


```C++
HRESULT get_MyStatus(
  [out, retval] MISTATUS *pmiStatus
);
```



## Property value

Pointer to the [**MISTATUS**](im-mistatus.md) of the user.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                       |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pmiStatus* is a **NULL** pointer.<br/> |



## Remarks

This property does not return any error codes.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrService As MessengerAPI.IMessengerService

Private Sub btnServiceStatus_Click()
    On Error Resume Next
    MsgBox("Service status= " & ServiceStatusLookup(MsgrService.MyStatus))
    ErrorTrap ("MsgrService.MyStatus")  'Error handling routine
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

[**MyFriendlyName**](im-imessengerservice-myfriendlyname.md)
</dt> <dt>

[**MySigninName**](im-imessengerservice-mysigninname.md)
</dt> </dl>

 

 





