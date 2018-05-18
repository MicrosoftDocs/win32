---
title: IDatabase ModifyIndex method
description: Will create or modify an index in the database.
ms.assetid: 'deda7090-c5e6-4817-8ca0-ac7e864da706'
keywords: ["ModifyIndex method Windows Mail (formerly Outlook Express)", "ModifyIndex method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , ModifyIndex method"]
topic_type:
- apiref
api_name:
- IDatabase.ModifyIndex
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::ModifyIndex method

\[**ModifyIndex** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Will create or modify an index in the database.

## Syntax


```C++
HRESULT ModifyIndex(
  [in] INDEXORDINAL iIndex,
  [in] LPCSTR       ppszFilter,
  [in] LPTABLEINDEX pIndex
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **[**INDEXORDINAL**](oe-indexordinal.md)**

Specifies an identifier of the index to modify or create.

</dd> <dt>

*ppszFilter* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a filter used ensure only certain rows appear in the database.

</dd> <dt>

*pIndex* \[in\]
</dt> <dd>

Type: **LPTABLEINDEX**

The LPCTABLEINDEX data structure specifies columns to be used in the index and options for those columns.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl>     | The index count has been successfully created or modified.<br/>                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates an invalid iIndex or **NULL** pointer was passed to the function.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





