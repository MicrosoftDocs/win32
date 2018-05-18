---
title: IMimeEnumAddressTypes Clone method
description: Creates another enumerator that contains the same enumeration state as the current one.
ms.assetid: 'a20144b9-c0f6-49dd-9dee-e203ffb9afb0'
keywords: ["Clone method Windows Mail (formerly Outlook Express)", "Clone method Windows Mail (formerly Outlook Express) , IMimeEnumAddressTypes interface", "IMimeEnumAddressTypes interface Windows Mail (formerly Outlook Express) , Clone method"]
topic_type:
- apiref
api_name:
- IMimeEnumAddressTypes.Clone
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEnumAddressTypes::Clone method

Creates another enumerator that contains the same enumeration state as the current one.

## Syntax


```C++
HRESULT Clone(
  [out] IMimeEnumAddressTypes **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* \[out\]
</dt> <dd>

Type: **[**IMimeEnumAddressTypes**](oe-imimeenumaddresstypes.md)\*\***

Receives the address of a pointer to the new [**IMimeEnumAddressTypes**](oe-imimeenumaddresstypes.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppEnum* is **NULL**. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

Using this method, a client can record a particular point in the enumeration sequence, and then return to that point at a later time. The new enumerator supports the same interface as the original one.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





