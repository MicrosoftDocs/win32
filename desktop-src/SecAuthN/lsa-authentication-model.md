---
Description: Explains the LSA Authentication Model.
ms.assetid: 0b2b868f-51a7-4f74-be4f-5f8db04d43ad
title: LSA Authentication Model
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LSA Authentication Model

The [*Local Security Authority*](security.l_gly#-security-local-security-authority-gly) (LSA) authentication model has the following features:

-   LSA authentication supports custom [authentication packages](authentication-packages.md). This allows end-customers and independent software vendors (ISVs) to customize or replace authentication routines to meet requirements beyond those provided by the standard Microsoft authentication packages. While the authentication packages provided by Microsoft require a user name and password logon data, a custom authentication package can take other forms of logon data, such as ATM card information and a personal identification number (PIN). A custom authentication package can also be used to implement a new [*security protocol*](security.s_gly#-security-security-protocol-gly).
-   The LSA supports custom security packages, which function as security support providers for distributed applications and as authentication packages for applications that require authentication services. The authentication functionality is accessed using the same interface as a stand-alone authentication package, while the security support provider functionality is accessed using [Security Support Provider Interface](sspi.md) (SSPI). The set of LSA support functions available to custom security packages allows them to supply advanced security features, such as token creation and [*supplemental credentials*](security.s_gly#-security-supplemental-credentials-gly) management.
-   The LSA supports heterogeneous credentials management to interface with non-Microsoft products, such as networks and databases. Because such products often have their own security credentials, the LSA provides functions that authentication packages can use to associate non-Microsoft credentials with Windows processes. Custom authentication packages can provide services for querying these credentials when needed, such as when a network redirector attempts to establish a connection to a remote system.
-   Each class of logon device installed on a system can have its own logon process. Device classes typically include devices such as smart card readers; however, for the purposes of [*LSA*](security.l_gly#-security-local-security-authority-gly) authentication, connected networks are also treated as devices. By default, the Windows operating system provides the logon process that supports user name and password logons using a keyboard. Developers can add support for other devices, such as [*smart card*](security.s_gly#-security-smart-card-gly) [*readers*](security.r_gly#-security-reader-gly). For more information about smart cards, see [Smart Card Authentication](smart-card-authentication.md). For more information about logon device support, see [Winlogon and GINA](winlogon-and-gina.md).

 

 



