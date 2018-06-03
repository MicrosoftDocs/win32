---
title: MimeOleParseRfc822AddressW function
description: Do not use. Parses the specified RFC 822 address string.
ms.assetid: 490cc0e8-40df-4901-a139-024e92cc20e8
keywords:
- MimeOleParseRfc822AddressW function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleParseRfc822AddressW
- MimeOleParseRfc822AddressW
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

# MimeOleParseRfc822AddressW function

Do not use. Parses the specified [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address string.

## Syntax


```C++
HRESULT MimeOleParseRfc822AddressW(
  _In_  DWORD         dwAdrType,
  _In_  LPCWSTR       pwszRfc822Adr,
  _Out_ LPADDRESSLIST pList
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a single IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the address type being parsed or an address type created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*pwszRfc822Adr* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the **LPCWSTR** that contains the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address string to parse.

</dd> <dt>

*pList* \[out\]
</dt> <dd>

Type: **LPADDRESSLIST**

Receives a pointer to an [**ADDRESSLIST**](oe-addresslist.md) structure that contains the list of parsed addresses. The client is responsible for freeing this structure by calling [**FreeAddressList**](oe-imimeallocator-freeaddresslist.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                        |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pwszRfc822Adr* or *pList* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>    |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **MimeOleParseRfc822AddressW** (Unicode)<br/>                                                            |



 

 





