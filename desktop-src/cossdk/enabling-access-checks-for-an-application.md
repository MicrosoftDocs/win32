---
description: Performing this step enables either process access checks or full role-based security, depending on what security level you select and whether you enable access checking for individual components.
ms.assetid: 266bdac1-41be-45a5-a8c7-f9c6fe08445c
title: Enabling Access Checks for an Application
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Access Checks for an Application

Performing this step enables either process access checks or full role-based security, depending on what security level you select and whether you enable access checking for individual components.

**To enable access checks for an application**

1.  In the console tree of the Component Services administrative tool, right-click the COM+ application for which you want to enable access checks, and then click **Properties**.

2.  In the application properties dialog box, click the **Security** tab.

3.  Select the **Enforce access checks for this application** check box.

4.  Click **OK**.

> [!Note]  
> As of Windows Server 2003, access checks are enabled by default when creating a COM+ application. Access checks are enabled by default at the application level and disabled by default at the component level. Previously, access checks were disabled by default at the application level and enabled by default at the component level.

 

After enabling access checks, you should select the appropriate security level. See [Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md). Also, you must be sure to define roles and add them to the application. If access checks are enabled but no roles have been added, all calls to the application will fail. See [Defining Roles for an Application](defining-roles-for-an-application.md).

> [!Note]  
> When debugging your application, it might be helpful to disable security so that you can concentrate on other aspects of your program's behavior and design.

 

## Related topics

<dl> <dt>

[Assigning Roles to Components, Interfaces, or Methods](assigning-roles-to-components--interfaces--or-methods.md)
</dt> <dt>

[Configuring Role-Based Security](configuring-role-based-security.md)
</dt> <dt>

[Defining Roles for an Application](defining-roles-for-an-application.md)
</dt> <dt>

[Enabling Access Checks at the Component Level](enabling-access-checks-at-the-component-level.md)
</dt> <dt>

[Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md)
</dt> </dl>

 

 



