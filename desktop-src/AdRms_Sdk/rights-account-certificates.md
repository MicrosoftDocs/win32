---
Description: An Active Directory Rights Management Services (AD RMS) rights account certificate (RAC) identifies a user account by signing it into the Pre-production or Production certificate hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5e5bf164-dc77-49d0-a540-3ecca5345c17
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Rights Account Certificates
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rights Account Certificates

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An Active Directory Rights Management Services (AD RMS) rights account certificate (RAC) identifies a user account by signing it into the Pre-production or Production certificate hierarchy. Each RAC is tied to the [*machine certificate*](https://www.bing.com/search?q=*machine certificate*) of the computer on which the user is activated. A RAC and a machine certificate must exist before an [*end-user license*](https://www.bing.com/search?q=*end-user license*) can be created and content encrypted or decrypted. A user can have more than one RAC on a computer, one for each AD RMS service against which the user is activated, but the user cannot transfer a RAC between computers. For more information, see [Activate a User Account](activate-a-user-account.md). A RAC can contain the following elements:

-   The issuance date and time.
-   The period over which the certificate is valid.
-   A certificate type ID and name.
-   The name and ID of the issuer.
-   The location from which the certificate was retrieved.
-   The principal ID, public key, digest and security processor.
-   The Active Directory Federated Service (ADFS) principals.
-   A signature created by using the private key of the AD RMS activation service.
-   A certificate chain that contains one or more server licensor certificates and one or more CA certificates.

The following diagram shows the basic XrML structure of the certificate. For a more complete example, see [Rights Account Certificate XML Example](rights-account-certificate-xml-example.md).


```XML
- <XrML xmlns="" version="1.2">
  - <BODY type="LICENSE" version="3.0">
    + <ISSUEDTIME>
    + <VALIDITYTIME>
    + <DESCRIPTOR>
    + <ISSUER>
    + <DISTRIBUTIONPOINT>
    + <ISSUEDPRINCIPALS>
    + <FEDERATIONPRINCIPALS>
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



> [!Note]
>
> If you are creating an Information Rights Management (IRM) enabled application in an enterprise environment, you can use the Active Directory **ms-Exch-RMS-Computer-Accounts-BL** attribute to specify a secondary user object whose security identifier (SID) is used for certification, rather than the SID from the authenticated request. In this case, a rights account certificate (RAC) is issued to the original caller, using the SID from the object specified by the **ms-Exch-RMS-Computer-Accounts-BL** attribute.
>
> This makes it possible for an IRM-enabled application to the share a single AD RMS identity across multiple computers. This can be useful where high performance is a requirement, such as in a web-farm scenario, because it makes it possible for the application to make fewer licensing requests.
>
> This feature is available in Windows Server 2008 with Service Pack 2 (SP2) and Hotfix KB973247, or in Windows Server 2008 R2.

 

## Related topics

<dl> <dt>

[Activating a User](activating-a-user.md)
</dt> <dt>

[Rights Account Certificate XML Example](rights-account-certificate-xml-example.md)
</dt> <dt>

[Rights Account Certificate Store](rights-account-certificate-store.md)
</dt> </dl>

 

 



