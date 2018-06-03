---
title: IMimeInternational Rfc1522Decode method
description: Decodes an RFC 1522 encoded string.
ms.assetid: a8e83551-7584-4ec2-b1ee-f5220eba0e56
keywords:
- Rfc1522Decode method Windows Mail (formerly Outlook Express)
- Rfc1522Decode method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , Rfc1522Decode method
topic_type:
- apiref
api_name:
- IMimeInternational.Rfc1522Decode
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeInternational::Rfc1522Decode method

Decodes an [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded string.

## Syntax


```C++
HRESULT Rfc1522Decode(
  [in]  LPCSTR pszValue,
  [in]  LPSTR  pszCharset,
  [in]  ULONG  cchmax,
  [out] LPSTR  *ppszDecoded
);
```



## Parameters

<dl> <dt>

*pszValue* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded string.

</dd> <dt>

*pszCharset* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the name of the character set contained in the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding.

</dd> <dt>

*cchmax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the maximum number of characters that can be copied into *pszCharset*.

</dd> <dt>

*ppszDecoded* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) decoded string. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszValue* is **NULL**. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that the conversion failed. <br/>  |



 

## Remarks

This method does not translate the text to a Windows code page. A client can call [**IMimeInternational::DecodeHeader**](oe-imimeinternational-decodeheader.md) to remove an [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding and translate the text to a Windows code page.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





