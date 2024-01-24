---
description: Assigning Roles to Components, Interfaces, or Methods
ms.assetid: 687d5692-4a83-4de8-b99d-859aaaddd16d
title: Assigning Roles to Components, Interfaces, or Methods
ms.topic: reference
ms.date: 05/31/2018
---

# Assigning Roles to Components, Interfaces, or Methods

You can explicitly assign a role to any item within a COM+ application that is visible through the Component Services administrative tool. Doing so ensures that any users that are members of the role will be permitted access to that item and any other items that it contains. For example, if you assign the role "Readers" to a component, any member of "Readers" is allowed access to that component and any interfaces and methods it exposes. "Readers" will show up as an Inherited role for any of those interfaces and methods.

A method is accessible to callers only if you assign a role to it, either by explicitly assigning the role directly to the method or by assigning a role to the method's interface or the method's component, in which case the role will be inherited by the method. If no role is assigned and if access checks are enabled, all calls to the method will fail.

Before you can assign a role, you must [define](defining-roles-for-an-application.md) it for the application. All roles defined for the application will appear in the **Roles explicitly set for selected item(s)** window on the **Security** tab for any components, methods, and interfaces within the application.

**To assign roles to a component, method, or interface**

1.  In the console tree of the Component Services administrative tool, locate the COM+ application for which the role has been defined. Expand the tree to view the application's components, interfaces, or methods, depending on what you are assigning the role to.

2.  Right-click the item to which you want to assign the role, and then click **Properties**.

3.  In the properties dialog box, click the **Security** tab.

4.  In the **Roles explicitly set for selected item(s)** box, select the roles that you want to assign to the item.

5.  Click **OK**.

Any roles that you have explicitly set for an item will be inherited by any lower-level items it contains and will show up in the **Roles inherited by selected item(s)** window for those items.

## Related topics

<dl> <dt>

[Configuring Role-Based Security](configuring-role-based-security.md)
</dt> <dt>

[Defining Roles for an Application](defining-roles-for-an-application.md)
</dt> <dt>

[Enabling Access Checks for an Application](enabling-access-checks-for-an-application.md)
</dt> <dt>

[Enabling Access Checks at the Component Level](enabling-access-checks-at-the-component-level.md)
</dt> <dt>

[Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md)
</dt> </dl>

 

 



