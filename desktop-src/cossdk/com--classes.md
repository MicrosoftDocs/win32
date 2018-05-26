---
Description: The following are the COM+ classes.
ms.assetid: 236725f6-16a3-4209-a9e3-a127c1d7243a
title: COM+ Classes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COM+ Classes

The following are the COM+ classes.



| Class                                                            | Description                                                                                                                                                                                                                             |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AppDomainHelper**](/windows/win32/ComSvcs/?branch=master)                       | Binds a managed object to an application domain, which is an isolated environment where applications execute.                                                                                                                           |
| [**ClrAssemblyLocator**](/windows/win32/ComSvcs/?branch=master)                 | Retrieves information about an assembly when using managed code in the .NET Framework common language runtime.                                                                                                                          |
| [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master)                         | Specifies and configures the services that are to be active in the service domain entered when calling either [**CoCreateActivity**](/windows/win32/ComSvcs/nf-comsvcs-cocreateactivity?branch=master) or [**CoEnterServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coenterservicedomain?branch=master).                     |
| [**SecurityCallContext**](/windows/win32/ComSvcs/?branch=master)               | Provides access to the current call's security context, which contains information about an object's callers.                                                                                                                           |
| [**SecurityCallers**](/windows/win32/ComSvcs/?branch=master)                       | Provides access to information about individual callers in a collection of callers. The collection represents the chain of calls ending with the current call, and each caller in the collection represents the identity of one caller. |
| [**SecurityIdentity**](/windows/win32/ComSvcs/?branch=master)                     | Provides access to a collection of security information representing a caller's identity. Using this class, you can find out about a particular caller in a chain of callers that is part of the security call context.                 |
| [**SharedProperty**](/windows/win32/ComSvcs/?branch=master)                         | Sets or retrieves the value of a shared property.                                                                                                                                                                                       |
| [**SharedPropertyGroup**](/windows/win32/ComSvcs/?branch=master)               | Creates and accesses the shared properties in a shared property group.                                                                                                                                                                  |
| [**SharedPropertyGroupManager**](/windows/win32/ComSvcs/?branch=master) | Creates shared property groups and to obtain access to existing shared property groups.                                                                                                                                                 |
| [**TransactionContext**](/windows/win32/ComSvcs/?branch=master)                 | Creates a generic transactional object that begins a transaction.                                                                                                                                                                       |
| [**TransactionContextEx**](/windows/win32/ComSvcs/?branch=master)             | Creates a generic transactional object that begins a transaction. By calling the methods of this class, you can compose the work of multiple COM objects in a single transaction and explicitly commit or abort the transaction.        |



 

 

 



