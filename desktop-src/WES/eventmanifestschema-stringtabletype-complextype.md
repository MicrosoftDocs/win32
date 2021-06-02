---
title: StringTableType Complex Type
description: Defines a list of localized strings that you can reference in your manifest. | StringTableType Complex Type
ms.assetid: 47a59ff7-aaf6-4200-805b-0a8b5f57f101
keywords:
- StringTableType complex type EventLog
topic_type:
- apiref
api_name:
- StringTableType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StringTableType Complex Type

Defines a list of localized strings that you can reference in your manifest.

``` syntax
<xs:complexType name="StringTableType">
    <xs:choice
        minOccurs="0"
        maxOccurs="unbounded"
    >
        <xs:element name="string">
            <xs:complexType
                mixed="true"
            >
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
    </xs:choice>
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                              | Type | Description                            |
|----------------------------------------------------------------------|------|----------------------------------------|
| [**string**](eventmanifestschema-string-stringtabletype-element.md) |      | Defines a localized string.<br/> |



## Attributes



| Name       | Type   | Description                                                                                                              |
|------------|--------|--------------------------------------------------------------------------------------------------------------------------|
| id         | string | An identifier that uniquely identifies the string within the string table. For example, "Printer.Connection".<br/> |
| stringType | string | Not used.<br/>                                                                                                     |
| value      | string | The localized string.<br/>                                                                                         |



## Remarks

You can reference the strings from any manifest type that contains the message attribute. To reference a string with a stringType of "string" and an id of "Printer.Connection", use $(string.Printer.Connection) as the value of the message attribute.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





