---
Description: Roles serve two different purposes in Authorization Manager.
ms.assetid: 02acf473-b072-4814-92e1-47a32baae4fc
title: Roles
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Roles

Roles serve two different purposes in Authorization Manager. A role is a set of tasks or operations to which a category of users requires access, and it is also a set of users and groups that fit into that category.

-   [Roles as Sets of Tasks](#roles-as-sets-of-tasks)
-   [Roles as Sets of Users and Groups](#roles-as-sets-of-users-and-groups)
-   [Related topics](#related-topics)

## Roles as Sets of Tasks

An authorization policy assigns [**IAzTask**](/windows/win32/Azroles/nn-azroles-iaztask?branch=master) objects to an [**IAzRole**](/windows/win32/Azroles/nn-azroles-iazrole?branch=master) object to create sets of tasks. All users and groups assigned to that **IAzRole** object then have permission to access all operations contained by those **IAzTask** objects.

Because an [**IAzRole**](/windows/win32/Azroles/nn-azroles-iazrole?branch=master) object represents both a set of tasks and a set of users and groups that have access to those tasks, Authorization Manager provides a way to create role definitions that can be assigned to more than one **IAzRole** object. An [**IAzTask**](/windows/win32/Azroles/nn-azroles-iaztask?branch=master) object can contain other **IAzTask** objects. You can then use that **IAzTask** object as a role definition by assigning it to one or more **IAzRole** objects. Set the [**IsRoleDefinition**](/windows/win32/Azroles/nf-azroles-iaztask-get_isroledefinition?branch=master) property of the **IAzTask** object to **TRUE** to cause the **Authorization Manager** MMC snap-in user interface to display the **IAzTask** object as a role.

## Roles as Sets of Users and Groups

Assign users and groups to an [**IAzRole**](/windows/win32/Azroles/nn-azroles-iazrole?branch=master) object to grant those users and groups access to the tasks assigned to that **IAzRole** object by calling the [**AddMember**](/windows/win32/Azroles/nf-azroles-iazrole-addmember?branch=master) or [**AddMemberName**](/windows/win32/Azroles/nf-azroles-iazrole-addmembername?branch=master) method. Assign existing application groups, represented by [**IAzApplicationGroup**](/windows/win32/Azroles/nn-azroles-iazapplicationgroup?branch=master) objects, to an **IAzRole** object by calling the [**AddAppMember**](/windows/win32/Azroles/nf-azroles-iazrole-addappmember?branch=master) method. All users and groups assigned to the **IAzRole** object have access to the tasks and operations assigned to that role. For more information about application groups, see [Users and Groups](users-and-groups.md).

## Related topics

<dl> <dt>

[Grouping Tasks into Roles in C++](grouping-tasks-into-roles-in-c--.md)
</dt> <dt>

[Defining Groups of Users in C++](defining-groups-of-users-in-c--.md)
</dt> <dt>

[Adding Users to an Application Group in C++](adding-users-to-an-application-group-in-c--.md)
</dt> </dl>

 

 



