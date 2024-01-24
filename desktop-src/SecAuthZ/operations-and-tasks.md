---
description: An operation is a low-level computer action.
ms.assetid: d75bc507-3502-417c-af05-cbff807a5778
title: Operations and Tasks
ms.topic: article
ms.date: 05/31/2018
---

# Operations and Tasks

An operation is a low-level computer action. In the Authorization Manager API, an operation is represented by an [**IAzOperation**](/windows/desktop/api/Azroles/nn-azroles-iazoperation) object. In general, operations are too many in number and too low-level to facilitate administration. Group operations into tasks to simplify administration of authorization policy.

A task is represented by an [**IAzTask**](/windows/desktop/api/Azroles/nn-azroles-iaztask) object and can contain one or more [**IAzOperation**](/windows/desktop/api/Azroles/nn-azroles-iazoperation) objects. An **IAzTask** object can also contain other **IAzTask** objects, so that tasks can be nested. To facilitate administration, an **IAzTask** object should represent a task that a real user wants to perform.

Access to the operations contained by a task can be qualified at run time by a business rule script associated with the [**IAzTask**](/windows/desktop/api/Azroles/nn-azroles-iaztask) object that represents that task. For more information about business rule scripts, see [Business Rules](business-rules.md).

An [**IAzTask**](/windows/desktop/api/Azroles/nn-azroles-iaztask) object can also represent a role definition by setting its [**IsRoleDefinition**](/windows/desktop/api/Azroles/nf-azroles-iaztask-get_isroledefinition) property to **TRUE**. The **Authorization Manager** MMC snap-in user interface then displays that **IAzTask** object as a role. For more information about role definitions, see [Roles](roles.md).

## Related topics

<dl> <dt>

[Defining Operations in C++](defining-operations-in-c--.md)
</dt> <dt>

[Grouping Operations into Tasks in C++](grouping-operations-into-tasks-in-c--.md)
</dt> <dt>

[Grouping Tasks into Roles in C++](grouping-tasks-into-roles-in-c--.md)
</dt> <dt>

[Users and Groups](users-and-groups.md)
</dt> </dl>

 

 



