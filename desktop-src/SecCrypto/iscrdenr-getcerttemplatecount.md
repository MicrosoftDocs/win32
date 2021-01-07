---
description: Retrieves the number of certificate templates.
ms.assetid: f56e6e72-1562-4c53-b0da-b4bc69511559
title: ISCrdEnr::getCertTemplateCount method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.getCertTemplateCount
- SCrdEnr.getCertTemplateCount
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::getCertTemplateCount method

The **getCertTemplateCount** method retrieves the number of certificate templates.

## Syntax


```C++
HRESULT getCertTemplateCount(
  [in]  DWORD     dwFlags,
  [out] LONG *pdwCertTemplateCount
);
```


```VB

SCrdEnr.getCertTemplateCount( _
  ByVal dwFlags, _
  ByRef pdwCertTemplateCount _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

A value that determines whether the template is for user or machine certificates. If this value is SCARD\_ENROLL\_USER\_CERT\_TEMPLATE (defined as 1) then the returned count will be for user certificate templates. If this value is SCARD\_ENROLL\_MACHINE\_CERT\_TEMPLATE (defined as 2) then the returned count will be for machine certificate templates.

</dd> <dt>

*pdwCertTemplateCount* \[out\]
</dt> <dd>

A pointer to a **LONG** that returns the number of certificate templates.

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

A **Long** value that represents the number of certificate templates.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Scrdenrl.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCrdEnr is defined as 753988a1-1357-436d-9cf5-f089bdd67d64<br/>             |



## See also

<dl> <dt>

[**ISCrdEnr**](iscrdenr.md)
</dt> <dt>

[**ISCrdEnr::enumCertTemplateName**](iscrdenr-enumcerttemplatename.md)
</dt> </dl>

 

 




