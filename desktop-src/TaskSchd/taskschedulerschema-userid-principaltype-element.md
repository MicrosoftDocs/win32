---
title: UserId (principalType) Element
description: Specifies the user identifier required to run those tasks associated with the principal.
ms.assetid: 7f3c92bf-c982-4155-9391-862f674a3665
keywords:
- UserId element Task Scheduler
topic_type:
- apiref
api_name:
- UserId
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# UserId (principalType) Element

Specifies the user identifier required to run those tasks associated with the principal.

``` syntax
<xs:element name="UserId"
    type="nonEmptyString"
 />
```

The **UserId** element is defined by the [**principalType**](taskschedulerschema-principaltype-complextype.md) complex type.

## Parent element



| Element                                                                  | Derived from                                                           | Description                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------|
| [**Principal**](taskschedulerschema-principal-principaltype-element.md) | [**principalType**](taskschedulerschema-principaltype-complextype.md) | Specifies the security credentials for a principal.<br/> |



## Remarks

The **UserId** element and the [**LogonType**](taskschedulerschema-logontype-principaltype-element.md) element are used together to define the user required to run those tasks that use this principal.

You cannot specify a user identifier and a group identifier at the same time. Specify either the **UserId** or the [**GroupId**](taskschedulerschema-groupid-principaltype-element.md) element, but not both.

For scripting development, the user identifier is specified using the [**Principal.UserId**](principal-userid.md) property.

For C++ development, the user identifier is specified using the [**IPrincipal::UserId**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_userid) property.

## Examples

The following XML defines a principle using a user identifier.


```XML
<Principal>
    <UserId></UserId>
    <LogonType><LogonType>
    <DisplayName></DisplayName>
 </Principal>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





