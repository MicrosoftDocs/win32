---
title: binary (TemplateItemType) Element
description: Contains the binary data that is supplied by the Event Log API.
ms.assetid: 3ad9c119-9395-49d3-b920-9a071bcc6a04
keywords:
- binary element EventLog
topic_type:
- apiref
api_name:
- binary
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# binary (TemplateItemType) Element

Contains the binary data that is supplied by the [Event Log](/windows/desktop/EventLog/event-logging) API.

``` syntax
<xs:element name="binary">
    <xs:complexType>
        <xs:attribute name="name"
            type="string"
            use="optional"
         />
    </xs:complexType>
</xs:element>
```

The **binary** element is defined by the [**TemplateItemType**](eventmanifestschema-templateitemtype-complextype.md) complex type.

## Attributes



| Name | Type   | Description                                          |
|------|--------|------------------------------------------------------|
| name | string | The name associated with the binary data.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**template (TemplateListType)**](eventmanifestschema-template-templatelisttype-element.md)
</dt> </dl>

 

