---
title: MimeOleVariantCopy function
description: Do not use. Copies memory pointed to by the source variant and allocates new memory for the destination variant.
ms.assetid: 'd47bd872-f772-4e52-9bca-d95a25cef23b'
keywords: ["MimeOleVariantCopy function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleVariantCopy
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleVariantCopy function

Do not use. Copies memory pointed to by the source variant and allocates new memory for the destination variant.

## Syntax


```C++
HRESULT MimeOleVariantCopy(
  _Out_ LPPROPVARIANT pDest,
  _In_  LPPROPVARIANT pSource
);
```



## Parameters

<dl> <dt>

*pDest* \[out\]
</dt> <dd>

Type: **LPPROPVARIANT**

Specifies pointer to destination structure.

</dd> <dt>

*pSource* \[in\]
</dt> <dd>

Type: **LPPROPVARIANT**

Specifies pointer to source structure.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                             |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that a pointer argument or structure content pointer is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





