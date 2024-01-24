---
description: The following methods are defined by the IOCSPAdmin interface. The property access methods are not shown here. To see the properties for IOCSPAdmin, see Properties of IOCSPAdmin.
ms.assetid: cbe43e5d-cd1b-467c-a0fd-1ee7cc5adcf7
title: Methods of IOCSPAdmin
ms.topic: article
ms.date: 05/31/2018
---

# Methods of IOCSPAdmin

The following methods are defined by the [**IOCSPAdmin**](/windows/desktop/api/certadm/nn-certadm-iocspadmin) interface. The property access methods are not shown here. To see the properties for **IOCSPAdmin**, see [Properties of IOCSPAdmin](properties-of-iocspadmin.md).



| Method                                                              | Description                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetConfiguration**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-getconfiguration)      | Connects to an Online Certificate Status Protocol (OCSP) responder server and initializes an **OCSPAdmin** object with the configuration information from the server.                                                                                                     |
| [**GetHashAlgorithms**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-gethashalgorithms)           | Gets a list of hash algorithm names. The responder server uses one of the named algorithms to sign OCSP responses for a given [*certification authority*](../secgloss/c-gly.md) (CA) configuration. |
| [**GetMyRoles**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-getmyroles)                  | Gets the access mask of privilege roles for a user on a given responder server.                                                                                                                                                                                           |
| [**GetSecurity**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-getsecurity)                       | Gets security descriptor information for a responder server.                                                                                                                                                                                                              |
| [**GetSigningCertificates**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-getsigningcertificates) | Gets the signing certificates that are available on a responder server for a given CA certificate.                                                                                                                                                                        |
| [**Ping**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-ping)                                     | Tests a DCOM connection with a responder service.                                                                                                                                                                                                                         |
| [**SetConfiguration**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-setconfiguration)      | Updates a responder service with configuration changes.                                                                                                                                                                                                                   |
| [**SetSecurity**](/windows/desktop/api/Certadm/nf-certadm-iocspadmin-setsecurity)                       | Updates security descriptor information for an OCSP responder server.                                                                                                                                                                                                     |



 

 

 
