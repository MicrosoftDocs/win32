---
description: A private assembly is an assembly that is deployed with an application and is available for the exclusive use of that application.
ms.assetid: 5E0E7423-85BD-4ED0-9149-9541F4D2371F
title: About Private Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# About Private Assemblies

A private assembly is an assembly that is deployed with an application and is available for the exclusive use of that application. That is, other applications do not share the private assembly. Private assemblies are one of the methods that can be used to create [isolated applications](isolated-applications.md). For more information, see [About Isolated Applications and Side-by-Side Assemblies](about-isolated-applications-and-side-by-side-assemblies.md).

Private assemblies must be designed to work side-by-side with other versions of the assembly on the system. For more information, see [Guidelines for Creating Side-by-side Assemblies](guidelines-for-creating-side-by-side-assemblies.md).

Private assemblies must be accompanied by an [assembly manifest](assembly-manifests.md). Note that name restrictions apply when packaging a DLL as a private assembly to accommodate the way in which Windows searches for private assemblies. When searching for private assemblies, the recommended method is to include the assembly manifest in the DLL as a resource. In this case, the resource ID must equal 1 and the name of the private assembly may be the same as the name of the DLL. For example, if the name of the DLL is MICROSOFT.WINDOWS.MYSAMPLE.DLL, the value of the name attribute used in the **assemblyIdentity** element of the manifest may also be Microsoft.Windows.mysample. An alternate method of searching for private assemblies is to provide the assembly manifest in a separate file. In this case, the name of the assembly and its manifest must be different than the name of the DLL. For example, Microsoft.Windows.mysampleAsm, Microsoft.Windows.mysampleAsm.manifest, and Microsoft.Windows.mysample.dll. For more information about how side-by-side searches for private assemblies see [Assembly Searching Sequence](assembly-searching-sequence.md).

Private assemblies are installed in a folder of the application's directory structure. Typically, this is the folder containing the application's executable file. Private assemblies may be deployed in the same folder as the application, in a folder with the same name as the assembly, or in a language specific subfolder with the same name as the assembly. For example, use one of the following directory structures to deploy a private assembly, Microsoft.tools.pop, with no language specified.



| Directory structure                                       | Description                                                                                            |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| APPDIR\\MICROSOFT.TOOLS.POP.DLL                           | The manifest is deployed as a resource in the DLL.                                                     |
| Appdir\\Microsoft.Tools.Pop.MANIFEST                      | The manifest is deployed as a separate file.                                                           |
| APPDIR\\MICROSOFT.TOOLS.POP\\MICROSOFT.TOOLS.POP.DLL      | The manifest is deployed as a resource in the DLL, which is in a subfolder having the assembly's name. |
| Appdir\\Microsoft.Tools.Pop\\Microsoft.Tools.Pop.MANIFEST | The manifest is deployed as a separate file in a subfolder having the assembly's name.                 |



 

> [!IMPORTANT]
>
> For versions of the Windows operating system before Windows 7 and Windows Server 2008 R2, native private assemblies must be deployed in the folder that contains the application's executable file. Installation in a language specific folder or in the folder with same name as assembly is not supported for native private assemblies.

 

Use one of the following directory structures to deploy a private assembly, Microsoft.tools.pop, with a specified language. In the following example, the language used by Microsoft.Tools.Pop is English (United States) and the language code is en-us. You should substitute the correct DHTML language code for your assembly.

``` syntax
appdir\en-us\Microsoft.tools.pop.DLL
appdir\en-us\Microsoft.tools.pop.MANIFEST
appdir\en-us\Microsoft.tools.pop\Microsoft.tools.pop.DLL
appdir\en-us\Microsoft.tools.pop\Microsoft.tools.pop.MANIFEST
```

Private assemblies can be installed by any installation method that can copy the assembly's file into this folder, such as the **xcopy** command. For more information about how to install private assemblies using the Windows Installer, see [Installation of Win32 Assemblies](../msi/installation-of-win32-assemblies.md).

Private assemblies can also be installed on operating systems earlier than Windows XP. In this case, the assembly must be registered and on these operating systems the manifest is not used. A copy of the private assembly is installed into a private folder for the exclusive use of the application. Another version of the assembly can be globally registered on the system and available to any application that binds to it. The global version of the assembly may be the version installed with the application or an earlier version. For more information, see [DLL/COM Redirection on Windows](dll-com-redirection-on-windows.md). An assembly can also be installed as a shared assembly for use by multiple applications. For more information, see [Shared Assemblies](/windows/desktop/Msi/shared-assemblies).

Note that the steps for creating a private assembly are identical to those for creating a shared assembly with two exceptions:

-   A private assembly is not required to be signed, and **publickeyToken** is not required in the **assemblyIdentity** element of the assembly manifest.
-   Private assemblies can be installed into the application's folder using any installation technology. Private assemblies are not required to be installed using the Windows Installer.

 

 
