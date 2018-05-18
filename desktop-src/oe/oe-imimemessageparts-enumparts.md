---
title: IMimeMessageParts EnumParts method
description: Creates an IMimeEnumMessageParts object that can be used to enumerate the partial messages in the collection.
ms.assetid: '8ff2779b-fbaa-47f9-9889-f90a625f6a58'
keywords: ["EnumParts method Windows Mail (formerly Outlook Express)", "EnumParts method Windows Mail (formerly Outlook Express) , IMimeMessageParts interface", "IMimeMessageParts interface Windows Mail (formerly Outlook Express) , EnumParts method"]
topic_type:
- apiref
api_name:
- IMimeMessageParts.EnumParts
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageParts::EnumParts method

Creates an [**IMimeEnumMessageParts**](oe-imimeenummessageparts.md) object that can be used to enumerate the partial messages in the collection.

## Syntax


```C++
HRESULT EnumParts(
  [out] IMimeEnumMessageParts **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* \[out\]
</dt> <dd>

Type: **[**IMimeEnumMessageParts**](oe-imimeenummessageparts.md)\*\***

Receives the address of a pointer to the [**IMimeEnumMessageParts**](oe-imimeenummessageparts.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppEnum* is **NULL**. <br/>           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





