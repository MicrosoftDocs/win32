---
title: xmlType (XmlTypeListType) Element
description: Defines an XML type.
ms.assetid: 4443963f-f47a-4371-87d8-58f508ba15d6
keywords:
- xmlType element EventLog
topic_type:
- apiref
api_name:
- xmlType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# xmlType (XmlTypeListType) Element

Defines an XML type.

``` syntax
<xs:element name="xmlType">
    <xs:complexType>
        <xs:complexContent>
            <xs:extension
                base="XmlType"
            >
                <xs:attribute name="name"
                    type="QName"
                    use="required"
                 />
                <xs:attribute name="value"
                    type="string"
                    use="required"
                 />
                <xs:attribute name="symbol"
                    type="string"
                    use="required"
                 />
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
</xs:element>
```

The **xmlType** element is defined by the [**XmlTypeListType**](eventmanifestschema-xmltypelisttype-complextype.md) complex type.

## Attributes



| Name   | Type      | Description                                                                                                                                                                                                                                                |
|--------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name   | **QName** | The name of the output type.<br/>                                                                                                                                                                                                                    |
| symbol | string    | The symbol to use to reference the output type in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the output type in the header file that the compiler generates.<br/> |
| value  | string    | An integer value that uniquely identifies the output type in the list of output types that you define.<br/>                                                                                                                                          |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**xmlTypes (TypeListType)**](eventmanifestschema-xmltypes-typelisttype-element.md)
</dt> </dl>

 

 





