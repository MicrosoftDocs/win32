---
title: IOERulesManager EnumRules method
description: IOERulesManager EnumRules is no longer available for use as of Windows Vista.
ms.assetid: cdb9c8b5-c613-46ea-bb24-c683214d8123
keywords:
- EnumRules method Windows Mail (formerly Outlook Express)
- EnumRules method Windows Mail (formerly Outlook Express) , IOERulesManager interface
- IOERulesManager interface Windows Mail (formerly Outlook Express) , EnumRules method
topic_type:
- apiref
api_name:
- IOERulesManager.EnumRules
api_location:
- Msoe.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOERulesManager::EnumRules method

\[**IOERulesManager::EnumRules** is no longer available for use as of Windows Vista.\]

Creates a new [**IOEEnumRules**](oe-ioeenumrules.md) object for the specified rule type.

## Syntax


```C++
HRESULT EnumRules(
  [in]  DWORD        dwFlags,
  [in]  RULE_TYPE    type,
  [out] IOEEnumRules **ppIEnumRules
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies one of the following filter types.

<dl> <dt>

<span id="ENUMF_ALL"></span><span id="enumf_all"></span>**ENUMF\_ALL** (0x00000001)
</dt> <dt>

<span id="ENUMF_EDIT"></span><span id="enumf_edit"></span>**ENUMF\_EDIT** (0x00000002)
</dt> <dt>

<span id="ENUMF_SENDER"></span><span id="enumf_sender"></span>**ENUMF\_SENDER** (0x00000004)
</dt> <dt>

<span id="ENUMF_POP3"></span><span id="enumf_pop3"></span>**ENUMF\_POP3** (0x00000008)
</dt> <dt>

<span id="ENUMF_NNTP"></span><span id="enumf_nntp"></span>**ENUMF\_NNTP** (0x00000010)
</dt> <dt>

<span id="ENUMF_IMAP"></span><span id="enumf_imap"></span>**ENUMF\_IMAP** (0x00000020)
</dt> <dt>

<span id="ENUMF_HTTPMAIL"></span><span id="enumf_httpmail"></span>**ENUMF\_HTTPMAIL** (0x00000040)
</dt> </dl> </dd> <dt>

*type* \[in\]
</dt> <dd>

Type: **[**RULE\_TYPE**](oe-rule-type.md)**

Specifies a [**RULE\_TYPE**](oe-rule-type.md) value.

</dd> <dt>

*ppIEnumRules* \[out\]
</dt> <dd>

Type: **[**IOEEnumRules**](oe-ioeenumrules.md)\*\***

Receives the address of a pointer to an [**IOEEnumRules**](oe-ioeenumrules.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                      |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                   |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that the new object could not be created.<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppIEnumRules* is **NULL** or that *type* is invalid. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                  |



 

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
| Header<br/>                   | <dl> <dt>Fsrmpipeline.h</dt> </dl>                  |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





