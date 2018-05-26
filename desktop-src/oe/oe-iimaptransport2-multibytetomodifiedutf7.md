---
title: IIMAPTransport2 MultiByteToModifiedUTF7 method
description: Converts a multibyte character set (MBCS) string to modified Internet Message Access Protocol (IMAP) 7-bit Unicode Transformation Format (UTF-7) (defined in RFC 2060).
ms.assetid: 95316f8d-8614-4241-b069-8ccbb11897d4
keywords:
- MultiByteToModifiedUTF7 method Windows Mail (formerly Outlook Express)
- MultiByteToModifiedUTF7 method Windows Mail (formerly Outlook Express) , IIMAPTransport2 interface
- IIMAPTransport2 interface Windows Mail (formerly Outlook Express) , MultiByteToModifiedUTF7 method
topic_type:
- apiref
api_name:
- IIMAPTransport2.MultiByteToModifiedUTF7
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

# IIMAPTransport2::MultiByteToModifiedUTF7 method

\[**IIMAPTransport2::MultiByteToModifiedUTF7** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Converts a multibyte character set (MBCS) string to modified Internet Message Access Protocol (IMAP) 7-bit Unicode Transformation Format (UTF-7) (defined in [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt)).

## Syntax


```C++
HRESULT MultiByteToModifiedUTF7(
  [in]  LPCSTR pszSource,
  [out] LPSTR  *ppszDestination,
  [in]  UINT   uiSourceCP,
  [in]  DWORD  dwFlags
);
```



## Parameters

<dl> <dt>

*pszSource* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the multibyte string to convert.

</dd> <dt>

*ppszDestination* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the modified IMAP UTF-7 equivalent of *pszSource*. The client is responsible for freeing this pointer.

</dd> <dt>

*uiSourceCP* \[in\]
</dt> <dd>

Type: **UINT**

Specifies a **UINT** that indicates the code page to use for *pszSource*.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved. Must be zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                     |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an attempt to convert one or more characters failed. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                |



 

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



 

 





