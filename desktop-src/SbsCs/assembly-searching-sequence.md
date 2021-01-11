---
description: If an isolated application specifies an assembly dependency, side-by-side first searches for the assembly among the shared assemblies in the WinSxS folder.
ms.assetid: 93496631-55cc-4dd9-9a51-b748c35fd477
title: Assembly Searching Sequence
ms.topic: article
ms.date: 05/31/2018
---

# Assembly Searching Sequence

If an isolated application specifies an assembly dependency, side-by-side first searches for the assembly among the [shared assemblies](/windows/desktop/Msi/shared-assemblies) in the WinSxS folder. If the required assembly is not found, side-by-side then searches for a private assembly installed in a folder of the application's directory structure.

[Private assemblies](/windows/desktop/Msi/private-assemblies) may be deployed in the following locations in the application's directory structure:

-   In the application's folder. Typically, this is the folder containing the application's executable file.
-   In a subfolder in the application's folder. The subfolder must have the same name as the assembly.
-   In a language-specific subfolder in the application's folder. The name of the subfolder is a string of DHTML language codes indicating a language-culture or language.
-   In a subfolder of a language-specific subfolder in the application's folder. The name of the higher subfolder is a string of DHTML language codes indicating a language-culture or language. The deeper subfolder has the same name as the assembly.

The first time side-by-side searches for a private assembly, it determines whether a language-specific subfolder exists in the application's directory structure. If no language-specific subfolder exists, side-by-side searches for the private assembly in the following locations using the following sequence.

1.  Side-by-side searches the WinSxS folder.
2.  \\\\<*appdir*>\\<*assemblyname*>.DLL
3.  \\\\<*appdir*>\\<*assemblyname*>.manifest
4.  \\\\<*appdir*>\\<*assemblyname*>\\<*assemblyname*>.DLL
5.  \\\\<*appdir*>\\<*assemblyname*>\\<*assemblyname*>.manifest

If a language-specific subfolder exists, the application's directory structure may contain the private assembly localized in multiple languages. Side-by-side searches the language-specific subfolders to ensure that the application uses the specified language or the best available language. Language-specific subfolders are named using a string of DHTML language codes that specify a language-culture or language. If a language-specific subfolder exists, side-by-side searches for the private assembly in the following locations using following sequence.

1.  Side-by-side searches the WinSxS folder.
2.  \\\\<*appdir*>\\<*language-culture*>\\<*assemblyname*>.DLL
3.  \\\\<*appdir*>\\<*language-culture*>\\<*assemblyname*>.manifest
4.  \\\\<*appdir*>\\<*language-culture*>\\<*assemblyname*>\\<*assemblyname*>.DLL
5.  \\\\<*appdir*>\\<*language-culture*>\\<*assemblyname*>\\<*assemblyname*>.manifest

Note that the side-by-side search sequence finds a DLL file with the assembly's name and stops before searching for a manifest file having the assembly's name. The recommended way to handle a private assembly that is a DLL is to put the assembly manifest in the DLL file as a resource. The resource ID must be equal to 1 and the name of the private assembly may be the same as the name of the DLL. For example, if the name of the DLL is MICROSOFT.WINDOWS.MYSAMPLE.DLL, the value of the name attribute used in the **assemblyIdentity** element of the assembly's manifest may also be Microsoft.Windows.mysample. As an alternative, you may put the assembly manifest in a separate file, however, the name of the assembly and its manifest must then be different than the name of the DLL. For example, Microsoft.Windows.mysampleAsm, Microsoft.Windows.mysampleAsm.manifest, and MICROSOFT.WINDOWS.MYSAMPLE.DLL.

For example, if myapp is installed at the root of drive c: and requires myasm in French-Belgian, side-by-side uses the following sequence to search for the best approximation to a localized instance of myasm.

