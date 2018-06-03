---
Description: An Active Directory Rights Management Services (AD RMS) machine certificate identifies a computer by signing it into the Pre-production or Production certificate hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 107236b6-c4fb-46a2-8226-5aa001cc4b05
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Machine Certificates
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Machine Certificates

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An Active Directory Rights Management Services (AD RMS) machine certificate identifies a computer by signing it into the Pre-production or Production certificate hierarchy. Machine certificates are created when a computer is activated. One machine certificate is installed for each user who activates the computer into the hierarchy. Each certificate typically contains the following elements:

-   The issuance date and time.
-   A certificate type ID and name.
-   The name and ID of the issuer.
-   The location from which the certificate was retrieved.
-   The principal ID, public key, digest and security processor.
-   A signature created by using the private key of the AD RMS activation service.
-   A certificate chain that contains the server licensor certificate and one or more CA certificates.

The following diagram shows the basic XrML structure of the certificate. For a more complete example, see [Machine Certificate XML Example](machine-certificate-xml-example.md).


```XML
- <XrML version="1.2" xmlns="">
  - <BODY >
    + <ISSUEDTIME> 
    + <DESCRIPTOR>
    + <ISSUER>
    + <DISTRIBUTIONPOINT>
    + <ISSUEDPRINCIPALS>
    </BODY>
    <SIGNATURE>
    + <DIGEST>
      <ALGORITHM/> 
      <VALUE/> 
   </SIGNATURE>
  </XrML>

+ <XrML xmlns="" version "1.2">  <!-- server licensor certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
```



## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[Machine Certificate XML Example](machine-certificate-xml-example.md)
</dt> <dt>

[Machine Certificate Store](machine-certificate-store.md)
</dt> </dl>

 

 



