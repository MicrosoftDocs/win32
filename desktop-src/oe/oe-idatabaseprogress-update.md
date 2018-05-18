---
title: IDatabaseProgress Update method
description: Will be called when progress has occurred during a Compact operation.
ms.assetid: '66600637-b59b-4756-8a04-cbc23b74b908'
keywords: ["Update method Windows Mail (formerly Outlook Express)", "Update method Windows Mail (formerly Outlook Express) , IDatabaseProgress interface", "IDatabaseProgress interface Windows Mail (formerly Outlook Express) , Update method"]
topic_type:
- apiref
api_name:
- IDatabaseProgress.Update
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabaseProgress::Update method

Will be called when progress has occurred during a Compact operation.

## Syntax


```C++
HRESULT Update(
  [in] DWORD cCount
);
```



## Parameters

<dl> <dt>

*cCount* \[in\]
</dt> <dd>

Type: **DWORD**

Unsupported.

</dd> </dl>

## Return value

Type: **HRESULT**

If the return value from this function causes the SUCCEEDED macro to return **FALSE**, the compact operation will terminate immediately.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





