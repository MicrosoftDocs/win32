---
description: Used to determine whether a certificate template contains the szOID\_PKIX\_KP\_EMAIL\_PROTECTION key usage.
ms.assetid: 1f0512e0-68b6-4b79-84bd-614babb4151d
title: ISCrdEnr::getCertTemplateSMIME method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.getCertTemplateSMIME
- SCrdEnr.getCertTemplateSMIME
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::getCertTemplateSMIME method

The **getCertTemplateSMIME** method is used to determine whether a certificate template contains the szOID\_PKIX\_KP\_EMAIL\_PROTECTION key usage.

If this key usage is part of the certificate template, the certificate template supports [*Secure/Multipurpose Internet Mail Extensions*](../secgloss/s-gly.md) (S/MIME) operations.

## Syntax


```C++
HRESULT getCertTemplateSMIME(
  [in]  BSTR      bstrCertTemplateName,
  [out] DWORD *pdwCertTemplateSMIME
);
```


```VB

SCrdEnr.getCertTemplateSMIME( _
  ByVal bstrCertTemplateName, _
  ByRef pdwCertTemplateSMIME _
)
```





## Parameters

<dl> <dt>

*bstrCertTemplateName* \[in\]
</dt> <dd>

The name of the certificate being queried for the S/MIME key usage.

</dd> <dt>

*pdwCertTemplateSMIME* \[out\]
</dt> <dd>

A pointer to a **DWORD** that returns a value of one if *bstrCertTemplateName* supports S/MIME; otherwise it returns zero.

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

**Long** value of one if *bstrCertTemplateName* supports S/MIME; otherwise zero.

## Remarks

The constant for szOID\_PKIX\_KP\_EMAIL\_PROTECTION is defined in Wincrypt.h.

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

[**ISCrdEnr::enroll**](/previous-versions/windows/desktop/legacy/aa386564(v=vs.85))
</dt> </dl>

 

 
