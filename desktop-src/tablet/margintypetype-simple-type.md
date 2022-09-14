---
description: Defines the type that contains valid values for the Type attribute for the Margin element.
ms.assetid: 5448ead5-0249-4cc7-9f2a-d2181e2af734
title: MarginTypeType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MarginTypeType
api_type: 
- Schema
api_location: 
---

# MarginTypeType Simple Type

Defines the type that contains valid values for the **Type** attribute for the [Margin element](margin-element.md).

``` syntax
<xs:simpleType name="MarginTypeType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="Left|Right"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **MarginTypeType** simple type is a **string** that is restricted by the following pattern:

-   `Left|Right`

## Remarks

The valid values for the **Type** attribute for the [Margin element](margin-element.md) are "Left" and "Right".

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



 

 




