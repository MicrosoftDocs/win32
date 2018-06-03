---
title: IMimeInternational ConvertBuffer method
description: Converts the buffer from one code page to another code page.
ms.assetid: 4b24dd80-0e7a-4391-bec3-decea0814f75
keywords:
- ConvertBuffer method Windows Mail (formerly Outlook Express)
- ConvertBuffer method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , ConvertBuffer method
topic_type:
- apiref
api_name:
- IMimeInternational.ConvertBuffer
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

# IMimeInternational::ConvertBuffer method

Converts the buffer from one code page to another code page.

## Syntax


```C++
HRESULT ConvertBuffer(
  [in]      CODEPAGEID cpiSource,
  [in]      CODEPAGEID cpiDest,
  [in]      LPBLOB     pIn,
  [in, out] LPBLOB     pOut,
  [out]     ULONG      *pcbRead
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

Type: **LPBLOB**

Specifies a pointer to the a [BLOB](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp) structure that contains the source buffer.

</dd> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **LPBLOB**

Receives a pointer to the a [BLOB](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp) structure that contains the converted buffer and the size. The client is responsible for freeing *pOut*-&gt;pBlobData by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> <dt>

*pcbRead* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a that contains the number of bytes read from *pIn*-&gt;[pBlobData](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp). This value can be less than or equal to *pIn*-&gt;cbSize.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Indicates success.<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | Indicates that *pIn*, *pIn*-&gt;[pBlobData](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp), or *pOut* is **NULL**. <br/>                                                                                                                                                                                                                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>                    | Indicates that there is nothing to convert or that a call to Mlang.dll to convert the buffer failed. <br/>                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>             | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**MIME\_S\_CHARSET\_CONFLICT**</dt> </dl> | Indicates that *pIn*-&gt;[pBlobData](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp) contains characters that could not be converted to *cpiDest* without data loss. This can happen when *pIn*-&gt;pBlobData contains characters from multiple code pages or is Unicode. A client can work around this problem by converting the buffer to Unicode, UTF-7, or UTF-8. <br/> |



 

## Remarks

A client may want to call [**IMimeInternational::CanConvertCodePages**](oe-imimeinternational-canconvertcodepages.md) before calling this method to make sure that it is valid to convert from *cpiSource* to *cpiDest*.

On successful return, *pcbRead* contains the number of bytes read from *pIn*-&gt;[pBlobData](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp). It is possible that *pcbRead* may not equal *pIn*-&gt;cbSize. For example, this can happen when *pIn* contains a double-byte character set (DBCS) buffer in which the last character of the buffer is a lead byte. The client is responsible for handling this case when converting a large stream of text by using multiple calls to **IMimeInternational::ConvertBuffer**.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





