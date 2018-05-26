---
title: IOECriteria Validate method
description: IOECriteria Validate is no longer available for use as of Windows Vista.
ms.assetid: d20e563a-1205-4408-bbe0-0f42c7597c1c
keywords:
- Validate method Windows Mail (formerly Outlook Express)
- Validate method Windows Mail (formerly Outlook Express) , IOECriteria interface
- IOECriteria interface Windows Mail (formerly Outlook Express) , Validate method
topic_type:
- apiref
api_name:
- IOECriteria.Validate
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOECriteria::Validate method

\[**IOECriteria::Validate** is no longer available for use as of Windows Vista.\]

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

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





