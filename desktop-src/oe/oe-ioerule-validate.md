---
title: IOERule Validate method
description: IOERule Validate is no longer available for use as of Windows Vista.
ms.assetid: 14492f67-bd58-4641-8f83-750f3f355517
keywords:
- Validate method Windows Mail (formerly Outlook Express)
- Validate method Windows Mail (formerly Outlook Express) , IOERule interface
- IOERule interface Windows Mail (formerly Outlook Express) , Validate method
topic_type:
- apiref
api_name:
- IOERule.Validate
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

# IOERule::Validate method

\[**IOERule::Validate** is no longer available for use as of Windows Vista.\]

Validates the criteria and actions associated with the rule.

## Syntax


```C++
HRESULT Validate(
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies one of the following values used for validating criteria.

<dl> <dt>

<span id="CRIT_FLAG_DEFAULT"></span><span id="crit_flag_default"></span>**CRIT\_FLAG\_DEFAULT** (0x00000000)
</dt> <dt>

<span id="CRIT_FLAG_INVERT"></span><span id="crit_flag_invert"></span>**CRIT\_FLAG\_INVERT** (0x00000001)
</dt> <dt>

<span id="CRIT_FLAG_MULTIPLEAND"></span><span id="crit_flag_multipleand"></span>**CRIT\_FLAG\_MULTIPLEAND** (0x00000002)
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                  |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the rule is valid. <br/>                |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the rule is invalid. <br/>              |
| <dl> <dt>**E\_FAIL**</dt> </dl>  | Indicates that there are no criteria or actions. <br/> |



 

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



 

 





