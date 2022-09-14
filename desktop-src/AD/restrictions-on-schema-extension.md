---
title: Restrictions on Schema Extension
description: In order to reduce the possibility of schema changes by one application breaking other applications and to maintain schema consistency, Active Directory Domain Services enforce restrictions on the type of schema changes that an application or user is allowed to make.
ms.assetid: 26254eb9-5dd9-414b-a398-be2a7f3b0279
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Restrictions on Schema Extension

In order to reduce the possibility of schema changes by one application breaking other applications and to maintain schema consistency, Active Directory Domain Services enforce restrictions on the type of schema changes that an application or user is allowed to make.

The restrictions are imposed only on modification of existing schema objects. The schema is categorized into two categories. The schema objects that ship with Windows 2000 in the base schema belong to Category 1. Any schema objects added later by other applications or users through dynamic schema extension belong to Category 2. The category of a schema object can be determined by the 0x10 bit set in the **systemFlags** attribute on the **classSchema** object. This bit is only set on Category 1 objects, and cannot be altered, nor can it be set on any Category 2 object.

The **systemFlags** attribute is used internally by Active Directory Domain Services to identify special characteristics of "infrastructure" objects in the base schema. In addition to identifying Category 1 objects, **systemFlags** controls whether an object can be moved, deleted, or renamed. These operations are prevented for objects that Windows 2000 depends on to run.

On any schema objects, Category 1 or 2, Active Directory Domain Services impose the following restrictions:

-   You cannot add a new **mustContain** to a class (directly or through inheritance by adding an auxiliary class).
-   You cannot delete any **mustContain** of the class (directly or through inheritance).

In addition, the following additional restrictions are imposed on Category 1 schema objects:

-   You cannot change the following attributes of a Category 1 attribute:

    -   **rangeLower** and **rangeUpper** (value range).
    -   **attributeSecurityGuid** (determines which property set the attribute belongs in, if any).

-   You cannot change the **defaultObjectCategory** of a Category 1 class.
-   You cannot change the **objectCategory** of any instance of a Category 1 class.
-   You cannot make a Category 1 class or attribute defunct.
-   You cannot change the **lDAPDisplayName** of a Category 1 class or attribute.
-   You cannot rename a Category 1 class or attribute.

 

 




