---
description: Enumerates the certificate template names.
ms.assetid: 4741eb0d-b8e0-468c-8a00-9ccacb52a9a7
title: ISCrdEnr::enumCertTemplateName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.enumCertTemplateName
- SCrdEnr.enumCertTemplateName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::enumCertTemplateName method

The **enumCertTemplateName** method enumerates the certificate template names.

## Syntax


```C++
HRESULT enumCertTemplateName(
  [in]  DWORD     dwIndex,
  [in]  DWORD     dwFlags,
  [out] BSTR *pbstrCertTemplateName
);
```


```VB

SCrdEnr.enumCertTemplateName( _
  ByVal dwIndex, _
  ByVal dwFlags, _
  ByRef pbstrCertTemplateName _
)
```





## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

The zero-based index for the enumeration sequence.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A value that determines whether the enumerated certificate template applies to user or machine certificates. If this value is SCARD\_ENROLL\_USER\_CERT\_TEMPLATE (defined as 1), the enumeration applies to user certificate templates. If this value is SCARD\_ENROLL\_MACHINE\_CERT\_TEMPLATE (defined as 2), the enumeration applies to machine certificate templates.

</dd> <dt>

*pbstrCertTemplateName* \[out\]
</dt> <dd>

A pointer to a string that returns the name of the enumerated certificate template.

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

A string that contains the name of the enumerated certificate template.

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

[**ISCrdEnr::getCertTemplateCount**](iscrdenr-getcerttemplatecount.md)
</dt> <dt>

[**ISCrdEnr::getCertTemplateName**](iscrdenr-getcerttemplatename.md)
</dt> <dt>

[**ISCrdEnr::setCertTemplateName**](iscrdenr-setcerttemplatename.md)
</dt> </dl>

 

 




