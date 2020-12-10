---
title: Principal (principalType) Element
description: Specifies the security credentials for a principal.
ms.assetid: 4ba65976-98d2-4329-80f0-566fac2e9fda
keywords:
- Principal element Task Scheduler
topic_type:
- apiref
api_name:
- Principal
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Principal (principalType) Element

Specifies the security credentials for a principal. These credentials define the security context that a task runs under.

``` syntax
<xs:element name="Principal"
    type="principalType"
 />
```

The **Principal** element is defined by the [**principalType**](taskschedulerschema-principaltype-complextype.md) complex type.

## Parent element



| Element                                                               | Derived from                                                             | Description                                                            |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**Principals**](taskschedulerschema-principals-tasktype-element.md) | [**principalsType**](taskschedulerschema-principalstype-complextype.md) | Specifies the security principals associated with the task.<br/> |



## Child elements



| Element                                                                      | Type                                                          | Description                                                                                                |
|------------------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**DisplayName**](taskschedulerschema-displayname-principaltype-element.md) | **string**                                                    | Specifies the name of the principal that is displayed in the Task Scheduler UI.<br/>                 |
| [**GroupId**](taskschedulerschema-groupid-principaltype-element.md)         | **string**                                                    | Specifies the identifier of the user group required to run tasks associated with the principal.<br/> |
| [**LogonType**](taskschedulerschema-logontype-principaltype-element.md)     | [**logonType**](taskschedulerschema-logontype-simpletype.md) | Specifies the security logon method required to run those tasks associated with the principal.<br/>  |
| [**UserId**](taskschedulerschema-userid-principaltype-element.md)           | **string**                                                    | Specifies the user identifier required to run tasks associated with the principal.<br/>              |



## Attributes



| Name | Type | Description                                        |
|------|------|----------------------------------------------------|
| Id   | ID   | Identifier of the principal definition.<br/> |



## Remarks

For scripting development, the security credentials for a principal are specified using the [**Principal**](principal.md) object.

For C++ development, the security credentials for a principal are specified using the [**IPrincipal**](/windows/desktop/api/taskschd/nn-taskschd-iprincipal) interface.

The child elements listed above are defined by the [**principalType**](taskschedulerschema-principaltype-complextype.md) complex type. For sequencing information for these child elements, see [**principalType**](taskschedulerschema-principaltype-complextype.md).

## Examples

The following XML defines a principal with a user identifier.


```XML
<Principals>
    <Principal>
        <UserId></UserId>
        <LogonType><LogonType>
        <DisplayName></DisplayName>
    </Principal>
</Principals>
```



The following XML defines a principal with a group identifier.


```XML
<Principals>
    <Principal>
        <GroupId></GroupId>
        <DisplayName></DisplayName>
    </Principal>
</Principals>
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

 

 