1.  Side-by-side searches WinSxS for the fr-be version.
2.  c:\\myapp\\fr-be\\myasm.dll
3.  c:\\myapp\\fr-be\\myasm.manifest
4.  c:\\myapp\\fr-be\\myasm\\myasm.dll
5.  c:\\myapp\\fr-be\\myasm\\myasm.manifest
6.  Side-by-side searches WinSxS for the fr version.
7.  c:\\myapp\\fr\\myasm.dll
8.  c:\\myapp\\fr\\myasm.manifest
9.  c:\\myapp\\fr\\myasm\\myasm.dll
10. c:\\myapp\\fr\\myasm\\myasm.manifest
11. Side-by-side searches WinSxS for the en-us version.
12. c:\\myapp\\en-us\\myasm.dll
13. c:\\myapp\\en-us\\myasm.manifest
14. c:\\myapp\\en-us\\myasm\\myasm.dll
15. c:\\myapp\\en-us\\myasm\\myasm.manifest
16. Side-by-side searches WinSxS for the en version.
17. c:\\myapp\\en\\myasm.dll
18. c:\\myapp\\en\\myasm.manifest
19. c:\\myapp\\en\\myasm\\myasm.dll
20. c:\\myapp\\en\\myasm\\myasm.manifest
21. Side-by-side searches WinSxS for the no language version.
22. c:\\myapp\\myasm.dll
23. c:\\myapp\\myasm.manifest
24. c:\\myapp\\myasm\\myasm.dll
25. c:\\myapp\\myasm\\myasm.manifest

If side-by-side searching reaches a language-neutral version of the assembly, and a [Multilanguage User Interface (MUI)](/windows/desktop/Intl/multilingual-user-interface) version of Windows is present on the system, side-by-side then attempts to bind to <*assemblyname*>.mui. Side-by-side does not attempt to bind to <*assemblyname*>.mui if the search reaches a localized version of the assembly. The [assembly manifest](assembly-manifests.md) of a language-neutral assembly will not have a language attribute in its **assemblyIdentity** element. If side-by-side reaches a language-neutral assembly, and MUI is installed, side-by-side searches the following locations using the following sequence for <*assemblyname*>.mui. Side-by-side uses the same search sequence if the assembly is culture-neutral, except <*no language*> is not searched.

1.  Side-by-side searches the WinSxS folder for <*assemblyname*>.mui.
2.  \\\\<*user's language-culture*>\\<*assemblyname*>.mui
3.  \\\\<*user's language*>\\<*assemblyname*>.mui
4.  \\\\<*system's language-culture*>\\<*assemblyname*>.mui
5.  \\\\<*system's language*>\\<*assemblyname*>.mui
6.  \\\\<*no language*>\\<*assemblyname*>.mui

For example, if side-by-side searching finds the private assembly at c:\\myapp\\myasm\\myasm.manifest, and myasm is a language-neutral assembly. Side-by-side then uses the following sequence to search for myasm.mui. Note that side-by-side will not search for a language-neutral MUI assembly.

1.  Side-by-side searches WinSxS for the fr-be version of the MUI assembly.
2.  c:\\myapp\\fr-be\\myasm.mui.dll
3.  c:\\myapp\\fr-be\\myasm.mui.manifest
4.  c:\\myapp\\fr-be\\myasm\\myasm.mui.dll
5.  c:\\myapp\\fr-be\\myasm\\myasm.mui.manifest
6.  Side-by-side searches WinSxS for the fr version of the MUI assembly.
7.  c:\\myapp\\fr\\myasm.mui.dll
8.  c:\\myapp\\fr\\myasm.mui.manifest
9.  c:\\myapp\\fr\\myasm\\myasm.mui.dll
10. c:\\myapp\\fr\\myasm\\myasm.mui.manifest
11. Side-by-side searches WinSxS for the en-us version of the MUI assembly.
12. c:\\myapp\\en-us\\myasm.mui.dll
13. c:\\myapp\\en-us\\myasm.mui.manifest
14. c:\\myapp\\en-us\\myasm\\myasm.mui.dll
15. c:\\myapp\\en-us\\myasm\\myasm.mui.manifest
16. Side-by-side searches WinSxS for the en version of the MUI assembly.
17. c:\\myapp\\en\\myasm.mui.dll
18. c:\\myapp\\en\\myasm.mui.manifest
19. c:\\myapp\\en\\myasm\\myasm.mui.dll
20. c:\\myapp\\en\\myasm\\myasm.mui.manifest

 

 
