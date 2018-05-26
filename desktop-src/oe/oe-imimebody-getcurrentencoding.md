---
title: IMimeBody GetCurrentEncoding method
description: Gets the current encoding type for the data that is currently stored in the body. For example, if the body currently has image data that is encoded in Base64, this method will return IET\_BASE64.
ms.assetid: 0b86f727-9c2f-4823-9ab6-72deaa675555
keywords:
- GetCurrentEncoding method Windows Mail (formerly Outlook Express)
- GetCurrentEncoding method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , GetCurrentEncoding method
topic_type:
- apiref
api_name:
- IMimeBody.GetCurrentEncoding
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

# IMimeBody::GetCurrentEncoding method

Gets the current encoding type for the data that is currently stored in the body. For example, if the body currently has image data that is encoded in Base64, this method will return [**IET\_BASE64**](oe-encodingtype.md).

## Syntax


```C++
HRESULT GetCurrentEncoding(
  [out] ENCODINGTYPE *pietEncoding
);
```



## Parameters

<dl> <dt>

*pietEncoding* \[out\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)\***

Receives a pointer to the [**ENCODINGTYPE**](oe-encodingtype.md) value.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                           |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pietEncoding* is **NULL**.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





