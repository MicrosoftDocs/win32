---
title: IOERulesManager Initialize method
description: IOERulesManager Initialize is no longer available for use as of Windows Vista.
ms.assetid: a49801ad-b953-4a9b-a394-f37548860750
keywords:
- Initialize method Windows Mail (formerly Outlook Express)
- Initialize method Windows Mail (formerly Outlook Express) , IOERulesManager interface
- IOERulesManager interface Windows Mail (formerly Outlook Express) , Initialize method
topic_type:
- apiref
api_name:
- IOERulesManager.Initialize
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

# IOERulesManager::Initialize method

\[**IOERulesManager::Initialize** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT Initialize(
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *dwFlags* is invalid. <br/> |



 

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



 

 





