---
title: IMimeAddressTable DeleteTypes method
description: Deletes a group of addresses that match the specified set of address types.
ms.assetid: c0e31cf6-cca2-4027-851f-5a3c722df884
keywords:
- DeleteTypes method Windows Mail (formerly Outlook Express)
- DeleteTypes method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , DeleteTypes method
topic_type:
- apiref
api_name:
- IMimeAddressTable.DeleteTypes
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

# IMimeAddressTable::DeleteTypes method

Deletes a group of addresses that match the specified set of address types.

## Syntax


```C++
HRESULT DeleteTypes(
  [in] DWORD dwAdrTypes
);
```



## Parameters

<dl> <dt>

*dwAdrTypes* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the types of addresses to delete. The bitmask may also include values for addresses types created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                    |
|--------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





