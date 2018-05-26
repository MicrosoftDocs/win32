---
title: IDatabase UnregisterNotify method
description: Will permanently stop any notifications from going to the given IDatabaseNotify. Any remaining queued notifications will not be dispatched.
ms.assetid: 6555b388-60cc-4d38-946f-81f7f6604c9c
keywords:
- UnregisterNotify method Windows Mail (formerly Outlook Express)
- UnregisterNotify method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , UnregisterNotify method
topic_type:
- apiref
api_name:
- IDatabase.UnregisterNotify
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

# IDatabase::UnregisterNotify method

Will permanently stop any notifications from going to the given IDatabaseNotify. Any remaining queued notifications will not be dispatched.

## Syntax


```C++
void UnregisterNotify(
  [in] IDatabaseNotify *pNotify
);
```



## Parameters

<dl> <dt>

*pNotify* \[in\]
</dt> <dd>

Type: **IDatabaseNotify\***

Specifies the IDatabaseNotify that will be unregistered.

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



 

 





