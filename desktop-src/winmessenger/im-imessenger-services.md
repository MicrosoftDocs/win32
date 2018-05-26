---
title: IMessenger Services property
description: Returns a list of services being used by the Messenger client.
ms.assetid: 9d3e33ac-8794-4cc7-9a62-d4d3119d878a
keywords:
- Services property Windows Messenger
- Services property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , Services property
topic_type:
- apiref
api_name:
- IMessenger.Services
- IMessenger.get_Services
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

# IMessenger::Services property

\[**Services** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Returns a list of services being used by the Messenger client.

This property is read-only.

## Syntax


```C++
HRESULT get_Services(
  [out, retval] IDispatch **ppdispServices
);
```



## Property value

Return Value. Pointer to a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerServices**](im-messengerservices.md) collection object.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                           |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                              |
| <dl> <dt>PRC\_X\_NULL\_REF\_POINTER</dt> </dl> | *ppdispServices*is a **NULL** pointer.<br/> |



## Remarks

> [!Note]  
> This property is available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





