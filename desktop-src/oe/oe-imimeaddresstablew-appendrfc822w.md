---
title: IMimeAddressTableW AppendRfc822W method
description: Appends an RFC 822 formatted address string to the address table. The RFC 822 address string must be formatted according to RFC 822 and may contain one or more friendly-name/email address pairs.
ms.assetid: 16ee01a7-8a0b-4f37-a4f0-494e372dee3a
keywords:
- AppendRfc822W method Windows Mail (formerly Outlook Express)
- AppendRfc822W method Windows Mail (formerly Outlook Express) , IMimeAddressTableW interface
- IMimeAddressTableW interface Windows Mail (formerly Outlook Express) , AppendRfc822W method
topic_type:
- apiref
api_name:
- IMimeAddressTableW.AppendRfc822W
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

# IMimeAddressTableW::AppendRfc822W method

Appends an [RFC 822](http://www.ietf.org/rfc/rfc822.txt) formatted address string to the address table. The [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address string must be formatted according to [RFC 822](http://www.ietf.org/rfc/rfc822.txt) and may contain one or more friendly-name/email address pairs.

## Syntax


```C++
HRESULT AppendRfc822W(
  [in] DWORD        dwAdrType,
  [in] ENCODINGTYPE ietEncoding,
  [in] LPCWSTR      pwszRfc822Adr
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a single IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the address type being appended or an address type created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies whether the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address is encoded. Only [**IET\_ENCODED**](oe-encodingtype.md) and **IET\_DECODED** are valid values for this parameter.

</dd> <dt>

*pwszRfc822Adr* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the **LPCWSTR** that contains the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) address to append.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred.<br/>                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pwszRfc822Adr* is **NULL**. <br/>                          |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *dwAdrType* does not specify an a valid address type. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





