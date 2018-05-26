---
title: IMimeEditTagCollection Reset method
description: Resets the enumerator to the start of the collection.
ms.assetid: 2f44b13e-8b0e-411a-8c36-9cc83a7bc2cf
keywords:
- Reset method Windows Mail (formerly Outlook Express)
- Reset method Windows Mail (formerly Outlook Express) , IMimeEditTagCollection interface
- IMimeEditTagCollection interface Windows Mail (formerly Outlook Express) , Reset method
topic_type:
- apiref
api_name:
- IMimeEditTagCollection.Reset
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

# IMimeEditTagCollection::Reset method

\[**IMimeEditTagCollection::Reset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Resets the enumerator to the start of the collection.

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



 

 





