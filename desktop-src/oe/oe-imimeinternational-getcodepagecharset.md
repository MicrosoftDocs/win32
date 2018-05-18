---
title: IMimeInternational GetCodePageCharset method
description: Finds a character set for the specified code page.
ms.assetid: 'c7af9c4f-3032-42f0-9881-c7e9303536e3'
keywords: ["GetCodePageCharset method Windows Mail (formerly Outlook Express)", "GetCodePageCharset method Windows Mail (formerly Outlook Express) , IMimeInternational interface", "IMimeInternational interface Windows Mail (formerly Outlook Express) , GetCodePageCharset method"]
topic_type:
- apiref
api_name:
- IMimeInternational.GetCodePageCharset
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeInternational::GetCodePageCharset method

Finds a character set for the specified code page.

## Syntax


```C++
HRESULT GetCodePageCharset(
  [in]  CODEPAGEID  cpiCodePage,
  [in]  CHARSETTYPE ctCsetType,
  [out] LPHCHARSET  phCharset
);
```



## Parameters

<dl> <dt>

*cpiCodePage* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the code page ID. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*ctCsetType* \[in\]
</dt> <dd>

Type: **[**CHARSETTYPE**](oe-charsettype.md)**

Specifies a value from [**CHARSETTYPE**](oe-charsettype.md) that indicates the type of character set.

</dd> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Receives the handle of the character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                    | Description                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | Indicates success.<br/>                                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | Indicates that *phCharset* is **NULL**. <br/>                                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                  | Indicates that an attempt to allocate memory failed.<br/>                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                         | Indicates that there is no default character set.<br/>                                                |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>             | Indicates that *cpiCodePage* is invalid or cannot be found. <br/>                                     |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>               | Indicates that *cpiCodePage* does not contain the character set for the specified *ctCsetType*. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_CHARSET\_TYPE**</dt> </dl> | Indicates that *ctCsetType* is not a valid [**CHARSETTYPE**](oe-charsettype.md). <br/>               |



 

## Remarks

There are three different character set types for every code page, each type having a different purpose. [**CHARSETTYPE**](oe-charsettype.md) enumerates these character set types.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





