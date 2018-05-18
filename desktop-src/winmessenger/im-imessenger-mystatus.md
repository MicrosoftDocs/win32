---
title: IMessenger MyStatus property
description: IMessenger MyStatus is no longer available for use as of Windows Vista.
ms.assetid: 'fec2d899-1780-4bf8-9852-88fbab2ccf32'
keywords: ["MyStatus property Windows Messenger", "MyStatus property Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , MyStatus property"]
topic_type:
- apiref
api_name:
- IMessenger.MyStatus
- IMessenger.get_MyStatus
- IMessenger.put_MyStatus
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::MyStatus property

\[**IMessenger::MyStatus** is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

Service status. Use [**MyStatus**](im-imessengerservice-mystatus.md) instead. To return a list of [**MessengerService**](im-messengerservice.md) objects, use the [**Services**](im-imessenger-services.md) property.

This property is read/write.

## Syntax


```C++
HRESULT put_MyStatus(
  [in]          MISTATUS pmiStatus
);

HRESULT get_MyStatus(
  [out, retval] MISTATUS *pmiStatus
);
```



## Property value

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pmiStatus* is a **NULL** pointer. <br/> |



## Remarks

If the local client is offline, this property returns without attempting to connect. Otherwise, this property will always query the server for the client's local state; it will not use locally stored information.

When multiple clients are registered, **get\_MyStatus** returns the status of the primary client at the time of the call. **put\_MyStatus** sets the status for all the services that each registered client is signed into to the status passed in *pmiStatus*. The **HRESULT** returned is from the primary client.

> [!Note]  
> The **get\_MyStatus** property is available for scripting languages; **put\_MyStatus** is not.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**MyStatus**](im-imessengerservice-mystatus.md)
</dt> </dl>

 

 





