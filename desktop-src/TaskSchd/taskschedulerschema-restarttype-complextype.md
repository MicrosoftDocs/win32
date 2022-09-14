---
title: restartType Complex Type
description: Defines the child elements and sequence information for the RestartOnFailure element.
ms.assetid: 3a192955-8a33-42b9-a974-faa9a3789f58
keywords:
- restartType complex type Task Scheduler
topic_type:
- apiref
api_name:
- restartType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# restartType Complex Type

Defines the child elements and sequence information for the [RestartOnFailure](taskschedulerschema-restartonfailure-settingstype-element.md) element.

``` syntax
<xs:complexType name="restartType">
    <xs:all>
        <xs:element name="Interval">
            <xs:simpleType>
                <xs:restriction
                    base="duration"
                >
                    <xs:minInclusive
                        value="PT1M"
                     />
                    <xs:maxInclusive
                        value="P31D"
                     />
                </xs:restriction>
            </xs:simpleType>
        </xs:element>
        <xs:element name="Count">
            <xs:simpleType>
                <xs:restriction
                    base="unsignedByte"
                >
                    <xs:minInclusive
                        value="1"
                     />
                </xs:restriction>
            </xs:simpleType>
        </xs:element>
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                              | Type | Description                                        |
|----------------------------------------------------------------------|------|----------------------------------------------------|
| [**Count**](taskschedulerschema-count-restarttype-element.md)       |      | Number of attempts to restart the task.<br/> |
| [**Interval**](taskschedulerschema-interval-restarttype-element.md) |      | How long to try to start the task.<br/>      |



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

 

 





