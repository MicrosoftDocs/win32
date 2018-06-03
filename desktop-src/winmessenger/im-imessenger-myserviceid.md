---
title: IMessenger MyServiceId property
description: IMessenger MyServiceId is no longer available for use as of Windows Vista.
ms.assetid: 215a04c7-2961-466d-9b83-333262d1c0d9
keywords:
- MyServiceId property Windows Messenger
- MyServiceId property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , MyServiceId property
topic_type:
- apiref
api_name:
- IMessenger.MyServiceId
- IMessenger.get_MyServiceId
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

# IMessenger::MyServiceId property

\[**IMessenger::MyServiceId** is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

Retrieves the service ID, a GUID, of the primary service to which the local client user is currently signed in. Use [**ServiceID**](im-imessengerservice-serviceid.md) instead. To return a list of [**MessengerService**](im-messengerservice.md) objects, use the [**Services**](im-imessenger-services.md) property.

This property is read-only.

## Syntax


```C++
HRESULT get_MyServiceId(
  [out, retval] BSTR *pbstrServiceId
);
```



## Property value

Return value. Pointer to a **BSTR** that contains a GUID that uniquely identifies the service used by the local client user.

## Error codes

Returns one of the following values.



| Name                                                                               | Meaning                      |
|------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>S\_OK</dt> </dl>   | Success. <br/>         |
| <dl> <dt>E\_FAIL</dt> </dl> | General failure. <br/> |



## Remarks

If the local client is offline, this method returns the service ID of the default service.

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



 

 





