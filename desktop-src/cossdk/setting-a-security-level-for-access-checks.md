---
description: After you have enabled access checks, for your COM+ application, you must select the level at which you wish to have access checks performed.
ms.assetid: 9c044add-7761-4378-b7eb-bf4e84e913b3
title: Setting a Security Level for Access Checks
ms.topic: article
ms.date: 05/31/2018
---

# Setting a Security Level for Access Checks

After you have enabled [access checks](enabling-access-checks-for-an-application.md), for your COM+ application, you must select the level at which you wish to have access checks performed.

**To select a security level**

1.  In the console tree of the Component Services administrative tool, right-click the COM+ application for which you want to enable access checks, and then click **Properties**.

2.  In the application properties dialog box, click the **Security** tab.

3.  Under **Security level**, select one of the following:

    -   **Perform access checks only at the process level**— This setting indicates that users in roles that are assigned to the application will be added to the process security descriptor. This has the following effects and implications:

        Fine-grained role checking is turned off at the component, method, and interface levels. Security checks are performed only at the application level.

        The security property is not included on the context for any objects running within the application. This can potentially affect how objects are activated. See [Security Context Property](security-context-property.md).

        The security call context will not be made available. Programmatic security that relies on security call context information will not function. See [Security Call Context Information](security-call-context-information.md).

    -   **Perform access checks at the process and component level**—This setting indicates that process-level security descriptor checks and full role-based security checks will be performed. This has the following effects and implications:

        To enable role checking for particular components, you must [enable access checks at the component level](enabling-access-checks-at-the-component-level.md).

        The security property is included on the context for any objects running within the application. This can potentially affect how objects are activated. See [Security Context Property](security-context-property.md).

        The security call context is available. Programmatic role-based security is enabled. See [Security Call Context Information](security-call-context-information.md).

        > [!Note]  
        > For COM+ library applications, you must choose to check both at process and at component levels for any meaningful access checking to work. Library applications rely on the host process for process-level security. You can determine how the library application interacts with authentication performed by the host process by [setting authentication](enabling-authentication-for-a-library-application.md). For more information, see [Library Application Security](library-application-security.md).

         

4.  Click **OK**.

The next time the application is started, security will automatically be checked at the specified level. Only users assigned to roles assigned to the application will be given access to the application.

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

[Enabling Access Checks at the Component Level](enabling-access-checks-at-the-component-level.md)
</dt> </dl>

 

 



