---
title: IOECriteria GetCriteria method
description: IOECriteria GetCriteria is no longer available for use as of Windows Vista.
ms.assetid: 4b2fb239-c553-4f0b-b5d8-50d89801992f
keywords:
- GetCriteria method Windows Mail (formerly Outlook Express)
- GetCriteria method Windows Mail (formerly Outlook Express) , IOECriteria interface
- IOECriteria interface Windows Mail (formerly Outlook Express) , GetCriteria method
topic_type:
- apiref
api_name:
- IOECriteria.GetCriteria
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

# IOECriteria::GetCriteria method

\[**IOECriteria::GetCriteria** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT GetCriteria(
  [in]  DWORD      dwFlags,
  [out] PCRIT_ITEM *ppItem,
  [out] ULONG      *pcItem
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

</dd> <dt>

*ppItem* \[out\]
</dt> <dd>

Type: **PCRIT\_ITEM\***

</dd> <dt>

*pcItem* \[out\]
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



 

 





