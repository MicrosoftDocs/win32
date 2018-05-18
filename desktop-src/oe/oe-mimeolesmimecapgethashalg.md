---
title: MimeOleSMimeCapGetHashAlg function
description: Do not use. Encodes an object of specified size using the best hash algorithm flagged in the cookie. On success, returns the number of bits used for the hash signing.
ms.assetid: '37f04047-0379-48d3-976f-759ff64e8ddd'
keywords: ["MimeOleSMimeCapGetHashAlg function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleSMimeCapGetHashAlg
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleSMimeCapGetHashAlg function

Do not use. Encodes an object of specified size using the best hash algorithm flagged in the cookie. On success, returns the number of bits used for the hash signing.

## Syntax


```C++
HRESULT MimeOleSMimeCapGetHashAlg(
  _In_    LPVOID pv,
  _Inout_ LPBYTE pbEncode,
  _Inout_ DWORD  *pcbEncode,
  _Inout_ DWORD  *pfBlobSign
);
```



## Parameters

<dl> <dt>

*pv* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies cookie containing capabilities.

</dd> <dt>

*pbEncode* \[in, out\]
</dt> <dd>

Type: **LPBYTE**

Returns pointer to the S/MIME capabilities array.

</dd> <dt>

*pcbEncode* \[in, out\]
</dt> <dd>

Type: **DWORD\***

Returns pointer to array length variable.

</dd> <dt>

*pfBlobSign* \[in, out\]
</dt> <dd>

Type: **DWORD\***

Returns the number of bits used for the hash signing.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                 |
|-----------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates hash signing success. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates hash signing failure. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





