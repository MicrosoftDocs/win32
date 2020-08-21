---
title: What Application and Service Developers Need to Know About Groups
description: When developing an application or service, you can use groups to delegate administration or control access to the application or service as a whole or part.
ms.assetid: 19e189a5-2880-4b45-84c8-e7b542c4fbb6
ms.tgt_platform: multiple
keywords:
- What Application and Service Developers Need to Know About Groups
- groups AD , information for application and service developers
ms.topic: article
ms.date: 05/31/2018
---

# What Application and Service Developers Need to Know About Groups

When developing an application or service, you can use groups to delegate administration or control access to the application or service as a whole or part. For example, an application can control who can perform various administrative operations. To do this, create ACEs that grant specified access rights to the appropriate groups. It is good programming practice to have an ACE that grants access to a group than to have several ACEs that grant access to individual users or computers.

It is recommended that applications use the following guidelines when using groups:

-   Do not create dependencies on hard-coded groups, which can create complications if the group is deleted or moved.
-   Avoid using built-in groups unless the function of the group provides the specific needs for the application. For example, do not require that a user be a member of the Administrators group just to provide the user with permission to create a computer account. Doing this provides the user with permissions and privileges that they may not need, which can cause security vulnerability. Instead, you should create a new security group that has the specific permissions required and add the user to this new group.
-   When creating new groups, keep in mind the following recommendations:
    -   Protect the group by setting ACEs that control who can add or remove members.
    -   Use global groups if they are used for access control on objects in Active Directory Domain Services.
    -   Use universal groups only if necessary (member data is required globally using global catalog; group can contain any user/group). If you do use universal groups, place global groups in the universal group and add/remove users from the global group. Avoid excess change to universal groups for replication efficiency.
-   Do not use group membership for access control. Instead, use an ACE and control access by having the system perform an access check.

To control access to operations that do not fit within the predefined access rights for objects in Active Directory Domain services, use the control access rights feature of access control in Windows 2000. For more information, see [**ADS\_RIGHTS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_rights_enum).

**To use a control access right to control the right to perform an operation**

1.  Create a control access right that defines the type of access to the application or service. For more information, see [Control Access Rights](control-access-rights.md).
2.  Create an object in Active Directory Domain Services that represents the application, service, or resource.
3.  Add object ACEs to the DACL in the object security descriptor to grant or deny users or groups the control access right on that object. For more information, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).
4.  When a user attempts to perform the protected operation, your application or service uses the [**AccessCheckByTypeResultList**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-accesscheckbytyperesultlist) function to determine whether the control access right is granted to the user. For more information, see [Checking a Control Access Right in an Object's ACL](checking-a-control-access-right-in-an-objectampaposs-acl.md).
5.  Based on the result of the access check on the object, your application or service can grant or deny the user access to the application or service.

A service application could also create a group whose members would be the various service instances. For example, a service with instances installed on multiple computers throughout an enterprise might have a common log file that all service instances write to. The service installation program creates the log file and uses a DACL to grant access only to members of a group. The group members would be the user accounts under which the various service instances are running, or if the services run under the LocalSystem account, the members would be the computer accounts of the host servers.

 

 