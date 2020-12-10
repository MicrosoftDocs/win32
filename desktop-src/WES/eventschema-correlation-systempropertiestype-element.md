---
title: Correlation (SystemPropertiesType) Element
description: The activity identifiers that consumers can use to group related events together.
ms.assetid: 63982f37-3581-4b11-ac14-b95bc52541cb
keywords:
- Correlation element EventLog
topic_type:
- apiref
api_name:
- Correlation
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Correlation (SystemPropertiesType) Element

The activity identifiers that consumers can use to group related events together.

``` syntax
<xs:element name="Correlation">
    <xs:complexType>
        <xs:attribute name="ActivityID"
            type="GUIDType"
            use="optional"
         />
        <xs:attribute name="RelatedActivityID"
            type="GUIDType"
            use="optional"
         />
    </xs:complexType>
</xs:element>
```

The **Correlation** element is defined by the [**SystemPropertiesType**](eventschema-systempropertiestype-complextype.md) complex type.

## Attributes



| Name              | Type                                                | Description                                                                                                                                                                                  |
|-------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ActivityID        | [**GUIDType**](eventschema-guidtype-simpletype.md) | A globally unique identifier that identifies the current activity. The events that are published with this identifier are part of the same activity.<br/>                              |
| RelatedActivityID | [**GUIDType**](eventschema-guidtype-simpletype.md) | A globally unique identifier that identifies the activity to which control was transferred to. The related events would then have this identifier as their ActivityID identifier.<br/> |



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

 

 





