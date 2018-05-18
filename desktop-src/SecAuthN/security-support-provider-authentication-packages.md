---
Description: 'The Windows operating system supports authentication using security packages that function as both security support providers and as authentication packages.'
ms.assetid: 'f40060be-fad2-4008-b981-727199d71581'
title: 'Security Support Provider/Authentication Packages'
---

# Security Support Provider/Authentication Packages

The Windows operating system supports authentication using [*security packages*](security.s_gly#-security-security-package-gly) that function as both [*security support providers*](security.s_gly#-security-security-support-provider-gly) and as [*authentication packages*](security.a_gly#-security-authentication-package-gly). Security packages provide the logon process support services of a Windows authentication package and also provide authentication services to applications by implementing a set of functions that are mapped to the [Security Support Provider Interface](sspi.md) (SSPI).

A security package that functions as an authentication package and implements the functionality required by [*SSPI*](security.s_gly#-security-security-support-provider-interface-gly) is called a security support provider/authentication package (SSP/AP).

For more information about security packages, see [SSP Packages Provided by Microsoft](ssp-packages-provided-by-microsoft.md). For information about developing custom SSP/APs, see [Custom Security Packages](custom-security-packages.md).

 

 



