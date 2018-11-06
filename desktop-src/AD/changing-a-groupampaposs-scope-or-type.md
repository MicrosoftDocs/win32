---
title: Changing a Group's Scope or Type
description: This topic shows how to change a group's scope or type in native mode domains.
ms.assetid: bdae7bc9-072a-4063-9562-8e0fcb1b7937
ms.tgt_platform: multiple
keywords:
- groups AD , changing a group's scope or type
ms.topic: article
ms.date: 05/31/2018
---

# Changing a Group's Scope or Type

Changing a group scope or type is not allowed in mixed-mode domains. However, the following conversions are allowed in native-mode domains:

Global group to universal group: This is only allowed if the global group is not a member of another global group.

Domain local group to universal group: The domain local group being converted cannot contain another domain local group.

Universal group to global or domain local group: For conversion to global group, the universal group being converted cannot contain users or global groups from another domain. For conversion to domain local group, the universal group being converted cannot be a member of any universal group or a domain local group from another domain.

In native mode, a group type can be converted freely between security groups and distribution groups.

Be aware that if a group is used to set access control, changing the scope or type can affect the access control entries (ACEs) that contain that group. The security system will ignore ACEs that contain groups that are not security groups.

 

 




