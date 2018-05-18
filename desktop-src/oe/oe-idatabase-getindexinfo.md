---
title: IDatabase GetIndexInfo method
description: Retrieves information about an index out of the database.
ms.assetid: 'b395854d-e234-4f6a-992b-a43511e077a0'
keywords: ["GetIndexInfo method Windows Mail (formerly Outlook Express)", "GetIndexInfo method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , GetIndexInfo method"]
topic_type:
- apiref
api_name:
- IDatabase.GetIndexInfo
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::GetIndexInfo method

\[**GetIndexInfo** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves information about an index out of the database.

## Syntax


```C++
HRESULT GetIndexInfo(
  [in]  INDEXORDINAL iIndex,
  [out] LPSTR        *ppszFilter,
  [out] LPTABLEINDEX pIndex
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **[**INDEXORDINAL**](oe-indexordinal.md)**

Specifies the index whose information is wanted.

</dd> <dt>

*ppszFilter* \[out\]
</dt> <dd>

Type: **LPSTR\***

Will receive the filter for the index. Must be freed by caller.

</dd> <dt>

*pIndex* \[out\]
</dt> <dd>

Type: **LPTABLEINDEX**

Will receive the TABLEINDEX information for this index.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                              | Description                                                       |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl> | The index information has been successfully retrieved.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>   | The index does not exist.<br/>                              |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Oledb.h</dt> </dl>                             |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





