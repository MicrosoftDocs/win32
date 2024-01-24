---
description: If the MOF compiler cannot finish compiling a MOF file, the WMI repository may be left in an undefined state.
ms.assetid: 13adc666-6588-4cfd-a5eb-17da93434468
ms.tgt_platform: multiple
title: Handling Errors with the MOF Compiler
ms.topic: article
ms.date: 05/31/2018
---

# Handling Errors with the MOF Compiler

If the MOF compiler cannot finish compiling a MOF file, the WMI repository may be left in an undefined state. For example, if you are compiling a MOF file and you use the **-class:createonly** command-line switch, the compilation terminates if a class specified in the MOF file already exists. The MOF compiler stores in the repository any classes or instances that were defined up to the point where the compiler stops. In some cases, this can leave the WMI repository in an undefined condition.

In this situation, you may need to stop WMI, delete the WMI repository, and have WMI rebuild it. All MOF files that contain the [**pragma autorecover**](pragma-autorecover.md) [preprocessor command](preprocessor-commands.md) are rebuilt when WMI is restarted. You must manually recompile any MOF files that do not include a `#pragma autorecover` statement.

For more information about how to declare classes and instances using the MOF syntax, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md).

## Related topics

<dl> <dt>

[Compiling MOF Files](compiling-mof-files.md)
</dt> <dt>

[**mofcomp**](mofcomp.md)
</dt> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 



