---
title: PatternMapType Complex Type
description: Not used. Defines a mapping between two regular expressions. One expression is used to find a matching string in the message string and the other is used to alter the string before the service places it back in the message string.
ms.assetid: 184b6aeb-a554-4a92-b19e-1849c711d33b
keywords:
- PatternMapType complex type EventLog
topic_type:
- apiref
api_name:
- PatternMapType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PatternMapType Complex Type

Not used. Defines a mapping between two regular expressions. One expression is used to find a matching string in the message string and the other is used to alter the string before the service places it back in the message string.

``` syntax
<xs:complexType name="PatternMapType">
    <xs:sequence>
        <xs:element name="map"
            type="PatternMapValueType"
            maxOccurs="unbounded"
         />
    </xs:sequence>
    <xs:attribute name="name"
        type="QName"
        use="required"
     />
    <xs:attribute name="format"
        type="anyURI"
        use="required"
     />
    <xs:attribute name="symbol"
        type="CSymbolType"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                       | Type                                                                               | Description                                                                                                   |
|---------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**map**](eventmanifestschema-map-patternmaptype-element.md) | [**PatternMapValueType**](eventmanifestschema-patternmapvaluetype-complextype.md) | Defines the regular expressions used to find a matching string in the message string and alter it.<br/> |



## Attributes



| Name   | Type                                                              | Description                                                                                                                                                                                                                                                                                                         |
|--------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| format | anyURI                                                            | The regular expression engine to use.<br/>                                                                                                                                                                                                                                                                    |
| name   | **QName**                                                         | The name of the pattern map. Use the name in a data element to reference the mappings.<br/>                                                                                                                                                                                                                   |
| symbol | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the mappings in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the map in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





