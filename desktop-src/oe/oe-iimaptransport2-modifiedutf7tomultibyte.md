---
title: IIMAPTransport2 ModifiedUTF7ToMultiByte method
description: Converts a modified Internet Message Access Protocol (IMAP) 7-bit Unicode Transformation Format (UTF-7) string (defined in RFC 2060) to a multibyte character set (MBCS) string.
ms.assetid: 81edd2d7-c7db-49a2-b2d4-1863b1913d9f
keywords:
- ModifiedUTF7ToMultiByte method Windows Mail (formerly Outlook Express)
- ModifiedUTF7ToMultiByte method Windows Mail (formerly Outlook Express) , IIMAPTransport2 interface
- IIMAPTransport2 interface Windows Mail (formerly Outlook Express) , ModifiedUTF7ToMultiByte method
topic_type:
- apiref
api_name:
- IIMAPTransport2.ModifiedUTF7ToMultiByte
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

# IIMAPTransport2::ModifiedUTF7ToMultiByte method

\[**IIMAPTransport2::ModifiedUTF7ToMultiByte** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Converts a modified Internet Message Access Protocol (IMAP) 7-bit Unicode Transformation Format (UTF-7) string (defined in [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt)) to a multibyte character set (MBCS) string.

## Syntax


```C++
HRESULT ModifiedUTF7ToMultiByte(
  [in]  LPCSTR pszSource,
  [out] LPSTR  *ppszDestination,
  [in]  UINT   uiDestinationCP,
  [in]  DWORD  dwFlags
);
```



## Parameters

<dl> <dt>

*pszSource* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a null-terminated string containing the modified IMAP UTF-7 string to convert.

</dd> <dt>

*ppszDestination* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the null-terminated multibyte equivalent of *pszSource*. The client is responsible for freeing this pointer.

</dd> <dt>

*uiDestinationCP* \[in\]
</dt> <dd>

Type: **UINT**

Specifies a **UINT** that indicates the code page to use for *ppszDestination*.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved. Must be zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success. <br/>                                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**IXP\_S\_IMAP\_VERBATIM\_MBOX**</dt> </dl> | Indicates that *pszSource* could not be converted. *ppszDestination* contains a duplicate of *pszSource*. When the **IMAP\_MBOXXLATE\_VERBATIMOK** flag is set through the [**IIMAPTransport2::SetDefaultCP**](oe-iimaptransport2-setdefaultcp.md) method and the target code page is Unicode, *pszSource* is converted to Unicode with the assumption that it is USASCII. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an attempt to convert one or more characters failed. <br/>                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed. <br/>                                                                                                                                                                                                                                                                                                                        |



 

## Remarks

IIMAPTransport usually handles the conversion automatically. This method must be explicitly called when the client has disabled mailbox name conversion using [**IIMAPTransport2::SetDefaultCP**](oe-iimaptransport2-setdefaultcp.md).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





