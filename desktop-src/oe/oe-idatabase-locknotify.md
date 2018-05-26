---
title: IDatabase LockNotify method
description: Provides a ref-counted way of preventing any notifications from being queued for this database object.
ms.assetid: 9c0f4a40-a82f-4d94-9ae5-dd0dc18af8b1
keywords:
- LockNotify method Windows Mail (formerly Outlook Express)
- LockNotify method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , LockNotify method
topic_type:
- apiref
api_name:
- IDatabase.LockNotify
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

# IDatabase::LockNotify method

Provides a ref-counted way of preventing any notifications from being queued for this database object.

## Syntax


```C++
void LockNotify(
  [in]  LOCKNOTIFYFLAGS dwFlags,
  [out] LPHLOCK         phLock
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **LOCKNOTIFYFLAGS**

Pass 0 for this parameter.

</dd> <dt>

*phLock* \[out\]
</dt> <dd>

Type: **LPHLOCK**

Use the value returned in this paramter when calling UnlockNotify.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





