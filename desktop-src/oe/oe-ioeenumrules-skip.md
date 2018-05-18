---
title: IOEEnumRules Skip method
description: IOEEnumRules Skip is no longer available for use as of Windows Vista.
ms.assetid: 'ed172005-29b1-42b5-862e-608a45f140bd'
keywords: ["Skip method Windows Mail (formerly Outlook Express)", "Skip method Windows Mail (formerly Outlook Express) , IOEEnumRules interface", "IOEEnumRules interface Windows Mail (formerly Outlook Express) , Skip method"]
topic_type:
- apiref
api_name:
- IOEEnumRules.Skip
api_location:
- Msoe.dll
api_type:
- COM
---

# IOEEnumRules::Skip method

\[**IOEEnumRules::Skip** is no longer available for use as of Windows Vista.\]

Skips over the next specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Skip(
  [in] ULONG cpIRule
);
```



## Parameters

<dl> <dt>

*cpIRule* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the number of elements to skip.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                                       |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the number of elements specified by *cpIRule* were skipped. <br/>            |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that fewer than the number of elements specified by *cpIRule* were skipped. <br/> |



 

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



 

 





