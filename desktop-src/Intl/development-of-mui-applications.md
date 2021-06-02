---
description: This topic summarizes the main programming considerations to keep in mind when adding MUI functionality to your applications.
ms.assetid: 10064f5c-5563-44f8-afb5-c6c77991e13c
title: Development of MUI Applications
ms.topic: article
ms.date: 05/31/2018
---

# Development of MUI Applications

This topic summarizes the main programming considerations to keep in mind when adding MUI functionality to your applications.

## Requirements for a MUI Application

MUI functionality is applied only to the localization of a fully globalized application, created using a process called software internationalization. The Microsoft [Go Global Developer Center](https://msdn.microsoft.com/goglobal) provides a wide selection of related documentation that helps you design, build, and deploy world-ready applications. These documents help you consider how the characteristics of different human languages can affect the design of your software. Note that the portal also provides a complete archive of Dr. International columns.

Your MUI application can run under any language or locale setting, and the user can request any language for which the application includes support. Therefore, the application must encode user interface text to support the widest possible variety of languages. The most important thing to remember is to use [Unicode](unicode.md) to handle all text processing. For more information about globalization using Unicode, see the Microsoft [Go Global Developer Center](https://msdn.microsoft.com/goglobal).

## Supported Programming Environments

You can add MUI functionality to a globalized Win32 forms application or console application as described in this SDK. In addition, you can create managed applications using .NET Framework, which is compatible with MUI. For more information, see [.NET Development](/previous-versions/ff361664(v=vs.100)).

## User Interface Language Settings

When planning your MUI application, you must first decide on the languages for the user interface and the way to present them to the user. The application can support languages in one of these ways:

-   Follow system language settings. Assume that the user preferred UI languages and the system preferred UI languages, taken together, represent the languages available to the user. Use the fallback mechanism of the resource loader for language selection.
-   Make application-specific language settings. Support specific languages and present a selection mechanism to the user.

## Resource Creation

This section describes the possibilities for creating the user interface language resources for the application. For more information, see [Preparing Resources](preparing-resources.md).

> [!Note]  
> On pre-Windows Vista operating systems, you generally create static and separately packaged single-language localized applications with the languages supported by resource sections included in the executable files. This type of implementation is largely obsolete, and you are recommended to choose one of the other resource creation techniques described in this section, supported for Windows Vista and later. The application can then be made to run on pre-Windows Vista operating systems by the use of [**LoadMUILibrary**](/windows/desktop/api/Muiload/nf-muiload-loadmuilibrarya).

 

### Use of a Single Language in a Resource DLL (MUI Resource Technology)

A standard satellite DLL resource implementation is used by many Microsoft applications. In this case, a core executable file is used for the MUI application and one resource DLL is created for each supported language. Use of a satellite DLL applies to applications that run on any Windows operating system. As described in [MUI Resource Management](mui-resource-management.md), the MUI resource technology supports a variation on the standard satellite DLL implementation.

### Use of Multiple Languages in a Resource DLL

You can choose to create one core executable file for your MUI application and one resource DLL for the resources associated with supported languages. Copies of the same resource identifier are defined in the base language resource file (.rc extension) under different language tags for all supported languages.

### Use of an Application-Specific Resource Mechanism

You can plan your MUI application to use a customized resource mechanism. In this case, the application handles its resource loading in a specialized way.

## Resource Localization

To support the user interface languages for your MUI application, you must have the language resources localized. MUI supports two types of localization, as described in the following table.



| Localization type       | Description                                                                                                                                                                                                                                                                |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pre-build localization  | Request localization before building the application and language-specific resources. The base language resource file for the supported user interface languages is copied and renamed for each supported language, and the copies are provided to localizers as required. |
| Post-build localization | Request localization after building the executable file and resource DLL for your application. In this case, a copy of the resource DLL is provided to each localizer.                                                                                                     |



 

## Related topics

<dl> <dt>

[About Multilingual User Interface](about-multilingual-user-interface.md)
</dt> </dl>

 

 
