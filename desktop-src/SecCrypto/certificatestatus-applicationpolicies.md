---
description: Returns an OIDs collection that represents the application policies used to create the Chain object.
ms.assetid: dca0acbf-e369-4216-a4f6-44ed965011d0
title: CertificateStatus.ApplicationPolicies method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CertificateStatus.ApplicationPolicies
api_type:
- COM
api_location:
- Capicom.dll
---

# CertificateStatus.ApplicationPolicies method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ChainStatus Structure**](/dotnet/api/system.security.cryptography.x509certificates.x509chainstatus?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **ApplicationPolicies** method returns an [**OIDs**](oids.md) collection that represents the application policies used to create the [**Chain**](chain.md) object.

## Syntax


```VB
CertificateStatus.ApplicationPolicies()
```



## Parameters

This method has no parameters.

## Return value

An [**OIDs**](oids.md) collection. Each [**OID**](oid.md) object in the collection represents an application policy OID.

## Remarks

Add application policy OIDs to the collection to specify the application policies that should be used to build the certificate trust chain. If the collection contains at least one [**OID**](oid.md) object, the [**EKU**](eku.md) object returned by the [**CertificateStatus.EKU**](certificatestatus-eku.md) method is ignored.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
