---
title: IDatabase Lock method
description: Locks the message database to prevent usage by other callers.
ms.assetid: 11d22b3c-f6a1-4ae6-a2e0-3bc22998dd46
keywords:
- Lock method Windows Mail (formerly Outlook Express)
- Lock method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , Lock method
topic_type:
- apiref
api_name:
- IDatabase.Lock
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

# IDatabase::Lock method

\[**Lock** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Locks the message database to prevent usage by other callers.

## Syntax


```C++
HRESULT Lock(
  [out] LPHLOCK phLock
);
```



## Parameters

<dl> <dt>

*phLock* \[out\]
</dt> <dd>

Type: **LPHLOCK**

The handle to use when calling Unlock to unlock the database.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                              | Description                              |
|------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl> | The database has been locked.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





