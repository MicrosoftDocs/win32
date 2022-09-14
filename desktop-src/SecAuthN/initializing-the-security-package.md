---
description: Lists and explains the steps necessary to initialize a security package.
ms.assetid: 60c11519-f7ca-4002-b3f6-d74f50310730
title: Initializing the Security Package
ms.topic: article
ms.date: 05/31/2018
---

# Initializing the Security Package

These steps are necessary before using SSPI:

1.  The initialization function must be called to obtain the address of the security function table.

    The client and server call [**InitSecurityInterface**](/windows/desktop/api/Sspi/nf-sspi-initsecurityinterfacea) for a pointer to a [**SecurityFunctionTable**](/windows/win32/api/sspi/ns-sspi-securityfunctiontablea) dispatch table. This table contains pointers to callback functions declared in Sspi.h. These pointers provide access to the DLL's implementations of the various SSPI functions.

2.  Information must be obtained about the supported security packages.

    While most applications use security packages that support default or common capabilities, security packages can have unique capabilities of interest to the application. An application needing special capabilities can use a package that offers those capabilities. For more information, see [Getting Information About Security Packages](getting-information-about-security-packages.md).

At this point, the application has successfully initialized an SSP and chosen a security package with sufficient capabilities.

The [*Negotiate*](../secgloss/n-gly.md) package can be used where agreement between client and server about which [*security package*](../secgloss/s-gly.md) to use is done behind the scenes. If the Negotiate package is not used, the client and server must agree on the specific security package to use before performing the setup steps above.

 

 
