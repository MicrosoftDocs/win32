---
title: IMessenger MyServiceName property
description: IMessenger MyServiceName is no longer available for use as of Windows Vista.
ms.assetid: 98c67b67-6279-4c47-bdb8-1362e4e6e52b
keywords:
- MyServiceName property Windows Messenger
- MyServiceName property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , MyServiceName property
topic_type:
- apiref
api_name:
- IMessenger.MyServiceName
- IMessenger.get_MyServiceName
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

# IMessenger::MyServiceName property

\[**IMessenger::MyServiceName** is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

Retrieves the service name of the primary service to which the local client user is currently signed in. Use [**ServiceName**](im-imessengerservice-servicename.md) instead. To return a list of [**MessengerService**](im-messengerservice.md) objects, use the [**Services**](im-imessenger-services.md) property.

This property is read-only.

## Syntax


```C++
HRESULT get_MyServiceName(
  [out, retval] BSTR *pbstrServiceName
);
```



## Property value

Return value. A pointer to the string that identifies the primary service.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                  |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | [**MySigninName**](im-imessenger-mysigninname.md) is a **NULL** pointer. <br/> |



## Remarks

If the local client is offline, this property returns the string of the default service. The default service and the primary service are usually the same.

> [!Note]  
> This property is available for scripting languages.

 

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

[**ServiceName**](im-imessengerservice-servicename.md)
</dt> </dl>

 

 





