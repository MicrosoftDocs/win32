---
title: INNTPTransport CommandQUIT method
description: Issues a QUIT command to the server and terminates the connection.
ms.assetid: '60fabbd6-59c3-4a35-bb39-02cc073fdbd8'
keywords: ["CommandQUIT method Windows Mail (formerly Outlook Express)", "CommandQUIT method Windows Mail (formerly Outlook Express) , INNTPTransport interface", "INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandQUIT method"]
topic_type:
- apiref
api_name:
- INNTPTransport.CommandQUIT
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport::CommandQUIT method

\[**INNTPTransport::CommandQUIT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues a `QUIT` command to the server and terminates the connection.

## Syntax


```C++
HRESULT CommandQUIT();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns the following value.



| Return code                                                                                   | Description                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An memory allocation failed<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





