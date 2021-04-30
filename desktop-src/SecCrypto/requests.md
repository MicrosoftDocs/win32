---
description: Certificate Services supports certificate requests based on the PKCS \#10 format and the Keygen (Netscape) format. Certificate Services also supports PKCS \#7 renewal requests and Cryptographic Message Syntax (CMS) requests.
ms.assetid: '6321ce99-f5d1-4d72-a062-99cffb543731'
title: Requests
ms.topic: article
ms.date: 05/31/2018
---

# Requests

Certificate Services supports [*certificate requests*](../secgloss/c-gly.md) based on the PKCS \#10 format and the Keygen (Netscape) format. Certificate Services also supports PKCS \#7 renewal requests and Cryptographic Message Syntax (CMS) requests.

Certificate Services also provides an [ICertRequest](/windows/desktop/api/Certcli/nn-certcli-icertrequest) interface, which contains methods for submitting a certificate request and (if the request is approved) for receiving the resulting issued certificate.

Additional security-related interfaces are available in the [Certificate Enrollment Control](certificate-enrollment-control.md).

 

 
