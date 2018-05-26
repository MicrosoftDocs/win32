---
title: MimeOleCreateVirtualStream function
description: Do not use. Creates a new virtual stream.
ms.assetid: 0b53323e-8a26-4be3-89ee-2874a82a72ad
keywords:
- MimeOleCreateVirtualStream function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateVirtualStream
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

# MimeOleCreateVirtualStream function

Do not use. Creates a new virtual stream.

## Syntax


```C++
HRESULT MimeOleCreateVirtualStream(
  _Out_ IStream **ppStream
);
```



## Parameters

<dl> <dt>

*ppStream* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

Receives the address of a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the new virtual stream.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppStream* is **NULL**. <br/>              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

> [!Note]  
> User is responsible for freeing [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





