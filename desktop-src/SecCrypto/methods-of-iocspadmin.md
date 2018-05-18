---
Description: 'The following methods are defined by the IOCSPAdmin interface. The property access methods are not shown here. To see the properties for IOCSPAdmin, see Properties of IOCSPAdmin.'
ms.assetid: 'cbe43e5d-cd1b-467c-a0fd-1ee7cc5adcf7'
title: Methods of IOCSPAdmin
---

# Methods of IOCSPAdmin

The following methods are defined by the [**IOCSPAdmin**](iocspadmin.md) interface. The property access methods are not shown here. To see the properties for **IOCSPAdmin**, see [Properties of IOCSPAdmin](properties-of-iocspadmin.md).



| Method                                                              | Description                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetConfiguration**](iocspadmin-getconfiguration-method.md)      | Connects to an Online Certificate Status Protocol (OCSP) responder server and initializes an **OCSPAdmin** object with the configuration information from the server.                                                                                                     |
| [**GetHashAlgorithms**](iocspadmin-gethashalgorithms.md)           | Gets a list of hash algorithm names. The responder server uses one of the named algorithms to sign OCSP responses for a given [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA) configuration. |
| [**GetMyRoles**](iocspadmin-getmyroles-method.md)                  | Gets the access mask of privilege roles for a user on a given responder server.                                                                                                                                                                                           |
| [**GetSecurity**](iocspadmin-getsecurity.md)                       | Gets security descriptor information for a responder server.                                                                                                                                                                                                              |
| [**GetSigningCertificates**](iocspadmin-getsigningcertificates.md) | Gets the signing certificates that are available on a responder server for a given CA certificate.                                                                                                                                                                        |
| [**Ping**](iocspadmin-ping.md)                                     | Tests a DCOM connection with a responder service.                                                                                                                                                                                                                         |
| [**SetConfiguration**](iocspadmin-setconfiguration-method.md)      | Updates a responder service with configuration changes.                                                                                                                                                                                                                   |
| [**SetSecurity**](iocspadmin-setsecurity.md)                       | Updates security descriptor information for an OCSP responder server.                                                                                                                                                                                                     |



 

 

 



