---
title: IImnAccount DoWizard method
description: Creates a wizard for handling accounts.
ms.assetid: '65f96eb8-f654-4927-be08-091dd5684364'
keywords: ["DoWizard method Windows Mail (formerly Outlook Express)", "DoWizard method Windows Mail (formerly Outlook Express) , IImnAccount interface", "IImnAccount interface Windows Mail (formerly Outlook Express) , DoWizard method"]
topic_type:
- apiref
api_name:
- IImnAccount.DoWizard
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnAccount::DoWizard method

\[**IImnAccount::DoWizard** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a wizard for handling accounts.

## Syntax


```C++
HRESULT DoWizard(
  [in] HWND  hwnd,
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

Specifies the handle of the parent window of the wizard.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that indicates the contents of the wizard.

<dl> <dt>

<span id="ACCT_WIZ_MIGRATE"></span><span id="acct_wiz_migrate"></span>**ACCT\_WIZ\_MIGRATE** (0x0001)
</dt> <dt>

<span id="ACCT_WIZ_MAILIMPORT"></span><span id="acct_wiz_mailimport"></span>**ACCT\_WIZ\_MAILIMPORT** (0x0002)
</dt> <dt>

<span id="ACCT_WIZ_OUTLOOK"></span><span id="acct_wiz_outlook"></span>**ACCT\_WIZ\_OUTLOOK** (0x0004)
</dt> <dt>

<span id="ACCT_WIZ_NEWSIMPORT"></span><span id="acct_wiz_newsimport"></span>**ACCT\_WIZ\_NEWSIMPORT** (0x0008)
</dt> <dt>

<span id="ACCT_WIZ_NO_NEW_POP"></span><span id="acct_wiz_no_new_pop"></span>**ACCT\_WIZ\_NO\_NEW\_POP** (0x0010)
</dt> <dt>

<span id="ACCT_WIZ_INTERNETCONNECTION"></span><span id="acct_wiz_internetconnection"></span>**ACCT\_WIZ\_INTERNETCONNECTION** (0x0020)
</dt> <dt>

<span id="ACCT_WIZ_HTTPMAIL"></span><span id="acct_wiz_httpmail"></span>**ACCT\_WIZ\_HTTPMAIL** (0x0040)
</dt> <dt>

<span id="ACCT_WIZ_OE"></span><span id="acct_wiz_oe"></span>**ACCT\_WIZ\_OE** (0x0080)
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that the operation cannot be done. <br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





