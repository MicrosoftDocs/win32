---
description: You determine a security policy for an application by defining the security privileges that it requires.
ms.assetid: 0348684f-aebd-4d2d-a69b-85fea551c0cd
title: Defining Roles for an Application
ms.topic: article
ms.date: 05/31/2018
---

# Defining Roles for an Application

You determine a security policy for an application by defining the security privileges that it requires. To do this you declare a symbolic level of privilege as a role—that is, define the role for the application—and then [assign the role](assigning-roles-to-components--interfaces--or-methods.md) to specific resources within the application. This design is fulfilled when the application is deployed and system administrators populate the role with actual users and user groups. For greater detail, see [Role-Based Security Administration](role-based-security-administration.md).

**To add a role to an application**

1.  In the console tree of the Component Services administrative tool, locate the COM+ application to which you want to add the role. Expand the tree to view the folders for the application.

2.  Right-click the **Roles** folder for the application, point to **New**, and then click **Role**.

3.  In the **Role**dialog box, type the name of the new role in the box provided.

4.  Click **OK**.

> [!Note]  
> After adding roles to the application, you must be sure to assign the roles to the appropriate components, interfaces, and methods. Otherwise, if role-based security has been chosen and enabled and if roles have been added but not assigned, all calls to the application will fail. For more information, see [Assigning Roles to Components, Interfaces, or Methods](assigning-roles-to-components--interfaces--or-methods.md).

 

## Related topics

<dl> <dt>

[Assigning Roles to Components, Interfaces, or Methods](assigning-roles-to-components--interfaces--or-methods.md)
</dt> <dt>

[Configuring Role-Based Security](configuring-role-based-security.md)
</dt> <dt>

[Enabling Access Checks for an Application](enabling-access-checks-for-an-application.md)
</dt> <dt>

[Enabling Access Checks at the Component Level](enabling-access-checks-at-the-component-level.md)
</dt> <dt>

[Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md)
</dt> </dl>

 

 



