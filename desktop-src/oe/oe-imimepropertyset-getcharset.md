---
title: IMimePropertySet GetCharset method
description: Gets the character set of the property set.
ms.assetid: '96f2ad6e-6bce-49b7-9ba3-4925e3135b13'
keywords: ["GetCharset method Windows Mail (formerly Outlook Express)", "GetCharset method Windows Mail (formerly Outlook Express) , IMimePropertySet interface", "IMimePropertySet interface Windows Mail (formerly Outlook Express) , GetCharset method"]
topic_type:
- apiref
api_name:
- IMimePropertySet.GetCharset
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimePropertySet::GetCharset method

Gets the character set of the property set.

## Syntax


```C++
HRESULT GetCharset(
  [out] LPHCHARSET phCharset
);
```



## Parameters

<dl> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Receives the handle of the character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *phCharset* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





