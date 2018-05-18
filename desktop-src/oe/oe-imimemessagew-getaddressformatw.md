---
title: IMimeMessageW GetAddressFormatW method
description: Gets a set of addresses in a text-based format.
ms.assetid: 'ba156796-95ec-473f-9aa3-fc1769d5140d'
keywords: ["GetAddressFormatW method Windows Mail (formerly Outlook Express)", "GetAddressFormatW method Windows Mail (formerly Outlook Express) , IMimeMessageW interface", "IMimeMessageW interface Windows Mail (formerly Outlook Express) , GetAddressFormatW method"]
topic_type:
- apiref
api_name:
- IMimeMessageW.GetAddressFormatW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageW::GetAddressFormatW method

Gets a set of addresses in a text-based format.

## Syntax


```C++
HRESULT GetAddressFormatW(
  [in]  DWORD         dwAdrType,
  [in]  ADDRESSFORMAT format,
  [out] LPWSTR        *ppwszFormat
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the type of addresses to return. For a list of possible values, see [**ADDRESSPROPS**](oe-addressprops.md).**dwAdrType**. This parameter can also include values created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*format* \[in\]
</dt> <dd>

Type: **[**ADDRESSFORMAT**](oe-addressformat.md)**

Specifies a value from [**ADDRESSFORMAT**](oe-addressformat.md) that indicates the format of the text-based address.

</dd> <dt>

*ppwszFormat* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to the address format string. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                      | Description                                                           |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success.<br/>                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>           | Indicates that an unknown error has occurred.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | Indicates that *ppwszFormat* is **NULL**.<br/>                  |
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



 

 





