---
Description: Explains how to validate Schannel credentials manually.
ms.assetid: 0229486a-5812-4a7e-98ad-446292997ee3
title: Manually Validating Schannel Credentials
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Manually Validating Schannel Credentials

By default, Schannel validates the [*server certificate*](security.s_gly#-security-server-certificate-gly) by calling the [**WinVerifyTrust**](security.winverifytrust) function; however, if you have disabled this feature using the ISC\_REQ\_MANUAL\_CRED\_VALIDATION flag, you must validate the certificate provided by the server that is attempting to establish its identity.

To manually validate the server certificate, you must first get it. Use the [**QueryContextAttributes (General)**](/windows/win32/Sspi/?branch=master) function and specify the SECPKG\_ATTR\_REMOTE\_CERT\_CONTEXT attribute value. This attribute returns a [**CERT\_CONTEXT**](security.cert_context) structure containing the certificate supplied by the server. This certificate is called the leaf certificate because it is the last certificate in the certificate chain and is farthest away from the [*root certificate*](security.r_gly#-security-root-certificate-gly).

Using the leaf certificate you must verify the following:

-   The certificate chain is complete and the root is a certificate from a trusted [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA).
-   The current time is not beyond the begin and end dates for each of the certificates in the certificate chain.
-   None of the certificates in the certificate chain have been revoked.
-   The depth of the leaf certificate is not deeper than the maximum allowable depth specified in the certificate extension. This check is only necessary if there is a depth specified.
-   The usage of the certificate is correct, for example, a [*client certificate*](security.c_gly#-security-client-certificate-gly) should not be used to authenticate a server.
-   For server authentication, the server identity contained in the server's leaf certificate matches the server that the client is attempting to contact. Typically, the client will match some item in the certificate's Subject Name field to the server's IP address or DNS name.

 

 



