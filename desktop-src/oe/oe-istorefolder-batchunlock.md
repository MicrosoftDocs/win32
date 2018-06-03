---
title: IStoreFolder BatchUnlock method
description: Unlocks a batched operation. Currently, not used.
ms.assetid: 38c7e071-ad41-4424-9f74-d6d328bace96
keywords:
- BatchUnlock method Windows Mail (formerly Outlook Express)
- BatchUnlock method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , BatchUnlock method
topic_type:
- apiref
api_name:
- IStoreFolder.BatchUnlock
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IStoreFolder::BatchUnlock method

Unlocks a batched operation. Currently, not used.

## Syntax


```C++
HRESULT BatchUnlock(
  [in] DWORD      dwReserved,
  [in] HBATCHLOCK hBatchLock
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*hBatchLock* \[in\]
</dt> <dd>

Type: **HBATCHLOCK**

Specifies handle to lock obtained from [**IStoreFolder::BatchLock**](oe-istorefolder-batchlock.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





