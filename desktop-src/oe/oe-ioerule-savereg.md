---
title: IOERule SaveReg method
description: IOERule SaveReg is no longer available for use as of Windows Vista.
ms.assetid: a8960137-7b5f-4049-b101-3d502f687230
keywords:
- SaveReg method Windows Mail (formerly Outlook Express)
- SaveReg method Windows Mail (formerly Outlook Express) , IOERule interface
- IOERule interface Windows Mail (formerly Outlook Express) , SaveReg method
topic_type:
- apiref
api_name:
- IOERule.SaveReg
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

# IOERule::SaveReg method

\[**IOERule::SaveReg** is no longer available for use as of Windows Vista.\]

Writes the rule to the registry.

## Syntax


```C++
HRESULT SaveReg(
  [in] LPCSTR szRegPath,
  [in] BOOL   fClearDirty
);
```



## Parameters

<dl> <dt>

*szRegPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the path to the rule's registry key.

</dd> <dt>

*fClearDirty* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether the rule state is dirty.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                                                           |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that there are no criteria or actions, that the registry key could not be created, or that *szRegPath* is invalid. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *szRegPath* is **NULL**. <br/>                                                                                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                                                          |



 

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



 

 





