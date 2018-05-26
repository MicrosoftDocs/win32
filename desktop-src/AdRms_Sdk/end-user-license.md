---
Description: An end-user license (EUL) identifies the rights and conditions to consume protected content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e5fe532c-8cb8-4dc8-a090-32350019b292
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: End-User License
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# End-User License

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An end-user license (EUL) identifies the rights and conditions to consume protected content. A [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly) and a [*machine certificate*](m-gly.md#-rm-machine-certificate-gly) must exist before your application can request and end-user license. The license can contain the following elements:

-   The issuance date and time.
-   A type identifier.
-   The name and ID of the issuer.
-   The principal ID, public key, digest and security processor.
-   The Active Directory Federated Service (ADFS) principals.
-   A WORK object that identifies the item of content and the associated rights.
-   Additional policies that apply to content use.
-   A signature created by using the private key of the AD RMS activation service.
-   A certificate chain that contains one or more server licensor certificates and one or more CA certificates.

The following diagram shows the basic XrML structure of the license. For a more complete example, see [End User License XML Example](end-user-license-xml-example.md).


```XML
- <XrML xmlns="" version="1.2" purpose="ContentLicense">
  - <BODY type="LICENSE" version="3.0">
    + <ISSUEDTIME>
    + <DESCRIPTOR>
    + <ISSUER>
    + <ISSUEDPRINCIPALS>
    - <WORK>
      + <OBJECT>
      + <METADATA>
      - <RIGHTSGROUP name="MainRights">
        + <RIGHTSLIST>
        </RIGHTSGROUP>
      </WORK>
    - <POLICYLIST>
      + <POLICY>
      </POLICYLIST>
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

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Decrypting Content Code Example](decrypting-content-code-example.md)
</dt> <dt>

[End-User License Store](end-user-license-store.md)
</dt> <dt>

[End User License XML Example](end-user-license-xml-example.md)
</dt> </dl>

 

 



