---
title: IDatabase MoveFile method
description: Moves the location of the database file.
ms.assetid: 691e1db3-7ea9-47f6-8d46-cb819c7c4a00
keywords:
- MoveFile method Windows Mail (formerly Outlook Express)
- MoveFile method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , MoveFile method
topic_type:
- apiref
api_name:
- IDatabase.MoveFile
api_location:
- Directdb.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDatabase::MoveFile method

\[**MoveFile** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Moves the location of the database file.

## Syntax


```C++
HRESULT MoveFile(
  [in] LPCWSTR pwszFilePath
);
```



## Parameters

<dl> <dt>

*pwszFilePath* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The new location to store the database file.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                    | Description                                                 |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | Indicates pszFile is **NULL**.<br/>                   |
| <dl> <dt>**DB\_E\_MOVEFILE**</dt> </dl> | Indicates that the file was not able to be moved<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Winbase.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





