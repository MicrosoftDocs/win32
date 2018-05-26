---
Description: The following methods are defined by the IOCSPAdmin interface. The property access methods are not shown here. To see the properties for IOCSPAdmin, see Properties of IOCSPAdmin.
ms.assetid: cbe43e5d-cd1b-467c-a0fd-1ee7cc5adcf7
title: Methods of IOCSPAdmin
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Methods of IOCSPAdmin

The following methods are defined by the [**IOCSPAdmin**](/windows/win32/certadm/nn-certadm-iocspadmin?branch=master) interface. The property access methods are not shown here. To see the properties for **IOCSPAdmin**, see [Properties of IOCSPAdmin](properties-of-iocspadmin.md).



| Method                                                              | Description                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetConfiguration**](/windows/win32/Certadm/nf-certadm-iocspadmin-getconfiguration?branch=master)      | Connects to an Online Certificate Status Protocol (OCSP) responder server and initializes an **OCSPAdmin** object with the configuration information from the server.                                                                                                     |
| [**GetHashAlgorithms**](/windows/win32/Certadm/nf-certadm-iocspadmin-gethashalgorithms?branch=master)           | Gets a list of hash algorithm names. The responder server uses one of the named algorithms to sign OCSP responses for a given [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA) configuration. |
| [**GetMyRoles**](/windows/win32/Certadm/nf-certadm-iocspadmin-getmyroles?branch=master)                  | Gets the access mask of privilege roles for a user on a given responder server.                                                                                                                                                                                           |
| [**GetSecurity**](/windows/win32/Certadm/nf-certadm-iocspadmin-getsecurity?branch=master)                       | Gets security descriptor information for a responder server.                                                                                                                                                                                                              |
| [**GetSigningCertificates**](/windows/win32/Certadm/nf-certadm-iocspadmin-getsigningcertificates?branch=master) | Gets the signing certificates that are available on a responder server for a given CA certificate.                                                                                                                                                                        |
| [**Ping**](/windows/win32/Certadm/nf-certadm-iocspadmin-ping?branch=master)                                     | Tests a DCOM connection with a responder service.                                                                                                                                                                                                                         |
| [**SetConfiguration**](/windows/win32/Certadm/nf-certadm-iocspadmin-setconfiguration?branch=master)      | Updates a responder service with configuration changes.                                                                                                                                                                                                                   |
| [**SetSecurity**](/windows/win32/Certadm/nf-certadm-iocspadmin-setsecurity?branch=master)                       | Updates security descriptor information for an OCSP responder server.                                                                                                                                                                                                     |



 

 

 



