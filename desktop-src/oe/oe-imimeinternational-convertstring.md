---
title: IMimeInternational ConvertString method
description: Converts a string from one code page to another.
ms.assetid: 5873e192-0057-4c3b-a31c-e8caf69e609c
keywords:
- ConvertString method Windows Mail (formerly Outlook Express)
- ConvertString method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , ConvertString method
topic_type:
- apiref
api_name:
- IMimeInternational.ConvertString
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

# IMimeInternational::ConvertString method

Converts a string from one code page to another.

## Syntax


```C++
HRESULT ConvertString(
  [in]      CODEPAGEID    cpiSource,
  [in]      CODEPAGEID    cpiDest,
  [in]      LPPROPVARIANT pIn,
  [in, out] LPPROPVARIANT pOut
);
```



## Parameters

<dl> <dt>

*cpiSource* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the source code page ID for *pIn*. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*cpiDest* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the code page ID to convert *pIn* into. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*pIn* \[in\]
</dt> <dd>

Type: **LPPROPVARIANT**

Specifies a pointer to the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the string to be converted.

</dd> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **LPPROPVARIANT**

Receives a pointer to the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the converted string. The client is responsible for freeing this structure.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pIn* or *pOut* is **NULL** or that *pIn*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) or *pOut*-&gt;vt is not equal to VT\_LPSTR ro VT\_LPWSTR. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that the conversion failed. <br/>                                                                                                        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                                                                          |



 

## Remarks

A client may want to call [**IMimeInternational::CanConvertCodePages**](oe-imimeinternational-canconvertcodepages.md) before calling this method to make sure that it is valid to convert from *cpiSource* to *cpiDest*.

If *cpiDest* is equal to CP\_UNICODE (1200), MimeOLE sets *pOut*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) equal to VT\_LPWSTR and returns the converted string in *pOut*-&gt;pwszVal. If *cpiDest* is not Unicode, MimeOLE sets *pOut*-&gt;vt to VT\_LPSTR and returns the converted string in *pOut*-&gt;pszVal.

The client must specify VT\_LPSTR or VT\_LPWSTR for *pIn*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





