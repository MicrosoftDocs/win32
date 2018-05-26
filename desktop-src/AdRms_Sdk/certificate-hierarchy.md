---
Description: Every license and certificate used in an Active Directory Rights Management Services (AD RMS) environment consists of a chain of certificates that leads back to a Microsoft certification authority (CA) certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e12abffa-1e23-4ad8-9afd-2b23b9dc24b6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Certificate Hierarchy
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Certificate Hierarchy

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Every license and certificate used in an Active Directory Rights Management Services (AD RMS) environment consists of a chain of certificates that leads back to a Microsoft certification authority (CA) certificate. Microsoft provides two chains into which a license or certificate can be nested, a Pre-production certificate chain and a Production chain. We recommend that you use the Pre-production hierarchy when developing an application so that you can work without signing a Production License Agreement with Microsoft. You must, however, switch to the Production chain before releasing your application. For more information, see [Application Licensing Information](application-licensing-information.md).

AD RMS licenses and certificates are XrML documents. The following example shows the basic XrML representation of a typical machine certificate. The first certificate in the chain identifies a specific computer. The second identifies the AD RMS server. The third and fourth identify two Microsoft subordinate certification authorities (CAs), and the last identifies a Microsoft root CA.

For more information about the individual XML elements and attributes that make up a license, see [XrML Elements](xrml-elements.md).


```XML
- <XrML version="1.2" xmlns="">  <!-- Individual certificate -->
  - <BODY >
    + <ISSUEDTIME> 
    + <DESCRIPTOR>
    + <ISSUER>
    + <DISTRIBUTIONPOINT>
    + <ISSUEDPRINCIPALS>
    </BODY>
  + <SIGNATURE>
  </XrML>

+ <XrML xmlns="" version "1.2">  <!-- server licensor certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
```



## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Certificates](certificates.md)
</dt> <dt>

[Configure the Registry](configure-the-registry.md)
</dt> <dt>

[Licenses](licenses.md)
</dt> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



