---
title: IDatabase GetFile method
description: Retrieves the filename of the database.
ms.assetid: 06587e62-9969-4cd1-b4d4-8a3178e58339
keywords:
- GetFile method Windows Mail (formerly Outlook Express)
- GetFile method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , GetFile method
topic_type:
- apiref
api_name:
- IDatabase.GetFile
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

# IDatabase::GetFile method

\[[**GetSize**](oe-idatabase-getsize.md) is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the filename of the database.

## Syntax


```C++
HRESULT GetFile(
  [out] LPWSTR *ppwszFile
);
```



## Parameters

<dl> <dt>

*ppwszFile* \[out\]
</dt> <dd>

Type: **LPWSTR\***

On success, will contain the filename of the database. Caller is responsible for freeing this buffer.

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
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





