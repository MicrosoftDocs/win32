---
title: principalType Complex Type
description: Defines the attribute, child elements, and sequencing information for the Principal element.
ms.assetid: 0f39d0a7-c9c9-402f-afe1-4378466ac1b6
keywords:
- principalType complex type Task Scheduler
topic_type:
- apiref
api_name:
- principalType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# principalType Complex Type

Defines the attribute, child elements, and sequencing information for the [**Principal**](taskschedulerschema-principal-principaltype-element.md) element.

``` syntax
<xs:complexType name="principalType">
    <xs:all>
        <xs:element name="UserId"
            type="nonEmptyString"
            minOccurs="0"
         />
        <xs:element name="LogonType"
            type="logonType"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="GroupId"
            type="nonEmptyString"
            minOccurs="0"
         />
        <xs:element name="DisplayName"
            type="string"
            minOccurs="0"
         />
        <xs:element name="RunLevel"
            type="runLevelType"
            minOccurs="0"
         />
        <xs:element name="ProcessTokenSidType"
            type="processTokenSidType"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="RequiredPrivileges"
            type="requiredPrivilegesType"
            minOccurs="0"
         />
    </xs:all>
    <xs:attribute name="id"
        type="ID"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                                                             | Type                                                                                     | Description                                                                                                                 |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**DisplayName**](taskschedulerschema-displayname-principaltype-element.md)                        | string                                                                                   | Specifies the name of the principal that is displayed in the Task Scheduler user interface (UI).<br/>                 |
| [**GroupId**](taskschedulerschema-groupid-principaltype-element.md)                                | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md)                  | Specifies the identifier of the user group that is required to run tasks that are associated with the principal.<br/> |
| [**LogonType**](taskschedulerschema-logontype-principaltype-element.md)                            | [**logonType**](taskschedulerschema-logontype-simpletype.md)                            | Specifies the security logon method that is required to run tasks that are associated with the principal.<br/>        |
| [**ProcessTokenSidType**](taskschedulerschema-processtokensidtype-principaltype-element.md)        | [**processTokenSidType**](taskschedulerschema-processtokensidtype-simpletype.md)        | Specifies the types of process security identifier (SID) that can be used by tasks.<br/>                              |
| [**RequiredPrivileges**](taskschedulerschema-requiredprivileges-requiredprivilegestype-element.md) | [**requiredPrivilegesType**](taskschedulerschema-requiredprivilegestype-complextype.md) | Specifies the required privileges to run the task.<br/>                                                               |
| [**RunLevel**](taskschedulerschema-runlevel-principaltype-element.md)                              | [**runLevelType**](taskschedulerschema-runleveltype-simpletype.md)                      | Specifies the permission level that the task will be run at.<br/>                                                     |
| [**UserId**](taskschedulerschema-userid-principaltype-element.md)                                  | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md)                  | Specifies the user identifier that is required to run tasks that are associated with the principal.<br/>              |



## Attributes



| Name | Type | Description                                           |
|------|------|-------------------------------------------------------|
| id   | ID   | Specifies the identifier of the principal.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





