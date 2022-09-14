---
title: opcode (TaskEventDefinitionType) Element
description: Contains a task-specific opcode for an event. All of the opcode definitions are assumed to be task-specific for the task that contains the event definitions.
ms.assetid: c7192772-401b-4602-918d-0e0bc4b65ca7
keywords:
- opcode element EventLog
topic_type:
- apiref
api_name:
- opcode
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# opcode (TaskEventDefinitionType) Element

\[Beginning with the message compiler that ships with the Windows 7 version of the Windows SDK, this element is no longer available.\]

Contains a task-specific opcode for an event. All of the opcode definitions are assumed to be task-specific for the task that contains the event definitions.

``` syntax
<xs:element name="opcode">
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
```

The **opcode** element is defined by the [**TaskEventDefinitionType**](eventmanifestschema-taskeventdefinitiontype-complextype.md) complex type.

## Child elements



| Element                                                   | Type                                                                               | Description                                        |
|-----------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------|
| [**event**](eventmanifestschema-event-opcode-element.md) | [**EventDefinitionType**](eventmanifestschema-eventdefinitiontype-complextype.md) | An event that is published with a task.<br/> |



## Attributes



| Name | Type      | Description                                      |
|------|-----------|--------------------------------------------------|
| name | **QName** | The name of the task-specific opcode.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**task (DefinitionType)**](eventmanifestschema-task-definitiontype-element.md)
</dt> </dl>

 

 





