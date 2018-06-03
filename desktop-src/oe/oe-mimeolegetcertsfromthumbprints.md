---
title: MimeOleGetCertsFromThumbprints function
description: Do not use. Given a set of thumbprints, returns an equivalent set of certificates.
ms.assetid: 0c111cb8-0bcf-47ac-9bd9-4a1e91823ec4
keywords:
- MimeOleGetCertsFromThumbprints function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetCertsFromThumbprints
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

# MimeOleGetCertsFromThumbprints function

Do not use. Given a set of thumbprints, returns an equivalent set of certificates.

## Syntax


```C++
HRESULT MimeOleGetCertsFromThumbprints(
  _In_          THUMBBLOB      rgThumbprint,
  _Inout_       X509CERTRESULT pResults,
  _In_    const HCERTSTORE     rghCertStore,
  _In_    const DWORD          cCertStore
);
```



## Parameters

<dl> <dt>

*rgThumbprint* \[in\]
</dt> <dd>

Type: **THUMBBLOB**

Specifies array of thumbprints to look up.

</dd> <dt>

*pResults* \[in, out\]
</dt> <dd>

Type: **[**X509CERTRESULT**](oe-x509certresult.md)**

Specifies the HRESULTS array containing [**CERTSTATE**](oe-certstate.md) error info for each certificate lookup. Arrays must be allocated on IN.

</dd> <dt>

*rghCertStore* \[in\]
</dt> <dd>

Type: **const HCERTSTORE**

Specifies set of stores to search.

</dd> <dt>

*cCertStore* \[in\]
</dt> <dd>

Type: **const DWORD**

Specifies size of *rghCertStore*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                    | Description                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | Indicates all certs were found. <br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | Indicates that pointer argument is **NULL**. <br/>        |
| <dl> <dt>**MIME\_S\_SECURITY\_ERROROCCURED**</dt> </dl> | Indicates that any of the lookups failed. <br/>           |
| <dl> <dt>**MIME\_S\_SECURITY\_NOOP**</dt> </dl>         | Indicates *pResults* is empty or *cCertStore* is 0. <br/> |



 

## Remarks

Only indexes with non-**NULL** thumbprints are considered.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





