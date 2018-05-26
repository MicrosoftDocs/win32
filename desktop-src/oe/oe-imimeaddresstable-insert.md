---
title: IMimeAddressTable Insert method
description: Inserts a new address into the address table.
ms.assetid: f7c2e606-1030-431f-b808-4014f8c960e9
keywords:
- Insert method Windows Mail (formerly Outlook Express)
- Insert method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , Insert method
topic_type:
- apiref
api_name:
- IMimeAddressTable.Insert
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

# IMimeAddressTable::Insert method

Inserts a new address into the address table.

## Syntax


```C++
HRESULT Insert(
  [in]  LPADDRESSPROPS pAddress,
  [out] LPHADDRESS     phAddress
);
```



## Parameters

<dl> <dt>

*pAddress* \[in\]
</dt> <dd>

Type: **LPADDRESSPROPS**

Specifies a pointer to an [**ADDRESSPROPS**](oe-addressprops.md) structures that defines the new address to insert.

</dd> <dt>

*phAddress* \[out\]
</dt> <dd>

Type: **LPHADDRESS**

Receives the handle of the newly inserted address.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success. <br/>                                                                                                                                                                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred. <br/>                                                                                                                                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pAddress* is **NULL**, that *pAddress*-&gt;**dwProps** does not include IAP\_ADRTYPE, or that *pAddress*-&gt;**pszEmail** is **NULL** when *pAddress*-&gt;**dwProps** includes IAP\_EMAIL. <br/> |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>      | Indicates that *pAddress*-&gt;**dwAdrType** is invalid. <br/>                                                                                                                                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                        |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *pAddress*-&gt;**hCharset** is invalid when *pAddress*-&gt;**dwProps** includes IAP\_CHARSET. <br/>                                                                                               |



 

## Remarks

The *pAddress*-&gt;**dwProps** member must be initialized to define valid fields in the [**ADDRESSPROPS**](oe-addressprops.md) structure. The *pAddress*-&gt;**dwAdrType** field must be set to one of the values in the IAT\_*xxx* bitmask or to an address type that was created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





