---
title: IPOP3Transport CommandSTAT method
description: Sends the STAT command to the server.
ms.assetid: 72770e62-fce3-4d5a-88bf-62c3102d245e
keywords:
- CommandSTAT method Windows Mail (formerly Outlook Express)
- CommandSTAT method Windows Mail (formerly Outlook Express) , IPOP3Transport interface
- IPOP3Transport interface Windows Mail (formerly Outlook Express) , CommandSTAT method
topic_type:
- apiref
api_name:
- IPOP3Transport.CommandSTAT
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPOP3Transport::CommandSTAT method

\[**IPOP3Transport::CommandSTAT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the STAT command to the server.

## Syntax


```C++
HRESULT CommandSTAT();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                     |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success. <br/>                                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed. <br/>                |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>            | Indicates that a connection to the server has not been established. <br/> |
| <dl> <dt>**IXP\_E\_BUSY**</dt> </dl>                 | Indicates that the server connection is busy. <br/>                       |
| <dl> <dt>**IXP\_E\_SOCKET\_WRITE\_ERROR**</dt> </dl> | Indicates that a transmission error occurred. <br/>                       |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





