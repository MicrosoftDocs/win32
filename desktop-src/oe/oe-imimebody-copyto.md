---
title: IMimeBody CopyTo method
description: Copies everything from the current body object to the specified body object.
ms.assetid: 39d5b4fe-60e4-4c03-8d19-c36b33fb910f
keywords:
- CopyTo method Windows Mail (formerly Outlook Express)
- CopyTo method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , CopyTo method
topic_type:
- apiref
api_name:
- IMimeBody.CopyTo
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimeBody::CopyTo method

Copies everything from the current body object to the specified body object.

## Syntax


```C++
HRESULT CopyTo(
  [in] IMimeBody *pBody
);
```



## Parameters

<dl> <dt>

*pBody* \[in\]
</dt> <dd>

Type: **[**IMimeBody**](oe-imimebody.md)\***

Specifies a pointer to the [**IMimeBody**](oe-imimebody.md) object to copy the current body object to. If this method fails, the state of *pBody* is undefined.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                               |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pBody* is **NULL**.<br/>                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>             |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | Indicates that *pBody* is not an object implemented by MimeOLE. <br/> |



 

## Remarks

After this method, *pBody* is an exact replica of the current body object. *pBody* has no association with the message that the current body object is part of.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





