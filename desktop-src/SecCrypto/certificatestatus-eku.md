---
Description: Returns the EKU object used to build the Chain object.
ms.assetid: d02f1614-6a4f-4c60-b406-ce174a99e9a5
title: CertificateStatus.EKU method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CertificateStatus.EKU method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ChainStatus Structure**](https://www.bing.com/search?q=**X509ChainStatus+Structure**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **EKU** method returns the [**EKU**](eku.md) object used to build the [**Chain**](chain.md) object.

## Syntax


```VB
CertificateStatus.EKU()
```



## Parameters

This method has no parameters.

## Return value

This method returns an [**EKU**](eku.md) object that indicates the extended key usage setting of the [*certificate*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb). The EKU setting establishes a certificate's valid use. Only a single **EKU** object can be set for each certificate.

## Remarks

The [**CertificateStatus.ApplicationPolicies**](certificatestatus-applicationpolicies.md) method provides the same functionality as this method but allows many settings to be specified instead of only one. If the [**OIDs**](oids.md) collection returned by the **ApplicationPolicies** method contains one or more [**OID**](oid.md) objects, the [**EKU**](eku.md) object returned by this method is ignored. Use the **ApplicationPolicies** method instead of this method.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**CertificateStatus**](certificatestatus.md)
</dt> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> <dt>

[**EKU**](eku.md)
</dt> </dl>

 

 




