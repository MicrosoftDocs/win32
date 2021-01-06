---
description: If your COM+ application uses role-based security, there are several tasks that need to be completed.
ms.assetid: f53b9945-cd34-4afc-a03a-dd72b0af160d
title: Configuring Role-Based Security
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Role-Based Security

If your COM+ application uses role-based security, there are several tasks that need to be completed. When designing the components in your application, you define the roles that are necessary to help protect access to those components. You also decide which roles to assign to the application's components, interfaces, and methods. During application integration, you use the Component Services administrative tool to add the defined roles to the application and assign each role to the appropriate components, interfaces, and methods.

In configuring role-based security, you perform the following steps:

1.  Enable access checks at the application level. To turn on security checking for an application. See [Enabling Access Checks for an Application](enabling-access-checks-for-an-application.md) for details on how to perform this step.
2.  Set security level for access checks. To set security either at process or at process and component level. See [Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md) for details on how to perform this step.
3.  Enable access checks at the component level. To turn on security checking at the component, interface, and method levels. See [Enabling Access Checks at the Component Level](enabling-access-checks-at-the-component-level.md) for details on how to perform this step.
4.  Define roles for an application. To create roles for an application. See [Defining Roles for an Application](defining-roles-for-an-application.md) for details on how to perform this step.
5.  Assign roles to components, interfaces, or methods. To assign roles to specific resources within an application. See [Assigning Roles to Components, Interfaces, or Methods](assigning-roles-to-components--interfaces--or-methods.md) for details on how to perform this step.

## Related topics

<dl> <dt>

[Configuring the Software Restriction Policy](configuring-the-software-restriction-policy.md)
</dt> <dt>

[Setting an Impersonation Level](setting-an-impersonation-level.md)
</dt> </dl>

 

 



