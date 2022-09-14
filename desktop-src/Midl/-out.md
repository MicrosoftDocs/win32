---
title: /out switch
description: The /out switch specifies the default directory where the MIDL compiler writes output files.
ms.assetid: 37cfe989-137a-4336-8c66-e6b9c23473df
keywords:
- /out switch MIDL
topic_type:
- apiref
api_name:
- /out
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /out switch

The **/out** switch specifies the default directory where the MIDL compiler writes output files.

``` syntax
midl /out path-specification
```

## Switch Options

<dl> <dt>

*path-specification* 
</dt> <dd>

Specifies the path to the directory in which the stub, header, and switch files are generated. A drive specification, an absolute directory path, or both can be specified. Paths can be explicitly quoted using double quotes (") to prevent the shell from interpreting the special characters.

</dd> </dl>

## Remarks

The output directory can be specified with a drive letter, an absolute path name, or both. The **/out** option can be used with any of the switches that enable individual output file specification.

When the **/out** switch is not specified, files are written to the current directory.

The default directory specified by the **/out** switch can be overridden by an explicit path name specified as part of the [**/cstub**](-cstub.md), [**/header**](-header.md), [**/proxy**](-proxy.md), or [**/sstub**](-sstub.md) switch.

## Examples

**midl /out c:\\mydir\\mysubdir\\subdir2 deeper filename.idl**

**midl /out c: filename.idl**

**midl /out \\mydir\\mysubdir\\another filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/cstub**](-cstub.md)
</dt> <dt>

[**/header**](-header.md)
</dt> <dt>

[**/proxy**](-proxy.md)
</dt> <dt>

[**/sstub**](-sstub.md)
</dt> </dl>

 

 




