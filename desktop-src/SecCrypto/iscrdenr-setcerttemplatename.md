---
description: Specifies the name of the certificate template.
ms.assetid: 15d22130-e614-4505-94e8-83c2efbf6d87
title: ISCrdEnr::setCertTemplateName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.setCertTemplateName
- SCrdEnr.setCertTemplateName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::setCertTemplateName method

The **setCertTemplateName** method specifies the name of the certificate template.

## Syntax


```C++
HRESULT setCertTemplateName(
  [in] DWORD dwFlags,
  [in] BSTR bstrCertTemplateName
);
```


```VB

SCrdEnr.setCertTemplateName( _
  ByVal dwFlags, _
  ByVal bstrCertTemplateName _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Value which determines if the certificate template's real name or display name is being set. If *dwFlags* has the value SCARD\_ENROLL\_CERT\_TEMPLATE\_DISPLAY\_NAME, the certificate template's display name is set. Otherwise, the real name of the certificate template is set.

</dd> <dt>

*bstrCertTemplateName* \[in\]
</dt> <dd>

Name of the certificate template which will be used in the certificate request.

</dd> </dl>

## Return value

### VB

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Remarks

If you do not set the certificate template name by calling **ISCrdEnr::setCertTemplateName**, the name defaults to the first name in the list of available certificate templates.

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

[**ISCrdEnr::getCertTemplateName**](iscrdenr-getcerttemplatename.md)
</dt> </dl>

 

 




