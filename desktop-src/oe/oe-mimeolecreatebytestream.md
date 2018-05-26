---
title: MimeOleCreateByteStream function
description: Do not use. Creates a new byte stream.
ms.assetid: a093651e-1559-4413-bd0f-f264ceca8ecb
keywords:
- MimeOleCreateByteStream function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateByteStream
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

# MimeOleCreateByteStream function

Do not use. Creates a new byte stream.

## Syntax


```C++
HRESULT MimeOleCreateByteStream(
  _Out_ IStream **ppStream
);
```



## Parameters

<dl> <dt>

*ppStream* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

Receives the address of a pointer to an [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the new byte stream.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *ppStream* is **NULL**. <br/> |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





