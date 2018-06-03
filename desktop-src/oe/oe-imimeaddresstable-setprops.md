---
title: IMimeAddressTable SetProps method
description: Changes the properties for an existing address in the address table.
ms.assetid: 646192c8-96b1-420a-9454-2d53fc38cc49
keywords:
- SetProps method Windows Mail (formerly Outlook Express)
- SetProps method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , SetProps method
topic_type:
- apiref
api_name:
- IMimeAddressTable.SetProps
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

# IMimeAddressTable::SetProps method

Changes the properties for an existing address in the address table.

## Syntax


```C++
HRESULT SetProps(
  [in] HADDRESS       hAddress,
  [in] LPADDRESSPROPS pAddress
);
```



## Parameters

<dl> <dt>

*hAddress* \[in\]
</dt> <dd>

Type: **HADDRESS**

Specifies the handle of the address.

</dd> <dt>

*pAddress* \[in\]
</dt> <dd>

Type: **LPADDRESSPROPS**

Specifies the [**ADDRESSPROPS**](oe-addressprops.md) structure that contains the new address properties.

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
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *pAddress*-&gt;**hCharset** is invalid when *pAddress*-&gt;**dwProps** includes IAP\_CHARSET or that *hAddress* is an invalid address handle. <br/>                                               |



 

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



 

 





