---
title: TimeCreated (SystemPropertiesType) Element
description: The time stamp that identifies when the event was logged.
ms.assetid: 16b2b71b-078e-4862-b1be-ef7cec315bc5
keywords:
- TimeCreated element EventLog
topic_type:
- apiref
api_name:
- TimeCreated
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TimeCreated (SystemPropertiesType) Element

The time stamp that identifies when the event was logged.

``` syntax
<xs:element name="TimeCreated">
    <xs:complexType>
        <xs:attribute name="SystemTime"
            type="dateTime"
            use="required"
         />
    </xs:complexType>
</xs:element>
```

The **TimeCreated** element is defined by the [**SystemPropertiesType**](eventschema-systempropertiestype-complextype.md) complex type.

## Attributes



| Name       | Type     | Description                                              |
|------------|----------|----------------------------------------------------------|
| SystemTime | dateTime | The system time of when the event was logged.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**System (EventType)**](eventschema-system-eventtype-element.md)
</dt> </dl>

 

 





