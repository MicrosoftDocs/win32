---
title: IOERule GetState method
description: IOERule GetState is no longer available for use as of Windows Vista.
ms.assetid: '2253a87a-710e-474c-a854-1851c75ee629'
keywords: ["GetState method Windows Mail (formerly Outlook Express)", "GetState method Windows Mail (formerly Outlook Express) , IOERule interface", "IOERule interface Windows Mail (formerly Outlook Express) , GetState method"]
topic_type:
- apiref
api_name:
- IOERule.GetState
api_location:
- Msoe.dll
api_type:
- COM
---

# IOERule::GetState method

\[**IOERule::GetState** is no longer available for use as of Windows Vista.\]

Gets the current state of the rule.

## Syntax


```C++
HRESULT GetState(
  [out] DWORD *pdwState
);
```



## Parameters

<dl> <dt>

*pdwState* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that indicates the state of the rule. A value of RULE\_STATE\_NULL indicates that the rule is invalid or disabled.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pdwState* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| End of client support<br/>    | Windows XP<br/>                                                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                                             |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





