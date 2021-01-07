---
description: Is similar to a command-line switch. However, you do not need to reenter a \#pragma command each time you compile a MOF file.
ms.assetid: 3cf22686-dd56-43a3-9584-3d707a20a3a0
ms.tgt_platform: multiple
title: '#pragma'
ms.topic: article
ms.date: 05/31/2018
---

# \#pragma

The **\#pragma** preprocessor command is similar to a command-line switch. However, you do not need to reenter a **\#pragma** command each time you compile a MOF file. The following example illustrates **\#pragma** command syntax:


```mof
#pragma [command]
```



You usually place a **\#pragma** command at the beginning of a MOF file. However, you can place some commands, such as the **\#pragma** command, in the body of your MOF code. The following example shows **\#pragma** commands that indicate to the MOF compiler that it must place classes and instances in the root\\cimv2 namespace and compile the file in which the commands are included during repository recovery:


```mof
#pragma autorecover
#pragma namespace ("\\\\.\\root\\cimv2")
```



The following lists the available **\#pragma** commands.



| Command                                         | Description                                                                                           |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**amendment**](pragma-amendment.md)           | Directs the MOF compiler to separate a MOF file into language-neutral and language-specific versions. |
| [**autorecover**](pragma-autorecover.md)       | Adds a MOF file to the list of files compiled during repository recovery.                             |
| [**classflags**](pragma-classflags.md)         | Controls the way classes are created or updated depending on the flags specified.                     |
| [**deleteclass**](pragma-deleteclass.md)       | Deletes an existing class and its instances from the repository.                                      |
| [**deleteinstance**](pragma-deleteinstance.md) | Deletes an existing instance of a class from the repository.                                          |
| [**instanceflags**](pragma-instanceflags.md)   | Controls the way instances are created or updated depending on the flags specified.                   |
| [**namespace**](pragma-namespace.md)           | Requests that the compiler load the MOF file into the namespace specified as *namespacepath*.         |



 

## Related topics

<dl> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 



