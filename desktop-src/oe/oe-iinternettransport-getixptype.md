---
title: IInternetTransport GetIXPType method
description: Gets the Internet transport type.
ms.assetid: d613506a-a870-448a-a5b3-c15d56175439
keywords:
- GetIXPType method Windows Mail (formerly Outlook Express)
- GetIXPType method Windows Mail (formerly Outlook Express) , IInternetTransport interface
- IInternetTransport interface Windows Mail (formerly Outlook Express) , GetIXPType method
topic_type:
- apiref
api_name:
- IInternetTransport.GetIXPType
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

# IInternetTransport::GetIXPType method

\[**IInternetTransport::GetIXPType** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the Internet transport type.

## Syntax


```C++
IXPTYPE GetIXPType();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**IXPTYPE**](oe-ixptype.md)**

Returns an [**IXPTYPE**](oe-ixptype.md) value.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





