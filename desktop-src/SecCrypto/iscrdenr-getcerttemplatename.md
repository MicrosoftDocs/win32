---
description: Retrieves the name of the certificate template.
ms.assetid: 26fd758a-b348-4efb-841b-c8f2ab88efea
title: ISCrdEnr::getCertTemplateName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.getCertTemplateName
- SCrdEnr.getCertTemplateName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::getCertTemplateName method

The **getCertTemplateName** method retrieves the name of the certificate template.

## Syntax


```C++
HRESULT getCertTemplateName(
  [in]  DWORD     dwFlags,
  [out] BSTR *pbstrCertTemplateName
);
```


```VB

SCrdEnr.getCertTemplateName( _
  ByVal dwFlags, _
  ByRef pbstrCertTemplateName _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

A value that determines whether the certificate template's real name or display name is returned. If *dwFlags* has the value SCARD\_ENROLL\_CERT\_TEMPLATE\_DISPLAY\_NAME, the certificate template's display name is retrieved; otherwise, the real name of the certificate template is displayed.

</dd> <dt>

*pbstrCertTemplateName* \[out\]
</dt> <dd>

A pointer to a string that returns the name of the certificate template which will be used in the [*certificate request*](../secgloss/c-gly.md).

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

A string that represents the name of the certificate template which will be used in the [*certificate request*](../secgloss/c-gly.md).

## Remarks

If you do not set the certificate template name by calling [**ISCrdEnr::setCertTemplateName**](iscrdenr-setcerttemplatename.md), the name defaults to the first name in the list of available certificate templates.

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

[**ISCrdEnr::setCertTemplateName**](iscrdenr-setcerttemplatename.md)
</dt> </dl>

 

 
