---
title: IStoreFolder BatchFlush method
description: Unlocks a batched operation. Currently, not used.
ms.assetid: 6b632707-1605-40fb-99ac-2ddeea0fd511
keywords:
- BatchFlush method Windows Mail (formerly Outlook Express)
- BatchFlush method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , BatchFlush method
topic_type:
- apiref
api_name:
- IStoreFolder.BatchFlush
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

# IStoreFolder::BatchFlush method

Unlocks a batched operation. Currently, not used.

## Syntax


```C++
HRESULT BatchFlush(
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



 

 





