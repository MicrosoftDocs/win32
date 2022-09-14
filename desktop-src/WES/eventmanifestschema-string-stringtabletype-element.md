---
title: string (StringTableType) Element
description: Defines a localized string.
ms.assetid: 845476a9-bcf4-4821-824c-06c9a9f64649
keywords:
- string element EventLog
topic_type:
- apiref
api_name:
- string
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# string (StringTableType) Element

Defines a localized string.

``` syntax
<xs:element name="string">
    <xs:complexType>
        <xs:attribute name="id"
            type="string"
            use="required"
         />
        <xs:attribute name="value"
            type="string"
            use="required"
         />
        <xs:attribute name="stringType"
            type="string"
            use="optional"
         />
    </xs:complexType>
</xs:element>
```

The **string** element is defined by the [**StringTableType**](eventmanifestschema-stringtabletype-complextype.md) complex type.

## Attributes



| Name       | Type   | Description                                                                           |
|------------|--------|---------------------------------------------------------------------------------------|
| id         | string | An identifier that uniquely identifies the string within the string table.<br/> |
| stringType | string | Not used.<br/>                                                                  |
| value      | string | The localized string.<br/>                                                      |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**stringTable (LocalizationType)**](eventmanifestschema-stringtable-localizationtype-element.md)
</dt> </dl>

 

 





