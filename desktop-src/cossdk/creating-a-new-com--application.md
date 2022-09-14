---
description: Creating a New COM+ Application
ms.assetid: eec4e871-36c2-4e60-9808-1400efcfc60c
title: Creating a New COM+ Application
ms.topic: article
ms.date: 05/31/2018
---

# Creating a New COM+ Application

Creating a new COM+ application requires two basic steps, as follows:

-   Creating an empty COM+ application (described below).
-   Adding components to the application. (See [Installing New Components](installing-new-components.md) and [Importing Components](importing-components.md).)

**To create an empty COM+ application**

1.  In the console tree of the Component Services administrative tool, select the computer on which you want to create an application.

2.  Select the **COM+ Applications** folder for that computer.

3.  On the **Action** menu, point to **New**, and then click **Application**. You can also right-click the **COM+ Applications** folder, point to **New**, and then click **Application**.

4.  On the **Welcome** page of the COM+ Application Install Wizard, click **Next**, and then in the **Install or Create a New Application** dialog box, click **Create an empty application**.

5.  In the box provided, type a name for the new application. (Note that the following special characters cannot be used in an application name: \\, /, ~, !, @, \#, %, ^, &, \*, (, ), \|, }, {, \], \[, ', ", >, <, ., ?, :, and ;.) Under **Activation type**, click **Library application** or **Server application**. Click **Next**.

    > [!Note]  
    > A server application runs in its own process. Server applications can support all COM+ services. A library application runs in the process of the client that creates it. Library applications can use role-based security but do not support remote access or queued components.

     

6.  In the **Set Application Identity** dialog box, choose an identity under which the application will run. If you select **This user**, type the user name and password. You must also retype the password in the **Confirm password** box. Click **Next**. (The default selection for application identity is **Interactive User**. The interactive user is the user logged on to the server computer at any given time. You can select a different user by selecting **This user** and entering a specific user or group.)

    > [!Note]  
    > The **Set Application Identity** dialog box appears only if you selected **Server application** for the new application's activation type in the COM Application Install Wizard's preceding dialog box. The identity property is not used for library applications.

     

7.  In the **Add Application Roles** dialog box, add any roles you want to associate with the application. By default, only the **CreatorOwner** role is defined. For information on roles, see [Role-Based Security Administration](role-based-security-administration.md).

8.  In the **Add Users to Roles** dialog box, populate each role you created in the last step with the users, groups, or built-in security principals to which you want to grant the privileges associated with that role. By default, the interactive user is placed in the **CreatorOwner** role.

9.  Click **Finish**.

The new application will now be displayed under the **COM+ Applications** folder in the console tree of the Component Services administrative tool.

> [!Note]  
> As of Windows Server 2003, access checks are enabled by default when creating a COM+ application. In previous versions, access checks were disabled by default at the application level. The result is that by default, access to a COM+ application is allowed only to users that are in the roles associated with the application. (See [Role-Based Security Administration](role-based-security-administration.md).) Alternatively, you can allow access to all users by disabling access checks on a COM+ application. (See [Enabling Access Checks for an Application](enabling-access-checks-for-an-application.md).)

 

## Related topics

<dl> <dt>

[Copying Components](copying-components.md)
</dt> <dt>

[Deleting a COM+ Application](deleting-a-com--application.md)
</dt> <dt>

[Importing Components](importing-components.md)
</dt> <dt>

[Installing New Components](installing-new-components.md)
</dt> <dt>

[Moving Components](moving-components.md)
</dt> <dt>

[Removing a Component from a COM+ Application](removing-a-component-from-a-com--application.md)
</dt> </dl>

 

 



