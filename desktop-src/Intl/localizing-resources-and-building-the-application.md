---
description: This topic describes how to build a typical MUI application.
ms.assetid: 386e9601-ce21-4ef0-b225-0c4249d1942d
title: Localizing Resources and Building the Application
ms.topic: article
ms.date: 05/31/2018
---

# Localizing Resources and Building the Application

This topic describes how to build a typical MUI application. It is assumed that you are using Microsoft Visual Studio for coding and either Microsoft Visual Studio or the Visual Studio command line for building. You are assumed to use an .sln solution file for your application and support a Resource.h file to reflect the base language resource file.

> [!Note]  
> If using the Visual Studio command line for the build, you will use the **vcbuild** command to build the solution file.

 

Application files are built separately for each language. Each build creates identical language-neutral .exe and language-specific .exe.mui files. In addition, various other files are copied to the appropriate release folders.

The application build depends on the type of resources and the type of localization that you are using. For pre-build localization, you have one copy of the base language file localized for each supported language. For post-build localization, you can copy the .mui file resulting from the build of the executable and resource module, and provide the copies to the localizers.

> [!Note]  
> The following procedure assumes Win32 PE resources with one Visual Studio project built for each language. The base language resources are provided in an .rc file and loaded using a DLL module. You can repeat the procedure as needed to build for all languages supported.

 

**To build the application**

1.  Set up a Visual Studio project for the base language.
2.  If interested in using a resource configuration file with the resource tools, set one up as described in [Preparing a Resource Configuration File](preparing-a-resource-configuration-file.md).
3.  Set parameters required by the RC Compiler utility in the property pages for the project under **Configuration Properties → Resources → Command Line → Additional options**.
4.  Run RC Compiler. The utility compiles and splits the non-localizable and localizable resources into two different object files, using resource configuration data. In this step the language-neutral resources are linked into an LN file. For more information, see the utility description in [Resource Utilities](resource-utilities.md).
5.  To link the language-specific resources into a language-specific .mui file, set a post-build event for the project in the property pages under **Configuration Properties → Build Events → Post-Build Event → Command Line**.
6.  Set a post-build event to apply the checksum value from the LN file to the .mui file for the language. You can use the MUIRCT utility for this step. For more information, see the utility description in [Resource Utilities](resource-utilities.md).
7.  Use the post-build event command line to add commands to copy the files into the appropriate release folder structure.

## Related topics

<dl> <dt>

[Using Multilingual User Interface](using-multilingual-user-interface.md)
</dt> <dt>

[Preparing a Resource Configuration File](preparing-a-resource-configuration-file.md)
</dt> <dt>

[Resource Utilities](resource-utilities.md)
</dt> </dl>

 

 



