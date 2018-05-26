---
title: IOERulesManager GetState method
description: IOERulesManager GetState is no longer available for use as of Windows Vista.
ms.assetid: 88d766a3-4de9-42ec-b6bd-f6511a266570
keywords:
- GetState method Windows Mail (formerly Outlook Express)
- GetState method Windows Mail (formerly Outlook Express) , IOERulesManager interface
- IOERulesManager interface Windows Mail (formerly Outlook Express) , GetState method
topic_type:
- apiref
api_name:
- IOERulesManager.GetState
api_location:
- Msoe.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOERulesManager::GetState method

\[**IOERulesManager::GetState** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT GetState(
  [in]  RULE_TYPE type,
  [in]  DWORD     dwFlags,
  [out] DWORD     *pdwState
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

Type: **[**RULE\_TYPE**](oe-rule-type.md)**

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

</dd> <dt>

*pdwState* \[out\]
</dt> <dd>

Type: **DWORD\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method can also return an **HRESULT** derived from the Microsoft Win32 error code ERROR\_NOT\_FOUND to indicate that the zone is unavailable.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| End of client support<br/>    | Windows XP<br/>                                                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                                             |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





