---
title: resources (LocalizationType) Element
description: Defines a group of string tables that contain the localized strings that you reference in your manifest.
ms.assetid: b984894a-0ae8-49be-af93-3acdcce53ee9
keywords:
- resources element EventLog
topic_type:
- apiref
api_name:
- resources
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# resources (LocalizationType) Element

Defines a group of string tables that contain the localized strings that you reference in your manifest.

``` syntax
<xs:element name="resources">
    <xs:complexType>
        <xs:choice
            minOccurs="0"
            maxOccurs="unbounded"
        >
            <xs:element name="stringTable"
                type="StringTableType"
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                namespace="##other"
             />
        </xs:choice>
        <xs:attribute name="culture"
            type="string"
            default="##fallback"
            use="optional"
         />
    </xs:complexType>
</xs:element>
```

The **resources** element is defined by the [**LocalizationType**](eventmanifestschema-localizationtype-complextype.md) complex type.

## Child elements



| Element                                                                  | Type                                                                       | Description                                                                             |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**stringTable**](eventmanifestschema-stringtable-resources-element.md) | [**StringTableType**](eventmanifestschema-stringtabletype-complextype.md) | Defines a list of localized strings that you can reference in your manifest.<br/> |



## Attributes



| Name    | Type   | Description                                                                                                                                            |
|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| culture | string | A language name that identifies the culture of the localized strings in the string table. For example, "en-US" for English (United States).<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**localization (instrumentationManifest)**](eventmanifestschema-localization-instrumentationmanifest-element.md)
</dt> </dl>

 

 





