---
description: Lists the certificate formats supported by Certificate Services.
ms.assetid: e6a324d0-9b62-4625-a604-cb1eeca22aae
title: Supported Certificate Formats
ms.topic: article
ms.date: 05/31/2018
---

# Supported Certificate Formats

Certificate Services can issue the following types of certificates.



| Term                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="X.509_version_3_SSL-compatible_client_authentication_certificate"></span><span id="x.509_version_3_ssl-compatible_client_authentication_certificate"></span><span id="X.509_VERSION_3_SSL-COMPATIBLE_CLIENT_AUTHENTICATION_CERTIFICATE"></span>[*X.509*](../secgloss/x-gly.md) version 3 SSL-compatible client authentication certificate<br/> | This client authentication certificate identifies a client and is used by servers to authenticate a client that requests server access.<br/>     |
| <span id="X.509_v3_SSL-compatible_server_authentication_certificate"></span><span id="x.509_v3_ssl-compatible_server_authentication_certificate"></span><span id="X.509_V3_SSL-COMPATIBLE_SERVER_AUTHENTICATION_CERTIFICATE"></span>X.509 v3 SSL-compatible server authentication certificate<br/>                                                                                         | This server authentication certificate identifies a server and is used by clients to authenticate a server that the client wants to access.<br/> |
| <span id="S_MIME_certificate"></span><span id="s_mime_certificate"></span><span id="S_MIME_CERTIFICATE"></span>[*S/MIME*](../secgloss/s-gly.md) certificate<br/>                                                                                                           | This certificate is used by clients for secure email under the S/MIME (Secure/Multipurpose Internet Mail Extensions) protocol.<br/>              |



 

In addition to these certificates, Certificate Services can also be used to issue other X.509 certificates by writing a custom policy module.

> [!Note]  
> "Server authentication certificate" and "server certificate" as well as "client authentication certificate" and "client certificate" are interchangeable terms.

 

Additionally, Certificate Services includes certificate templates in the Microsoft enterprise certification authority configuration. Consult the Windows Help documentation for certificate templates to understand how they define certificate purposes.

 

 
