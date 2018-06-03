---
title: IMimeAddressTable EnumTypes method
description: Enumerates a group of addresses that match the specified set of address types.
ms.assetid: 5dc13d55-9e7f-4a68-80b2-b113ee5bc157
keywords:
- EnumTypes method Windows Mail (formerly Outlook Express)
- EnumTypes method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , EnumTypes method
topic_type:
- apiref
api_name:
- IMimeAddressTable.EnumTypes
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

# IMimeAddressTable::EnumTypes method

Enumerates a group of addresses that match the specified set of address types.

## Syntax


```C++
HRESULT EnumTypes(
  [in]  DWORD                 dwAdrTypes,
  [in]  DWORD                 dwProps,
  [out] IMimeEnumAddressTypes **ppEnum
);
```



## Parameters

<dl> <dt>

*dwAdrTypes* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the types of addresses to enumerate. The bitmask may also include values for addresses types created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*dwProps* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAP\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that specifies which properties to return in each **ADDRESSPROPS** structure in a call to [**Next**](oe-imimeenumaddresstypes-next.md).

</dd> <dt>

*ppEnum* \[out\]
</dt> <dd>

Type: **[**IMimeEnumAddressTypes**](oe-imimeenumaddresstypes.md)\*\***

Receives the address of a pointer to a [**IMimeEnumAddressTypes**](oe-imimeenumaddresstypes.md) object. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppEnum* is **NULL**. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





