---
Description: The Encrypting Content Code Example uses an owner license to encrypt content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 084d2e71-e03b-4aa8-8d43-fe1735aa6dea
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Owner License
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Owner License

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The [Encrypting Content Code Example](encrypting-content-code-example.md) uses an owner license to encrypt content. An owner license is an end-user license that contains the OWNER right and allows the user to exercise all rights regardless of whether they have been explicitly granted. You do not need an owner license to encrypt. An end-user license that contains the EDIT right will suffice. You can retrieve an owner license by calling the [**DRMGetOwnerLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetownerlicense?branch=master) function. An owner license can contain the following elements:

-   The issuance date and time.
-   A type identifier.
-   The name and ID of the issuer.
-   The principal ID, public key, digest and security processor.
-   The Active Directory Federated Service (ADFS) principals.
-   A WORK object that identifies the item of content and the associated rights.
-   Additional policies that apply to content use.
-   A signature created by using the private key of the AD RMS activation service.
-   A certificate chain that contains one or more server licensor certificates and one or more CA certificates.

The following diagram shows the basic XrML structure of the license. For a more complete example, see the [Owner License XML Example](owner-license-xml-example.md).


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
        - <RIGHTSLIST>
          + <RIGHT name="OWNER">
          </RIGHTSLIST>
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

[Encrypting Content](encrypting-content.md)
</dt> <dt>

[Encrypting Content Code Example](encrypting-content-code-example.md)
</dt> <dt>

[Owner License Store](owner-license-store.md)
</dt> <dt>

[Owner License XML Example](owner-license-xml-example.md)
</dt> </dl>

 

 



