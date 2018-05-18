---
title: IDatabase DeleteRecord method
description: Deletes an existing record from the database.
ms.assetid: '5285fb14-14e3-4741-a3be-f26e6057434c'
keywords: ["DeleteRecord method Windows Mail (formerly Outlook Express)", "DeleteRecord method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , DeleteRecord method"]
topic_type:
- apiref
api_name:
- IDatabase.DeleteRecord
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::DeleteRecord method

\[**DeleteRecord** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes an existing record from the database.

## Syntax


```C++
HRESULT DeleteRecord(
  [in] LPVOID pRecord
);
```



## Parameters

<dl> <dt>

*pRecord* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies the record to be deleted in the database.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                    | Description                                                            |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl>       | The record has been successfully deleted from the database.<br/> |
| <dl> <dt>**DB\_E\_NOTFOUND**</dt> </dl> | Indicates that the record to delete could not be found.<br/>     |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





