---
title: GroupId (principalType) Element
description: Specifies the identifier of the user group required to run those tasks associated with the principal.
ms.assetid: 1e576c31-79a9-42d4-b497-74412e464d60
keywords:
- GroupId element Task Scheduler
topic_type:
- apiref
api_name:
- GroupId
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GroupId (principalType) Element

Specifies the identifier of the user group required to run those tasks associated with the principal.

``` syntax
<xs:element name="GroupId"
    type="nonEmptyString"
 />
```

The **GroupId** element is defined by the [**principalType**](taskschedulerschema-principaltype-complextype.md) complex type.

## Parent element



| Element                                                                  | Derived from                                                           | Description                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------|
| [**Principal**](taskschedulerschema-principal-principaltype-element.md) | [**principalType**](taskschedulerschema-principaltype-complextype.md) | Specifies the security credentials for a principal.<br/> |



## Remarks

You cannot specify a group identifier and a user identifier at the same time. Specify either the [**UserId**](taskschedulerschema-userid-principaltype-element.md) or **GroupId** elements, but not both.

For script development, the group identifier of the principal is specified using the [**Principal.GroupId**](principal-groupid.md) property.

For C++ development, the group identifier of the principal is specified using the [**IPrincipal::GroupId**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_groupid) property.

## Examples

For a complete example of the XML for a task that uses this element, see [Logon Trigger Example (XML)](logon-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





