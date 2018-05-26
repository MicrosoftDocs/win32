---
title: IImnAdviseAccount AdviseAccount method
description: Used in account change.
ms.assetid: 4066a316-dd0b-4a31-bfe1-eed00dbd4576
keywords:
- AdviseAccount method Windows Mail (formerly Outlook Express)
- AdviseAccount method Windows Mail (formerly Outlook Express) , IImnAdviseAccount interface
- IImnAdviseAccount interface Windows Mail (formerly Outlook Express) , AdviseAccount method
topic_type:
- apiref
api_name:
- IImnAdviseAccount.AdviseAccount
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

# IImnAdviseAccount::AdviseAccount method

\[**IImnAdviseAccount::AdviseAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Used in account change.

## Syntax


```C++
HRESULT AdviseAccount(
  [in] DWORD dwAdviseType,
  [in] ACTX  *pAcctCtx
);
```



## Parameters

<dl> <dt>

*dwAdviseType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask of the advise type.

<dl><span id="AN_DEFAULT_CHANGED"></span><span id="an_default_changed"></span><dt>

**AN\_DEFAULT\_CHANGED**
</dt><span id="AN_ACCOUNT_DELETED"></span><span id="an_account_deleted"></span><dt>

**AN\_ACCOUNT\_DELETED**
</dt><span id="AN_ACCOUNT_ADDED"></span><span id="an_account_added"></span><dt>

**AN\_ACCOUNT\_ADDED**
</dt><span id="AN_ACCOUNT_CHANGED"></span><span id="an_account_changed"></span><dt>

**AN\_ACCOUNT\_CHANGED**
</dt> </dl> </dd> <dt>

*pAcctCtx* \[in\]
</dt> <dd>

Type: **[**ACTX**](oe-actx.md)\***

Specifies a pointer to a structure containing account information.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                         |
|----------------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success. <br/>                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | *pAcctCtx* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





