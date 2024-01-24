---
description: Creating the Base Language Resource File
ms.assetid: 770e1f4b-5258-4b6b-afa4-5c19743daaaa
title: Creating the Base Language Resource File
ms.topic: article
ms.date: 05/31/2018
---

# Creating the Base Language Resource File

Resources for user interface elements are defined for the basic language that the application supports, for example, English (United States). An example of a Win32 PE resource file is an .rc file, created using RC Compiler. For details of .rc file creation, see [About Resource Files](../menurc/about-resource-files.md).

If using an .rc file for the base language resources, you have the option of using a resource configuration file for an XML representation of resource configuration data. To create this file, see [Preparing a Resource Configuration File](preparing-a-resource-configuration-file.md).

You can also use a non-Win32 PE file to define base language resources. For example, you might use an .xml file or .txt file for this purpose.

> [!Note]  
> When you define base language resources using a non-Win32 PE file, you cannot use RC Compiler for resource definition. Instead, you define your own resource format, and your application must provide its own functionality to find and load the required resources.

 

## Related topics

<dl> <dt>

[Preparing Resources](preparing-resources.md)
</dt> <dt>

[Preparing a Resource Configuration File](preparing-a-resource-configuration-file.md)
</dt> </dl>

 

 
