---
title: Type Library Viewers and Conversion Tools
description: Type Library Viewers and Conversion Tools
ms.assetid: 35c29e2c-3ee3-4e73-b925-6aa0ccb50a00
ms.topic: article
ms.date: 05/31/2018
---

# Type Library Viewers and Conversion Tools

Type libraries contain the specification for one or more COM elements, including classes, interfaces, enumerations, and more. These files are stored in a standard binary format. A type library can be a stand-alone file with the .tlb file name extension, or it can be stored as a resource in an executable file, which can have an .ocx, .dll, or .exe file name extension. The type library viewers and conversion tools described following read this format to gain information about the COM elements in the library.

Before you can program an object in a particular programming language, you must be able to view its type library in that language. Doing this provides you with the proper syntax for the classes, interfaces, methods, properties, and events of the COM object.

Microsoft development products provide the following tools that you can use to generate, extract, and view type library information.

## C++

-   [OLE-COM Object Viewer](ole-com-object-viewer.md)
-   [MIDL compiler](midl-compiler.md)
-   [MkTypLib](mktyplib-command-line-tool.md)

## Visual Basic

-   [Visual Basic Object Browser](visual-basic-object-browser.md)

## Java

-   [JActiveX](jactivex-command-line-tool.md)
-   [Java Type Library Wizard](java-type-library-wizard.md)
-   [JavaTLB](javatlb-command-line-tool.md)

For an overview of how these tools interact with type libraries, see [How Developer Tools Use Type Libraries](how-developer-tools-use-type-libraries.md).

 

 




