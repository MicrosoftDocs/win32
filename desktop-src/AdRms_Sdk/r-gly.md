---
Description: Contains definitions of Active Directory Rights Management Services SDK terms that begin with the letter R.
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 880adf97-4870-49c2-9256-f082d6b6a771
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: R
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# R

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) H [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) N O [P](p-gly.md) Q R [S](s-gly.md) T [U](u-gly.md) V W X Y Z

<dl> <dt>

<span id="_rm_rac_gly"></span><span id="_RM_RAC_GLY"></span>**RAC**
</dt> <dd>

See *rights account certificate*.

</dd> <dt>

<span id="_rm_revocation_gly"></span><span id="_RM_REVOCATION_GLY"></span>**revocation**
</dt> <dd>

A process by which entities are listed as having licenses that are not valid.

</dd> <dt>

<span id="_rm_revocation_list_gly"></span><span id="_RM_REVOCATION_LIST_GLY"></span>**revocation list**
</dt> <dd>

A list of users or other principals that have had their licenses revoked for some reason. These lists are posted on the Internet and periodically refreshed. A revocation list is retrieved by using the [**DRMAcquireAdvisories**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireadvisories) function.

</dd> <dt>

<span id="_rm_right_gly"></span><span id="_RM_RIGHT_GLY"></span>**right**
</dt> <dd>

An action permitted to specified users for content protected by RMS technology. These rights can be further constrained by using conditions.

</dd> <dt>

<span id="_rm_rights_management_gly"></span><span id="_RM_RIGHTS_MANAGEMENT_GLY"></span>**rights management**
</dt> <dd>

A technology that provides persistent protection to digital data using encryption, certificates, and authentication. Authorized recipients or users must acquire a license in order to consume the protected files, according to the rights, or business rules, set by the content owner.

</dd> <dt>

<span id="_rm_rights_template_gly"></span><span id="_RM_RIGHTS_TEMPLATE_GLY"></span>**rights template**
</dt> <dd>

The saved settings for file usage rights for the AD RMS server in a specified domain. The administrator sets these in the Administration Console, and saves them for use by the client applications.

</dd> <dt>

<span id="_rm_rights_account_certificate_gly"></span><span id="_RM_RIGHTS_ACCOUNT_CERTIFICATE_GLY"></span>**rights account certificate**
</dt> <dd>

(RAC) The certificate that uses the machine certificate from RMS activation to bind user accounts to specific computers or groups of computers. The certificate is used to enable consumers to use protected content. Also known as [*group identity certificate*](https://www.bing.com/search?q=*group identity certificate*).

</dd> <dt>

<span id="_rm_root_of_trust_gly"></span><span id="_RM_ROOT_OF_TRUST_GLY"></span>**root of trust**
</dt> <dd>

A trusted entity that provides the basis for the certificates in the certificate trust list (CTL). All the certificate providers and the ultimate user must trust the destination.

</dd> </dl>

 

 



