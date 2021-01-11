---
description: CRM components can be installed into either a COM+ server application or a COM+ library application.
ms.assetid: d1ce3a0c-1278-498c-b5dc-4e14b26b4fc2
title: Configuring COM+ CRM Components
ms.topic: article
ms.date: 05/31/2018
---

# Configuring COM+ CRM Components

CRM components can be installed into either a COM+ server application or a COM+ library application. However, they must always run in a COM+ server application. If they are installed in a COM+ library application, they are not available for use in client processes.

If the CRM components they are installed in a library application, they are available to more than one server application. If installed in a specific server application, they are available only to that specific server application.

To enable use of a CRM in a server application, use the following steps:

1.  From Component Services, under the server application properties page, click the **Advanced** tab.

2.  Select the **Enable compensating Resource Managers** option for that server application. If this option is not selected, attempts to use a CRM within this server application will fail.

    > [!Note]  
    > If installed in a library application, it is not necessary to select the **Enable compensating Resource Managers** option for that library application, but this option must be selected for the server application in which the CRM is intended to run.

     

It is recommended that the CRM Worker and CRM Compensator components for a specific CRM be installed in the same application.

The recommended settings for CRM components are as follows.



| Component           | Settings                                                                                             |
|---------------------|------------------------------------------------------------------------------------------------------|
| **CRM Worker**      | transaction = requiredsync = yesJIT = yesthreading model = Both (or threading model = Apartment)     |
| **CRM Compensator** | transaction = disabledsync = disabledJIT = nothreading model = Both (or threading model = Apartment) |



 

> [!Note]  
> Components that use the CRM must explicitly specify a threading model when they are registered. The default, 'Main Thread Apartment,' is not supported. The only two threading models supported are Apartment and Both.

 

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 



