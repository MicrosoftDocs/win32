---
title: IOERule LoadReg method
description: IOERule LoadReg is no longer available for use as of Windows Vista.
ms.assetid: 49edce3e-c96d-4441-883e-ecfd5b6ec257
keywords:
- LoadReg method Windows Mail (formerly Outlook Express)
- LoadReg method Windows Mail (formerly Outlook Express) , IOERule interface
- IOERule interface Windows Mail (formerly Outlook Express) , LoadReg method
topic_type:
- apiref
api_name:
- IOERule.LoadReg
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

# IOERule::LoadReg method

\[**IOERule::LoadReg** is no longer available for use as of Windows Vista.\]

Gets the rule from the registry.

## Syntax


```C++
HRESULT LoadReg(
  [in] LPCSTR szRegPath
);
```



## Parameters

<dl> <dt>

*szRegPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the path to the rule's registry key.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *szRegPath* is **NULL**. <br/>                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that the registry key could not be opened or that *szRegPath* is invalid. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                 |



 

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



 

 





