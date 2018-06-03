---
title: IOEExecRules PlaySounds method
description: IOEExecRules PlaySounds is no longer available for use as of Windows Vista.
ms.assetid: 7ad4bb0c-7627-40b6-9a2b-7e6f56cbdb59
keywords:
- PlaySounds method Windows Mail (formerly Outlook Express)
- PlaySounds method Windows Mail (formerly Outlook Express) , IOEExecRules interface
- IOEExecRules interface Windows Mail (formerly Outlook Express) , PlaySounds method
topic_type:
- apiref
api_name:
- IOEExecRules.PlaySounds
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOEExecRules::PlaySounds method

\[**IOEExecRules::PlaySounds** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT PlaySounds(
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



 

 





