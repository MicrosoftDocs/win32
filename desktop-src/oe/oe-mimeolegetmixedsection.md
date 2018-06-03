---
title: MimeOleGetMixedSection function
description: Do not use. Returns a handle to the first body in the message tree that has the mixed content type. Also returns whether other instances were found. If mixed content type is not found, method argument specifies whether it should be created.
ms.assetid: b73de187-e896-416b-aadc-b2deef9bfea4
keywords:
- MimeOleGetMixedSection function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetMixedSection
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleGetMixedSection function

Do not use. Returns a handle to the first body in the message tree that has the mixed content type. Also returns whether other instances were found. If mixed content type is not found, method argument specifies whether it should be created.

## Syntax


```C++
HRESULT MimeOleGetMixedSection(
  _In_  IMimeMessageTree *pTree,
  _In_  boolean          fCreate,
  _Out_ LPHBODY          phMixed,
  _Out_ boolean          *pfMultiple
);
```



## Parameters

<dl> <dt>

*pTree* \[in\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)\***

Specifies a pointer to the [**IMimeMessageTree**](oe-imimemessagetree.md) object.

</dd> <dt>

*fCreate* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether to create section if not found.

</dd> <dt>

*phMixed* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives handle of the mixed body section.

</dd> <dt>

*pfMultiple* \[out\]
</dt> <dd>

Type: **boolean\***

Returns whether there were multiple/mixed body parts.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                        |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pTree* is **NULL**. <br/>                    |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that content type neither found nor created. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





