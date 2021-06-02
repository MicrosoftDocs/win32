---
title: EventDataType Complex Type
description: Defines the event data items and structures that contains the event data.
ms.assetid: 9531163f-34ce-4673-b2d8-636042915c73
keywords:
- EventDataType complex type EventLog
topic_type:
- apiref
api_name:
- EventDataType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EventDataType Complex Type

Defines the event data items and structures that contains the event data.

``` syntax
<xs:complexType name="EventDataType">
    <xs:sequence>
        <xs:choice
            minOccurs="0"
            maxOccurs="unbounded"
        >
            <xs:element name="Data"
                type="DataType"
             />
            <xs:element name="ComplexData"
                type="ComplexDataType"
             />
        </xs:choice>
        <xs:element name="Binary"
            type="hexBinary"
            minOccurs="0"
         />
    </xs:sequence>
    <xs:attribute name="Name"
        type="string"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                              | Type                                                               | Description                                                                                          |
|----------------------------------------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**Binary**](eventschema-binary-eventdatatype-element.md)           | hexBinary                                                          | A binary data blob for events that are written using [Event Logging](/windows/desktop/EventLog/event-logging).<br/> |
| [**ComplexData**](eventschema-complexdata-eventdatatype-element.md) | [**ComplexDataType**](eventschema-complexdatatype-complextype.md) | A structure that is defined in the template for the event.<br/>                                |
| [**Data**](eventschema-data-eventdatatype-element.md)               | [**DataType**](eventschema-datafieldtype-complextype.md)          | A top-level data item that is defined in the template for the event.<br/>                      |



## Attributes



| Name | Type   | Description                                                       |
|------|--------|-------------------------------------------------------------------|
| Name | string | The name of the template that contains the data items.<br/> |



## Remarks

The [**EvtRender**](/windows/desktop/api/WinEvt/nf-winevt-evtrender) function renders arrays and structures as binary blobs.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

