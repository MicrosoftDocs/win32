---
title: Security Support Providers (SSPs)
description: Beginning with Windows 2000, RPC supports a variety of security providers and packages.
ms.assetid: f82eba3d-412e-4cb6-9353-2e66bd0f377a
ms.topic: article
ms.date: 05/31/2018
---

# Security Support Providers (SSPs)

Beginning with Windows 2000, RPC supports a variety of security providers and packages. These include:

-   **Kerberos Protocol Security Package.** Kerberos v5 protocol is an industry-standard security package. It uses fullsic principal names.
-   **SCHANNEL SSP.** This SSP implements the Microsoft Unified Protocol Provider security package, which unifies SSL, private communication technology (PCT), and transport level security (TLS) into one security package. It recognizes msstd and fullsic principal names.
-   **NTLM Security Package.** This was the primary security package for NTLM networks prior to Windows 2000.

In addition, Microsoft RPC provides a *pseudo-SSP* that enables applications to negotiate between the use of real SSPs. This pseudo-SSP, called the Simple GSS-API Negotiation Mechanism (Snego) SSP, does not provide any actual authentication features. Its only use is to help applications select a real SSP. Currently, client and server programs can use the Snego SSP to negotiate between the use of the NTLM security package and Kerberos protocol security package. For more information on selecting SSPs, see [Authentication-Service Constants](authentication-service-constants.md).

All of the SSPs that Microsoft provides, except SCHANNEL, recognize authentication credentials in the form provided by the [**SEC\_WINNT\_AUTH\_IDENTITY**](/windows/desktop/api/Rpcdce/ns-rpcdce-sec_winnt_auth_identity_a) structure. For details, see [Client Authentication Credentials](client-authentication-credentials.md). For information on how to use specific SSPs, see [SSPI Functions](/windows/desktop/SecMgmt/management-functions) and [Using the Schannel Security Provider](/windows/desktop/SecAuthN/secure-channel) in the Security documentation of the Platform Software Development Kit (SDK).

 

 