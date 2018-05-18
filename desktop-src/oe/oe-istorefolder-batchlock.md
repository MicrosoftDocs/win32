---
title: IStoreFolder BatchLock method
description: Lock to prepare for a batch operation. Currently, not used.
ms.assetid: 'f62c93e2-cfd8-4059-afee-9e7d2f09bd30'
keywords: ["BatchLock method Windows Mail (formerly Outlook Express)", "BatchLock method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , BatchLock method"]
topic_type:
- apiref
api_name:
- IStoreFolder.BatchLock
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::BatchLock method

Lock to prepare for a batch operation. Currently, not used.

## Syntax


```C++
HRESULT BatchLock(
  [in]  DWORD        dwReserved,
  [out] LPHBATCHLOCK phBatchLock
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*phBatchLock* \[out\]
</dt> <dd>

Type: **LPHBATCHLOCK**

Specifies handle to newly-created lock.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





