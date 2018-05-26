---
title: IImnAccountManager AccountListDialog method
description: Displays the dialog box that lists current accounts.
ms.assetid: 2722b26e-d418-48d9-9a2c-db282fb8b7f2
keywords:
- AccountListDialog method Windows Mail (formerly Outlook Express)
- AccountListDialog method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , AccountListDialog method
topic_type:
- apiref
api_name:
- IImnAccountManager.AccountListDialog
api_location:
- Msoeacct.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IImnAccountManager::AccountListDialog method

\[**IImnAccountManager::AccountListDialog** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Displays the dialog box that lists current accounts.

## Syntax


```C++
HRESULT AccountListDialog(
  [in] HWND         hwnd,
  [in] ACCTLISTINFO *pinfo
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

Specifies the handle to the parent window.

</dd> <dt>

*pinfo* \[in\]
</dt> <dd>

Type: **[**ACCTLISTINFO**](oe-acctlistinfo.md)\***

Specifies a pointer to an [**ACCTLISTINFO**](oe-acctlistinfo.md) structure that contains the type of accounts to be displayed in the dialog.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                                                   |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                                                                                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an unknown error has occurred.<br/>                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pinfo* is **NULL** or that *pinfo*.**dwAcctFlags** or *pinfo*.**dwFlags** contains too many flags.<br/> |



 

## Remarks

This dialog allows for the creation, deletion, and modification of accounts.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





