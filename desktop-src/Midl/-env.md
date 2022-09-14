---
title: /env switch
description: The /env switch selects the environment in which the application runs.
ms.assetid: 70a548c8-fdc3-48f3-a865-14ba9b29fb02
keywords:
- /env switch MIDL
topic_type:
- apiref
api_name:
- /env
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /env switch

The **/env** switch selects the environment in which the application runs.

``` syntax
midl /env { win32 | ia64 | amd64 | win64 }
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="win32"></span><span id="WIN32"></span>

<span id="win32"></span><span id="WIN32"></span>****win32****


</dt> <dd>

Directs the MIDL compiler to generate stub files, or a type library file, for a 32-bit environment.

</dd> <dt>

<span id="ia64"></span><span id="IA64"></span>

<span id="ia64"></span><span id="IA64"></span>****ia64****


</dt> <dd>

Directs the MIDL compiler to generate stub files, or a type library file, for a Intel Architecture 64-bit (IA64) environment.

</dd> <dt>

<span id="amd64"></span><span id="AMD64"></span>

<span id="amd64"></span><span id="AMD64"></span>****amd64****


</dt> <dd>

Directs the MIDL compiler to generate stub files, or a type library file, for an Advanced Micro Devices 64-bit (AMD64) environment.

</dd> <dt>

<span id="win64"></span><span id="WIN64"></span>

<span id="win64"></span><span id="WIN64"></span>****win64****


</dt> <dd>

Same behavior as *ia64*.

</dd> </dl> </dd> </dl>

## Remarks

The **/env** switch primarily affects the packing level used for structures in that environment. Be sure you specify the same packing-level setting for both the MIDL compiler and the C compiler.

The **/env** switch determines the packing level and other settings as follows:

-   When you specify **win32**, generated stubs use C-compiler packing-level 8 for all types involved in remote operations. The [**int**](int.md) data types are both 32 bits. Pointers are 32 bits.
-   When you specify **ia64** or **amd64**, the MIDL compiler runs in a cross-compiler mode for the indicated (Intel or AMD) 64-bit platform. The generated stubs use C-compiler packing-level 8 for all types involved in remote operations. The [**long**](long.md) and [**int**](int.md) data types are 32 bits. Pointers are 64 bits.

The [**/align**](-align.md), [**/pack**](-pack.md), and [**/Zp**](-zp.md) switches take precedence over the **/env** settings.

For more information on 64 bit support for MIDL and RPC see [Designing 64-bit-Compatible Interfaces](/windows/desktop/WinProg64/designing-64-bit-compatible-interfaces).

## Examples

**midl /env win32 filename.idl**

**midl /env ia64 filename.idl**

**midl /env amd64 filename.idl**

**midl /env win64 filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/pack**](-pack.md)
</dt> <dt>

[**/Zp**](-zp.md)
</dt> </dl>

 

 