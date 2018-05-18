---
title: IMimeMessage EnumAddressTypes method
description: Enumerates a set of addresses from the message.
ms.assetid: '7fcea658-5997-4bdc-9985-5e2085063617'
keywords: ["EnumAddressTypes method Windows Mail (formerly Outlook Express)", "EnumAddressTypes method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , EnumAddressTypes method"]
topic_type:
- apiref
api_name:
- IMimeMessage.EnumAddressTypes
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::EnumAddressTypes method

Enumerates a set of addresses from the message.

## Syntax


```C++
HRESULT EnumAddressTypes(
  [in]  DWORD                 dwAdrTypes,
  [in]  DWORD                 dwProps,
  [out] IMimeEnumAddressTypes **ppEnum
);
```



## Parameters

<dl> <dt>

*dwAdrTypes* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the type of addresses to return. See [**ADDRESSPROPS**](oe-addressprops.md).**dwAdrType** for a list of possible values. This parameter can also include values created by the [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md) method.

</dd> <dt>

*dwProps* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies which properties to return in each [**ADDRESSPROPS**](oe-addressprops.md) structure in a call to [**RegisterAddressType**](oe-imimepropertyschema-registeraddresstype.md). See [**ADDRESSPROPS**](oe-addressprops.md).**dwProps** for a list of possible values.

</dd> <dt>

*ppEnum* \[out\]
</dt> <dd>

Type: **[**IMimeEnumAddressTypes**](oe-imimeenumaddresstypes.md)\*\***

Receives a pointer to an [**IMimeEnumAddressTypes**](oe-imimeenumaddresstypes.md) object. The client is responsible for releasing the object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppEnum* is **NULL**.<br/>                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

This method is equivalent to:

pMessage-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(HBODY\_ROOT, IID\_IMimeAddressTable, (LPVOID \*)&pAddressTable);

pAddressTable-&gt;[**EnumTypes**](oe-imimeaddresstable-enumtypes.md)(*dwAdrTypes*, *dwProps*, *ppEnum*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





