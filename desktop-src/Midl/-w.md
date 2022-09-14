---
title: /W switch
description: The /W switch specifies the warning level of the MIDL compiler. The warning level indicates the severity of the warning.
ms.assetid: ee894d73-cbd1-455f-9836-a6d80cfc95f9
keywords:
- /W switch MIDL
topic_type:
- apiref
api_name:
- /W
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /W switch

The **/W** switch specifies the warning level of the MIDL compiler. The warning level indicates the severity of the warning.

``` syntax
midl /W level
```

## Switch Options

<dl> <dt>

*level* 
</dt> <dd>

Specifies the warning level, an integer in the range 0 through 4. There is no space between the **/W** switch and the digit indicating the warning-level value.

</dd> </dl>

## Remarks

Warning levels range from 1 to 4, with a value of zero meaning to display no warning information. The highest-severity warning is level 1. The following table describes the warnings for each warning level.



| Warning level | Description                                             | Example                                                                   |
|---------------|---------------------------------------------------------|---------------------------------------------------------------------------|
| W0            | No warnings.                                            |                                                                           |
| W1            | Severe warnings that can cause application errors.      | No binding handle specified, unattributed pointers, conflicting switches. |
| W2            | May cause problems in the user's operating environment. | Identifier length exceeds 31 characters. No default union arm specified.  |
| W3            | Reserved.                                               |                                                                           |
| W4            | Lowest warning level.                                   | Non-ANSI C constructs.                                                    |



 

Warnings are different from errors. Errors cause the MIDL compiler to halt processing of the IDL file. Warnings cause the MIDL compiler to emit an informational message and continue processing the IDL file.

The warning level set by the **/W** switch can be used with the [**/WX**](-wx.md) switch to cause the MIDL compiler to halt processing of the IDL file.

The **/W** switch behaves the same as the [**/warn**](-warn.md) switch.

## Examples

**midl /W2 filename.idl**

**midl /W4 bar.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/warn**](-warn.md)
</dt> </dl>

 

 




