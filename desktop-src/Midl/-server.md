---
title: /server switch
description: The /server switch directs the MIDL compiler to generate server-side C source files for an RPC interface.
ms.assetid: c5ca6a47-e8b0-4a13-ba73-2d35a9ac8240
keywords:
- /server switch MIDL
topic_type:
- apiref
api_name:
- /server
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /server switch

The **/server** switch directs the MIDL compiler to generate server-side C source files for an RPC interface.

``` syntax
midl /server { stub | none }
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="stub"></span><span id="STUB"></span>

<span id="stub"></span><span id="STUB"></span>****stub****


</dt> <dd>

Generates the server-side files.

</dd> <dt>

<span id="none"></span><span id="NONE"></span>

<span id="none"></span><span id="NONE"></span>****none****


</dt> <dd>

Does not generate server-side files.

</dd> </dl> </dd> </dl>

## Remarks

When the **/server** switch is not specified, the MIDL compiler generates the server stub file. This switch does not affect OLE interfaces.

The **none** option causes no files to be generated.

The **/server** switch takes precedence over the **/sstub** switch.

## Examples

**midl /server none**

**midl /server stub**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/client**](-client.md)
</dt> <dt>

[**/sstub**](-sstub.md)
</dt> </dl>

 

 




