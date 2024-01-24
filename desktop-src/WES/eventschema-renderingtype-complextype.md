---
title: RenderingInfoType Complex Type
description: Defines the rendered messages for the event.
ms.assetid: 85a4cfc6-6277-4af8-af4e-cae3bd3aac13
keywords:
- RenderingInfoType complex type EventLog
topic_type:
- apiref
api_name:
- RenderingInfoType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RenderingInfoType Complex Type

Defines the rendered messages for the event.

``` syntax
<xs:complexType name="RenderingInfoType">
    <xs:sequence>
        <xs:element name="Message"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Level"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Opcode"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Task"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Channel"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Provider"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Keywords"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="Keyword"
                        type="string"
                        minOccurs="0"
                     />
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:any
            minOccurs="0"
            maxOccurs="unbounded"
            processContents="lax"
            namespace="##other"
         />
    </xs:sequence>
    <xs:attribute name="Culture"
        type="language"
        use="required"
     />
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                             | Type   | Description                                                                   |
|---------------------------------------------------------------------|--------|-------------------------------------------------------------------------------|
| [**Channel**](eventschema-task-renderingtype-element.md)           | string | The rendered message string of the channel specified in the event.<br/> |
| [**Keyword**](eventschema-keyword-keywords-element.md)             | string | The rendered message string of a keyword specified in the event.<br/>   |
| [**Keywords**](eventschema-keywords-renderingtype-element.md)      |        | A list of rendered keywords.<br/>                                       |
| [**Level**](eventschema-level-renderingtype-element.md)            | string | The rendered message string of the level specified in the event.<br/>   |
| [**Message**](eventschema-message-renderingtype-element.md)        | string | The rendered message string of the event.<br/>                          |
| [**Opcode**](eventschema-opcode-renderingtype-element.md)          | string | The rendered message string of the opcode specified in the event.<br/>  |
| [**Provider**](eventschema-publisher-renderinginfotype-element.md) | string | The rendered message string for the provider.<br/>                      |
| [**Task**](eventschema-task-renderingtype-element.md)              | string | The rendered message string of the task specified in the event.<br/>    |



## Attributes



| Name    | Type     | Description                                                                                                      |
|---------|----------|------------------------------------------------------------------------------------------------------------------|
| Culture | language | The language name (for example, en-US) that identifies the locale used to render the message strings.<br/> |



## Remarks

Only events that have been collected using the [Windows Event Collector](/windows/desktop/WEC/windows-event-collector) service will contain this section.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

