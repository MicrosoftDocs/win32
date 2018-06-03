---
title: MimeOleCreateMessage function
description: Do not use. On success, creates and initializes a message.
ms.assetid: c812b983-ca4a-4645-aaa2-c3e2661018c2
keywords:
- MimeOleCreateMessage function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateMessage
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

# MimeOleCreateMessage function

Do not use. On success, creates and initializes a message.

## Syntax


```C++
HRESULT MimeOleCreateMessage(
  _In_  IUnknown     *pUnkOuter,
  _Out_ IMimeMessage **ppMessage
);
```



## Parameters

<dl> <dt>

*pUnkOuter* \[in\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\***

Specifies pointer to controlling [IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp).

</dd> <dt>

*ppMessage* \[out\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\*\***

Receives the address of a pointer to a new [**IMimeMessage**](oe-imimemessage.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                   |
|----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates *ppMessage* is **NULL**.<br/> |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [**IMimeMessage**](oe-imimemessage.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





