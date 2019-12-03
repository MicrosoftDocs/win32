---
title: /header switch
description: The /header switch specifies the name of the header file.
ms.assetid: d36cb6c9-df57-4ef4-aff3-9968ac8ac001
keywords:
- /header switch MIDL
topic_type:
- apiref
api_name:
- /header
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /header switch

The **/header** switch specifies the name of the header file.

``` syntax
midl /header filename
```

## Switch Options

<dl> <dt>

*filename* 
</dt> <dd>

Specifies a header file name that overrides the default header file name. File names can be explicitly quoted using double quotes (") to prevent the shell from interpreting special characters.

</dd> </dl>

## Remarks

The specified file name replaces the default file name. The default file name is obtained by replacing the IDL file name extension (usually .idl) with the file name extension .h. For OLE interfaces, the **/header** switch overrides the default name of the interface header file.

When you are importing files, the specified file name applies to only one header file — the header file that corresponds to the IDL file specified on the command line.

If *filename* does not include an explicit path, the file is written to the current directory or the directory specified by the [**/out**](-out.md) switch. An explicit path in *filename* overrides the **/out** switch specification.

## Examples

**midl /header "bar.h" filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/h**](-h.md)
</dt> <dt>

[**/cstub**](-cstub.md)
</dt> <dt>

[**/out**](-out.md)
</dt> <dt>

[**/sstub**](-sstub.md)
</dt> <dt>

[**/proxy**](-proxy.md)
</dt> </dl>

 

 




