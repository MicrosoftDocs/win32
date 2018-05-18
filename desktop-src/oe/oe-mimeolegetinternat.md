---
title: MimeOleGetInternat function
description: Do not use. Returns an interface used to perform character-set conversions and query information about character sets and codepages.
ms.assetid: 'd38bf061-afc7-404a-9587-a3cd870f2fc6'
keywords: ["MimeOleGetInternat function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleGetInternat
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleGetInternat function

Do not use. Returns an interface used to perform character-set conversions and query information about character sets and codepages.

## Syntax


```C++
HRESULT MimeOleGetInternat(
  _Out_ IMimeInternational **ppInternat
);
```



## Parameters

<dl> <dt>

*ppInternat* \[out\]
</dt> <dd>

Type: **[**IMimeInternational**](oe-imimeinternational.md)\*\***

Receives the address of a pointer to an [**IMimeInternational**](oe-imimeinternational.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                 |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that a pointer parameter is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an allocation failed. <br/>            |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [**IMimeInternational**](oe-imimeinternational.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





