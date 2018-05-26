---
title: IMimeBody GetDataHere method
description: Copies the body data into a stream in a specified encoding.
ms.assetid: 9d6a44a6-bc1c-450f-a07c-cf50b346281e
keywords:
- GetDataHere method Windows Mail (formerly Outlook Express)
- GetDataHere method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , GetDataHere method
topic_type:
- apiref
api_name:
- IMimeBody.GetDataHere
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

# IMimeBody::GetDataHere method

Copies the body data into a stream in a specified encoding.

## Syntax


```C++
HRESULT GetDataHere(
  [in] ENCODINGTYPE ietEncoding,
  [in] IStream      *pStream
);
```



## Parameters

<dl> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies the [**ENCODINGTYPE**](oe-encodingtype.md) to copy the body data in.

</dd> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to an [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) to copy the data into.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                                                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>                                                                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pStream* is **NULL**.<br/>                                                                                                                             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>                                                                                                              |
| <dl> <dt>**ISequentialStream::Write**</dt> </dl> | This method may return a failure result from the [ISequentialStream::Write](http://msdn.microsoft.com/library/stg/stg/isequentialstream_write.asp) method. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





