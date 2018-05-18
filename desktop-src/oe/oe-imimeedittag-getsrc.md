---
title: IMimeEditTag GetSrc method
description: Gets the source attributes on a tag.
ms.assetid: 'ae04a53a-6884-45a8-800d-8d38a35d7442'
keywords: ["GetSrc method Windows Mail (formerly Outlook Express)", "GetSrc method Windows Mail (formerly Outlook Express) , IMimeEditTag interface", "IMimeEditTag interface Windows Mail (formerly Outlook Express) , GetSrc method"]
topic_type:
- apiref
api_name:
- IMimeEditTag.GetSrc
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEditTag::GetSrc method

\[**IMimeEditTag::GetSrc** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the source attributes on a tag. This is tag-specific and is where the data is coming from. Implementors should adjust the HTML source accordingly.

## Syntax


```C++
HRESULT GetSrc(
  [out] BSTR *pbstr
);
```



## Parameters

<dl> <dt>

*pbstr* \[out\]
</dt> <dd>

Type: **BSTR\***

Specifies pointer to source.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





