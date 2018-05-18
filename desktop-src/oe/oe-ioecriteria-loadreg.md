---
title: IOECriteria LoadReg method
description: IOECriteria LoadReg is no longer available for use as of Windows Vista.
ms.assetid: 'ca596a79-bf7a-4f73-ba3c-619b3b09a821'
keywords: ["LoadReg method Windows Mail (formerly Outlook Express)", "LoadReg method Windows Mail (formerly Outlook Express) , IOECriteria interface", "IOECriteria interface Windows Mail (formerly Outlook Express) , LoadReg method"]
topic_type:
- apiref
api_name:
- IOECriteria.LoadReg
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOECriteria::LoadReg method

\[**IOECriteria::LoadReg** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT LoadReg(
  [in] LPCSTR szRegPath
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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





