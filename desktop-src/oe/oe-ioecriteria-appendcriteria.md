---
title: IOECriteria AppendCriteria method
description: IOECriteria AppendCriteria is no longer available for use as of Windows Vista.
ms.assetid: 1caae7bb-7106-4b48-919e-cedc55b9e689
keywords:
- AppendCriteria method Windows Mail (formerly Outlook Express)
- AppendCriteria method Windows Mail (formerly Outlook Express) , IOECriteria interface
- IOECriteria interface Windows Mail (formerly Outlook Express) , AppendCriteria method
topic_type:
- apiref
api_name:
- IOECriteria.AppendCriteria
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOECriteria::AppendCriteria method

\[**IOECriteria::AppendCriteria** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT AppendCriteria(
  [in]  DWORD      dwFlags,
  [in]  CRIT_LOGIC logic,
  [in]  CRIT_ITEM  *pItem,
  [in]  ULONG      cItem,
  [out] ULONG      *pcItemAppended
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

</dd> <dt>

*logic* \[in\]
</dt> <dd>

Type: **[**CRIT\_LOGIC**](oe-crit-logic.md)**

</dd> <dt>

*pItem* \[in\]
</dt> <dd>

Type: **[**CRIT\_ITEM**](oe-crit-item.md)\***

</dd> <dt>

*cItem* \[in\]
</dt> <dd>

Type: **ULONG**

</dd> <dt>

*pcItemAppended* \[out\]
</dt> <dd>

Type: **ULONG\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





