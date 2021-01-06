---
description: COM+ CRM Security Considerations
ms.assetid: e212c847-b43b-43be-b089-82336551b89a
title: COM+ CRM Security Considerations
ms.topic: article
ms.date: 05/31/2018
---

# COM+ CRM Security Considerations

A CRM log file could contain sensitive information that must be secured. For this reason, if the server application is running under any identity other than Interactive User when the CRM log file is first created, the CRM log file is security protected for that user only. This feature is available only on the NTFS file system. If the identity of the server application is subsequently changed, the security information for the CRM log file is not automatically changed. It can be changed manually by using existing Windows administration tools. The alternative is simply to delete the CRM log file when it is in a clean state (which is expected after a controlled shutdown of the server application).

In normal operation, COM+ creates the CRM compensator component and calls the [**ICrmCompensator**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmcompensator) interface. However, a user having privileges to create the CRM Compensator can call the **ICrmCompensator** interface at inappropriate times, possibly causing system security problems. To help protect against these security problems, the system administrator can use role-based security to restrict the CRM Compensator component to only those identities of the server applications in which it runs. If the component is running in a library application, this would include all the identities of the server applications.

> [!Note]  
> Starting with Windows Server 2003, to help prevent activation from outside the server application, it is possible to further ensure a more secure system by marking the CRM Compensator component as private.

 

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 



