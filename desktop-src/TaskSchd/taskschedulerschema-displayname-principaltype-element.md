---
title: DisplayName (principalType) Element
description: Specifies the name of the principal that is displayed in the Task Scheduler UI.
ms.assetid: a8640cc9-fc16-4e73-9f0c-1ebff338fb84
keywords:
- DisplayName element Task Scheduler
topic_type:
- apiref
api_name:
- DisplayName
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DisplayName (principalType) Element

Specifies the name of the principal that is displayed in the Task Scheduler UI.

``` syntax
<xs:element name="DisplayName"
    type="string"
 />
```

The **DisplayName** element is defined by the [**principalType**](taskschedulerschema-principaltype-complextype.md) complex type.

## Parent element



| Element                                                                  | Derived from                                                           | Description                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------|
| [**Principal**](taskschedulerschema-principal-principaltype-element.md) | [**principalType**](taskschedulerschema-principaltype-complextype.md) | Specifies the security credentials for a principal.<br/> |



## Remarks

For scripting development, the display name of the principal is specified using the [**Principal.DisplayName**](principal-displayname.md) property.

For C++ development, the display name of the principal is specified using the [**IPrincipal::DisplayName**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_displayname) property.

## Examples

The following XML defines a using a group identifier and a display name.


```XML
<Principal>
    <GroupId></GroupId>
    <DisplayName></DisplayName>
 </Principal>
```



The following XML defines a principal using a user identifier and a display name.


```XML
<Principal>
    <UserId></UserId>
    <LogonType></LogonType>
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

 

 





