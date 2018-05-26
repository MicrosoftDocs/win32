---
title: IDatabase FreeRecord method
description: Frees resources related to pRecord. It should be called when you are done using pRecord.
ms.assetid: 0e75f7b7-933a-4d2b-98eb-5c1b17bab625
keywords:
- FreeRecord method Windows Mail (formerly Outlook Express)
- FreeRecord method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , FreeRecord method
topic_type:
- apiref
api_name:
- IDatabase.FreeRecord
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

# IDatabase::FreeRecord method

Frees resources related to pRecord. It should be called when you are done using pRecord.

## Syntax


```C++
void FreeRecord(
  [in, out] LPVOID pRecord
);
```



## Parameters

<dl> <dt>

*pRecord* \[in, out\]
</dt> <dd>

Type: **LPVOID**

Specifies the record to free.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





