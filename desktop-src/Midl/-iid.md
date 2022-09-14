---
title: /iid switch
description: The /iid switch specifies the name of the interface identifier file for a COM interface, overriding the default name obtained by adding \_i.c to the IDL file name.
ms.assetid: 051593f5-e612-4b19-94e5-d7885dbede21
keywords:
- /iid switch MIDL
topic_type:
- apiref
api_name:
- /iid
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /iid switch

The **/iid** switch specifies the name of the interface identifier file for a COM interface, overriding the default name obtained by adding \_i.c to the IDL file name.

``` syntax
midl /iid filename
```

## Switch Options

<dl> <dt>

*filename* 
</dt> <dd>

Specifies an interface identifier file name that overrides the default interface identifier file name for a COM interface. File names can be explicitly quoted using double quotes (") to prevent the shell from interpreting the special characters.

</dd> </dl>

## Remarks

The **/iid** switch does not affect RPC interfaces.

If *filename* does not include an explicit path, the file is written to the current directory or to the directory specified by the [**/out**](-out.md) switch. An explicit path in *filename* overrides the **/out** switch specification.

## Examples

**midl /iid "my\_iid.c" filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/header**](-header.md)
</dt> <dt>

[**/out**](-out.md)
</dt> <dt>

[**/proxy**](-proxy.md)
</dt> </dl>

 

 




