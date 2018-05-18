---
title: IMimeAddressTable GetFormat method
description: Gets a text-based representation for a group of addresses that match a specified set of address types.
ms.assetid: '90b4260e-6b3c-413d-a721-0aa7660e80b9'
keywords: ["GetFormat method Windows Mail (formerly Outlook Express)", "GetFormat method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface", "IMimeAddressTable interface Windows Mail (formerly Outlook Express) , GetFormat method"]
topic_type:
- apiref
api_name:
- IMimeAddressTable.GetFormat
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeAddressTable::GetFormat method

Gets a text-based representation for a group of addresses that match a specified set of address types.

## Syntax


```C++
HRESULT GetFormat(
  [in]  DWORD         dwAdrType,
  [in]  ADDRESSFORMAT format,
  [out] LPSTR         *ppszFormat
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the types of addresses to count. The bitmask may also include values for addresses types created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*format* \[in\]
</dt> <dd>

Type: **[**ADDRESSFORMAT**](oe-addressformat.md)**

Specifies a value from [**ADDRESSFORMAT**](oe-addressformat.md) that indicates the format of the text-based address.

</dd> <dt>

*ppszFormat* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to the address format string. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                      | Description                                                           |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success. <br/>                                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>           | Indicates that an unknown error has occurred. <br/>             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | Indicates that *ppszFormat* is **NULL**. <br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>    | Indicates that an attempt to allocate memory failed.<br/>       |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl> | Indicates that no address was found with type *dwAdrType*.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





