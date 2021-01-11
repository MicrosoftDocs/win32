---
description: Defines the type that defines valid values for the Type attribute of the Content element \[Journal Reader\].
ms.assetid: f38f7a7e-a517-4156-9c60-e1b6d35baa07
title: ContentTypeType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ContentTypeType
api_type: 
- Schema
api_location: 
---

# ContentTypeType Simple Type

Defines the type that defines valid values for the *Type* attribute of the [Content element \[Journal Reader\]](content-element--journal-reader.md).

``` syntax
<xs:simpleType name="ContentTypeType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="Normal|Inert"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **ContentTypeType** simple type is a string that is restricted by the following pattern:

-   `Normal|Inert`

## Remarks

Valid values are "Normal" and "Inert".

If the type is "Inert", then the content contained is a Journal page that is the read-only/non-editable "background" for the document. This occurs when a document is created by using the Journal Note Writer printer driver.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



 

 




