---
title: NAP Interfaces
description: NAP Interfaces
ms.assetid: fff854b9-9c83-4db2-bceb-22509b261a97
ms.topic: article
ms.date: 05/31/2018
---

# NAP Interfaces

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The NAP system is composed of the following interfaces.



| Interface Name                                                                   | Description                                                                                                                                         |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**INapCertRelyingParty**](inapcertrelyingparty.md)                             | Provides methods that certificate-relying parties must use to communicate with the NapAgent.                                                        |
| [**INapClientManagement**](inapclientmanagement.md)                             | Used for NAP client management of SoH cache and SoH exchange triggering. Deprecated.                                                                |
| [**INapClientManagement2**](inapclientmanagement2.md)                           | Used for NAP client management of SoH cache and SoH exchange triggering.                                                                            |
| [**INapComponentConfig**](inapcomponentconfig.md)                               | Used for customized configuration of SHV components. Deprecated.                                                                                    |
| [**INapComponentConfig2**](inapcomponentconfig2.md)                             | Provides NAP system configuration methods for system health validators (SHVs) to configure a network policy server (NPS) user interface remotely.   |
| [**INapComponentConfig3**](inapcomponentconfig3.md)                             | Provides NAP system configuration methods for system health validators (SHVs) to set and modify configuration data for a specific configuration ID. |
| [**INapComponentInfo**](inapcomponentinfo.md)                                   | Must be implemented by plug-in components, such as SHAs and SHVs, so that they can be communicated with by the NAP system.                          |
| [**INapEnforcementClientBinding**](inapenforcementclientbinding.md)             | Used by enforcement clients to communicate with the NapAgent.                                                                                       |
| [**INapEnforcementClientCallback**](inapenforcementclientcallback.md)           | Enforcement clients must implement this interface to enable the NapAgent to communicate with them.                                                  |
| [**INapEnforcementClientConnection**](inapenforcementclientconnection.md)       | Allows for client connection management. Deprecated.                                                                                                |
| [**INapEnforcementClientConnection2**](inapenforcementclientconnection2.md)     | Allows for client connection management.                                                                                                            |
| [**INapServerCallback**](inapservercallback.md)                                 | SHVs use the single method on this interface to signal asynchronous request completion.                                                             |
| [**INapServerInfo**](inapserverinfo.md)                                         | Used by management clients (e.g. WMI providers, command-line tools, etc.) to query the status of the NAP server system.                             |
| [**INapServerManagement**](inapservermanagement.md)                             | Used for basic management of the NAP Server.                                                                                                        |
| [**INapSoHConstructor**](inapsohconstructor.md)                                 | Used by SHAs to construct SoH-requests and by SHVs to construct SoH-responses.                                                                      |
| [**INapSoHProcessor**](inapsohprocessor.md)                                     | Used by SHAs to process the contents of SoH-responses and by SHVs to process the contents of SoH-requests.                                          |
| [**INapSystemHealthAgentBinding**](inapsystemhealthagentbinding.md)             | SHAs must use this interface to communicate with the NapAgent. Deprecated.                                                                          |
| [**INapSystemHealthAgentBinding2**](inapsystemhealthagentbinding2.md)           | SHAs must use this interface to communicate with the NapAgent.                                                                                      |
| [**INapSystemHealthAgentCallback**](inapsystemhealthagentcallback.md)           | SHAs must implement this interface to coordinate processing with the NAP system.                                                                    |
| [**INapSystemHealthAgentRequest**](inapsystemhealthagentrequest.md)             | SHAs use this interface to communicate and coordinate their processing with the NAP system.                                                         |
| [**INapSystemHealthValidator**](inapsystemhealthvalidator.md)                   | Provides methods that an SHV must implement so that the NAP system can communicate with it.                                                         |
| [**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md)   | SHVs use this interface for data communication with their client-side counterpart. Deprecated.                                                      |
| [**INapSystemHealthValidationRequest2**](inapsystemhealthvalidationrequest2.md) | SHVs use this interface for data communication with their client-side counterpart.                                                                  |



 

 

 




