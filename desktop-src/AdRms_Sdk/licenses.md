---
Description: An Active Directory Rights Management Services (AD RMS) licensing server can issue end-user licenses or issuance licenses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bc473b83-836d-4735-a27c-ccd7eb58ad23
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Licenses
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Licenses

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An Active Directory Rights Management Services (AD RMS) licensing server can issue [*end-user licenses*](e-gly.md#-rm-end-user-license-gly) or [*issuance licenses*](i-gly.md#-rm-issuance-license-gly). End-user licenses specify the right(s) granted to a specific user to consume protected content. For more information, see [Decrypting Content](decrypting-content.md). Issuance licenses specify the users who can consume protected content and the rights that can be made available to them. For more information, see [Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md).

AD RMS licenses are structurally similar to AD RMS certificates. Both are XrML documents and both consist of a certificate chain that ends with a Microsoft root of trust. The purpose of the two documents, however, differs. Licenses typically specify rights and conditions that govern content use. Certificates identify entities such as computers or users by singing them into an AD RMS certificate hierarchy.

The following example shows the basic XrML structure of an AD RMS end-user license. For more information about the individual XML elements and attributes that make up a license, see [XrML Elements](xrml-elements.md).


```XML
- <XrML xmlns="" version="1.2" purpose="ContentLicense">
  - <BODY type="LICENSE" version="3.0">
    + <ISSUEDTIME>
    + <DESCRIPTOR>
    + <ISSUER>
    + <ISSUEDPRINCIPALS>
    + <WORK>
    + <POLICYLIST>
      <AUTHENTICATEDDATA/>
    </BODY>
  - <SIGNATURE>
    + <DIGEST>
      <ALGORITHM/>
      <VALUE/>
    </SIGNATURE>
  </XrML>
+ <XrML xmlns="" version "1.2">  <!-- server licensor certificate -->
+ <XrML xmlns="" version "1.2">  <!-- server licensor certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
+ <XrML xmlns="" version "1.2">  <!-- DRM-CA-Certificate -->
```



## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Certificates](certificates.md)
</dt> <dt>

[Certificate Hierarchy](certificate-hierarchy.md)
</dt> </dl>

 

 



