---
title: IMessengerService MySigninName property
description: Retrieves the local user's sign-in name that corresponds to the selected service.
ms.assetid: 'f0793434-a952-452f-a9e1-d94725200b25'
keywords: ["MySigninName property Windows Messenger", "MySigninName property Windows Messenger , IMessengerService interface", "IMessengerService interface Windows Messenger , MySigninName property"]
topic_type:
- apiref
api_name:
- IMessengerService.MySigninName
- IMessengerService.get_MySigninName
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerService::MySigninName property

\[**MySigninName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the local user's sign-in name that corresponds to the selected service.

This property is read-only.

## Syntax


```C++
HRESULT get_MySigninName(
  [out, retval] BSTR *pbstrName
);
```



## Property value

**BSTR** that contains the sign-in name for the local user of this service.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                            |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                               |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrName* is a **NULL** pointer.<br/>      |
| <dl> <dt>E\_FAIL</dt> </dl>                    | *pbstrName* returned a **NULL** string.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | String comparison failed.<br/>               |
| <dl> <dt>MSGR\_E\_NOT\_LOGGED\_ON</dt> </dl>   | This service is offline.<br/>                |



## Remarks

The following table lists error codes returned by this method.



| Error Code               | Meaning                                                  |
|--------------------------|----------------------------------------------------------|
| 0x80004005               | *pbstrName* returned a **NULL** string.                  |
| 0x8007000E               | String comparison failed.                                |
| MSGR\_E\_NOT\_LOGGED\_ON | The local user is not logged in to the selected service. |



 

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

> [!Note]  
> This property is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrService As MessengerAPI.IMessengerService

Private Sub btnServiceSigninName_Click()
    On Error Resume Next
    MsgBox("Service SigninName: " & MsgrService.MySigninName)
    ErrorTrap ("MsgrService.FriendlyName")  'Error handling routine
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

[**MySigninName**](im-imessengerservice-mysigninname.md)
</dt> <dt>

[**MyStatus**](im-imessengerservice-mystatus.md)
</dt> <dt>

[**MyFriendlyName**](im-imessengerservice-myfriendlyname.md)
</dt> </dl>

 

 





