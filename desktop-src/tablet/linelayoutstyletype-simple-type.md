---
description: Defines the valid values for the Style attribute of the LineLayout element.
ms.assetid: b257f0da-1bee-4d1b-9829-70f91cdcabe0
title: LineLayoutStyleType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LineLayoutStyleType
api_type: 
- Schema
api_location: 
---

# LineLayoutStyleType Simple Type

Defines the valid values for the **Style** attribute of the [LineLayout element](linelayout-element.md).

``` syntax
<xs:simpleType name="LineLayoutStyleType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="None|Solid|Dash|Dot|DashDot|DashDotDot|Double"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **LineLayoutStyleType** simple type is a string that is restricted by the following pattern:

-   `None|Solid|Dash|Dot|DashDot|DashDotDot|Double`

## Remarks

Valid values for the **Style** attribute of the [LineLayout element](linelayout-element.md) are:

-   None
-   Solid
-   Dash
-   Dot
-   DashDot
-   DashDotDot
-   Double

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



 

 




