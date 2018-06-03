---
title: MimeOleCreateMessageTree function
description: Do not use. On success, creates and initializes a message tree.
ms.assetid: 59cb55ae-4153-467a-88ef-5e7b0bb0ffb2
keywords:
- MimeOleCreateMessageTree function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateMessageTree
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

# MimeOleCreateMessageTree function

Do not use. On success, creates and initializes a message tree.

## Syntax


```C++
HRESULT MimeOleCreateMessageTree(
  _In_  IUnknown         *pUnkOuter,
  _Out_ IMimeMessageTree **ppMessageTree
);
```



## Parameters

<dl> <dt>

*pUnkOuter* \[in\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\***

Specifies pointer to the controlling [IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp) interface on the outer object if the property set object is being created as part of an aggregate object. This parameter can be **NULL** if the object is not part of an aggregate.

</dd> <dt>

*ppMessageTree* \[out\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)\*\***

Receives the address of a pointer to a new [**IMimeMessageTree**](oe-imimemessagetree.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates *ppMessageTree* is **NULL**.<br/> |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [**IMimeMessageTree**](oe-imimemessagetree.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





