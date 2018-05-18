---
Description: 'Retrieves the number of PolicyInformation objects in the collection.'
ms.assetid: 'd4fb6bd8-4e92-4de8-9430-dd3b6262a806'
title: 'CertificatePolicies.Count property'
---

# CertificatePolicies.Count property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to retrieve the certificate policies.\]

The **Count** property retrieves the number of [**PolicyInformation**](policyinformation.md) objects in the collection.

This property is read-only.

## Syntax


```VB
CertificatePolicies.Count As Long
```



## Property value

The number of [**PolicyInformation**](policyinformation.md) objects in the collection. Each **PolicyInformation** object represents a single certificate policy in the collection.

## Remarks

The **Count** property can be used to specify the last [**PolicyInformation**](policyinformation.md) object in the collection when retrieving a specific **PolicyInformation** object using the [**CertificatePolicies.Item**](certificatepolicies-item.md) property.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




