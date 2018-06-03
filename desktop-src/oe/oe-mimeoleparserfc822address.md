---
title: MimeOleParseRfc822Address function
description: Do not use. Parses the specified address string (on success).
ms.assetid: 716ba7b9-5197-4680-a7d5-0e0041c385f9
keywords:
- MimeOleParseRfc822Address function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleParseRfc822Address
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleParseRfc822Address function

Do not use. Parses the specified address string (on success).

## Syntax


```C++
HRESULT MimeOleParseRfc822Address(
  _In_  DWORD         dwAdrType,
  _In_  ENCODINGTYPE  ietEncoding,
  _In_  LPCSTR        pszRfc822Adr,
  _Out_ LPADDRESSLIST pList
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a single IAT\_*xxx* bitmask that indicates the address type being parsed or an address type created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method. See [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values.

</dd> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies the [**ENCODINGTYPE**](oe-encodingtype.md) value.

</dd> <dt>

*pszRfc822Adr* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the **LPCSTR** that contains the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address string to parse.

</dd> <dt>

*pList* \[out\]
</dt> <dd>

Type: **LPADDRESSLIST**

Receives a pointer to an [**ADDRESSLIST**](oe-addresslist.md) structure that contains the list of parsed addresses. The client is responsible for freeing this structure by calling [**FreeAddressList**](oe-imimeallocator-freeaddresslist.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                       |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszRfc822Adr* or *pList* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>   |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**MimeOleParseRfc822AddressW**](oe-mimeoleparserfc822addressw.md)
</dt> </dl>

 

 





