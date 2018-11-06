---
title: Role Property
description: The Role property describes an object's user interface element. All objects support the Role property.
ms.assetid: f6abf95b-a77a-406d-9ca0-4663adc8245f
ms.topic: article
ms.date: 05/31/2018
---

# Role Property

The **Role** property describes an object's user interface element. All objects support the **Role** property.

In many cases, the object's role is obvious. For example, windows have the [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) role and push buttons have the [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md) role.

The **Role** property is retrieved by calling [**IAccessible::get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole).

## Identifying an Object's Role

Microsoft Active Accessibility provides [role constants](object-roles.md), defined in oleacc.h, that identify common object roles. It is recommended that server developers use these predefined role values. If a predefined role constant is returned, clients use the [**GetRoleText**](/windows/desktop/api/Oleacc/nf-oleacc-getroletexta) function to retrieve a localized string that describes the role.

For animation controls, such as the animation control displayed when copying files, use [**ROLE\_SYSTEM\_ANIMATION**](object-roles.md). Graphics that are occasionally animated are described as [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md) with the [**State**](state-property.md) property set to [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md).

Note that some roles are not easy to describe. For example, a folder's large-icon view allows arbitrary arrangement of icons, so its role could be described as [**ROLE\_SYSTEM\_GROUPING**](object-roles.md). Or, a control that provides items in fixed rows and columns could have the [**ROLE\_SYSTEM\_TABLE**](object-roles.md) role. Since a role is used to communicate the use model to an end user, it is important to use the appropriate role. For example, if your control acts like a button, then use [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md).

 

 




