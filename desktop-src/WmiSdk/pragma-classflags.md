---
description: Controls the way WMI creates or updates classes depending on the flags specified.
ms.assetid: ec535662-be14-44dc-ba0f-f9d2cbf630ea
ms.tgt_platform: multiple
title: pragma classflags
ms.topic: reference
ms.date: 06/09/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pragma
api_type: 
- NA
api_location: 
---

# pragma classflags

The `pragma classflags` preprocessor command controls the way WMI creates or updates classes depending on the flags specified.

The following describes the syntax for this command:

```mof
#pragma classflags ("[flag1], [flag2]")
```

*\[Flag\]* must be one or more of the following arguments. You can combine any flags that don't contradict each other.

| Flag | Description |
|-|-|
| createonly | Instructs the compiler not make any changes to existing classes and terminates a compilation if a class specified in the MOF file already exists in WMI. |
| forceupdate | Forces updates of classes when conflicting child classes exist. For example, if you define a class qualifier in a child class and the base class attempts to add the same qualifier, using this flag causes the compiler to resolve this conflict by deleting the conflicting qualifier in the child class. If the child class has instances, the update fails. |
| safeupdate | Allows the compiler to update classes even if child classes exist, if the change does not cause conflicts with child classes. For example, this flag allows you to add a new property to a base class without also having to add the property to any pre-existing child class. |
| updateonly | Instructs the compiler to not create any new classes and causes the compiler to terminate the compilation if a class specified in the MOF file does not exist. |

## Examples

The following example shows how to use this command with the `updateonly` and `forceupdate` flags.

```mof
#pragma classflags ("updateonly", "forceupdate")
```

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client<br/> | Windows Vista |
| Minimum supported server<br/> | Windows Server 2008 |

## See also

* [Preprocessor commands](preprocessor-commands.md)
