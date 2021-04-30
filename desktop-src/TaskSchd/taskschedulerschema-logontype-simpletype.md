---
title: logonType Simple Type
description: Defines the possible values of the LogonType element.
ms.assetid: a08cd549-f45c-4278-a428-1ffe91b67564
keywords:
- logonType simple type Task Scheduler
topic_type:
- apiref
api_name:
- logonType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# logonType Simple Type

Defines the possible values of the [**LogonType**](taskschedulerschema-logontype-principaltype-element.md) element.

``` syntax
<xs:simpleType name="logonType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="S4U"
         />
        <xs:enumeration
            value="Password"
         />
        <xs:enumeration
            value="InteractiveToken"
         />
        <xs:enumeration
            value="InteractiveTokenOrPassword"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **logonType** simple type defines the following values.



| Value                      | Description                                                                                                                                                                                                                                                                                                                                                |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S4U                        | User must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to either the network or encrypted files.<br/>                                                                                                                                                          |
| Password                   | User must log on using a password.<br/>                                                                                                                                                                                                                                                                                                              |
| InteractiveToken           | User must already be logged on. The task will be run only in an existing interactive session.<br/>                                                                                                                                                                                                                                                   |
| InteractiveTokenOrPassword | No longer in use; currently identical to Password.<br/> **Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows Server 2012 R2, Windows 8, Windows Server 2012, Windows Vista and Windows Server 2008:** The task will be run in an existing interactive session or the user must log on using a password.<br/> <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Simple Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





