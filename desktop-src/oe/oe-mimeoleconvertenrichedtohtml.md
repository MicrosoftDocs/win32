---
title: MimeOleConvertEnrichedToHTML function
description: Do not use. Converts text/enriched to text/html.
ms.assetid: '8aa953d0-49f9-4ea7-ab1c-a97fd34db90a'
keywords: ["MimeOleConvertEnrichedToHTML function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleConvertEnrichedToHTML
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleConvertEnrichedToHTML function

Do not use. Converts text/enriched to text/html.

## Syntax


```C++
HRESULT MimeOleConvertEnrichedToHTML(
  _In_ CODEPAGEID codepage,
  _In_ IStream    *pIn,
  _In_ IStream    *pOut
);
```



## Parameters

<dl> <dt>

*codepage* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies a code page. See [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*pIn* \[in\]
</dt> <dd>

Type: **[**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034)\***

Specifies a pointer to an enriched [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) object.

</dd> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034)\***

Specifies a pointer to an HTML [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                    |
|--------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





