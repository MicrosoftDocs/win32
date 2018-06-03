---
title: IDatabase GetSize method
description: Retrieves the sizes of various parts of the database.
ms.assetid: b1b338f8-73ec-4acd-838b-7ef27f35fb8b
keywords:
- GetSize method Windows Mail (formerly Outlook Express)
- GetSize method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , GetSize method
topic_type:
- apiref
api_name:
- IDatabase.GetSize
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

# IDatabase::GetSize method

\[**GetSize** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the sizes of various parts of the database.

## Syntax


```C++
HRESULT GetSize(
  [out] LPDWORD pcbFile,
  [out] LPDWORD pcbAllocated,
  [out] LPDWORD pcbFreed,
  [out] LPDWORD pcbStreams
);
```



## Parameters

<dl> <dt>

*pcbFile* \[out\]
</dt> <dd>

Type: **LPDWORD**

Optional. On success, will contain the size of the database file.

</dd> <dt>

*pcbAllocated* \[out\]
</dt> <dd>

Type: **LPDWORD**

Optional. On success, will contain the allocated size of the database.

</dd> <dt>

*pcbFreed* \[out\]
</dt> <dd>

Type: **LPDWORD**

Optional. On success, will contain the freed size of the database.

</dd> <dt>

*pcbStreams* \[out\]
</dt> <dd>

Type: **LPDWORD**

Optional. On success, will contain the size of streams within the database.

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



 

 





