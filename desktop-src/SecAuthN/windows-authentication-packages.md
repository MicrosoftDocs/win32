---
Description: Windows authentication packages provide authentication services by implementing package-specific functionality for the LsaLogonUser and LsaCallAuthenticationPackage functions provided by the LSA.
ms.assetid: 71f7eccd-694d-475f-b6d0-1eaf9ac468f5
title: Windows Authentication Packages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Authentication Packages

Windows authentication packages provide authentication services by implementing package-specific functionality for the [**LsaLogonUser**](/windows/win32/Ntsecapi/nf-ntsecapi-lsalogonuser?branch=master) and [**LsaCallAuthenticationPackage**](/windows/win32/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage?branch=master) functions provided by the LSA.

MSV1\_0 is an example of a Windows [*authentication package*](security.a_gly#-security-authentication-package-gly). The MSV1\_0 package accepts a user name and a [*hashed*](security.h_gly#-security-hash-gly) password, which it looks up in the [*Security Accounts Manager*](security.s_gly#-security-security-accounts-manager-gly) (SAM) database. Depending on the results of the lookup, the MSV1\_0 authentication package accepts or rejects the authentication attempt.

For a list of the support functions the LSA provides for use by Windows authentication packages that require system services, see [LSA Functions Called by Authentication Packages](authentication-functions.md#lsa-functions-called-by-authentication-packages).

Windows authentication packages must implement a set of functions that are called by the LSA. For the complete list of functions, see [Functions Implemented by Authentication Packages](authentication-functions.md#functions-implemented-by-authentication-packages).

 

 



