---
title: IMimeAddressTableW ParseRfc822W method
description: Parses the specified RFC 822 address string.
ms.assetid: '3c05cd2f-76bc-4b9f-b57b-4549c0b77a1d'
keywords: ["ParseRfc822W method Windows Mail (formerly Outlook Express)", "ParseRfc822W method Windows Mail (formerly Outlook Express) , IMimeAddressTableW interface", "IMimeAddressTableW interface Windows Mail (formerly Outlook Express) , ParseRfc822W method"]
topic_type:
- apiref
api_name:
- IMimeAddressTableW.ParseRfc822W
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeAddressTableW::ParseRfc822W method

Parses the specified [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address string.

## Syntax


```C++
HRESULT ParseRfc822W(
  [in]      DWORD         dwAdrType,
  [in]      ENCODINGTYPE  ietEncoding,
  [in]      LPCWSTR       pwszRfc822Adr,
  [in, out] LPADDRESSLIST pList
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a single IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the address type being parsed or an address type created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies whether the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address is encoded. Only [**IET\_ENCODED**](oe-encodingtype.md) and **IET\_DECODED** are valid values for this parameter.

</dd> <dt>

*pwszRfc822Adr* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the **LPCWSTR** that contain the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address string to parse.

</dd> <dt>

*pList* \[in, out\]
</dt> <dd>

Type: **LPADDRESSLIST**

Receives a pointer to an [**ADDRESSLIST**](oe-addresslist.md) structure that contains the list of parsed addresses. The client is responsible for freeing this structure by calling [**FreeAddressList**](oe-imimeallocator-freeaddresslist.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred.<br/>                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pwszRfc822Adr* is **NULL**. <br/>                          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/>                  |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *dwAdrType* does not specify an a valid address type. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





