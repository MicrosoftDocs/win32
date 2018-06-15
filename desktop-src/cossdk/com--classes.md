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
| [**AppDomainHelper**](https://msdn.microsoft.com/en-us/library/ms684250(v=VS.85).aspx)                       | Binds a managed object to an application domain, which is an isolated environment where applications execute.                                                                                                                           |
| [**ClrAssemblyLocator**](https://msdn.microsoft.com/en-us/library/ms681167(v=VS.85).aspx)                 | Retrieves information about an assembly when using managed code in the .NET Framework common language runtime.                                                                                                                          |
| [**CServiceConfig**](https://msdn.microsoft.com/en-us/library/ms688295(v=VS.85).aspx)                         | Specifies and configures the services that are to be active in the service domain entered when calling either [**CoCreateActivity**](/windows/desktop/api/ComSvcs/nf-comsvcs-cocreateactivity) or [**CoEnterServiceDomain**](/windows/desktop/api/ComSvcs/nf-comsvcs-coenterservicedomain).                     |
| [**SecurityCallContext**](https://msdn.microsoft.com/en-us/library/ms687633(v=VS.85).aspx)               | Provides access to the current call's security context, which contains information about an object's callers.                                                                                                                           |
| [**SecurityCallers**](https://msdn.microsoft.com/en-us/library/ms679185(v=VS.85).aspx)                       | Provides access to information about individual callers in a collection of callers. The collection represents the chain of calls ending with the current call, and each caller in the collection represents the identity of one caller. |
| [**SecurityIdentity**](https://msdn.microsoft.com/en-us/library/ms686443(v=VS.85).aspx)                     | Provides access to a collection of security information representing a caller's identity. Using this class, you can find out about a particular caller in a chain of callers that is part of the security call context.                 |
| [**SharedProperty**](https://msdn.microsoft.com/en-us/library/ms679208(v=VS.85).aspx)                         | Sets or retrieves the value of a shared property.                                                                                                                                                                                       |
| [**SharedPropertyGroup**](https://msdn.microsoft.com/en-us/library/ms679250(v=VS.85).aspx)               | Creates and accesses the shared properties in a shared property group.                                                                                                                                                                  |
| [**SharedPropertyGroupManager**](https://msdn.microsoft.com/en-us/library/ms681236(v=VS.85).aspx) | Creates shared property groups and to obtain access to existing shared property groups.                                                                                                                                                 |
| [**TransactionContext**](https://msdn.microsoft.com/en-us/library/ms687785(v=VS.85).aspx)                 | Creates a generic transactional object that begins a transaction.                                                                                                                                                                       |
| [**TransactionContextEx**](https://msdn.microsoft.com/en-us/library/ms681749(v=VS.85).aspx)             | Creates a generic transactional object that begins a transaction. By calling the methods of this class, you can compose the work of multiple COM objects in a single transaction and explicitly commit or abort the transaction.        |



 

 

 



