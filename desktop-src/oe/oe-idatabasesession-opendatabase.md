---
title: IDatabaseSession OpenDatabase method
description: Opens or creates the specified file as a database using the specified schema.
ms.assetid: b3014f3c-ce24-4fc6-8ebb-f67feae1d20c
keywords:
- OpenDatabase method Windows Mail (formerly Outlook Express)
- OpenDatabase method Windows Mail (formerly Outlook Express) , IDatabaseSession interface
- IDatabaseSession interface Windows Mail (formerly Outlook Express) , OpenDatabase method
topic_type:
- apiref
api_name:
- IDatabaseSession.OpenDatabase
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

# IDatabaseSession::OpenDatabase method

\[**OpenDatabase** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Opens or creates the specified file as a database using the specified schema.

## Syntax


```C++
HRESULT OpenDatabase(
  [in]  LPCSTR             pszFile,
  [in]  OPENDATABASEFLAGS  dwFlags,
  [in]  LPCTABLESCHEMA     pSchema,
  [in]  IDatabaseExtension *pExtension,
  [out] IDatabase          **ppDB
);
```



## Parameters

<dl> <dt>

*pszFile* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the file to be opened as a database.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **[**OPENDATABASEFLAGS**](oe-opendatabaseflags.md)**

Flags that control the open/create operation.

</dd> <dt>

*pSchema* \[in\]
</dt> <dd>

Type: **LPCTABLESCHEMA**

The table schema for this database.

</dd> <dt>

*pExtension* \[in\]
</dt> <dd>

Type: **IDatabaseExtension\***

Specifies a database extension, which will be notified when changes occur in the database. This pointer should point to data that will remain in memory as long as the instance of the IDatabase is active, since the IDatabase does not make its own copy of the data specified by the pointer. Having the schema be a const global is the suggested way to do that.

</dd> <dt>

*ppDB* \[out\]
</dt> <dd>

Type: **[**IDatabase**](oe-idatabase.md)\*\***

On success, will contain a pointer to the newly created IDatabase.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether this function failed.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





