---
description: Intermediaries communicate with client applications to allow them to submit certificate requests, and (assuming that the request results in an issued certificate) to download the issued certificate to the client.
ms.assetid: c696f09e-98d3-4cea-8ea1-cd8f40b74f12
title: Intermediaries
ms.topic: article
ms.date: 05/31/2018
---

# Intermediaries

Intermediaries communicate with client applications to allow them to submit [*certificate requests*](../secgloss/c-gly.md), and (assuming that the request results in an issued certificate) to download the issued certificate to the client. Each transport layer protocol requires its own intermediary.

Microsoft Certificate Services ships with an intermediary (the web enrollment pages) for HTTP. Another example of an intermediary is the Microsoft Windows Certificates MMC snap-in (which allows the Certificate Request Wizard to be invoked). If other transport layer protocols are to be used with Certificate Services, a developer can create an intermediary for each desired transport layer protocol.

Intermediaries communicate with Certificate Services using the [**ICertRequest**](/windows/desktop/api/Certcli/nn-certcli-icertrequest) and [**ICertConfig**](/windows/desktop/api/Certcli/nn-certcli-icertconfig) interfaces provided by the server engine. The [**ICertRequest::Submit**](/windows/desktop/api/Certcli/nf-certcli-icertrequest-submit) method is used to submit a [*certificate request*](../secgloss/c-gly.md), and [**ICertRequest::GetCertificate**](/windows/desktop/api/Certcli/nf-certcli-icertrequest-getcertificate) is used to get the resulting issued certificate. Similarly, [**ICertConfig::GetConfig**](/windows/desktop/api/Certcli/nf-certcli-icertconfig-getconfig) is used to determine which certification authority can be used to issue the certificate.

An intermediary is not language-dependent. It may be a program written in C++, Visual Basic, Java, script, or another language.

In addition to gathering data from the client to build a certificate request, an intermediary may specify request attributes. Requests submitted to a [*certification authority*](../secgloss/c-gly.md) running the enterprise policy module must indicate the type of certificate requested by specifying either a "CertificateTemplate" attribute or a Certificate Template extension in the request itself.

Note that during the creation of a certificate request, developers (and intermediaries) are responsible for maintaining the secrecy of the private key. After a private key has been compromised (lost its secrecy), it is useless.

The Certificate Services web enrollment pages use the [Certificate Enrollment Interfaces](cryptography-interfaces.md), which protects private keys by generating them on the workstation. In addition to maintaining the secrecy of the private key, the Certificate Enrollment Control allows an intermediary to specify the Cryptographic Service Provider, key specification, key strength, and hash algorithm.

The Certificates MMC snap-in also uses the Certificate Enrollment Control (Xenroll.dll). However, where the Certificate Services web enrollment pages cause the Certificate Enrollment Control resource (Xenroll.dll) to be downloaded to the client if needed, the Certificates MMC snap-in runs in an environment where Xenroll.dll is already an available resource.

In addition to [**ICertRequest**](/windows/desktop/api/Certcli/nn-certcli-icertrequest) and [**ICertConfig**](/windows/desktop/api/Certcli/nn-certcli-icertconfig), developers of intermediaries may find the [Certificate Enrollment Interfaces](cryptography-interfaces.md) and the [Smart Card Enrollment Control](certificate-enrollment-control.md) to be useful.

 

 
