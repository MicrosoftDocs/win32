---
title: IDatabase FindRecord method
description: Finds one record in the database based on the index and number of keys provided.
ms.assetid: c395053b-32d2-45fe-a36f-5e4e06cc6229
keywords:
- FindRecord method Windows Mail (formerly Outlook Express)
- FindRecord method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , FindRecord method
topic_type:
- apiref
api_name:
- IDatabase.FindRecord
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

# IDatabase::FindRecord method

Finds one record in the database based on the index and number of keys provided.

## Syntax


```C++
HRESULT FindRecord(
  [in]      INDEXORDNIAL iIndex,
  [in]      DWORD        cColumns,
  [in, out] LPVOID       pRecord,
  [out]     LPROWORDINAL piRow
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **INDEXORDNIAL**

Specifies the index used to search the record with

</dd> <dt>

*cColumns* \[in\]
</dt> <dd>

Type: **DWORD**

Number of columns(keys) of the index to search with. COLUMNS\_ALL means search with all keys in the index. If cColumns is smaller than the number of keys in the index, it means a partial search with only the first cColumns keys is.

</dd> <dt>

*pRecord* \[in, out\]
</dt> <dd>

Type: **LPVOID**

The record to be searched for. On input, pRecord should contain information in the columns that will be used for the search. On success, pRecord is filled with all information available from the database for the matching record.

</dd> <dt>

*piRow* \[out\]
</dt> <dd>

Type: **LPROWORDINAL**

Returns the ordinal position of the record that was found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                    | Description                          |
|------------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**DB\_S\_FOUND**</dt> </dl>    | The record was found.<br/>     |
| <dl> <dt>**DB\_S\_NOTFOUND**</dt> </dl> | The record was not found.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





