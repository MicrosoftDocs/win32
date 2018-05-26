---
title: IDatabase CloseRowset method
description: Frees the internal resources related to this rowset.
ms.assetid: 5d9eb323-8022-4660-8e8b-7d6e9fedf70b
keywords:
- CloseRowset method Windows Mail (formerly Outlook Express)
- CloseRowset method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , CloseRowset method
topic_type:
- apiref
api_name:
- IDatabase.CloseRowset
api_location:
- Directdb.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDatabase::CloseRowset method

\[**CloseRowset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Frees the internal resources related to this rowset.

## Syntax


```C++
HRESULT CloseRowset(
  [in, out] HROWSET hRowset
);
```



## Parameters

<dl> <dt>

*hRowset* \[in, out\]
</dt> <dd>

Type: **HROWSET**

Specifies the Rowset to free.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





