---
title: MimeOleIsTnefStream function
description: Do not use. Reads the first four bytes to determine whether data stream is Transport Neutral Encapsulation Format (TNEF).
ms.assetid: '93dada0f-f56c-4fb6-a19b-d2afaca8b1fc'
keywords: ["MimeOleIsTnefStream function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleIsTnefStream
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleIsTnefStream function

Do not use. Reads the first four bytes to determine whether data stream is Transport Neutral Encapsulation Format (TNEF).

## Syntax


```C++
HRESULT MimeOleIsTnefStream(
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



| Return code                                                                                  | Description                                                 |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates TNEF. <br/>                                 |
| <dl> <dt>**S\_FALSE**</dt> </dl>      | Indicates not TNEF, or fewer than 4 bytes read. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pStream* is **NULL**. <br/>           |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





