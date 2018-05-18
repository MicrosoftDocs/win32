---
title: IDatabase DeleteIndex method
description: Removes the index from the database.
ms.assetid: '1134d0aa-757f-4b6b-9d63-e85c5215ca31'
keywords: ["DeleteIndex method Windows Mail (formerly Outlook Express)", "DeleteIndex method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , DeleteIndex method"]
topic_type:
- apiref
api_name:
- IDatabase.DeleteIndex
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::DeleteIndex method

\[**DeleteIndex** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes the index from the database.

## Syntax


```C++
HRESULT DeleteIndex(
  [in] INDEXORDINAL iIndex
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **[**INDEXORDINAL**](oe-indexordinal.md)**

Specifies the index to be deleted.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl>     | The index successfully deleted.<br/>                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates an invalid iIndex or **NULL** pointer was passed to the function.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





