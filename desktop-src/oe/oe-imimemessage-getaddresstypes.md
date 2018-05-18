---
title: IMimeMessage GetAddressTypes method
description: Gets a set of addresses from the message.
ms.assetid: 'a94cf61e-adab-4a63-b104-d876540f6f6a'
keywords: ["GetAddressTypes method Windows Mail (formerly Outlook Express)", "GetAddressTypes method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , GetAddressTypes method"]
topic_type:
- apiref
api_name:
- IMimeMessage.GetAddressTypes
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::GetAddressTypes method

Gets a set of addresses from the message.

## Syntax


```C++
HRESULT GetAddressTypes(
  [in]      DWORD         dwAdrTypes,
  [in]      DWORD         dwProps,
  [in, out] LPADDRESSLIST pList
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

Specifies the properties to return in each [**ADDRESSPROPS**](oe-addressprops.md) structure. See [**ADDRESSPROPS**](oe-addressprops.md).**dwProps** for a list of possible values.

</dd> <dt>

*pList* \[in, out\]
</dt> <dd>

Type: **LPADDRESSLIST**

Receives the requested [**ADDRESSLIST**](oe-addresslist.md) object. The client is responsible for freeing this structure by calling [**FreeAddressList**](oe-imimeallocator-freeaddresslist.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pList* is **NULL**.<br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

This method is equivalent to:

pMessage-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(HBODY\_ROOT, IID\_IMimeAddressTable, (LPVOID \*)&pAddressTable);

pAddressTable-&gt;[**GetTypes**](oe-imimeaddresstable-gettypes.md)(*dwAdrTypes*, *dwProps*, *pList*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





