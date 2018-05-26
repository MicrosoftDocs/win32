---
title: IMessenger MyFriendlyName property
description: IMessenger MyFriendlyName is no longer available for use as of Windows Vista.
ms.assetid: bdff566b-b6e6-46df-b952-ead936a853fe
keywords:
- MyFriendlyName property Windows Messenger
- MyFriendlyName property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , MyFriendlyName property
topic_type:
- apiref
api_name:
- IMessenger.MyFriendlyName
- IMessenger.get_MyFriendlyName
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

# IMessenger::MyFriendlyName property

\[**IMessenger::MyFriendlyName** is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

Retrieves the friendly (display) name of the local client user. Use [**MyFriendlyName**](im-imessengerservice-myfriendlyname.md) instead. To return a list of [**MessengerService**](im-messengerservice.md) objects, use the [**Services**](im-imessenger-services.md) property.

This property is read-only.

## Syntax


```C++
HRESULT get_MyFriendlyName(
  [out, retval] BSTR *pbstrName
);
```



## Property value

Return value. Pointer to a **BSTR** that contains the current user's friendly name.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrName* is a **NULL** pointer. <br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | String comparison failed.<br/>           |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Local user is disconnected.<br/>         |



## Remarks

If the local client is offline when **MyFriendlyName** is called, the call will succeed and *pbstrName* will contain an empty string.

Even when online, this method does not recheck the user store for the current user's friendly name. The value returned will always be the value sent through the protocol upon the initial primary service sign-in.

> [!Note]  
> This property is available for scripting languages only in a trusted zone.

 

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

[**MyFriendlyName**](im-imessengerservice-myfriendlyname.md)
</dt> </dl>

 

 





