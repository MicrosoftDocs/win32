---
description: Enumerates the name of the certification authorities (CAs) for a given certificate template name.
ms.assetid: 82cc3346-a8b9-4abd-933a-c212a37a373e
title: ISCrdEnr::enumCAName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.enumCAName
- SCrdEnr.enumCAName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::enumCAName method

The **enumCAName** method enumerates the name of the [*certification authorities*](../secgloss/c-gly.md) (CAs) for a given certificate template name.

## Syntax


```C++
HRESULT enumCAName(
  [in]  DWORD     dwIndex,
  [in]  DWORD     dwFlags,
  [in]  BSTR     bstrCertTemplateName,
  [out] BSTR *pbstrCAName
);
```


```VB

SCrdEnr.enumCAName( _
  ByVal dwIndex, _
  ByVal dwFlags, _
  ByVal bstrCertTemplateName, _
  ByRef pbstrCAName _
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

A value that determines whether the name refers to the CA name or the CA's machine name. If this value is SCARD\_ENROLL\_CA\_MACHINE\_NAME (defined as 0x01), the name refers to the CA's machine name. Otherwise the name refers to the CA name.

</dd> <dt>

*bstrCertTemplateName* \[in\]
</dt> <dd>

The name of the certificate template.

</dd> <dt>

*pbstrCAName* \[out\]
</dt> <dd>

A pointer to a string that returns the name of the CA.

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

A string that represents the name of the CA.

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

[**ISCrdEnr::getCACount**](iscrdenr-getcacount.md)
</dt> <dt>

[**ISCrdEnr::getCAName**](iscrdenr-getcaname.md)
</dt> <dt>

[**ISCrdEnr::setCAName**](iscrdenr-setcaname.md)
</dt> </dl>

 

 
