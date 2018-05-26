---
title: ISMTPTransport CommandDATA method
description: Sends the DATA command to the server.
ms.assetid: 855a7473-2629-4ff0-b15e-fcd60587bb66
keywords:
- CommandDATA method Windows Mail (formerly Outlook Express)
- CommandDATA method Windows Mail (formerly Outlook Express) , ISMTPTransport interface
- ISMTPTransport interface Windows Mail (formerly Outlook Express) , CommandDATA method
topic_type:
- apiref
api_name:
- ISMTPTransport.CommandDATA
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

# ISMTPTransport::CommandDATA method

\[**ISMTPTransport::CommandDATA** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the DATA command to the server.

## Syntax


```C++
HRESULT CommandDATA();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





