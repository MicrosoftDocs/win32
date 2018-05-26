---
title: IOECriteria SetCriteria method
description: IOECriteria SetCriteria is no longer available for use as of Windows Vista.
ms.assetid: 5d3c1d93-0bd8-4f9c-a82b-a0908d54fd02
keywords:
- SetCriteria method Windows Mail (formerly Outlook Express)
- SetCriteria method Windows Mail (formerly Outlook Express) , IOECriteria interface
- IOECriteria interface Windows Mail (formerly Outlook Express) , SetCriteria method
topic_type:
- apiref
api_name:
- IOECriteria.SetCriteria
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

# IOECriteria::SetCriteria method

\[**IOECriteria::SetCriteria** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT SetCriteria(
  [in] DWORD     dwFlags,
  [in] CRIT_ITEM *pItem,
  [in] ULONG     cItem
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

</dd> <dt>

*pItem* \[in\]
</dt> <dd>

Type: **[**CRIT\_ITEM**](oe-crit-item.md)\***

</dd> <dt>

*cItem* \[in\]
</dt> <dd>

Type: **ULONG**

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



 

 





