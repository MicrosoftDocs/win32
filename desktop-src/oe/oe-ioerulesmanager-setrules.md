---
title: IOERulesManager SetRules method
description: IOERulesManager SetRules is no longer available for use as of Windows Vista.
ms.assetid: '8f9ed55c-154d-4962-8441-fefaa513bb38'
keywords: ["SetRules method Windows Mail (formerly Outlook Express)", "SetRules method Windows Mail (formerly Outlook Express) , IOERulesManager interface", "IOERulesManager interface Windows Mail (formerly Outlook Express) , SetRules method"]
topic_type:
- apiref
api_name:
- IOERulesManager.SetRules
api_location:
- Msoe.dll
api_type:
- COM
---

# IOERulesManager::SetRules method

\[**IOERulesManager::SetRules** is no longer available for use as of Windows Vista.\]

Adds the specified set of rules.

## Syntax


```C++
HRESULT SetRules(
  [in] DWORD     dwFlags,
  [in] RULE_TYPE typeRule,
  [in] RULEINFO  *pinfoRule,
  [in] ULONG     cpIRule
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies one of the following filter types.

<dl> <dt>

<span id="SETF_APPEND"></span><span id="setf_append"></span>**SETF\_APPEND** (0x00000000)
</dt> <dt>

<span id="SETF_CLEAR"></span><span id="setf_clear"></span>**SETF\_CLEAR** (0x00000001)
</dt> <dt>

<span id="SETF_SENDER"></span><span id="setf_sender"></span>**SETF\_SENDER** (0x00000002)
</dt> <dt>

<span id="SETF_JUNK"></span><span id="setf_junk"></span>**SETF\_JUNK** (0x00000004)
</dt> <dt>

<span id="SETF_REPLACE"></span><span id="setf_replace"></span>**SETF\_REPLACE** (0x00000008)
</dt> </dl> </dd> <dt>

*typeRule* \[in\]
</dt> <dd>

Type: **[**RULE\_TYPE**](oe-rule-type.md)**

Specifies a [**RULE\_TYPE**](oe-rule-type.md) value.

</dd> <dt>

*pinfoRule* \[in\]
</dt> <dd>

Type: **[**RULEINFO**](oe-ruleinfo.md)\***

Specifies a pointer to an array of [**RULEINFO**](oe-ruleinfo.md) structures.

</dd> <dt>

*cpIRule* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the number of items in the *pinfoRule* array.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that the set of rules could not be added.<br/>                                             |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that an unknown error has occurred.<br/>                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pinfoRule* is **NULL**, that *cpIRule* is zero, or that *typeRule* is invalid. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                            |



 

## Remarks

This method can also return an **HRESULT** derived from the Microsoft Win32 error code ERROR\_NOT\_FOUND to indicate that the zone is unavailable.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| End of client support<br/>    | Windows XP<br/>                                                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                                             |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





