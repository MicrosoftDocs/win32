---
title: IOEActions SaveReg method
description: IOEActions SaveReg is no longer available for use as of Windows Vista.
ms.assetid: 6aa6aa2a-07c0-48a9-87fe-c03ab3cc1d37
keywords:
- SaveReg method Windows Mail (formerly Outlook Express)
- SaveReg method Windows Mail (formerly Outlook Express) , IOEActions interface
- IOEActions interface Windows Mail (formerly Outlook Express) , SaveReg method
topic_type:
- apiref
api_name:
- IOEActions.SaveReg
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

# IOEActions::SaveReg method

\[**IOEActions::SaveReg** is no longer available for use as of Windows Vista.\]

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

</dd> <dt>

*fClearDirty* \[in\]
</dt> <dd>

Type: **BOOL**

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



 

 





