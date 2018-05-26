---
title: MimeOleSplitMessage function
description: Do not use. Splits message into a collection of parts, as determined by a specified maximum part size.
ms.assetid: 22ca361f-2a0b-48ec-83cb-7503b639d181
keywords:
- MimeOleSplitMessage function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSplitMessage
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleSplitMessage function

Do not use. Splits message into a collection of parts, as determined by a specified maximum part size.

## Syntax


```C++
HRESULT MimeOleSplitMessage(
  _In_  IMimeMessage      *pMessage,
  _In_  ULONG             cbMaxPart,
  _Out_ IMimeMessageParts **ppParts
);
```



## Parameters

<dl> <dt>

*pMessage* \[in\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\***

Specifies a pointer to a [**IMimeMessage**](oe-imimemessage.md) object.

</dd> <dt>

*cbMaxPart* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the maximum size of a part, in bytes.

</dd> <dt>

*ppParts* \[out\]
</dt> <dd>

Type: **[**IMimeMessageParts**](oe-imimemessageparts.md)\*\***

Receives the address of a pointer to a new [**IMimeMessageParts**](oe-imimemessageparts.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                  |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success. <br/>                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates *ppParts* is **NULL**.<br/>                  |
| <dl> <dt>**E\_MAX\_SIZE\_TOO\_SMALL**</dt> </dl> | Indicates *cbMaxPart* is smaller than the header.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





