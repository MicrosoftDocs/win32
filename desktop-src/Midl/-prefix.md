---
title: /prefix switch
description: The /prefix switch directs the MIDL compiler to add prefix strings to the client and/or server stub routine names.
ms.assetid: 5530e972-08bf-4cca-9bb4-9631db824bdb
keywords:
- /prefix switch MIDL
topic_type:
- apiref
api_name:
- /prefix
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /prefix switch

The **/prefix** switch directs the MIDL compiler to add prefix strings to the client and/or server stub routine names. This can be used to allow a single program to be both a client and server of the same interface, without having the client- and server-side routine names conflict with each other.

``` syntax
midl /prefix { client | cstub | server | sstub | switch | all }
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="client"></span><span id="CLIENT"></span>

<span id="client"></span><span id="CLIENT"></span>****client****


</dt> <dd>

Affects only the client stub routine names.

</dd> <dt>

<span id="cstub"></span><span id="CSTUB"></span>

<span id="cstub"></span><span id="CSTUB"></span>****cstub****


</dt> <dd>

Same as *client*. Affects only the client stub routine names.

</dd> <dt>

<span id="server"></span><span id="SERVER"></span>

<span id="server"></span><span id="SERVER"></span>****server****


</dt> <dd>

Affects only the routine names called by the server stub routine.

</dd> <dt>

<span id="sstub"></span><span id="SSTUB"></span>

<span id="sstub"></span><span id="SSTUB"></span>****sstub****


</dt> <dd>

Same as *server*. Affects only the routine names called by the server stub routine.

</dd> <dt>

<span id="switch"></span><span id="SWITCH"></span>

<span id="switch"></span><span id="SWITCH"></span>****switch****


</dt> <dd>

Affects an extra prototype added to the header file.

</dd> <dt>

<span id="all"></span><span id="ALL"></span>

<span id="all"></span><span id="ALL"></span>****all****


</dt> <dd>

Affects both the client and server stub routine names.

</dd> </dl> </dd> </dl>

## Remarks

If the prefix for the client-side routines is different from the prefix for the server-side routines, the generated header file will have both client-side routine prototypes and server-side routine prototypes.

The **/prefix** switch is useful when a single header file will be used with stubs from multiple runs of the MIDL compiler. This forces additional routine prototypes in the header file.

In all cases, the client, server, and switch prefixes will override an all prefix.

## Examples

**midl /prefix client "c\_" server "s\_"**

**midl /prefix all "moo\_"**

**midl /prefix client "bark\_"**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 




