---
title: TemplateListType Complex Type
description: Defines a list of templates that specify the data to include with the events.
ms.assetid: '7f676746-6773-4ae2-8330-60d432c29e3a'
keywords: ["TemplateListType complex type EventLog"]
topic_type:
- apiref
api_name:
- TemplateListType
api_type:
- Schema
---

# TemplateListType Complex Type

Defines a list of templates that specify the data to include with the events.

``` syntax
<xs:complexType name="TemplateListType">
    <xs:sequence>
        <xs:element name="template"
            type="TemplateItemType"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                                   | Type                                                                         | Description                                                           |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**template**](eventmanifestschema-template-templatelisttype-element.md) | [**TemplateItemType**](eventmanifestschema-templateitemtype-complextype.md) | A template that defines the data to include with an event.<br/> |



## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





