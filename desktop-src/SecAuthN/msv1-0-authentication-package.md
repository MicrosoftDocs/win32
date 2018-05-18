---
Description: 'Microsoft provides the MSV1\_0 authentication package for local machine logons that do not require custom authentication.'
ms.assetid: '8b85588d-0a79-43af-b526-7a5fc8248f99'
title: 'MSV1\_0 Authentication Package'
---

# MSV1\_0 Authentication Package

Microsoft provides the MSV1\_0 [*authentication package*](security.a_gly#-security-authentication-package-gly) for local machine logons that do not require custom authentication. The [*Local Security Authority*](security.l_gly#-security-local-security-authority-gly) (LSA) calls the MSV1\_0 authentication package to process logon data collected by the [*GINA*](security.g_gly#-security-gina-gly) for the [*Winlogon*](security.w_gly#-security-winlogon-gly) logon process. The MSV1\_0 package checks the local security accounts manager (SAM) database to determine whether the logon data belongs to a valid [*security principal*](security.s_gly#-security-security-principal-gly) and then returns the result of the logon attempt to the LSA.

MSV1\_0 also supports domain logons. MSV1\_0 processes domain logons using pass-through authentication, as illustrated in the following diagram.

![msv1\-0 authentication package](images/lsaint4.png)

In pass-through authentication, the local instance of MSV1\_0 uses the Netlogon service to call the instance of MSV1\_0 running on the domain controller. The domain controller's instance of MSV1\_0 then checks the SAM database of the domain controller and returns the logon result to the instance of MSV1\_0 on the local machine. The local version of MSV1\_0 forwards the logon result to the instance of the LSA on the local machine.

If the domain controller is not available, and the LSA contains cached [*credentials*](security.c_gly#-security-credentials-gly) for the user, the local instance of MSV1\_0 can authenticate the user using the cached logon data.

The MSV1\_0 authentication package also supports [subauthentication packages](subauthentication-packages.md). A subauthentication package is a DLL that can replace part of the authentication and validation criteria used by the MSV1\_0 authentication package.

The MSV1\_0 authentication package defines a [*primary credentials*](security.p_gly#-security-primary-credentials-gly) key/string value pair. The primary credentials string holds the credentials derived from the data provided at logon time. It includes the user name and both case-sensitive and case-insensitive forms of the user's password.

 

 



