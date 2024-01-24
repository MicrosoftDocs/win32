---
title: Provider (SystemPropertiesType) Element
description: Identifies the provider that logged the event.
ms.assetid: 4560c938-4e2a-40d5-97f9-85a38141ac8f
keywords:
- Provider element EventLog
topic_type:
- apiref
api_name:
- Provider
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Provider (SystemPropertiesType) Element

Identifies the provider that logged the event.

``` syntax
<xs:element name="Provider">
    <xs:complexType>
        <xs:attribute name="Name"
            type="anyURI"
            use="optional"
         />
        <xs:attribute name="Guid"
            type="GUIDType"
            use="optional"
         />
        <xs:attribute name="EventSourceName"
            type="string"
            use="optional"
         />
    </xs:complexType>
</xs:element>
```

The **Provider** element is defined by the [**SystemPropertiesType**](eventschema-systempropertiestype-complextype.md) complex type.

## Attributes



| Name            | Type                                                | Description                                                                                                                                        |
|-----------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| EventSourceName | string                                              | The name of the event source that published the event (if the event source is from the legacy [Event Logging](/windows/desktop/EventLog/event-logging) API).<br/> |
| Guid            | [**GUIDType**](eventschema-guidtype-simpletype.md) | The globally unique identifier that uniquely identifies the provider.<br/>                                                                   |
| Name            | anyURI                                              | The name of the event provider that logged the event.<br/>                                                                                   |



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

 

