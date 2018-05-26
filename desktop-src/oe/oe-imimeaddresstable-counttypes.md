---
title: IMimeAddressTable CountTypes method
description: Gets the number of addresses that match the specified set of address types.
ms.assetid: d2dcbbf6-87ba-4a95-995a-ad54a60c2c5c
keywords:
- CountTypes method Windows Mail (formerly Outlook Express)
- CountTypes method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , CountTypes method
topic_type:
- apiref
api_name:
- IMimeAddressTable.CountTypes
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

# IMimeAddressTable::CountTypes method

Gets the number of addresses that match the specified set of address types.

## Syntax


```C++
HRESULT CountTypes(
  [in]  DWORD dwAdrTypes,
  [out] ULONG *pcAdrs
);
```



## Parameters

<dl> <dt>

*dwAdrTypes* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the types of addresses to count. The bitmask may also include values for addresses types created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*pcAdrs* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of addresses whose type matches *dwAdrTypes*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pcAdrs* is **NULL**. <br/>                |
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



 

 





