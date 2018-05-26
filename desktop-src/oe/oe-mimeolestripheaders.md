---
title: MimeOleStripHeaders function
description: Do not use. Strips and adds a message header.
ms.assetid: acfcb2d1-e44f-4d0c-83dc-bb615eb9ee2c
keywords:
- MimeOleStripHeaders function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleStripHeaders
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

# MimeOleStripHeaders function

Do not use. Strips and adds a message header.

## Syntax


```C++
HRESULT MimeOleStripHeaders(
  _In_    IMimeMessage *pMessage,
  _In_    HBODY        hBody,
  _In_    LPCSTR       pszNameDelete,
  _In_    LPCSTR       pszHeaderAdd,
  _Inout_ IStream      **ppStream
);
```



## Parameters

<dl> <dt>

*pMessage* \[in\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\***

Specifies a pointer to the [**IMimeMessage**](oe-imimemessage.md) object.

</dd> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies a handle to the message body.

</dd> <dt>

*pszNameDelete* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies header to strip.

</dd> <dt>

*pszHeaderAdd* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies header to write.

</dd> <dt>

*ppStream* \[in, out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

Receives the address of a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the stream for action.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that a pointer argument is **NULL**. <br/> |



 

## Remarks

> [!Note]  
> Caller of this function is responsible for freeing [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object pointed to by *ppStream*.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





