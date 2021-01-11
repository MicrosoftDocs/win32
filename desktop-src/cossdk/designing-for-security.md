---
description: Designing for Security
ms.assetid: 436f9d86-fbfa-4d5a-8580-fa1d4065c0aa
title: Designing for Security
ms.topic: article
ms.date: 05/31/2018
---

# Designing for Security

Your end-to-end strategy for security obviously depends on the type of distributed application you are developing. Following are several suggestions for addressing security with respect to middle-tier application logic:

-   For efficiency and performance, authenticate as close to the user as you can. If your application involves a browser-to-business-logic-to-database architecture, consider mapping the browser clients to domain identities, run the COM+ application under identities specific to each application, and configure tables in the data tier to be accessible only by a particular application identity. This trusted server scenario is more scalable and less problematic than using the DBMS for authenticating.
-   If you are designing a component that will be used in a distributed application using role-based security, you can use the [COM+ security](com--security.md) functionality. This functionality allows you to call methods such as [**IObjectContext::IsCallerInRole**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-iscallerinrole) and [**IObjectContext::IsSecurityEnabled**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-issecurityenabled) to help protect blocks of code from unauthorized access. You can also use the security call context to get information about an object's callers.
-   If you are designing a component that will be used in a distributed application without using role-based security, security is automatically checked only at the process level. Process access permissions determine who is given access to the application. If you need finer grain control over security settings at the process or at the interface level, use the programmatic security functionality provided by COM.
-   If a component using COM+ programmatic security is run without being integrated into a COM+ application, exceptions will be thrown. Therefore, if you want such a component to be successfully integrated into an application that is not part of the COM+ environment, you must handle all exceptions appropriately.

## Related topics

<dl> <dt>

[Designing for Availability](designing-for-availability.md)
</dt> <dt>

[Designing for Deployment](designing-for-deployment.md)
</dt> <dt>

[Designing for Scalability](designing-for-scalability.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> </dl>

 

 



