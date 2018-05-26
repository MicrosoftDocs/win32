---
title: IMessenger MySigninName property
description: IMessenger MySigninName is no longer available for use as of Windows Vista.
ms.assetid: f28850d2-929b-4f56-b448-5db56d2a8f76
keywords:
- MySigninName property Windows Messenger
- MySigninName property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , MySigninName property
topic_type:
- apiref
api_name:
- IMessenger.MySigninName
- IMessenger.get_MySigninName
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

# IMessenger::MySigninName property

\[**IMessenger::MySigninName** is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

Sign-in name. Use [**MySigninName**](im-imessengerservice-mysigninname.md) instead. To return a list of [**MessengerService**](im-messengerservice.md) objects, use the [**Services**](im-imessenger-services.md) property.

This property is read-only.

## Syntax


```C++
HRESULT get_MySigninName(
  [out, retval] BSTR *pbstrName
);
```



## Property value

Return value. A pointer to a **BSTR** that contains the current user's sign-in name.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrName* is a **NULL** pointer. <br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | String comparison failed. <br/>          |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Local client is offline. <br/>           |
| <dl> <dt>MSGR\_E\_NOT\_LOGGED\_ON</dt> </dl>   | Client is offline. <br/>                 |



## Remarks

This property fails if the local client is offline. This property does not recheck the user store for the current user's sign-in name. The value returned will be the value entered on the client upon the initial sign-in for this session, which is cleared when the current user signs out.

The Microsoft .NET Messenger Service client can potentially be signed in to multiple services. The client must be signed in to the primary service; if multiple services are enabled, this property returns the sign-in name for the primary service only. For the Microsoft .NET Messenger Service, the sign-in name is a Windows Live ID sign-in name and thus will follow validation rules for email addresses and correspond to a Windows Live ID identity. For other services, the sign-in name may follow different validation rules.

> [!Note]  
> This property is not available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**MySigninName**](im-imessengerservice-mysigninname.md)
</dt> </dl>

 

 





