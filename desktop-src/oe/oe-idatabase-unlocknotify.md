---
title: IDatabase UnlockNotify method
description: Call when you are ready for transactions to be queued for this object after calling LockNotify. You must call UnlockNotify the same number of times you call LockNotify.
ms.assetid: 03ee7a6d-2553-446f-aa75-346caed84c71
keywords:
- UnlockNotify method Windows Mail (formerly Outlook Express)
- UnlockNotify method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , UnlockNotify method
topic_type:
- apiref
api_name:
- IDatabase.UnlockNotify
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

# IDatabase::UnlockNotify method

Call when you are ready for transactions to be queued for this object after calling LockNotify. You must call UnlockNotify the same number of times you call LockNotify.

## Syntax


```C++
void UnlockNotify(
  [in, out] LPHLOCK phLock
);
```



## Parameters

<dl> <dt>

*phLock* \[in, out\]
</dt> <dd>

Type: **LPHLOCK**

Pass the value received from LockNotify.

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



 

 





