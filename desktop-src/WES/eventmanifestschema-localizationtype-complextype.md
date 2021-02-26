---
title: LocalizationType Complex Type
description: Defines a group of localized resources that you reference in your manifest. | LocalizationType Complex Type
ms.assetid: fecab4e0-7136-4b13-8c24-bebbad0812e6
keywords:
- LocalizationType complex type EventLog
topic_type:
- apiref
api_name:
- LocalizationType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LocalizationType Complex Type

Defines a group of localized resources that you reference in your manifest.

``` syntax
<xs:complexType name="LocalizationType">
    <xs:choice
        minOccurs="0"
        maxOccurs="unbounded"
    >
        <xs:element name="resources">
            <xs:complexType>
                <xs:choice
                    minOccurs="0"
                    maxOccurs="unbounded"
                >
                    <xs:element name="stringTable"
                        type="StringTableType"
                     />
                </xs:choice>
                <xs:attribute name="culture"
                    type="string"
                    use="required"
                 />
                <xs:anyAttribute
                    processContents="lax"
                    namespace="##other"
                 />
            </xs:complexType>
        </xs:element>
        <xs:any
            processContents="lax"
            minOccurs="0"
            namespace="##other"
         />
    </xs:choice>
    <xs:attribute name="fallbackCulture"
        type="string"
        default="en-us"
        use="optional"
     />
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                                         | Type                                                                       | Description                                                                                                         |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**resources**](eventmanifestschema-resources-localizationtype-element.md)     |                                                                            | Defines a group of string tables that contain the localized strings that you reference in your manifest.<br/> |
| [**stringTable**](eventmanifestschema-stringtable-localizationtype-element.md) | [**StringTableType**](eventmanifestschema-stringtabletype-complextype.md) | Defines a list of localized strings that you can reference in your manifest.<br/>                             |



## Attributes



| Name            | Type   | Description                                                                                                                                            |
|-----------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| culture         | string | A language name that identifies the culture of the localized strings in the string table. For example, "en-US" for English (United States).<br/> |
| fallbackCulture | string | Not used.<br/>                                                                                                                                   |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





