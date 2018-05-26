---
Description: Defines the valid values for the Style attribute of the LineLayout element.
ms.assetid: b257f0da-1bee-4d1b-9829-70f91cdcabe0
title: LineLayoutStyleType Simple Type
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                                     |                                                               |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



 

 




