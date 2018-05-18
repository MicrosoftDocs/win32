---
title: MimeOleIsEnrichedStream function
description: Do not use. Checks whether stream is enriched, as indicated by existence of \ 0034;c\_szXRich \ 0034; in stream.
ms.assetid: '14303ef4-27e6-4996-9fe9-9d84371ca8fa'
keywords: ["MimeOleIsEnrichedStream function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleIsEnrichedStream
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleIsEnrichedStream function

Do not use. Checks whether stream is enriched, as indicated by existence of "c\_szXRich" in stream.

## Syntax


```C++
HRESULT MimeOleIsEnrichedStream(
  _In_ IStream *pStream
);
```



## Parameters

<dl> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates enriched. <br/>                   |
| <dl> <dt>**S\_FALSE**</dt> </dl>      | Indicates failure. <br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pStream* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





