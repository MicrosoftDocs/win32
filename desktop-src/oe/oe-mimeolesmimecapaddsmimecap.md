---
title: MimeOleSMimeCapAddSMimeCap function
description: Do not use. Receives an array of CRYPT\_SMIME\_CAPABILITIES allocated by MimeOleSMimeCapInit and returns a cookie flagged with a filtered list of available algorithms. See wincrypt.h.
ms.assetid: 523b5a95-c07a-4dec-869f-2188805185c3
keywords:
- MimeOleSMimeCapAddSMimeCap function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSMimeCapAddSMimeCap
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

# MimeOleSMimeCapAddSMimeCap function

Do not use. Receives an array of CRYPT\_SMIME\_CAPABILITIES allocated by [**MimeOleSMimeCapInit**](oe-mimeolesmimecapinit.md) and returns a cookie flagged with a filtered list of available algorithms. See wincrypt.h.

## Syntax


```C++
HRESULT MimeOleSMimeCapAddSMimeCap(
  _In_  LPBYTE pbSMimeCap,
  _In_  DWORD  cbSMimeCap,
  _Out_ LPVOID pv
);
```



## Parameters

<dl> <dt>

*pbSMimeCap* \[in\]
</dt> <dd>

Type: **LPBYTE**

Specifies pointer to the S/MIME capabilities array.

</dd> <dt>

*cbSMimeCap* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies array length.

</dd> <dt>

*pv* \[out\]
</dt> <dd>

Type: **LPVOID**

Returns cookie flagged with a filtered list of available algorithms. Note: *pv* must be greater than 9 bytes in size.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                              |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates algorithm list set. <br/>                                                |
| <dl> <dt>**S\_FALSE**</dt> </dl>      | Indicates algorithm list not set. <br/>                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates array pointer **NULL**, array length 0, or output buffer **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





