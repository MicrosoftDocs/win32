---
description: Defines a structure that contains one or more counter values.
ms.assetid: 3085d490-4ac1-491c-bce0-8af46b16fab9
title: struct Complex Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# struct Complex Type

Defines a structure that contains one or more counter values.

``` syntax
<xs:complexType name="struct">
    <xs:simpleContent>
        <xs:extension
            base="xs:string"
        >
            <xs:attribute name="name"
                type="man:CSymbolType"
                use="required"
             />
            <xs:attribute name="type"
                type="man:CSymbolType"
                use="required"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name | Type                                                                    | Description                                                                                                                                      |
|------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| name | [**man:CSymbolType**](performance-counters-csymboltype-simple-type.md) | The name of the structure.<br/>                                                                                                            |
| type | [**man:CSymbolType**](performance-counters-csymboltype-simple-type.md) | A symbolic name that identifies the structure. The [CTRPP](ctrpp.md) tool creates a struct variable with this name that you can use.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




