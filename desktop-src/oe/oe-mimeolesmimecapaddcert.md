---
title: MimeOleSMimeCapAddCert function
description: Do not use. Sets a passed-in cookie with a flag indicating the encryption algorithm to be used.
ms.assetid: 6936c05c-3442-48b1-ac65-d465d0434ce2
keywords:
- MimeOleSMimeCapAddCert function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSMimeCapAddCert
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleSMimeCapAddCert function

Do not use. Sets a passed-in cookie with a flag indicating the encryption algorithm to be used.

## Syntax


```C++
HRESULT MimeOleSMimeCapAddCert(
  _In_    LPBYTE pbCert,
  _In_    DWORD  cbCert,
  _In_    BOOL   fParanoid,
  _Inout_ LPVOID pv
);
```



## Parameters

<dl> <dt>

*pbCert* \[in\]
</dt> <dd>

Type: **LPBYTE**

Not used.

</dd> <dt>

*cbCert* \[in\]
</dt> <dd>

Type: **DWORD**

Not used.

</dd> <dt>

*fParanoid* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies algorithm choice. Forces 3-DES encryption when **TRUE**, RC2 40-bit when **FALSE**.

</dd> <dt>

*pv* \[in, out\]
</dt> <dd>

Type: **LPVOID**

Returns cookie containing flag indicating the encryption algorithm to be used. Note: *pv* must be greater than 9 bytes in size.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                         |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates encryption algorithm set. <br/>     |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates encryption algorithm not set. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





