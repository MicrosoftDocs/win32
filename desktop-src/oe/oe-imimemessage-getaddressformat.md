---
title: IMimeMessage GetAddressFormat method
description: Gets a set of addresses in a text-based format.
ms.assetid: '3aa6421b-3be6-4487-aa42-94e5340aae89'
keywords: ["GetAddressFormat method Windows Mail (formerly Outlook Express)", "GetAddressFormat method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , GetAddressFormat method"]
topic_type:
- apiref
api_name:
- IMimeMessage.GetAddressFormat
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::GetAddressFormat method

Gets a set of addresses in a text-based format.

## Syntax


```C++
HRESULT GetAddressFormat(
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

Specifies the type of addresses to return. See [**ADDRESSPROPS**](oe-addressprops.md).**dwAdrType** for a list of possible values. This parameter can also include values created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

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



| Return code                                                                                      | Description                                                                   |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success.<br/>                                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>           | Indicates that an unknown error has occurred.<br/>                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | Indicates that *ppszFormat* is **NULL**.<br/>                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>    | Indicates that an attempt to allocate memory failed.<br/>               |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl> | Indicates that no address was found with address type *dwAdrType*.<br/> |



 

## Remarks

This method is equivalent to:

pMessage-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(HBODY\_ROOT, IID\_IMimeAddressTable, (LPVOID \*)&pAddressTable);

pAddressTable-&gt;[**GetFormat**](oe-imimeaddresstable-getformat.md)(*dwAdrType*, *format*, *ppszFormat*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





