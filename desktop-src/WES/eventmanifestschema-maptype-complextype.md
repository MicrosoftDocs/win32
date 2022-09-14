---
title: MapType Complex Type
description: Defines a list of name/value pairs.
ms.assetid: 208ae219-8f79-4049-b946-a57b33c97b1b
keywords:
- MapType complex type EventLog
topic_type:
- apiref
api_name:
- MapType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MapType Complex Type

Defines a list of name/value pairs.

``` syntax
<xs:complexType name="MapType">
    <xs:choice
        maxOccurs="unbounded"
    >
        <xs:element name="valueMap"
            type="ValueMapType"
         />
        <xs:element name="bitMap"
            type="BitMapType"
         />
    </xs:choice>
</xs:complexType>
```

## Child elements



| Element                                                          | Type                                                                 | Description                                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**bitMap**](eventmanifestschema-bitmap-maptype-element.md)     | [**BitMapType**](eventmanifestschema-bitmaptype-complextype.md)     | Defines a list of name/value pairs that map bit values and string values.<br/>     |
| [**valueMap**](eventmanifestschema-valuemap-maptype-element.md) | [**ValueMapType**](eventmanifestschema-valuemaptype-complextype.md) | Defines a list of name/value pairs that map integer values and string values.<br/> |



## Remarks

Typically, you create maps to provide enumerated string values for event data.

## Examples

The following example shows how to specify a value map and bitmap.


```XML
<maps>
   <valueMap name="MyValueMap">
       <map value="5" message="$(string.value5)"/>
       <map value="45" message="$(string.value45)"/>
   </valueMap>
 
   <bitMap name="MyBitmap">
       <map value="0x8" message="$(string.bit3)/>
       <map value="0x80" message="$(string.bit7)/>
   </bitMap>
</maps>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





