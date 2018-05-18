---
title: IMimeAddressTable Clone method
description: Creates a new address table object that is an exact replica of the current address table object. The new address table object has no association with the current address table object.
ms.assetid: 'fb4715c0-0f0b-4536-807d-05ab4cde4abe'
keywords: ["Clone method Windows Mail (formerly Outlook Express)", "Clone method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface", "IMimeAddressTable interface Windows Mail (formerly Outlook Express) , Clone method"]
topic_type:
- apiref
api_name:
- IMimeAddressTable.Clone
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeAddressTable::Clone method

Creates a new address table object that is an exact replica of the current address table object. The new address table object has no association with the current address table object.

## Syntax


```C++
HRESULT Clone(
  [out] IMimeAddressTable **ppTable
);
```



## Parameters

<dl> <dt>

*ppTable* \[out\]
</dt> <dd>

Type: **[**IMimeAddressTable**](oe-imimeaddresstable.md)\*\***

Receives the address of a pointer to the new [**IMimeAddressTable**](oe-imimeaddresstable.md) object. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppTable* is **NULL**. <br/>               |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





