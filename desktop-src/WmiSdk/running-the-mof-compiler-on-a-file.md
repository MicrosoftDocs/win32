---
description: 'You have two choices when compiling a MOF file: using the command-line utility or using a programmatic interface.'
ms.assetid: 1760f1bd-7027-4201-97a2-ca902f945b52
ms.tgt_platform: multiple
title: Running the MOF Compiler on a File
ms.topic: article
ms.date: 05/31/2018
---

# Running the MOF Compiler on a File

You have two choices when compiling a MOF file: using the command-line utility or using a programmatic interface.

Until you run the MOF compiler, [**Mofcomp.exe**](mofcomp.md), a provider is not registered with WMI and the classes it created in the MOF file are not available in the [*WMI repository*](gloss-w.md). The following procedure describes how to compile a MOF file.

**To run the MOF compiler on a file from the command line**

1.  Call the MOF compiler from the command line, using the following syntax.

    **mofcomp** *MOFfile***.mof**

    The MOF compiler supports a variety of switches to control special processing situations. All of the switches are optional, and any combination of switches is allowed. However, it does not make sense to use some of the switches in combination with others. For example, to combine the **-class:updateonly** and **-class:createonly** switches results in the compiler not performing any action.

    By default, Mofcomp.exe stores the compiled classes in the root\\default WMI namespace. Note that the default namespace for Mofcomp.exe is not the same as the default namespace for scripting. The default namespace for scripting is specified in the WMI Control on the Advanced tab. For more information, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md).

    You can change the namespace that receives the classes in two ways.

    1.  Use the **-N** switch for the **mofcomp** command.
    2.  Insert the preprocessor command \#[**pragma namespace**](pragma-namespace.md) in the MOF file.

2.  Optionally, you can compile a MOF file programmatically. For more information, see [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler).

## Related topics

<dl> <dt>

[Compiling MOF Files](compiling-mof-files.md)
</dt> <dt>

[**mofcomp**](mofcomp.md)
</dt> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 



