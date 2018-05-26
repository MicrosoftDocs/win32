---
title: MimeOleCreatePropertySet function
description: Do not use. On success, creates a new property set object.
ms.assetid: 78f40867-dbf5-4ca0-9d7a-5f07e7e1cc7e
keywords:
- MimeOleCreatePropertySet function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreatePropertySet
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

# MimeOleCreatePropertySet function

Do not use. On success, creates a new property set object.

## Syntax


```C++
HRESULT MimeOleCreatePropertySet(
  _In_  IUnknown         *pUnkOuter,
  _Out_ IMimePropertySet **ppPropertySet
);
```



## Parameters

<dl> <dt>

*pUnkOuter* \[in\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\***

Specifies pointer to the controlling [IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp) interface on the outer object if the property set object is being created as part of an aggregate object. This parameter can be **NULL** if the object is not part of an aggregate.

</dd> <dt>

*ppPropertySet* \[out\]
</dt> <dd>

Type: **[**IMimePropertySet**](oe-imimepropertyset.md)\*\***

Receives the address of a pointer to a new [**IMimePropertySet**](oe-imimepropertyset.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that a pointer argument is **NULL**. <br/> |



 

## Remarks

> [!Note]  
> User is responsible for freeing [**IMimePropertySet**](oe-imimepropertyset.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





