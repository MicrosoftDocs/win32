---
title: ProcessTokenSidType (principalType) Element
description: Specifies the process security identify (SID) type of the task.
ms.assetid: d9bffa92-c0dc-4332-a29c-7f2710ec34e3
keywords:
- ProcessTokenSidType element Task Scheduler
topic_type:
- apiref
api_name:
- ProcessTokenSidType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ProcessTokenSidType (principalType) Element

Specifies the process security identify (SID) type of the task.

``` syntax
<xs:element name="ProcessTokenSidType"
    type="processTokenSidType"
    maxOccurs="1"
    minOccurs="0"
 />
```

The **ProcessTokenSidType** element is defined by the [**principalType**](taskschedulerschema-principaltype-complextype.md) complex type.

## Parent element



| Element                                                                  | Derived from                                                           | Description                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------|
| [**Principal**](taskschedulerschema-principal-principaltype-element.md) | [**principalType**](taskschedulerschema-principaltype-complextype.md) | Specifies the security credentials for a principal.<br/> |



## Remarks

For C++ development, the process SID type is specified by using the [**IPrincipal2::ProcessTokenSidType**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal2-get_processtokensidtype) property.

## Examples

The following XML defines the process SID type of the task.


```XML
<Principal>
    <GroupId>NT AUTHORITY\LOCAL SERVICE</GroupId>
    <ProcessTokenSidType>None</ProcessTokenSidType>
</Principal>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





