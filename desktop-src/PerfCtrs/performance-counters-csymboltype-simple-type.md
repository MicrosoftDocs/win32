---
description: CSymbolType Simple Type (Performance Counters) - Defines a valid C/C++ symbol name.
ms.assetid: 75f74a16-0be4-466b-a88d-247c8c94f4ce
title: CSymbolType Simple Type (Performance Counters)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# CSymbolType Simple Type (Performance Counters)

Defines a valid C/C++ symbol name.

``` syntax
<xs:simpleType name="CSymbolType">
    <xs:restriction
        base="xs:string"
    >
        <xs:pattern
            value="()|([_a-zA-Z][_0-9a-zA-Z]*)"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **CSymbolType** simple type is a **xs:string** that is restricted by the following pattern:

-   `()|([_a-zA-Z][_0-9a-zA-Z]*)`

    The symbol name can be empty or contain alphanumeric characters and underscores. If you specify a name, the name must begin with an underscore (\_) or an alphabetical character.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




