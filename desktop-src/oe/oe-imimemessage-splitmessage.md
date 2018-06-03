---
title: IMimeMessage SplitMessage method
description: Splits the message into smaller parts for transmission.
ms.assetid: 4d71fb01-efa1-4cd8-8b66-e07b19953945
keywords:
- SplitMessage method Windows Mail (formerly Outlook Express)
- SplitMessage method Windows Mail (formerly Outlook Express) , IMimeMessage interface
- IMimeMessage interface Windows Mail (formerly Outlook Express) , SplitMessage method
topic_type:
- apiref
api_name:
- IMimeMessage.SplitMessage
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeMessage::SplitMessage method

Splits the message into smaller parts for transmission.

## Syntax


```C++
HRESULT SplitMessage(
  [in]  ULONG             cbMaxPart,
  [out] IMimeMessageParts **ppParts
);
```



## Parameters

<dl> <dt>

*cbMaxPart* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the maximum size of a part in bytes.

</dd> <dt>

*ppParts* \[out\]
</dt> <dd>

Type: **[**IMimeMessageParts**](oe-imimemessageparts.md)\*\***

Receives the address of a pointer to the [**IMimeMessageParts**](oe-imimemessageparts.md) object. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                           |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success.<br/>                                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *ppParts* is **NULL**.<br/>                                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/>                       |
| <dl> <dt>**MIME\_E\_MAX\_SIZE\_TOO\_SMALL**</dt> </dl> | *cbMaxPart* specifies a size smaller than the root header of the message. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IMimeMessage**](oe-imimemessage.md)
</dt> <dt>

[**IMimeMessageParts**](oe-imimemessageparts.md)
</dt> </dl>

 

 





