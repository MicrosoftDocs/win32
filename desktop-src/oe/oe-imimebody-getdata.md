---
title: IMimeBody GetData method
description: Gets an IStream object that can be used to read the data stored in the body. The client can request that the data be converted to the specified encoding type.
ms.assetid: 0ef80717-2476-4d84-afd5-1130b111097e
keywords:
- GetData method Windows Mail (formerly Outlook Express)
- GetData method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , GetData method
topic_type:
- apiref
api_name:
- IMimeBody.GetData
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

# IMimeBody::GetData method

Gets an [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that can be used to read the data stored in the body. The client can request that the data be converted to the specified encoding type.

## Syntax


```C++
HRESULT GetData(
  [in]  ENCODINGTYPE ietEncoding,
  [out] IStream      **ppStream
);
```



## Parameters

<dl> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies the [**ENCODINGTYPE**](oe-encodingtype.md) to be read from the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp).

</dd> <dt>

*ppStream* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

Receives the address of a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppStream* is **NULL**.<br/>               |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

This method actually does very little of the work. MimeOLE converts data as the client calls [IStream::Read](http://msdn.microsoft.com/library/stg/stg/isequentialstream_read.asp).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





