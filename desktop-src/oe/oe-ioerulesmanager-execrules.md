---
title: IOERulesManager ExecRules method
description: IOERulesManager ExecRules is no longer available for use as of Windows Vista.
ms.assetid: 9f0e56b1-5f62-42dd-95b9-6b60a8c5de31
keywords:
- ExecRules method Windows Mail (formerly Outlook Express)
- ExecRules method Windows Mail (formerly Outlook Express) , IOERulesManager interface
- IOERulesManager interface Windows Mail (formerly Outlook Express) , ExecRules method
topic_type:
- apiref
api_name:
- IOERulesManager.ExecRules
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

# IOERulesManager::ExecRules method

\[**IOERulesManager::ExecRules** is no longer available for use as of Windows Vista.\]

Creates a new [**IOEExecRules**](oe-ioeexecrules.md) object for the specified rule type.

## Syntax


```C++
HRESULT ExecRules(
  [in]  DWORD        dwFlags,
  [in]  RULE_TYPE    type,
  [out] IOEExecRules **ppIExecRules
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*type* \[in\]
</dt> <dd>

Type: **[**RULE\_TYPE**](oe-rule-type.md)**

Specifies a [**RULE\_TYPE**](oe-rule-type.md) value.

</dd> <dt>

*ppIExecRules* \[out\]
</dt> <dd>

Type: **[**IOEExecRules**](oe-ioeexecrules.md)\*\***

Receives the address of a pointer to the new [**IOEExecRules**](oe-ioeexecrules.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                      |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppIExecRules* is **NULL** or that *type* is invalid. <br/> |
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
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





