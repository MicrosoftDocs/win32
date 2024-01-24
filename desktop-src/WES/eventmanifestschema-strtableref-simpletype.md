---
title: strTableRef Simple Type
description: Defines a string that references a message string that is defined in a string table in the manifest or in a message (.mc) file.
ms.assetid: ecbcefcb-3265-4508-be7d-17a0fe3fe911
keywords:
- strTableRef simple type EventLog
topic_type:
- apiref
api_name:
- strTableRef
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# strTableRef Simple Type

Defines a string that references a message string that is defined in a string table in the manifest or in a message (.mc) file.

``` syntax
<xs:simpleType name="strTableRef">
    <xs:restriction
        base="xs:string"
    >
        <xs:pattern
            value="(\$([Ss]tring\..*))|(\$([Mm][Cc]\..*))"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **strTableRef** simple type is a **xs:string** that is restricted by the following pattern:

-   `(\$([Ss]tring\..*))|(\$([Mm][Cc]\..*))`

    The string must be of the form, $string.*stringid* or $mc.*symbolid*. If the string is of the form, $string.*stringid*, it must reference a string in the [**stringTable**](eventmanifestschema-stringtable-resources-element.md) section of the manifest. If the string is of the form, $mc.*symbolid*, it must reference a symbol defined in the message file.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





