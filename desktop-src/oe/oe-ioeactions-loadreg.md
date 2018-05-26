---
title: IOEActions LoadReg method
description: IOEActions LoadReg is no longer available for use as of Windows Vista.
ms.assetid: 39ffc894-3fc6-4b8c-8e32-a43daa8eeb59
keywords:
- LoadReg method Windows Mail (formerly Outlook Express)
- LoadReg method Windows Mail (formerly Outlook Express) , IOEActions interface
- IOEActions interface Windows Mail (formerly Outlook Express) , LoadReg method
topic_type:
- apiref
api_name:
- IOEActions.LoadReg
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

# IOEActions::LoadReg method

\[**IOEActions::LoadReg** is no longer available for use as of Windows Vista.\]

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



 

 





