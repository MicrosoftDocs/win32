---
title: EAPHost Registry Settings
description: Registry values in the following registry keys control aspects of the functionality of EAPHost.
ms.assetid: 2b954911-7c2e-4c86-b031-24632235a669
ms.topic: article
ms.date: 05/31/2018
---

# EAPHost Registry Settings

Registry values in the following registry keys control aspects of the functionality of EAPHost.



| Subkey                                                                 | Description                                                                                                                                                              |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BypassNegotiation](bypassnegotiation.md)                             | Determines if capabilities negotiation between the RAS server and client occurs.<br/>                                                                              |
| [AssumePhase2Fragmentation](assumephase2fragmentation.md)             | Determines if the RAS server and client assume phase 2 fragmentation.<br/>                                                                                         |
| [OverrideEAPCertificateSelection](overrideeapcertificateselection.md) | Determines whether the client will override the default smart card certificate selection behavior and provide the user with more certificates to choose from.<br/> |
| [PeapServerUseAllPurposeCert](peapserveruseallpurposecert.md)         | Determines if all-purpose certificates are used for PEAP authentication.<br/>                                                                                      |
| [PeapServerAcceptAllPurposeCert](peapserveracceptallpurposecert.md)   | Determines if all-purpose certificates are accepted for PEAP authentication.<br/>                                                                                  |
| [TlsServerUseAllPurposeCert](tlsserveruseallpurposecert.md)           | Determines if all-purpose certificates are used for EAP-TLS authentication.<br/>                                                                                   |
| [TlsServerAcceptAllPurposeCert](tlsserveracceptallpurposecert.md)     | Determines if all-purpose certificates are accepted for EAP-TLS authentication.<br/>                                                                               |



 

## Related topics

<dl> <dt>

[EAPHost API Reference](eaphost-api-reference.md)
</dt> </dl>

 

 





