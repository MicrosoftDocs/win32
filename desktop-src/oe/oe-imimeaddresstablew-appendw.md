---
title: IMimeAddressTableW AppendW method
description: Appends a new address to the address table.
ms.assetid: bbabe17d-91a8-4c6e-816e-b70e6ae9b672
keywords:
- AppendW method Windows Mail (formerly Outlook Express)
- AppendW method Windows Mail (formerly Outlook Express) , IMimeAddressTableW interface
- IMimeAddressTableW interface Windows Mail (formerly Outlook Express) , AppendW method
topic_type:
- apiref
api_name:
- IMimeAddressTableW.AppendW
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

# IMimeAddressTableW::AppendW method

Appends a new address to the address table.

## Syntax


```C++
HRESULT AppendW(
  [in]  DWORD        dwAdrType,
  [in]  ENCODINGTYPE ietFriendly,
  [in]  LPCWSTR      pwszFriendly,
  [in]  LPCWSTR      pwszEmail,
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

Specifies an [**ENCODINGTYPE**](oe-encodingtype.md) value that indicates how the *pwszFriendly* parameter is encoded.

</dd> <dt>

*pwszFriendly* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the friendly name of the address to append.

</dd> <dt>

*pwszEmail* \[in\]
</dt> <dd>

Type: **LPCWSTR**

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



| Return code                                                                                        | Description                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred.<br/>                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/>                  |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>   | Indicates that no address was found with type *dwAdrType*.<br/>            |
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



 

 





