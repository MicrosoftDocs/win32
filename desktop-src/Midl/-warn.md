---
title: /warn switch
description: The /warn switch specifies the warning level of the MIDL compiler.
ms.assetid: b1e26e67-8c47-40a2-8f34-22273ddfaa1d
keywords:
- /warn switch MIDL
topic_type:
- apiref
api_name:
- /warn
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /warn switch

The **/warn** switch specifies the warning level of the MIDL compiler.

``` syntax
midl /warn level
```

## Switch Options

<dl> <dt>

*level* 
</dt> <dd>

Specifies the warning level, an integer in the range 0 through 4. There is no space between the **/warn** switch and the digit indicating the warning-level value.

</dd> </dl>

## Remarks

The warning level indicates the severity of the warning. Warning levels range from 1 to 4, with a value of zero meaning to display no warning information. The highest severity warning is level 1. The following table describes the warnings for each warning level.



| Warning level | Description                                             | Example                                                                   |
|---------------|---------------------------------------------------------|---------------------------------------------------------------------------|
| 0             | No warnings.                                            |                                                                           |
| 1             | Severe warnings that can cause application errors.      | No binding handle specified, unattributed pointers, conflicting switches. |
| 2             | May cause problems in the user's operating environment. | Identifier length exceeds 31 characters. No default union arm specified.  |
| 3             | Reserved.                                               |                                                                           |
| 4             | Lowest warning level.                                   | Non-ANSI C constructs.                                                    |



 

Warnings are different from errors. Errors cause the MIDL compiler to halt processing of the IDL file. Warnings cause the MIDL compiler to emit an informational message and continue processing the IDL file.

The warning level set by the **/warn** switch can be used with the [**WX**](-wx.md) switch to cause the MIDL compiler to halt processing of the IDL file.

The **/warn** switch behaves the same as the [**/W**](-w.md) switch.

## Examples

**midl /warn2 filename.idl**

**midl /warn4 bar.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 




