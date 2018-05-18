---
title: IMimeInternational MLANG\_ConvertInetString method
description: Passes its arguments through to ConvertINetString, which performs character-set conversion between a given source codepage and a destination codepage identifier.
ms.assetid: 'd3924606-1e29-4f4c-b938-90bfc7740473'
keywords: ["MLANG_ConvertInetString method Windows Mail (formerly Outlook Express)", "MLANG_ConvertInetString method Windows Mail (formerly Outlook Express) , IMimeInternational interface", "IMimeInternational interface Windows Mail (formerly Outlook Express) , MLANG_ConvertInetString method"]
topic_type:
- apiref
api_name:
- IMimeInternational.MLANG_ConvertInetString
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeInternational::MLANG\_ConvertInetString method

Passes its arguments through to [**ConvertINetString**](https://msdn.microsoft.com/library/aa741106), which performs character-set conversion between a given source codepage and a destination codepage identifier.

## Syntax


```C++
HRESULT MLANG_ConvertInetString(
  [in]  CODEPAGEID cpiSource,
  [in]  CODEPAGEID cpiDest,
  [in]  LPCSTR     pSource,
  [in]  int        *pnSizeOfSource,
  [out] LPSTR      pDestination,
  [in]  int        *pnDstSize
);
```



## Parameters

<dl> <dt>

*cpiSource* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the source code page ID for *pSource*. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*cpiDest* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the destination code page ID for *pDestination*. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*pSource* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the string to convert.

</dd> <dt>

*pnSizeOfSource* \[in\]
</dt> <dd>

Type: **int\***

Specifies a pointer to an **int** that contains the length of the source string in bytes. If the value is **NULL**, or if the length specified is -1, the method assumes that the source string is **null** terminated.

</dd> <dt>

*pDestination* \[out\]
</dt> <dd>

Type: **LPSTR**

Receives an **LPSTR** that contains the converted string.

</dd> <dt>

*pnDstSize* \[in\]
</dt> <dd>

Type: **int\***

Specifies a pointer to an **int** that contains the length of the destination string in bytes.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                                       |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that the specified conversion is not supported on the system. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>                           |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IMimeInternational**](oe-imimeinternational.md)
</dt> <dt>

[**ConvertINetString**](https://msdn.microsoft.com/library/aa741106)
</dt> </dl>

 

 





