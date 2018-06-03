---
title: IMimeEditTagCollection Count method
description: On success, obtains a count of IMimeEditTag objects in collection.
ms.assetid: f1334f22-4979-4db6-8501-0b0759717c95
keywords:
- Count method Windows Mail (formerly Outlook Express)
- Count method Windows Mail (formerly Outlook Express) , IMimeEditTagCollection interface
- IMimeEditTagCollection interface Windows Mail (formerly Outlook Express) , Count method
topic_type:
- apiref
api_name:
- IMimeEditTagCollection.Count
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

# IMimeEditTagCollection::Count method

\[**IMimeEditTagCollection::Count** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

On success, obtains a count of [**IMimeEditTag**](oe-imimeedittag.md) objects in collection.

## Syntax


```C++
HRESULT Count(
  [out] ULONG *pcItems
);
```



## Parameters

<dl> <dt>

*pcItems* \[out\]
</dt> <dd>

Type: **ULONG\***

Specifies number of items in collection.

</dd> </dl>

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



 

 





