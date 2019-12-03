---
title: /Zp switch
description: The /Zp switch is the same as the /pack option.
ms.assetid: ccdae6a5-e53c-4ddc-9f5f-2b2118709fdb
keywords:
- /Zp switch MIDL
topic_type:
- apiref
api_name:
- /Zp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /Zp switch

The **/Zp** switch is the same as the [**/pack**](-pack.md) option.

``` syntax
midl /Zp packing_level
```

## Switch Options

<dl> <dt>

*packing\_level* 
</dt> <dd>

Specifies the packing level of structures in the target system. The packing-level value can be set to 1, 2, 4, or 8.

</dd> </dl>

## Remarks

The **/Zp** switch designates the packing level of structures in the target system. The packing-level value corresponds to the **/Zp** option value used by the Microsoft C/C++ compiler. For more information, see your Microsoft C/C++ programming documentation.

Specify the same packing level when you invoke the MIDL compiler and the C compiler.

The default packing level used when neither the **/Zp** nor [**/pack**](-pack.md) switch is specified is 8 in all build environments.

> [!Note]  
> Do not use **/Zp1** or **/Zp2** on MIPS or Alpha platforms and do not use **/Zp4** or **/Zp8** on 16-bit platforms. Depending on the data type and memory location assigned by the C compiler at run time, this can result in a data misalignment exception on MIPS and Alpha platforms. On MS-DOS platforms, the C compiler will not ensure the alignment at 4 or 8, and so the application may terminate.

 

## Examples

**midl /Zp4 filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/pack**](-pack.md)
</dt> </dl>

 

 




