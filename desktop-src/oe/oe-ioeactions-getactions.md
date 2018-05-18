---
title: IOEActions GetActions method
description: IOEActions GetActions is no longer available for use as of Windows Vista.
ms.assetid: 'add14232-8367-4dfb-a734-15e37853ab6d'
keywords: ["GetActions method Windows Mail (formerly Outlook Express)", "GetActions method Windows Mail (formerly Outlook Express) , IOEActions interface", "IOEActions interface Windows Mail (formerly Outlook Express) , GetActions method"]
topic_type:
- apiref
api_name:
- IOEActions.GetActions
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOEActions::GetActions method

\[**IOEActions::GetActions** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT GetActions(
  [in]  DWORD     dwFlags,
  [out] PACT_ITEM *ppItem,
  [out] ULONG     *pcItem
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

Type: **PACT\_ITEM\***

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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





