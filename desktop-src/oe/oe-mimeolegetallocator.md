---
title: MimeOleGetAllocator function
description: Do not use. Creates a new IMimeAllocator object.
ms.assetid: '486118cd-e432-4664-81b7-7c8846a30b00'
keywords: ["MimeOleGetAllocator function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleGetAllocator
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleGetAllocator function

Do not use. Creates a new [**IMimeAllocator**](oe-imimeallocator.md) object.

## Syntax


```C++
HRESULT MimeOleGetAllocator(
  _Out_ IMimeAllocator **ppAllocator
);
```



## Parameters

<dl> <dt>

*ppAllocator* \[out\]
</dt> <dd>

Type: **[**IMimeAllocator**](oe-imimeallocator.md)\*\***

Receives the address of a pointer to the new [**IMimeAllocator**](oe-imimeallocator.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                 |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppAllocator* is **NULL**.<br/>        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





