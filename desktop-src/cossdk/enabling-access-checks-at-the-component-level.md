---
description: Enabling Access Checks at the Component Level
ms.assetid: b9ff5296-9076-4492-833c-7402b7090f8f
title: Enabling Access Checks at the Component Level
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Access Checks at the Component Level

If your application includes a component that does not need security checks, you might decide to disable role checks for that component to improve performance. Or when debugging, it might be helpful to disable security so that you can concentrate on other aspects of program functionality.

By default, when you install a component, component-level access checks are enabled. However, this takes effect only when [application-level access checks](enabling-access-checks-for-an-application.md) are enabled and when the [security level](setting-a-security-level-for-access-checks.md) is set to **Perform access checks at the process and component level**.

**To enable or disable access checks at the component level**

1.  In the console tree of the Component Services administrative tool, locate the COM+ application that contains the component for which you want to disable (or enable) role checks. Expand the view in the tree to view the components in the **Components** folder.

2.  Right-click the component for which you want to enable role checks, and then click **Properties**.

3.  In the component properties dialog box, click the **Security** tab.

4.  Select **Enforce component level access checks** to enforce component-level checks.

5.  Click **OK**.

The new setting will take effect the next time the application is started.

> [!Note]  
> As of Windows Server 2003, component-level access checks are disabled by default when creating a COM+ application. Access checks are enabled by default at the application level and disabled by default at the component level. Previously, access checks were disabled by default at the application level and enabled by default at the component level.

 

## Related topics

<dl> <dt>

[Assigning Roles to Components, Interfaces, or Methods](assigning-roles-to-components--interfaces--or-methods.md)
</dt> <dt>

[Configuring Role-Based Security](configuring-role-based-security.md)
</dt> <dt>

[Defining Roles for an Application](defining-roles-for-an-application.md)
</dt> <dt>

[Enabling Access Checks for an Application](enabling-access-checks-for-an-application.md)
</dt> <dt>

[Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md)
</dt> </dl>

 

 



