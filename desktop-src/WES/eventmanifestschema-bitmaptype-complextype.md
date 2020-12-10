---
title: BitMapType Complex Type
description: Defines a list of name/value mappings between bit values and string values.
ms.assetid: 65dc6a48-878c-415c-872c-41dc27691b7f
keywords:
- BitMapType complex type EventLog
topic_type:
- apiref
api_name:
- BitMapType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# BitMapType Complex Type

Defines a list of name/value mappings between bit values and string values.

``` syntax
<xs:complexType name="BitMapType">
    <xs:sequence>
        <xs:element name="map"
            type="BitMapValueType"
            maxOccurs="unbounded"
         />
    </xs:sequence>
    <xs:attribute name="name"
        type="string"
     />
    <xs:attribute name="symbol"
        type="CSymbolType"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                   | Type                                                                       | Description                                                            |
|-----------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**map**](eventmanifestschema-map-bitmaptype-element.md) | [**BitMapValueType**](eventmanifestschema-bitmapvaluetype-complextype.md) | Defines the mapping between a bit value and a string value.<br/> |



## Attributes



| Name   | Type                                                              | Description                                                                                                                                                                                                                                                                                                         |
|--------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name   | string                                                            | The name of the bitmap.<br/>                                                                                                                                                                                                                                                                                  |
| symbol | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the mappings in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the map in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





