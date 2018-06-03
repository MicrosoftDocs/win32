---
Description: The following are the COM+ classes.
ms.assetid: 236725f6-16a3-4209-a9e3-a127c1d7243a
title: COM+ Classes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Classes

The following are the COM+ classes.



| Class                                                            | Description                                                                                                                                                                                                                             |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AppDomainHelper**](/windows/desktop/api/ComSvcs/)                       | Binds a managed object to an application domain, which is an isolated environment where applications execute.                                                                                                                           |
| [**ClrAssemblyLocator**](/windows/desktop/api/ComSvcs/)                 | Retrieves information about an assembly when using managed code in the .NET Framework common language runtime.                                                                                                                          |
| [**CServiceConfig**](/windows/desktop/api/ComSvcs/)                         | Specifies and configures the services that are to be active in the service domain entered when calling either [**CoCreateActivity**](/windows/desktop/api/ComSvcs/nf-comsvcs-cocreateactivity) or [**CoEnterServiceDomain**](/windows/desktop/api/ComSvcs/nf-comsvcs-coenterservicedomain).                     |
| [**SecurityCallContext**](/windows/desktop/api/ComSvcs/)               | Provides access to the current call's security context, which contains information about an object's callers.                                                                                                                           |
| [**SecurityCallers**](/windows/desktop/api/ComSvcs/)                       | Provides access to information about individual callers in a collection of callers. The collection represents the chain of calls ending with the current call, and each caller in the collection represents the identity of one caller. |
| [**SecurityIdentity**](/windows/desktop/api/ComSvcs/)                     | Provides access to a collection of security information representing a caller's identity. Using this class, you can find out about a particular caller in a chain of callers that is part of the security call context.                 |
| [**SharedProperty**](/windows/desktop/api/ComSvcs/)                         | Sets or retrieves the value of a shared property.                                                                                                                                                                                       |
| [**SharedPropertyGroup**](/windows/desktop/api/ComSvcs/)               | Creates and accesses the shared properties in a shared property group.                                                                                                                                                                  |
| [**SharedPropertyGroupManager**](/windows/desktop/api/ComSvcs/) | Creates shared property groups and to obtain access to existing shared property groups.                                                                                                                                                 |
| [**TransactionContext**](/windows/desktop/api/ComSvcs/)                 | Creates a generic transactional object that begins a transaction.                                                                                                                                                                       |
| [**TransactionContextEx**](/windows/desktop/api/ComSvcs/)             | Creates a generic transactional object that begins a transaction. By calling the methods of this class, you can compose the work of multiple COM objects in a single transaction and explicitly commit or abort the transaction.        |



 

 

 



