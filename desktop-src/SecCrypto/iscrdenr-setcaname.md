---
description: Specifies the name of the certification authority (CA).
ms.assetid: 224c2a51-8a25-4b66-b86b-c87531475145
title: ISCrdEnr::setCAName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.setCAName
- SCrdEnr.setCAName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::setCAName method

The **setCAName** method specifies the name of the [*certification authority*](../secgloss/c-gly.md) (CA).

## Syntax


```C++
HRESULT setCAName(
  [in] DWORD dwFlags,
  [in] BSTR bstrCertTemplateName,
  [in] BSTR bstrCAName
);
```


```VB

SCrdEnr.setCAName( _
  ByVal dwFlags, _
  ByVal bstrCertTemplateName, _
  ByVal bstrCAName _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Value that specifies whether the name refers to the CA name or the CA's machine name. If this value is SCARD\_ENROLL\_CA\_MACHINE\_NAME (defined as 0x01), the name refers to the CA's machine name. Otherwise, the name refers to the CA name.

</dd> <dt>

*bstrCertTemplateName* \[in\]
</dt> <dd>

Name of the certificate template.

</dd> <dt>

*bstrCAName* \[in\]
</dt> <dd>

CA name to be used with the certificate template specified by *bstrCertTemplateName*.

</dd> </dl>

## Return value

### VB

The return value is an **HRESULT**. A value of S\_OK indicates that the call was successful.

## Remarks

Use this method to specify a CA for a certificate template.

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

[**ISCrdEnr::enumCAName**](iscrdenr-enumcaname.md)
</dt> <dt>

[**ISCrdEnr::getCAName**](iscrdenr-getcaname.md)
</dt> </dl>

 

 
