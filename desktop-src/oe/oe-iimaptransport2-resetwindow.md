---
title: IIMAPTransport2 ResetWindow method
description: Closes the current window used for asynchronous Windows Sockets (Winsock) processing.
ms.assetid: 56eecbe4-d08f-43b7-9863-35419d93736e
keywords:
- ResetWindow method Windows Mail (formerly Outlook Express)
- ResetWindow method Windows Mail (formerly Outlook Express) , IIMAPTransport2 interface
- IIMAPTransport2 interface Windows Mail (formerly Outlook Express) , ResetWindow method
topic_type:
- apiref
api_name:
- IIMAPTransport2.ResetWindow
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

# IIMAPTransport2::ResetWindow method

\[**IIMAPTransport2::ResetWindow** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Closes the current window used for asynchronous Windows Sockets (Winsock) processing.

## Syntax


```C++
HRESULT ResetWindow();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**NOERROR**</dt> </dl>       | Indicates success. <br/>                            |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Indicates that an unknown error has occurred. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





