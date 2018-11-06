---
title: About Resource Files
description: Describes how to include resources in your Windows-based application with RC.
ms.assetid: af7c7aed-5d28-40ac-ad00-da0986fd89c1
ms.topic: article
ms.date: 05/31/2018
---

# About Resource Files

To include resources in your Windows-based application with RC, do the following:

1.  Create individual files for your cursors, icons, bitmaps, dialog boxes, and fonts.
2.  Create a resource-definition script (.rc file) that describes the resources used by your application.
3.  Compile the script with RC. For more information, see [Using RC (The RC Command Line)](using-rc-the-rc-command-line-.md).
4.  Link the compiled resource (.res) file into the application's executable file with your linker.

A resource file is a text file with the extension .rc. The file can use single-byte, double-byte, or Unicode characters. The syntax and semantics for the RC preprocessor are similar to those of the Microsoft C/C++ compiler. However, RC supports a subset of the preprocessor directives, defines, and pragmas in a script.

The script file defines resources. For a resource that exists in a separate file, such as an icon or cursor, the script specifies the resource and the file that contains it. For some resources, such as a menu, the entire definition of the resource exists within the script.

The following topics describe the information a script file can contain:

-   [Comments](comments.md), which are notes to be ignored by RC.
-   [Predefined macros](predefined-macros.md), which take no arguments and cannot be redefined.
-   [Preprocessor directives](preprocessor-directives.md), which instruct RC to perform actions on the script before compiling it.
-   [Preprocessor operators](preprocessor-operators.md), which are used with the **\#define** directive.
-   [Pragma directives](pragma-directives.md)
-   [Resource-definition statements](resource-definition-statements.md), which name and describe resources.

 

 




