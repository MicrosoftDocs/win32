---
Description: Everything signed by using the production certificate provided by Microsoft with the Production License Agreement must meet the minimum standards described in Required Application Security Standards.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 96dadba4-f166-4ece-899b-e08dfff03475
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Protecting the Production Certificate
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Protecting the Production Certificate

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Everything signed by using the production certificate provided by Microsoft with the Production License Agreement must meet the minimum standards described in [Required Application Security Standards](required-application-security-standards.md). Beyond this minimum, we recommend that you protect the production certificate by:

-   Storing the certificate in purpose-built secure cryptographic key storage.
-   Making sure that the hardware that contains the certificate is not connected to an internal or external network.
-   Restricting hardware access to trusted employees.
-   Requiring the presence of at least two employees to log on to the computer that contains the certificate.
-   Using smart card or equivalent authentication methods.

We also recommend that you distinguish prerelease and postrelease builds of the product by using unique production certificates to sign each. This enables you to specifically revoke or exclude prerelease software from access to protected information. Keep in mind, however, that this may impact postrelease access to prerelease protected data. We recommend that you sign hotfixes with the same certificate used to sign the release build and that your application authenticate the certificate signature before installing upgrades.

## Related topics

<dl> <dt>

[Recommended Software Development Practices](recommended-software-development-practices.md)
</dt> </dl>

 

 



