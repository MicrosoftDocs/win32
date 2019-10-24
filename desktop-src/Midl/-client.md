---
title: /client switch
description: The /client switch directs the MIDL compiler to generate client-side C source files for an RPC interface.
ms.assetid: bce5af72-2201-4b42-9348-cb97f08b7fdf
keywords:
- /client switch MIDL
topic_type:
- apiref
api_name:
- /client
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /client switch

The **/client** switch directs the MIDL compiler to generate client-side C source files for an RPC interface.

``` syntax
midl /client { stub | none }
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="stub"></span><span id="STUB"></span>

<span id="stub"></span><span id="STUB"></span>****stub****


</dt> <dd>

Generates the client-side files.

</dd> <dt>

<span id="none"></span><span id="NONE"></span>

<span id="none"></span><span id="NONE"></span>****none****


</dt> <dd>

Does not generate any client-side files.

</dd> </dl> </dd> </dl>

## Remarks

When the **/client** switch is not specified, the MIDL compiler generates the client stub file. This switch does not affect OLE interfaces.

The **/client** switch takes precedence over the [**/cstub**](-cstub.md) switch.

## Examples

**midl /client none filename.idl**

**midl /client stub filename.idl**

## See also

<dl> <dt>

[**/cstub**](-cstub.md)
</dt> <dt>

[**/server**](-server.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 




