---
Description: Certificate Services supports certificate requests based on the PKCS \#10 format and the Keygen (Netscape) format. Certificate Services also supports PKCS \#7 renewal requests and Cryptographic Message Syntax (CMS) requests.
ms.assetid: 40641167-12de-4008-80e4-2fb758146421
title: Requests
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Requests

Certificate Services supports [*certificate requests*](security.c_gly#-security-certificate-request-gly) based on the PKCS \#10 format and the Keygen (Netscape) format. Certificate Services also supports PKCS \#7 renewal requests and Cryptographic Message Syntax (CMS) requests.

Certificate Services also provides an [ICertRequest](/windows/win32/Certcli/nn-certcli-icertrequest?branch=master) interface, which contains methods for submitting a certificate request and (if the request is approved) for receiving the resulting issued certificate.

Additional security-related interfaces are available in the [Certificate Enrollment Control](certificate-enrollment-control.md).

 

 



