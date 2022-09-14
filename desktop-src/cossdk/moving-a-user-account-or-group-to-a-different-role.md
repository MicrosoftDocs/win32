---
description: You can remove user accounts or groups from a role when the users or members of the groups should no longer be given access to the application resources to which the role is assigned.
ms.assetid: d2cfa5cb-a143-41de-9aa2-7af7fce10ed7
title: Moving a User Account or Group to a Different Role
ms.topic: article
ms.date: 05/31/2018
---

# Moving a User Account or Group to a Different Role

You can remove user accounts or groups from a role when the users or members of the groups should no longer be given access to the application resources to which the role is assigned.

**To remove a user account or group from a role**

1.  In the console tree of the Component Services administrative tool, locate the COM+ application that contains the role you are interested in. Expand the view in the console tree until the users for the role are visible.

2.  Right-click the user account or group you want to remove, and then click **Delete**.

3.  When prompted by the **Confirm Item Delete** dialog box, click **Yes** to delete the user account or group.

The user account or group that you have removed from the role no longer appears in the **Users** folder. The new role membership takes effect the next time the application is started. If you have made changes to the **System Application**, you must restart the computer for the changes to take effect.

 

 



