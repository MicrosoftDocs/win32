---
title: IMimeAddressTableW GetFormatW method
description: Gets a text-based representation for a group of addresses that match a specified set of address types.
ms.assetid: dcb6e139-538c-44a8-8e5c-4d9602956ebc
keywords:
- GetFormatW method Windows Mail (formerly Outlook Express)
- GetFormatW method Windows Mail (formerly Outlook Express) , IMimeAddressTableW interface
- IMimeAddressTableW interface Windows Mail (formerly Outlook Express) , GetFormatW method
topic_type:
- apiref
api_name:
- IMimeAddressTableW.GetFormatW
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

# IMimeAddressTableW::GetFormatW method

Gets a text-based representation for a group of addresses that match a specified set of address types.

## Syntax


```C++
HRESULT GetFormatW(
  [in]  DWORD         dwAdrType,
  [in]  ADDRESSFORMAT format,
  [out] LPWSTR        *ppwszFormat
);
```



## Parameters

<dl> <dt>

*dwAdrType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies an IAT\_*xxx* bitmask (see [**ADDRESSPROPS**](oe-addressprops.md) for the list of bitmask values) that indicates the types of addresses to count. The bitmask may also include values for address types created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

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



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppwszFormat* is **NULL**. <br/>           |
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



 

 





