---
title: CSymbolType Simple Type (Windows Event Log)
description: CSymbolType Simple Type (Windows Event Log) - Defines a valid C/C++ symbol name.
ms.assetid: d19827b6-2b61-4d75-ac9d-56a384b0cc4b
keywords:
- CSymbolType simple type EventLog
topic_type:
- apiref
api_name:
- CSymbolType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CSymbolType Simple Type (Windows Event Log)

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

    The symbol name can be empty or contain alphanumeric characters and underscores. If the name is empty, the message compiler will generate the symbol name. If you specify a name, the name must begin with an underscore (\_) or an alphabetical character.

## Remarks

If the symbol name is empty, the message compiler uses the **name** attribute of the element that you are defining to generate the symbol name. The compiler replaces any non-alphanumeric characters and leading digits with underscores. For example, if the channel's **name** attribute is Microsoft-Windows-SampleProvider/Operational, the compiler would use Microsoft\_Windows\_SampleProvider\_Operational as the symbol name.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





