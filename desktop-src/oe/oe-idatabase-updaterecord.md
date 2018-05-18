---
title: IDatabase UpdateRecord method
description: Updates an existing record in the database.
ms.assetid: 'ebb31568-7927-45df-83fa-d70418211df5'
keywords: ["UpdateRecord method Windows Mail (formerly Outlook Express)", "UpdateRecord method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , UpdateRecord method"]
topic_type:
- apiref
api_name:
- IDatabase.UpdateRecord
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::UpdateRecord method

\[**UpdateRecord** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Updates an existing record in the database.

## Syntax


```C++
HRESULT UpdateRecord(
  [in] LPVOID pRecord
);
```



## Parameters

<dl> <dt>

*pRecord* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies the new record to be updated in the database.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                | Description                                                                                         |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl>                   | The record has been successfully inserted into the database.<br/>                             |
| <dl> <dt>**DB\_E\_NOTFOUND**</dt> </dl>             | Indicates that the record to update could not be found.<br/>                                  |
| <dl> <dt>**DB\_E\_RECORDVERSIONCHANGED**</dt> </dl> | Indicates that the version of the record in the DB did not match the version of pRecord.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





