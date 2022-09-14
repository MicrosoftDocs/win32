---
title: /cstub switch
description: The /cstub switch specifies the name of the client stub file for an RPC interface.
ms.assetid: f2c9e083-3511-4e72-b1d1-14a3a662ffaf
keywords:
- /cstub switch MIDL
topic_type:
- apiref
api_name:
- /cstub
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /cstub switch

The **/cstub** switch specifies the name of the client stub file for an RPC interface.

``` syntax
midl /cstub stub_file_name
```

## Switch Options

<dl> <dt>

*stub\_file\_name* 
</dt> <dd>

Specifies a file name that overrides the default client stub file name. File names can be explicitly quoted using double quotes (") to prevent the shell from interpreting the special characters.

</dd> </dl>

## Remarks

The specified file name replaces the default file name. By default, the file name is obtained by adding the extension \_c.c to the name of the IDL file. This switch does not affect OLE interfaces.

When you are importing files, the specified file name applies to only one stub file — the stub file that corresponds to the IDL file specified on the command line.

If *stub\_file\_name* does not include an explicit path, the file is written to the current directory or the directory specified by the [**/out**](-out.md) switch. An explicit path in *stub\_file\_name* overrides the **/out** switch specification.

The **/client** none switch takes precedence over the **/cstub** switch.

## Examples

**midl /cstub my\_cstub.c filename.idl**

## See also

<dl> <dt>

[**/header**](-header.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/out**](-out.md)
</dt> <dt>

[**/sstub**](-sstub.md)
</dt> </dl>

 

 




