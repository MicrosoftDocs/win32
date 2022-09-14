---
title: TypeListType Complex Type
description: Defines the types that are used in the manifest.
ms.assetid: e7ce0ecf-3bd0-49ab-82c7-dc28fd0e59a2
keywords:
- TypeListType complex type EventLog
topic_type:
- apiref
api_name:
- TypeListType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TypeListType Complex Type

Defines the types that are used in the manifest.

``` syntax
<xs:complexType name="TypeListType">
    <xs:choice
        maxOccurs="unbounded"
    >
        <xs:element name="xmlTypes"
            type="XmlTypeListType"
         />
        <xs:element name="inTypes"
            type="InputTypeListType"
         />
        <xs:any
            processContents="lax"
            namespace="##other"
         />
    </xs:choice>
</xs:complexType>
```

## Child elements



| Element                                                               | Type                                                                           | Description                                                                                                 |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**inTypes**](eventmanifestschema-intypes-typelisttype-element.md)   | [**InputTypeListType**](eventmanifestschema-inputtypelisttype-complextype.md) | Defines a list of input data types.<br/>                                                              |
| [**xmlTypes**](eventmanifestschema-xmltypes-typelisttype-element.md) | [**XmlTypeListType**](eventmanifestschema-xmltypelisttype-complextype.md)     | Defines a list output types that the service uses to determine how to render an input data type.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





