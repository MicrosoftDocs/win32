---
title: IOECriteria SaveReg method
description: IOECriteria SaveReg is no longer available for use as of Windows Vista.
ms.assetid: 6056e86e-a9e7-4b32-b645-abfd1d27f0c5
keywords:
- SaveReg method Windows Mail (formerly Outlook Express)
- SaveReg method Windows Mail (formerly Outlook Express) , IOECriteria interface
- IOECriteria interface Windows Mail (formerly Outlook Express) , SaveReg method
topic_type:
- apiref
api_name:
- IOECriteria.SaveReg
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

# IOECriteria::SaveReg method

\[**IOECriteria::SaveReg** is no longer available for use as of Windows Vista.\]

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



 

 





