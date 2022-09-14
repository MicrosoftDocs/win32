---
title: /pack switch
description: The /pack switch is the same as the /Zp option.
ms.assetid: 381e3099-adb4-4219-bbb4-89c9e1dd3928
keywords:
- /pack switch MIDL
topic_type:
- apiref
api_name:
- /pack
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /pack switch

The **/pack** switch is the same as the [**/Zp**](-zp.md) option.

``` syntax
midl /pack packing_level
```

## Switch Options

<dl> <dt>

*packing\_level* 
</dt> <dd>

Specifies the packing level of structures in the target system. The packing-level value can be set to 1, 2, 4, or 8.

</dd> </dl>

## Remarks

The **/pack** switch designates the packing level of structures in the target system. The packing-level value corresponds to the [**/Zp**](-zp.md) option value used by the Microsoft C/C++ version 7.0 compiler. For more information, see your Microsoft C/C++ programming documentation.

Specify the same packing level when you invoke the MIDL compiler and the C compiler. The default packing level used when neither the [**/Zp**](-zp.md) nor **/pack** switch is specified is 8, in both all build environments.

For a discussion of the potential dangers in using nonstandard packing levels, see the [**/Zp**](-zp.md) help topic.

## Examples

**midl /pack 2 filename.idl**

**midl /pack 8 bar.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/env**](-env.md)
</dt> <dt>

[**/Zp**](-zp.md)
</dt> </dl>

 

 




