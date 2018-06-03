---
Description: Active Directory Rights Management Services (AD RMS) uses the following certificates. Each identifies a specific entity, such as a computer or user, by signing it into the AD RMS certificate hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 76c7cb6b-a0e8-477d-bbb7-b9cdae39ee11
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Certificates
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Certificates

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) uses the following certificates. Each identifies a specific entity, such as a computer or user, by signing it into the AD RMS certificate hierarchy.



| Certificate                 | Description                                                                                                                                                                                                                                                                |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Machine certificate         | Issued by an AD RMS certification service to identify a computer in the AD RMS certificate hierarchy. For more information, see [Activating a Computer](activating-a-computer.md).                                                                                        |
| Rights account certificate  | Issued by an AD RMS certification service to identify an Active Directory user account in the AD RMS certificate hierarchy. For more information, see [Activating a User](activating-a-user.md).                                                                          |
| Client licensor certificate | Issued the AD RMS licensing service to enable offline signing of an issuance license. For more information, see [Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md).                                                                          |
| Server licensor certificate | Identifies an AD RMS server in the AD RMS certificate hierarchy. Beginning with Windows Server 2008, the certificate is created automatically when you install the AD RMS role. For more information, see [Server Enrollment](server-enrollment.md).                      |
| Application manifest        | Identifies an AD RMS application by signing it with the Pre-production or Production certificate provided by Microsoft. For more information, see [Application Manifests](application-manifests.md).                                                                      |
| Pre-Production certificate  | Provided by Microsoft to sign a custom application into the Pre-production AD RMS certificate hierarchy. This certificate is used during application development. For more information, see [Certificate Hierarchy](certificate-hierarchy.md).                            |
| Production certificate      | Provided by Microsoft to sign a custom application into the Production AD RMS certificate hierarchy. This certificate is used by released applications that have been licensed by Microsoft. For more information, see [Certificate Hierarchy](certificate-hierarchy.md). |



 

AD RMS certificates and licenses are structurally similar. Both are XrML documents and both consist of a certificate chain that ends with a Microsoft root of trust. The purpose of the two documents, however, differs. Certificates are used to identify entities and sign them into an AD RMS certificate hierarchy. Licenses typically specify rights and conditions that govern content use.

The following example shows the basic XrML structure of an AD RMS machine certificate. For more information about the individual XML elements and attributes that make up a license, see [XrML Elements](xrml-elements.md).


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

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Certificate Hierarchy](certificate-hierarchy.md)
</dt> <dt>

[Licenses](licenses.md)
</dt> </dl>

 

 



