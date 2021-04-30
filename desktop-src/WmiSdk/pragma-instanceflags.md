---
description: Controls the way instances are created or updated depending on the flags specified.
ms.assetid: 9932edf2-2e5f-4c5e-9889-f2be4af11bf2
ms.tgt_platform: multiple
title: pragma instanceflags
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pragma
api_type: 
- NA
api_location: 
---

# pragma instanceflags

The **pragma instanceflags** preprocessor command controls the way instances are created or updated depending on the flags specified.

The following describes the syntax:


```mof
#pragma instanceflags ([Flag])
```



*\[Flag\]* must be one of the following arguments.



| Flag       | Description                                                                                                |
|------------|------------------------------------------------------------------------------------------------------------|
| createonly | Prevents the compiler from changing any existing instances in the MOF file.                                |
| updateonly | Prevents the compiler from creating new instances if an instance specified in the MOF file does not exist. |



 

## Examples

The following example shows how to use this command.


```mof
#pragma instanceflags("createonly")
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 




