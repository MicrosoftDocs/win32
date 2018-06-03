---
title: IImnAccountManager2 GetIncompleteAccount method
description: Gets an incomplete account.
ms.assetid: 1ef95924-51b5-4778-9887-dd726c46eba7
keywords:
- GetIncompleteAccount method Windows Mail (formerly Outlook Express)
- GetIncompleteAccount method Windows Mail (formerly Outlook Express) , IImnAccountManager2 interface
- IImnAccountManager2 interface Windows Mail (formerly Outlook Express) , GetIncompleteAccount method
topic_type:
- apiref
api_name:
- IImnAccountManager2.GetIncompleteAccount
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

# IImnAccountManager2::GetIncompleteAccount method

\[**IImnAccountManager2::GetIncompleteAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets an incomplete account.

## Syntax


```C++
HRESULT GetIncompleteAccount(
  [in] ACCTTYPE AcctType,
  [in] LPSTR    pszAccountId,
  [in] ULONG    cchMax
);
```



## Parameters

<dl> <dt>

*AcctType* \[in\]
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)**

Specifies the account type defined in [**ACCTTYPE**](oe-accttype.md).

</dd> <dt>

*pszAccountId* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies the account ID.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the size.

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
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





