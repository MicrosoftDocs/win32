---
Description: Explains how to validate Schannel credentials manually.
ms.assetid: 0229486a-5812-4a7e-98ad-446292997ee3
title: Manually Validating Schannel Credentials
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Manually Validating Schannel Credentials

By default, Schannel validates the [*server certificate*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) by calling the [**WinVerifyTrust**](https://msdn.microsoft.com/b7efac6a-ac9f-477a-aada-63fe32208e6f) function; however, if you have disabled this feature using the ISC\_REQ\_MANUAL\_CRED\_VALIDATION flag, you must validate the certificate provided by the server that is attempting to establish its identity.

To manually validate the server certificate, you must first get it. Use the [**QueryContextAttributes (General)**](/windows/desktop/api/Sspi/) function and specify the SECPKG\_ATTR\_REMOTE\_CERT\_CONTEXT attribute value. This attribute returns a [**CERT\_CONTEXT**](https://msdn.microsoft.com/f0a3200e-6541-423d-a4a3-595a31026eea) structure containing the certificate supplied by the server. This certificate is called the leaf certificate because it is the last certificate in the certificate chain and is farthest away from the [*root certificate*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd).

Using the leaf certificate you must verify the following:

-   The certificate chain is complete and the root is a certificate from a trusted [*certification authority*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CA).
-   The current time is not beyond the begin and end dates for each of the certificates in the certificate chain.
-   None of the certificates in the certificate chain have been revoked.
-   The depth of the leaf certificate is not deeper than the maximum allowable depth specified in the certificate extension. This check is only necessary if there is a depth specified.
-   The usage of the certificate is correct, for example, a [*client certificate*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) should not be used to authenticate a server.
-   For server authentication, the server identity contained in the server's leaf certificate matches the server that the client is attempting to contact. Typically, the client will match some item in the certificate's Subject Name field to the server's IP address or DNS name.

 

 



