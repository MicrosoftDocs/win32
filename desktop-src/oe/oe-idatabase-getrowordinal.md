---
title: IDatabase GetRowOrdinal method
description: Returns the position of the row in the database.
ms.assetid: a24a282f-2581-4363-b3db-b7992c69d611
keywords:
- GetRowOrdinal method Windows Mail (formerly Outlook Express)
- GetRowOrdinal method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , GetRowOrdinal method
topic_type:
- apiref
api_name:
- IDatabase.GetRowOrdinal
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

# IDatabase::GetRowOrdinal method

Returns the position of the row in the database.

## Syntax


```C++
HRESULT GetRowOrdinal(
  [in] INDEXORDNIAL iIndex,
  [in] DWORD        cColumns,
  [in] LPVOID       pRecord
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **INDEXORDNIAL**

Specifies the index used to search the record with.

</dd> <dt>

*cColumns* \[in\]
</dt> <dd>

Type: **DWORD**

Number of columns(keys) of the index to search with. COLUMNS\_ALL means search with all keys in the index. If cColumns is smaller than the number of keys in the index, it means a partial search with only the first cColumns keys is.

</dd> <dt>

*pRecord* \[in\]
</dt> <dd>

Type: **LPVOID**

The record to be searched for. On input, pRecord should contain information in the columns that will be used for the search.

</dd> </dl>

## Return value

Type: **HRESULT**

Either returns the ordinal position of the record being searched or one of the following values.



| Return code                                                                                    | Description                       |
|------------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**DB\_E\_NOTFOUND**</dt> </dl> | The row was not found.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





