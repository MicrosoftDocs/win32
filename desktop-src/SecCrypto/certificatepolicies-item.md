---
Description: 'Retrieves the PolicyInformation object that represents the indexed policy. This is the default property.'
ms.assetid: '0143629a-97cf-43f4-8f96-774f0f5cfeca'
title: 'CertificatePolicies.Item property'
---

# CertificatePolicies.Item property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to retrieve the certificate policies.\]

The **Item** property retrieves the [**PolicyInformation**](policyinformation.md) object that represents the indexed policy. This is the default property.

This property is read-only.

## Syntax


```VB
CertificatePolicies.Item( _
  ByVal Index _
) As Variant
```



## Property value

A [**PolicyInformation**](policyinformation.md) object that represents the indexed policy.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




