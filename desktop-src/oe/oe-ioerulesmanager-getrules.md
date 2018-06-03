---
title: IOERulesManager GetRules method
description: IOERulesManager GetRules is no longer available for use as of Windows Vista.
ms.assetid: 93ee0dd5-59e4-4797-8530-aa4f1ef0355f
keywords:
- GetRules method Windows Mail (formerly Outlook Express)
- GetRules method Windows Mail (formerly Outlook Express) , IOERulesManager interface
- IOERulesManager interface Windows Mail (formerly Outlook Express) , GetRules method
topic_type:
- apiref
api_name:
- IOERulesManager.GetRules
api_location:
- Msoe.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOERulesManager::GetRules method

\[**IOERulesManager::GetRules** is no longer available for use as of Windows Vista.\]

Gets a set of rules of the specified type.

## Syntax


```C++
HRESULT GetRules(
  [in] DWORD     dwFlags,
  [in] RULE_TYPE typeRule,
  [in] RULEINFO  **ppinfoRule,
  [in] ULONG     *pcpinfoRule
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies one of the following filter types.

<dl> <dt>

<span id="GETF_ALL"></span><span id="getf_all"></span>**GETF\_ALL** (0x00000000)
</dt> <dt>

<span id="GETF_EDIT"></span><span id="getf_edit"></span>**GETF\_EDIT** (0x00000001)
</dt> <dt>

<span id="GETF_SENDER"></span><span id="getf_sender"></span>**GETF\_SENDER** (0x00000002)
</dt> <dt>

<span id="GETF_JUNK"></span><span id="getf_junk"></span>**GETF\_JUNK** (0x00000004)
</dt> <dt>

<span id="GETF_POP3"></span><span id="getf_pop3"></span>**GETF\_POP3** (0x00000008)
</dt> <dt>

<span id="GETF_NNTP"></span><span id="getf_nntp"></span>**GETF\_NNTP** (0x00000010)
</dt> <dt>

<span id="GETF_IMAP"></span><span id="getf_imap"></span>**GETF\_IMAP** (0x00000020)
</dt> <dt>

<span id="GETF_HTTPMAIL"></span><span id="getf_httpmail"></span>**GETF\_HTTPMAIL** (0x00000040)
</dt> </dl> </dd> <dt>

*typeRule* \[in\]
</dt> <dd>

Type: **[**RULE\_TYPE**](oe-rule-type.md)**

Specifies a [**RULE\_TYPE**](oe-rule-type.md) value.

</dd> <dt>

*ppinfoRule* \[in\]
</dt> <dd>

Type: **[**RULEINFO**](oe-ruleinfo.md)\*\***

Specifies the address of a pointer to an array of [**RULEINFO**](oe-ruleinfo.md) structures.

</dd> <dt>

*pcpinfoRule* \[in\]
</dt> <dd>

Type: **ULONG\***

Specifies a pointer to a **ULONG** that indicates the number of items in the array specified by *ppinfoRule*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                   |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppinfoRule* is **NULL** or *typeRule* is invalid. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>               |



 

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



 

 





