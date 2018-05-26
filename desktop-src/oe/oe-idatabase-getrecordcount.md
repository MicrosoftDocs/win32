---
title: IDatabase GetRecordCount method
description: Retrieves the total number of records in the specified index.
ms.assetid: 6ef9998d-9468-4289-8f33-69aca4484ee1
keywords:
- GetRecordCount method Windows Mail (formerly Outlook Express)
- GetRecordCount method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , GetRecordCount method
topic_type:
- apiref
api_name:
- IDatabase.GetRecordCount
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

# IDatabase::GetRecordCount method

\[**GetRecordCount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the total number of records in the specified index.

## Syntax


```C++
HRESULT GetRecordCount(
  [in]  INDEXORDINAL iIndex,
  [out] LPDWORD      pcRecords
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **[**INDEXORDINAL**](oe-indexordinal.md)**

Specifies the index to retrieve the record count.

</dd> <dt>

*pcRecords* \[out\]
</dt> <dd>

Type: **LPDWORD**

Will receive the record count for the specified index.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                              | Description                                                 |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl> | The index count has been successfully retrieved.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





