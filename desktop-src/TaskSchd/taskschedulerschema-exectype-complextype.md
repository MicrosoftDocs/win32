---
title: execType Complex Type
description: Defines the child elements and sequencing information of the Exec (actionGroup) element.
ms.assetid: ab23801a-453d-4fab-8584-30c5c9d57dff
keywords:
- execType complex type Task Scheduler
topic_type:
- apiref
api_name:
- execType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# execType Complex Type

Defines the child elements and sequencing information of the [**Exec (actionGroup)**](taskschedulerschema-exec-actiongroup-element.md) element.

``` syntax
<xs:complexType name="execType">
    <xs:complexContent>
        <xs:extension
            base="actionBaseType"
        >
            <xs:all>
                <xs:element name="Command"
                    type="pathType"
                 />
                <xs:element name="Arguments"
                    type="string"
                    minOccurs="0"
                 />
                <xs:element name="WorkingDirectory"
                    type="pathType"
                    minOccurs="0"
                 />
            </xs:all>
        </xs:extension>
    </xs:complexContent>
</xs:complexType>
```

## Child elements



| Element                                                                           | Type                                                        | Description                                                                                                  |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**Arguments**](taskschedulerschema-arguments-exectype-element.md)               | **string**                                                  | Specifies the arguments associated with the command-line operation. <br/>                              |
| [**Command**](taskschedulerschema-command-exectype-element.md)                   | [**pathType**](taskschedulerschema-pathtype-simpletype.md) | Specifies the executable file or document to be run.<br/>                                              |
| [**WorkingDirectory**](taskschedulerschema-workingdirectory-exectype-element.md) | [**pathType**](taskschedulerschema-pathtype-simpletype.md) | Specifies the directory where either the executable or those files used by the executable exists.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





