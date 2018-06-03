---
Description: If a principal in an Active Directory Rights Management Services (AD RMS) system is compromised, you can use revocation to invalidate all associated licenses and certificates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1e1a7cfc-8445-4d0c-bc45-310fa9364839
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revoking a Certificate
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Revoking a Certificate

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

If a principal in an Active Directory Rights Management Services (AD RMS) system is compromised, you can use revocation to invalidate all associated licenses and certificates. Call the [**DRMSetRevocationPoint**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetrevocationpoint) function to specify that the principal must obtain a [*revocation list*](https://www.bing.com/search?q=*revocation list*) at a scheduled interval. This function specifies a URL where the revocation list is posted and a refresh frequency that specifies how often the list must be updated. The URL is known as the *revocation point*. The revocation list contains all group identities, end-user licenses, or other principals that have been revoked and cannot therefore publish or consume content. The following table discusses the rules for revoking various types of licenses and certificates.



| License/Certificate          | Revocation criteria                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Server licensor certificate  | Revoke by license ID, license hash, issuer ID, and issuer key                                                                               |
| End-user licenses            | Revoke by principal ID, principal key, license ID, license hash, issuer ID, issuer key, or content ID.                                      |
| Client licensor certificates | Revoke by principal ID, license ID, license hash, issuer ID, issuer key, or content ID.                                                     |
| Rights account certificates  | Revoke by principal ID, principal key, federated principal ID, federated principal key, license ID, license hash, issuer ID, or issuer key. |
| Machine certificates         | Revoke by principal ID, principal key, license ID, license hash, issuer ID, or issuer key.                                                  |
| Manifests                    | Revoke by license ID, license hash, issuer ID, or issuer key.                                                                               |



 

Every issued AD RMS certificate and license consists of a certificate chain that leads back to a Microsoft root of trust, and each item in the chain can require a separate revocation list and identify a unique revocation point. The final license in the chain, therefore, could require multiple lists. For more information, see the following topics:

-   [Revocation XML Example](revocation-xml-example.md)
-   [Revocation Code Example](revocation-code-example.md)

## Related topics

<dl> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



