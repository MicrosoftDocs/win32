---
title: IDatabase GenerateId method
description: Retrieves an ID unique to this database.
ms.assetid: dc5c87bb-ebf8-4468-9c1f-b64e93b5dcf7
keywords:
- GenerateId method Windows Mail (formerly Outlook Express)
- GenerateId method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , GenerateId method
topic_type:
- apiref
api_name:
- IDatabase.GenerateId
api_location:
- Directdb.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDatabase::GenerateId method

\[**GenerateId** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves an ID unique to this database.

## Syntax


```C++
HRESULT GenerateId(
  [out] LPDWORD pdwld
);
```



## Parameters

<dl> <dt>

*pdwld* \[out\]
</dt> <dd>

Type: **LPDWORD**

On success, will contain a new ID.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether this function failed.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





