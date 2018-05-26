---
title: VML Eqn Attribute
description: VML Eqn Attribute
ms.assetid: b2c41bad-2f83-4280-9441-33206d8dc1b7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML Eqn Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the equation used by a formula. Read/write. **String**.

**Applies To**

[F](msdn-online-vml-f-element.md) (subelement of [Formulas](msdn-online-vml-formulas-element.md))

**Tag Syntax**

&lt;v: *element* eqn=" *expression* "&gt;

**Script Syntax**

*element* .eqn="*expression*"

*expression*=*element*.eqn

**Remarks**

Equations are defined by the evaluation of a text expression that has the general form of an operation followed by up to three arguments. Each argument may be of the following types:

-   adjustment (for example, \#2)
-   another formula (for example, @2)
-   fixed numbers (for example, 2)
-   predefined values

The table below defines the formulas that can be used withthe optional arguments given the names *v*, *p1*, and *p2*.The formula pattern is:

&lt;f eqn=" *operation* \[*v* \] \[*p1* \] \[*p2* \]"/&gt;



| Operation | Params | Exact  | Result                    | Description                                                                    |
|-----------|--------|--------|---------------------------|--------------------------------------------------------------------------------|
| val       | 1      | yes    | v                         | Defines a guide value from some other value.                                   |
| sum       | 3      | yes    | v + p1 - p2               | Used for addition and subtraction.                                             |
| product   | 3      | rounds | v \* p1 / p2              | Used for multiplication and division.                                          |
| mid       | 2      | (c)    | (v + p1)/ 2               | Average.                                                                       |
| abs       | 1      | yes    | abs(v)                    | Absolute value.                                                                |
| min       | 2      | yes    | min(v,p1)                 | The lesser value of v and p1.                                                  |
| max       | 2      | yes    | max(v,p1)                 | The greater value of v and p1.                                                 |
| if        | 3      | yes    | v &gt; 0 ? p1 : p2        | Conditional testing.                                                           |
| mod       | 3      | no     | sqrt(v^2 + p1^2 + p2^2)   | Modulus value.                                                                 |
| atan2     | 2      | no     | atan2(p1,v)               | Polar value in degrees \* 2^16 (fd units).                                     |
| sin       | 2      | no     | v \* sin(p1)              | Sin, argument in degrees \* 2^16 (fd [units](msdn-online-vml-units.md) ).     |
| cos       | 2      | no     | v \* cos(p1)              | Cos, argument in degrees \* 2^16 (fd [units](msdn-online-vml-units.md) ).     |
| cosatan2  | 3      | no     | v \* cos(atan2(p2,p1))    | Preserves full accuracy in intermediate calculation.                           |
| sinatan2  | 3      | no     | v \* sin(atan2(p2,p1))    | Preserves full accuracy in intermediate calculation.                           |
| sqrt      | 1      | no     | sqrt(v)                   | Result is positive and rounds down.                                            |
| sumangle  | 3      | yes    | v + p1 \* 2^16 + p2\*2^16 | v scaled by 2^16; p1 and p2 are degrees.<br/>                            |
| ellipse   | 3      | no     | p2 \* sqrt(1-(v/p1)^2)    | Ellipse.                                                                       |
| tan       | 2      | no     | v \* tan(p1)              | Tangent, argument in degrees \* 2^16 (fd [units](msdn-online-vml-units.md) ). |



 

Note that the equation only consists of operations and numbers; mathematical symbols are omitted. For example, the equation

eqn="sum 5 9 3"

would yield the equivalent of

5 + 9 - 3

for the returned value of 11. If operands are missing, the value is not used. For example,

eqn="sum 5 9"

would yield the equivalent of

5 + 9

and would ignore the missing operand.

*VML Standard Attribute*

**Example**

The following formula would yield a result of 6 (the sum of both numbers divided by 2), which, if this were the first formula, could be retrieved by the symbol "@0".


```HTML
    <v:f eqn="mid 5 7"/>
```



 

 





