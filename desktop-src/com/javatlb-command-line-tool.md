---
title: JavaTLB Command-Line Tool
description: JavaTLB Command-Line Tool
ms.assetid: b46d7bcc-ccd9-4242-9b19-f398d2cb8f91
ms.topic: article
ms.date: 05/31/2018
---

# JavaTLB Command-Line Tool

JavaTLB is a component of Visual J++ 5.0. JavaTLB is a command-line application that generates class files for a COM object. Methods that contain data types that cannot be accurately and safely represented in Java are not converted.

Unlike the [Java Type Library Wizard](java-type-library-wizard.md), JavaTLB does not generate a summary file containing the Java type library information.

To generate Java class files for a single COM object, from the command prompt run:

**javatlb** *filename*

where *filename*is the name of the file that contains the type library. This file may have any of the following file name extensions: .tlb, .olb, .ocx, .dll, or .exe.

To generate Java class files for multiple COM objects, from the command prompt run:

**javatlb @***TextFile*

where *TextFile* is the name of a text file that contains a list of the files containing the COM object's type libraries.

> [!Note]  
> In Visual J++ 6.0, the JavaTLB command-line tool is replaced by the [JActiveX tool](jactivex-command-line-tool.md). For more information, see the Visual J++ 6.0 documentation.

 

## Related topics

<dl> <dt>

[Translating to Java](translating-to-java.md)
</dt> </dl>

 

 




