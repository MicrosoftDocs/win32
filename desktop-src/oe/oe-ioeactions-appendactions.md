---
title: IOEActions AppendActions method
description: IOEActions AppendActions is no longer available for use as of Windows Vista.
ms.assetid: 'd26f0dab-eecc-440d-a50d-baa298a68d55'
keywords: ["AppendActions method Windows Mail (formerly Outlook Express)", "AppendActions method Windows Mail (formerly Outlook Express) , IOEActions interface", "IOEActions interface Windows Mail (formerly Outlook Express) , AppendActions method"]
topic_type:
- apiref
api_name:
- IOEActions.AppendActions
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOEActions::AppendActions method

\[**IOEActions::AppendActions** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT AppendActions(
  [in]  DWORD    dwFlags,
  [in]  ACT_ITEM *pItem,
  [in]  ULONG    cItem,
  [out] ULONG    *pcItemAppended
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

Type: **[**ACT\_ITEM**](oe-act-item.md)\***

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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





