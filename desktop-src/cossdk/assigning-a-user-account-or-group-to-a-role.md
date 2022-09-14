---
description: You can use the Component Services administrative tool to populate a role with user accounts or groups.
ms.assetid: 1cf7dc38-185a-4cc4-8f4c-44b6af4c5f4a
title: Assigning a User Account or Group to a Role
ms.topic: article
ms.date: 05/31/2018
---

# Assigning a User Account or Group to a Role

You can use the Component Services administrative tool to populate a role with user accounts or groups. The preferred way to assign a user account to a role is to assign the user account to a group and then assign the group to the role. Using groups to populate roles makes it easier for you to manage large numbers of users. In the online help for the Computer Management administrative tool, see the topic "Local Users and Groups" for more information about creating groups or assigning a user account to a group.

> [!Note]  
> To allow unauthenticated network users to run a COM+ application, the application roles must include the Anonymous user. Starting with Windows Server 2003, by default, the Anonymous user is not included in the Everyone group.

 

After you have assigned the user account to the appropriate Windows group, follow these steps to assign the Windows group to the role.

**To assign a Windows group to a security role**

1.  In the console tree of the Component Services administrative tool, locate the COM+ application that contains the role to which you want to add the user account or group. Expand the view in the console tree until the application's roles are visible.

2.  Locate the role to which you want to add the user account or group.

    > [!Note]  
    > If the role you are looking for is not in the **Roles** folder, the role has not been added to the application. It must be added to the application by the developer before you can assign user accounts to the role.

     

3.  Right-click the **Users** folder in the role, point to **New**, and then click **User**.

4.  In the **Select Users or Groups** window, in the bottom pane, type the fully qualified name of the user or group you want to add. If you do not know the name, click the **Advanced** button and then click **Find Now** to view a list of users and groups in the selected domain. Select a user or group from the **Name (RDN)** list, and click **OK**.

5.  To add more user accounts or groups, repeat step 4.

6.  When you have finished adding user accounts and groups to the role, click **OK**.

For each user account or group you have assigned to the role, an icon appears in the **Users** folder. The new role membership takes effect the next time the application is started.

 

 



