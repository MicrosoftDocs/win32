---
title: IInternetTransport DropConnection method
description: This method disconnects the transport.
ms.assetid: 39c5f7d5-2c13-43e6-8e32-0a158004936d
keywords:
- DropConnection method Windows Mail (formerly Outlook Express)
- DropConnection method Windows Mail (formerly Outlook Express) , IInternetTransport interface
- IInternetTransport interface Windows Mail (formerly Outlook Express) , DropConnection method
topic_type:
- apiref
api_name:
- IInternetTransport.DropConnection
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IInternetTransport::DropConnection method

\[**IInternetTransport::DropConnection** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This method disconnects the transport. This is a guaranteed, but not clean, method of breaking the connection between the client and the server.

## Syntax


```C++
HRESULT DropConnection();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                      | Description                                                        |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success. <br/>                                     |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl> | Indicates that the transport has not been initialized. <br/> |



 

## Remarks

The [**IInternetTransport::Disconnect**](oe-iinternettransport-disconnect.md) method allows the protocol to shut down normally.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





