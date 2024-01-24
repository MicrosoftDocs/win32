---
title: ValueMapType Complex Type
description: Defines a list of name/value mappings between integer values and string values.
ms.assetid: 754578bf-d3c6-4467-af39-af56d5a11dce
keywords:
- ValueMapType complex type EventLog
topic_type:
- apiref
api_name:
- ValueMapType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ValueMapType Complex Type

Defines a list of name/value mappings between integer values and string values.

``` syntax
<xs:complexType name="ValueMapType">
    <xs:sequence>
        <xs:element name="map"
            type="ValueMapValueType"
            maxOccurs="unbounded"
         />
    </xs:sequence>
    <xs:attribute name="name"
        type="string"
        use="required"
     />
    <xs:attribute name="symbol"
        type="CSymbolType"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                     | Type                                                                           | Description                                                                 |
|-------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**map**](eventmanifestschema-map-valuemaptype-element.md) | [**ValueMapValueType**](eventmanifestschema-valuemapvaluetype-complextype.md) | Defines the mapping between an integer value and a string value.<br/> |



## Attributes



| Name   | Type                                                              | Description                                                                                                                                                                                                                                                                                                         |
|--------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name   | string                                                            | The name of the value map. Use the name in a data element to reference the mappings.<br/>                                                                                                                                                                                                                     |
| symbol | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the mappings in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the map in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





