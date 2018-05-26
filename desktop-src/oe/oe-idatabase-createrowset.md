---
title: IDatabase CreateRowset method
description: Creates a Rowset.
ms.assetid: 5c58d4ca-8883-473d-babf-54f914196862
keywords:
- CreateRowset method Windows Mail (formerly Outlook Express)
- CreateRowset method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , CreateRowset method
topic_type:
- apiref
api_name:
- IDatabase.CreateRowset
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

# IDatabase::CreateRowset method

\[**CreateRowset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a Rowset. Rowsets allow you to iterate through the rows in a database.

## Syntax


```C++
HRESULT CreateRowset(
  [in]  INDEXORDINAL iIndex,
  [in]  DWORD        dwReserved,
  [out] LPHROWSET    phRowset
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **[**INDEXORDINAL**](oe-indexordinal.md)**

Specifies the index used to order the rows being iterated over.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

A reserved field.

</dd> <dt>

*phRowset* \[out\]
</dt> <dd>

Type: **LPHROWSET**

Returns a handle that will be used to interact with rowset later.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following codes. Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                              | Description                                     |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl>                 | The operation succeeded.<br/>             |
| <dl> <dt>**DB\_E\_TOOMANYOPENROWSETS**</dt> </dl> | Too many Rowsets are currently open.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





