---
title: IMimeInternational CanConvertCodePages method
description: Determines whether the specified source code page can be translated to the specified destination code page.
ms.assetid: '23d4dff0-3ea5-4436-aaf8-ae2c4abc9706'
keywords: ["CanConvertCodePages method Windows Mail (formerly Outlook Express)", "CanConvertCodePages method Windows Mail (formerly Outlook Express) , IMimeInternational interface", "IMimeInternational interface Windows Mail (formerly Outlook Express) , CanConvertCodePages method"]
topic_type:
- apiref
api_name:
- IMimeInternational.CanConvertCodePages
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeInternational::CanConvertCodePages method

Determines whether the specified source code page can be translated to the specified destination code page.

## Syntax


```C++
HRESULT CanConvertCodePages(
  [in] CODEPAGEID cpiSource,
  [in] CODEPAGEID cpiDest
);
```



## Parameters

<dl> <dt>

*cpiSource* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the source code page ID. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*cpiDest* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the destination code page ID. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that it is possible to convert from *cpiSource* to *cpiDest*. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the conversion is not possible. <br/>                          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





