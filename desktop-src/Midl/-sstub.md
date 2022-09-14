---
title: /sstub switch
description: The /sstub switch specifies the name of the server stub file for an RPC interface.
ms.assetid: 8e695e81-7c1b-40c0-aeaa-5390512fa099
keywords:
- /sstub switch MIDL
topic_type:
- apiref
api_name:
- /sstub
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /sstub switch

The **/sstub** switch specifies the name of the server stub file for an RPC interface.

``` syntax
midl /sstub stub_file_name
```

## Switch Options

<dl> <dt>

*stub\_file\_name* 
</dt> <dd>

Specifies a file name that overrides the default server stub file name. File names can be explicitly quoted using double quotes (") to prevent the shell from interpreting the special characters.

</dd> </dl>

## Remarks

The specified file name replaces the default file name. By default, the file name is obtained by adding \_S.C to the name of the IDL file. This switch does not affect OLE interfaces.

When you are importing files, the specified file name applies to only one stub file — the stub file that corresponds to the IDL file specified on the command line.

If *stub\_file\_name* does not include an explicit path, the file is written to the current directory or the directory specified by the [**/out**](-out.md) switch. An explicit path in *stub\_file\_name* overrides the **/out** switch specification.

The **/server** none switch takes precedence over the **/sstub** switch.

## Examples

**midl /sstub my\_sstub.c filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/cstub**](-cstub.md)
</dt> <dt>

[**/header**](-header.md)
</dt> <dt>

[**/out**](-out.md)
</dt> </dl>

 

 




