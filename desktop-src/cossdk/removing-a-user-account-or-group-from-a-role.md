---
description: If a users privileges change or if roles are added to an application, you can move an account from one role to another role.
ms.assetid: 2d81a45a-9762-48b9-8395-3c3a4dcd5e8c
title: Removing a User Account or Group from a Role
ms.topic: article
ms.date: 05/31/2018
---

# Removing a User Account or Group from a Role

If a user's privileges change or if roles are added to an application, you can move an account from one role to another role. To move a user account or group of users from one role to another, you must remove the user account or group from its current role and then assign it to the new role.

**To move a user account or group from one role to another**

1.  Remove the user account or group from the role that it should no longer belong to, as follows:

    1.  In the console tree of the Component Services administrative tool, locate the COM+ application that contains the role you are interested in. Expand the view in the console tree until the users for the role are visible.

    2.  Right-click the user account or group you want to remove, and then click **Delete**.

    3.  When prompted by the **Confirm Item Delete** dialog box, click **Yes** to delete the user account or group.

    The user account or group that you have removed from the role no longer appears in the **Users** folder.

2.  Assign the user account or group you have removed to the roles that the user or group should be assigned to, as follows:

    1.  In the console tree of the Component Services administrative tool, locate the COM+ application that contains the role to which you want to add the user account or group. Expand the view in the console tree until the application's roles are visible.

    2.  Locate the role to which you want to add the user account or group.

        > [!Note]  
        > If the role you are looking for is not in the **Roles** folder, the role has not been added to the application. It must be added to the application by the developer before you can assign user accounts to the role.

         

    3.  Right-click the **Users** folder in the role, point to **New**, and then click **User**.

    4.  In the **Select Users or Groups** window, in the bottom pane, type the fully qualified name of the user or group you want to add. If you do not know the name, click the **Advanced** button and then click **Find Now** to view a list of users and groups in the selected domain. Select a user or group from the **Name (RDN)** list and click **OK**.

    5.  When you have finished adding the user account or group to the role, click **OK**.

    For each user account or group you have assigned to the role, an icon appears in the **Users** folder.

The changed role membership for the user account or group takes effect the next time the application is started.

 

 



