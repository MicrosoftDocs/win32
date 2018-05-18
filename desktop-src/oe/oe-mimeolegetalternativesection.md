---
title: MimeOleGetAlternativeSection function
description: Do not use. Returns handle to the first body in the message tree that has the alternative content type. Also returns whether other instances were found.
ms.assetid: '456c62d3-65d7-4af9-afd6-2d1a744eebed'
keywords: ["MimeOleGetAlternativeSection function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleGetAlternativeSection
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleGetAlternativeSection function

Do not use. Returns handle to the first body in the message tree that has the alternative content type. Also returns whether other instances were found.

## Syntax


```C++
HRESULT MimeOleGetAlternativeSection(
  _In_  IMimeMessageTree *pTree,
  _Out_ LPHBODY          phAlternative,
  _Out_ boolean          *pfMultiple
);
```



## Parameters

<dl> <dt>

*pTree* \[in\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)\***

Specifies a pointer to the [**IMimeMessageTree**](oe-imimemessagetree.md) object.

</dd> <dt>

*phAlternative* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives handle of an alternative body section.

</dd> <dt>

*pfMultiple* \[out\]
</dt> <dd>

Type: **boolean\***

Returns whether more than one multipart/mixed content type was found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                        |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success whether found or not. <br/>                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pTree* or *phAlternative* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





