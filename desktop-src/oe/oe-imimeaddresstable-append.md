---
title: IMimeAddressTable Append method
description: Appends a new address to the address table.
ms.assetid: 831717a4-6b0e-4ea1-9448-492f430f295b
keywords:
- Append method Windows Mail (formerly Outlook Express)
- Append method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , Append method
topic_type:
- apiref
api_name:
- IMimeAddressTable.Append
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

# IMimeAddressTable::Append method

Appends a new address to the address table.

## Syntax


```C++
HRESULT Append(
  [in]  DWORD        dwAdrType,
  [in]  ENCODINGTYPE ietFriendly,
  [in]  LPCSTR       pszFriendly,
  [in]  LPCSTR       pszEmail,
  [out] LPHADDRESS   phAddress
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a single IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the address type being appended or an address type created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*ietFriendly* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies an [**ENCODINGTYPE**](oe-encodingtype.md) value that indicates how the *pszFriendly* parameter is encoded.

</dd> <dt>

*pszFriendly* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the friendly name of the address to append.

</dd> <dt>

*pszEmail* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the email address for the address to append.

</dd> <dt>

*phAddress* \[out\]
</dt> <dd>

Type: **LPHADDRESS**

Receives the handle of the new address.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                   |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred.<br/>                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pszEmail* is an empty string.<br/>                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/>               |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *dwAdrType* does not specify a valid address type. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





