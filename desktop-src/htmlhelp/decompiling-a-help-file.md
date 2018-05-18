---
title: Decompiling a Help File
description: Decompiling a help file involves copying the files in a compiled help file to a directory that you specify while leaving the compiled help file intact.
ms.assetid: '2A738852-F135-487b-9C1B-8194C06A80A0'
---

# Decompiling a Help File

Decompiling a help file involves copying the files in a compiled help file to a directory that you specify while leaving the compiled help file intact. This procedure is useful for reconstructing individual HTML source files from a compiled help file. It is also useful when you want to use the source files contained in the compiled help file in a browser that does not support compiled help files.

## To decompile a help file

1.  On the **File** menu, click **Decompile**.
2.  In the **Destination folder** box, enter the name of the folder where you want the decompiled files to be copied.
3.  In the **Compiled help file** box, enter the name of the compiled help (.chm) file you want to decompile.

> [!Note]  
> The decompile command is part of the HTML Help executable program (Hh.exe) and is therefore also a client-side command line switch that works when HTML Help Workshop is not set up. From a DOS prompt or from the **Run** command, type **-decompile** *folder* *chm* where **-decompile** is the switch, *folder* is the name of the destination folder where you want the decompiled files to be copied, and *chm* is the name of the compiled help file you want to decompile.

 

## Related topics

<dl> <dt>

[About Compiling a Help Project](compile-a-help-project.md)
</dt> </dl>

 

 




