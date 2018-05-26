---
title: IMimeEnumHeaderRows Reset method
description: Resets the enumeration sequence to the beginning.
ms.assetid: e31b5fb2-823f-4bd5-bec9-5a582404c1ab
keywords:
- Reset method Windows Mail (formerly Outlook Express)
- Reset method Windows Mail (formerly Outlook Express) , IMimeEnumHeaderRows interface
- IMimeEnumHeaderRows interface Windows Mail (formerly Outlook Express) , Reset method
topic_type:
- apiref
api_name:
- IMimeEnumHeaderRows.Reset
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

# IMimeEnumHeaderRows::Reset method

\[**IMimeEnumHeaderRows::Reset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Resets the enumeration sequence to the beginning.

## Syntax


```C++
HRESULT Reset();
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
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





