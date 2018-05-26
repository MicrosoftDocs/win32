---
title: IDatabase InsertRecord method
description: Inserts a new record into the database.
ms.assetid: a3d841be-a16e-41f6-81a2-dc359f300762
keywords:
- InsertRecord method Windows Mail (formerly Outlook Express)
- InsertRecord method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , InsertRecord method
topic_type:
- apiref
api_name:
- IDatabase.InsertRecord
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

# IDatabase::InsertRecord method

\[**InsertRecord** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Inserts a new record into the database.

## Syntax


```C++
HRESULT InsertRecord(
  [in] LPVOID pRecord
);
```



## Parameters

<dl> <dt>

*pRecord* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies the new record to be inserted into the database.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                              | Description                                                             |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl> | The record has been successfully inserted into the database.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





