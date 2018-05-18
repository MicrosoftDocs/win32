---
title: IPOP3Transport CommandNOOP method
description: Sends the NOOP command to the server.
ms.assetid: '89cbfd2d-af29-49f4-9b4b-68d62b47a63e'
keywords: ["CommandNOOP method Windows Mail (formerly Outlook Express)", "CommandNOOP method Windows Mail (formerly Outlook Express) , IPOP3Transport interface", "IPOP3Transport interface Windows Mail (formerly Outlook Express) , CommandNOOP method"]
topic_type:
- apiref
api_name:
- IPOP3Transport.CommandNOOP
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IPOP3Transport::CommandNOOP method

\[**IPOP3Transport::CommandNOOP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the NOOP command to the server.

## Syntax


```C++
HRESULT CommandNOOP();
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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





