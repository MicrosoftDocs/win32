---
Description: If a principal in an Active Directory Rights Management Services (AD RMS) system is compromised, you can use revocation to invalidate all associated licenses and certificates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ec8ec1d8-5c43-4f6d-93bd-7875c110cac0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Revocation

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

If a principal in an Active Directory Rights Management Services (AD RMS) system is compromised, you can use revocation to invalidate all associated licenses and certificates.

When you build a license or certificate, you can use the [**DRMSetRevocationPoint**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetrevocationpoint?branch=master) function to specify that the principal must obtain a [*revocation list*](r-gly.md#-rm-revocation-list-gly) at a scheduled interval. This function specifies a URL where the revocation list is posted and a refresh frequency that specifies how often the list must be updated. The URL is known as the *revocation point*. The revocation list contains all group identities, end-user licenses, or other principals that have been revoked and cannot therefore publish or consume content. The following table discusses the rules for revoking various types of licenses and certificates.



| License/Certificate          | Revocation criteria                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Server licensor certificate  | Revoke by license ID, license hash, issuer ID, and issuer key                                                                               |
| End-user licenses            | Revoke by principal ID, principal key, license ID, license hash, issuer ID, issuer key, or content ID.                                      |
| Client licensor certificates | Revoke by principal ID, license ID, license hash, issuer ID, issuer key, or content ID.                                                     |
| Rights account certificates  | Revoke by principal ID, principal key, federated principal ID, federated principal key, license ID, license hash, issuer ID, or issuer key. |
| Machine certificates         | Revoke by principal ID, principal key, license ID, license hash, issuer ID, or issuer key.                                                  |
| Manifests                    | Revoke by license ID, license hash, issuer ID, or issuer key.                                                                               |



 

Every issued AD RMS certificate and license consists of a certificate chain that leads back to a Microsoft root of trust, and each item in the chain can require a separate revocation list and identify a unique revocation point. The final license in the chain, therefore, could require multiple lists. The following syntax contains a simplified sample revocation list. To improve readability, the ellipsis (...) punctuation symbol replaces selected text.


```XML
<REVOCATIONLIST>
  <REVOKE category="license" type="license-id">
    <OBJECT>
      <ID type="MS-GUID">EUL{...}</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="license" type="license-hash">
    <DIGEST>
      <ALGORITHM>SHA1</ALGORITHM>
      <VALUE encoding="base64" size="160">...</VALUE>
    </DIGEST>
  </REVOKE>
  <REVOKE category="license" type="issuer-key">
    <PUBLICKEY>
      <ALGORITHM>RSA</ALGORITHM>
      <PARAMETER name="public-exponent">
        <VALUE encoding="integer32">65537</VALUE>
      </PARAMETER>
      <PARAMETER name="modulus">
       <VALUE encoding="base64" size="512">...</VALUE>
      </PARAMETER>
    </PUBLICKEY>
  </REVOKE>
  <REVOKE category="license" type="issuer-id">
    <OBJECT>
      <ID type="ascii-tag">Contoso, Inc.</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="content" type="content-id">
    <OBJECT>
      <ID type="ascii-tag">July 2003 Subscriber List</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="principal" type="principal-id">
    <OBJECT>
      <ID type="MS-PassportID">Compromised@example.com</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="principal" type="principal-key">
    <PUBLICKEY>
      <ALGORITHM>RSA</ALGORITHM>
      <PARAMETER name="public-exponent">
        <VALUE encoding="integer32">65537</VALUE>
      </PARAMETER>
      <PARAMETER name="modulus">
        <VALUE encoding="base64" size="512">...</VALUE>
      </PARAMETER>
   </PUBLICKEY>
  </REVOKE>
 </REVOCATIONLIST>
```



## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Exclusion](revocation.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



