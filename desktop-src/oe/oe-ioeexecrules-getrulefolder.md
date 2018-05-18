---
title: IOEExecRules GetRuleFolder method
description: IOEExecRules GetRuleFolder is no longer available for use as of Windows Vista.
ms.assetid: 'c924846a-2005-42e8-bb29-72e0d02ca75c'
keywords: ["GetRuleFolder method Windows Mail (formerly Outlook Express)", "GetRuleFolder method Windows Mail (formerly Outlook Express) , IOEExecRules interface", "IOEExecRules interface Windows Mail (formerly Outlook Express) , GetRuleFolder method"]
topic_type:
- apiref
api_name:
- IOEExecRules.GetRuleFolder
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOEExecRules::GetRuleFolder method

\[**IOEExecRules::GetRuleFolder** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT GetRuleFolder(
  [in]  FOLDERID  idfolder,
  [out] DWORD_PTR *pdwFolder
);
```



## Parameters

<dl> <dt>

*idfolder* \[in\]
</dt> <dd>

Type: **FOLDERID**

</dd> <dt>

*pdwFolder* \[out\]
</dt> <dd>

Type: **DWORD\_PTR\***

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



 

 





