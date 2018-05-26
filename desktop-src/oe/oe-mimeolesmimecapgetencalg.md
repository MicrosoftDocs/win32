---
title: MimeOleSMimeCapGetEncAlg function
description: Do not use. Encodes an object of a specified size, using the best encryption algorithm flagged in the cookie. On success, returns the number of bits used for the encryption.
ms.assetid: c10be8c1-f489-48a8-9790-93e09c9ee29d
keywords:
- MimeOleSMimeCapGetEncAlg function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSMimeCapGetEncAlg
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

# MimeOleSMimeCapGetEncAlg function

Do not use. Encodes an object of a specified size, using the best encryption algorithm flagged in the cookie. On success, returns the number of bits used for the encryption.

## Syntax


```C++
HRESULT MimeOleSMimeCapGetEncAlg(
  _In_    LPVOID pv,
  _Inout_ LPBYTE pbEncode,
  _Inout_ DWORD  *pcbEncode,
  _Inout_ DWORD  *pdwBits
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

*pdwBits* \[in, out\]
</dt> <dd>

Type: **DWORD\***

Receives the number of bits used for the encryption.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                             |
|-----------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates encoding success. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates encoding failure. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





