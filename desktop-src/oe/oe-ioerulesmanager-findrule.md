---
title: IOERulesManager FindRule method
description: IOERulesManager FindRule is no longer available for use as of Windows Vista.
ms.assetid: '6954b63f-bfdc-4714-9174-5b64f4178384'
keywords: ["FindRule method Windows Mail (formerly Outlook Express)", "FindRule method Windows Mail (formerly Outlook Express) , IOERulesManager interface", "IOERulesManager interface Windows Mail (formerly Outlook Express) , FindRule method"]
topic_type:
- apiref
api_name:
- IOERulesManager.FindRule
api_location:
- Msoe.dll
api_type:
- COM
---

# IOERulesManager::FindRule method

\[**IOERulesManager::FindRule** is no longer available for use as of Windows Vista.\]

Gets the rule by the specified name and type.

## Syntax


```C++
HRESULT FindRule(
  [in]  LPCSTR    pszRuleName,
  [in]  RULE_TYPE type,
  [out] IOERule   **ppIRule
);
```



## Parameters

<dl> <dt>

*pszRuleName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the rule name.

</dd> <dt>

*type* \[in\]
</dt> <dd>

Type: **[**RULE\_TYPE**](oe-rule-type.md)**

Specifies a [**RULE\_TYPE**](oe-rule-type.md) value.

</dd> <dt>

*ppIRule* \[out\]
</dt> <dd>

Type: **[**IOERule**](oe-ioerule.md)\*\***

Receives the address of a pointer to the [**IOERule**](oe-ioerule.md) object found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                     |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszRuleName* or *type* is **NULL**. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that a rule cannot be found. <br/>              |



 

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



 

 





