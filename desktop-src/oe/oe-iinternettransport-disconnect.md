---
title: IInternetTransport Disconnect method
description: This method disconnects the transport. This method may cause the transport to send a command, such as the QUIT command, to the server.
ms.assetid: a40ad499-326c-4bed-9ed1-cbffd414bb55
keywords:
- Disconnect method Windows Mail (formerly Outlook Express)
- Disconnect method Windows Mail (formerly Outlook Express) , IInternetTransport interface
- IInternetTransport interface Windows Mail (formerly Outlook Express) , Disconnect method
topic_type:
- apiref
api_name:
- IInternetTransport.Disconnect
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

# IInternetTransport::Disconnect method

\[**IInternetTransport::Disconnect** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This method disconnects the transport. This method may cause the transport to send a command, such as the QUIT command, to the server.

## Syntax


```C++
HRESULT Disconnect();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                           | Description                                                        |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Indicates success. <br/>                                     |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>      | Indicates that the transport has not been initialized. <br/> |
| <dl> <dt>**IXP\_E\_NOT\_CONNECTED**</dt> </dl> | Indicates that the transport is not connected. <br/>         |



 

## Remarks

The **IInternetTransport::Disconnect** method terminates the connection to the server and allows the server to clean up the session. The [**IInternetTransport::DropConnection**](oe-iinternettransport-dropconnection.md) method immediately breaks the server connection without allowing for session clean-up.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





