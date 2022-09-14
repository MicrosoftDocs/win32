---
title: Saving Preprocessor Output
description: Viewing preprocessor output can be an effective troubleshooting method, such as when invalid IDL, C, or C-preprocessor syntax occurs, or when bogus -D values on the MIDL command line result in MIDL reporting arcane errors.
ms.assetid: 79c53f0c-c179-4731-a2c3-a1022d378e7b
keywords:
- MIDL compiler MIDL , saving preprocessor output
ms.topic: article
ms.date: 05/31/2018
---

# Saving Preprocessor Output

Viewing preprocessor output can be an effective troubleshooting method, such as when invalid IDL, C, or C-preprocessor syntax occurs, or when bogus -D values on the MIDL command line result in MIDL reporting arcane errors. Developers may also want to examine preprocessor output to determine which files and definitions were present in the compiler input stream, such as when a difficult case of type redefinition conflict must be resolved. Or less commonly, certain developers may want to force private switches on the preprocessor with [**/cpp\_opt**](-cpp-opt.md), or may want to see how the switches work.

The easiest and the least obtrusive way to obtain the preprocessed files from a MIDL compile run is to use the [**-savePP**](-savepp.md) switch. The **-savePP** switch simply prevents MIDL from deleting the temporary files that the preprocessor passes back to MIDL. Consider the following:

**midl -savePP -Id:\\nt\\public\\sdk\\inc -DNTENV=1 -Oicf -env win32 stub.idl**

This directive compiles Stub.idl, yet preserves all preprocessor files.

> [!Note]  
> MIDL spawns separate preprocessor runs for IDL and ACF file (if present) as well as for every imported file.

 

For a DCOM compile, several preprocessor files are typically produced, even though they are processed by MIDL as a virtual contiguous input stream. In a typical Windows programming environment, the temporary files can be found in the Temp directory as file names such as MID\*.tmp. If preserving preprocessor output, it is good practice to watch for recent files in the Temp directory to identify which files are associated with which preprocessor run.

In simple cases, such as when the compiled IDL file does not import other files directly or indirectly, or when examining the top-level file, the preprocessor can be invoked directly. Executing C/C++ preprocessor directly can reveal errors masked or confused by MIDL. For example, the following two preprocessor command lines can be used for the previously quoted MIDL line:

**cl /E /nologo -Id:\\nt\\public\\sdk\\inc -DNTENV=1 stub.idl > stub.pp**

**cl /E /P -Id:\\nt\\public\\sdk\\inc -DNTENV=1 stub.idl**

In the first of these two examples, **/E** [**/nologo**](-nologo.md) are the switches that MIDL adds when invoking the preprocessor. The preprocessor output is sent to stdout (the screen), and therefore requires redirection to a file for examination. In the second of these examples, **/P** directs the preprocessor to redirect the output to a \*.i file; in this case a Stub.i file would be created in the current directory.

The [**/cpp\_opt**](-cpp-opt.md) switch can also be used to obtain a preprocessed file, but is difficult and inferior to the previously mentioned methods. The following example also produces a Stub.i file, as did the previous example. The quotes in the following example are essential:

**Midl -Oicf -win32 -cpp\_opt "/E /P -Id:\\nt\\public\\sdk\\inc -DNTENV=1" stub.idl**

 

 




