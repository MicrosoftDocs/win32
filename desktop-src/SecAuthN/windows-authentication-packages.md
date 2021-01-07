---
description: Windows authentication packages provide authentication services by implementing package-specific functionality for the LsaLogonUser and LsaCallAuthenticationPackage functions provided by the LSA.
ms.assetid: 71f7eccd-694d-475f-b6d0-1eaf9ac468f5
title: Windows Authentication Packages
ms.topic: article
ms.date: 05/31/2018
---

# Windows Authentication Packages

Windows authentication packages provide authentication services by implementing package-specific functionality for the [**LsaLogonUser**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalogonuser) and [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) functions provided by the LSA.

MSV1\_0 is an example of a Windows [*authentication package*](../secgloss/a-gly.md). The MSV1\_0 package accepts a user name and a [*hashed*](../secgloss/h-gly.md) password, which it looks up in the [*Security Accounts Manager*](../secgloss/s-gly.md) (SAM) database. Depending on the results of the lookup, the MSV1\_0 authentication package accepts or rejects the authentication attempt.

For a list of the support functions the LSA provides for use by Windows authentication packages that require system services, see [LSA Functions Called by Authentication Packages](authentication-functions.md).

Windows authentication packages must implement a set of functions that are called by the LSA. For the complete list of functions, see [Functions Implemented by Authentication Packages](authentication-functions.md).

 

 
