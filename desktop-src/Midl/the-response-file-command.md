---
title: The Response File Command
description: A response file is a text file containing one or more MIDL compiler command-line options.
ms.assetid: ad47ea1a-fe7a-4354-be2f-599ba77685ee
keywords:
- command-line reference MIDL , response file command
ms.topic: article
ms.date: 05/31/2018
---

# The Response File Command

A response file is a text file containing one or more MIDL compiler command-line options. Unlike a command line, a response file allows multiple lines of options and file names. This may be useful due to limitations of your build environment, or as a convenience for your build process.

## Switch Options

``` syntax
midl @response_file
```

<dl> <dt>

<span id="response_file"></span><span id="RESPONSE_FILE"></span>*response\_file*
</dt> <dd>

Specifies the name of a response file. The response file name must immediately follow the @ character. No white space is allowed between the @ character and the response file name.

</dd> </dl>

## Remarks

As an alternative to placing all options associated with a switch on the command line, the MIDL compiler accepts response files that contain switches and arguments. Options in a response file are interpreted as if they are present in that location in the MIDL command line.

Each argument in a response file must begin and end on the same line. The backslash character (\\) cannot be used to concatenate lines. When it is part of a quoted string in the response file, the backslash character can only be used before another backslash or before a double quotation mark character ("). When it is not part of a quoted string, the backslash character can only be used before a double quotation mark character.

MIDL supports command-line arguments that include one or more response files combined with other command-line switches.

The MIDL compiler does not support nested response files.

## Examples

**midl @midl.rsp**

**midl -Oicf @midl1.rsp -env win32 @midl2.rsp itf.idl**

## Related topics

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 




