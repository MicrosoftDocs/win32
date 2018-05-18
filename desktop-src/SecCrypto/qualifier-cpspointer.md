---
Description: 'Retrieves the URI that points to a Certification Practice Statement (CPS) published by the certification authority (CA).'
ms.assetid: 'fd030c1c-137c-4036-bf13-ae989a9703cc'
title: 'Qualifier.CPSPointer property'
---

# Qualifier.CPSPointer property

\[The **CPSPointer** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

The **CPSPointer** property retrieves the URI that points to a Certification Practice Statement (CPS) published by the certification authority (CA).

## Syntax


```VB
Qualifier.CPSPointer As String
```



## Property value

The URI that points to a CPS published by the CA.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Qualifier**](qualifier.md)
</dt> </dl>

 

 




