---
title: EventID (SystemPropertiesType) Element
description: The identifier that the provider used to identify the event.
ms.assetid: 2d5ac44b-4157-4b87-bd8f-e992e85dd0b1
keywords:
- EventID element EventLog
topic_type:
- apiref
api_name:
- EventID
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EventID (SystemPropertiesType) Element

The identifier that the provider used to identify the event.

``` syntax
<xs:element name="EventID">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension
                base="unsignedInt"
             />
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
```

The **EventID** element is defined by the [**SystemPropertiesType**](eventschema-systempropertiestype-complextype.md) complex type.

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

 

 





