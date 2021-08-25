---
title: / system switch
description: The / system switch directs the MIDL compiler to generate a type library for the specified system. The default is the current operating system.
ms.assetid: 0fb69ffc-5ab4-49f3-b34d-859da776ce9e
keywords:
- / system switch MIDL
topic_type:
- apiref
api_name:
- / system
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /&lt;system&gt; switch

The **/&lt;system&gt;** switch directs the MIDL compiler to generate a type library for the specified system. The default is the current operating system.

``` syntax
midl /{win32 | ia64 | amd64}
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="win32"></span><span id="WIN32"></span>

<span id="win32"></span><span id="WIN32"></span>****win32****


</dt> <dd>

Windows 2000, Windows XP, Windows Vista, Windows 7

</dd> <dt>

<span id="ia64"></span><span id="IA64"></span>

<span id="ia64"></span><span id="IA64"></span>****ia64****


</dt> <dd>

An Intel-based 64-bit Windows environment such as Windows 2000, Windows Server 2003, Windows XP Professional x64 Edition, Windows Vista, or Windows 7.

</dd> <dt>

<span id="amd64"></span><span id="AMD64"></span>

<span id="amd64"></span><span id="AMD64"></span>****amd64****


</dt> <dd>

An American Micro Devices-based 64-bit Windows environment such as Windows 2000, Windows Server 2003, Windows XP Professional x64 Edition, Windows Vista, or Windows 7.

</dd> </dl> </dd> </dl>

## Remarks

The **/&lt;system&gt;** switch is functionally the same as the MIDL [**/env**](-env.md) option and is recognized by the MIDL compiler solely for backward compatibility with MkTypLib. If you are generating a new makefile, use the **/env** switch.

## Examples

**midl /win32 filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/env**](-env.md)
</dt> </dl>

 

 




