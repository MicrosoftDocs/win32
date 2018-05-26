---
title: ISMTPTransport CommandEHLO method
description: Sends the EHLO command to the server.
ms.assetid: 9ca850e3-a654-49d3-bb4c-8b42f3d1e986
keywords:
- CommandEHLO method Windows Mail (formerly Outlook Express)
- CommandEHLO method Windows Mail (formerly Outlook Express) , ISMTPTransport interface
- ISMTPTransport interface Windows Mail (formerly Outlook Express) , CommandEHLO method
topic_type:
- apiref
api_name:
- ISMTPTransport.CommandEHLO
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

# ISMTPTransport::CommandEHLO method

\[**ISMTPTransport::CommandEHLO** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the EHLO command to the server.

## Syntax


```C++
HRESULT CommandEHLO();
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



 

 





