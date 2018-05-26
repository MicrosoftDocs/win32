---
title: IMimeAddressTable GetTypes method
description: Get a list of addresses that match the specified set of address types.
ms.assetid: 4747cd44-5002-4a75-bfa5-7e9f774392f5
keywords:
- GetTypes method Windows Mail (formerly Outlook Express)
- GetTypes method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , GetTypes method
topic_type:
- apiref
api_name:
- IMimeAddressTable.GetTypes
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

# IMimeAddressTable::GetTypes method

Get a list of addresses that match the specified set of address types.

## Syntax


```C++
HRESULT GetTypes(
  [in]      DWORD         dwAdrTypes,
  [in]      DWORD         dwProps,
  [in, out] LPADDRESSLIST pList
);
```



## Parameters

<dl> <dt>

*dwAdrTypes* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the types of addresses to get. The bitmask may also include values for addresses types created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*dwProps* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAP\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that specifies which properties to return in each **ADDRESSPROPS** structure.

</dd> <dt>

*pList* \[in, out\]
</dt> <dd>

Type: **LPADDRESSLIST**

Receives a pointer to an [**ADDRESSLIST**](oe-addresslist.md) structure that contains the list of [**ADDRESSPROPS**](oe-addressprops.md) structures. The client is responsible for freeing this structure by calling [**FreeAddressList**](oe-imimeallocator-freeaddresslist.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pList* is **NULL**. <br/>                 |
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



 

 





