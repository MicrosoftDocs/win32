---
title: TaskEventDefinitionType Complex Type
description: Defines a task-specific event that your provider can log. | TaskEventDefinitionType Complex Type
ms.assetid: f0329728-e7b5-4161-a30f-78b81a7b6812
keywords:
- TaskEventDefinitionType complex type EventLog
topic_type:
- apiref
api_name:
- TaskEventDefinitionType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TaskEventDefinitionType Complex Type

\[Beginning with the message compiler that ships with the Windows 7 version of the Windows SDK, the TaskEventDefinitionType complex type is no longer available. Instead use task-specific opcodes to provide the same functionality.\]

Defines a task-specific event that your provider can log.

``` syntax
<xs:complexType name="TaskEventDefinitionType">
    <xs:sequence>
        <xs:element name="opcode"
            maxOccurs="unbounded"
        >
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="event"
                        type="EventDefinitionType"
                        maxOccurs="unbounded"
                     />
                </xs:sequence>
                <xs:attribute name="name"
                    type="QName"
                    use="required"
                 />
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="name"
        type="anyURI"
        use="required"
     />
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                                      | Type                                                                               | Description                                             |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------|
| **event**                                                                    | [**EventDefinitionType**](eventmanifestschema-eventdefinitiontype-complextype.md) | A task-specific event published with a task.<br/> |
| [**opcode**](eventmanifestschema-opcode-taskeventdefinitiontype-element.md) |                                                                                    | A task-specific opcode that for an event. <br/>   |



## Attributes



| Name | Type      | Description                                      |
|------|-----------|--------------------------------------------------|
| name | **QName** | The name of the task-specific opcode.<br/> |
| name | anyURI    | The name of the task.<br/>                 |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





