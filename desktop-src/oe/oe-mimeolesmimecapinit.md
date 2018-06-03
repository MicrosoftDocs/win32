---
title: MimeOleSMimeCapInit function
description: Do not use.
ms.assetid: eeceb00c-7f26-4a75-b78b-82ab0e597e16
keywords:
- MimeOleSMimeCapInit function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSMimeCapInit
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

# MimeOleSMimeCapInit function

Do not use. Returns an equivalent of the cookie returned by [**MimeOleSMimeCapAddSMimeCap**](oe-mimeolesmimecapaddsmimecap.md) when an array of CRYPT\_SMIME\_CAPABILITIES is passed in; otherwise, the function attempts to match MimeOle encryption capabilities to a Microsoft-enhanced provider (CryptoAPI), and flags matching algorithms in the returned cookie.

## Syntax


```C++
HRESULT MimeOleSMimeCapInit(
  _In_  LPBYTE pbSMimeCap,
  _In_  DWORD  cbSMimeCap,
  _Out_ LPVOID *ppv
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

*ppv* \[out\]
</dt> <dd>

Type: **LPVOID\***

Returns cookie flagged with matching algorithms.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates algorithm list set. <br/>                                                |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates algorithm list not set. <br/>                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates array pointer **NULL**, array length 0, or output buffer **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates memory allocation failed. <br/>                                          |



 

## Remarks

Using **NULL** values for *pbSMimeCap* and *cbSMimeCap* gives maximum results allowed by providers.

> [!Note]  
> Caller of this function is responsible for freeing what *ppv* points to.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





