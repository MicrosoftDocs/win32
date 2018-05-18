---
title: Supporting Visual Styles in Snap-ins
description: Visual styles are a feature of Windows and are supported by MMC 2.0. Your snap-in should support visual styles for improved user interface (UI) experience and consistency.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd1d8ed92-94a0-4217-8a31-dd2a127998a0'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Supporting Visual Styles in Snap-ins

Visual styles are a feature of Windows and are supported by MMC 2.0. Your snap-in should support visual styles for improved user interface (UI) experience and consistency.

When your snap-in supports visual styles, UI elements (such as dialog boxes) that are created by your snap-in will display in the visual style selected by the user.

To support visual styles, create a manifest resource to your snap-in DLL. The manifest resource indicates that your snap-in uses Microsoft Common Control version 6 (Comctl32.dll) if it is available (otherwise, it uses an earlier version of Microsoft Common Control).

The following sections provide information about how to support visual styles in your snap-in:

-   [Create a manifest resource](#create-a-manifest-resource)
-   [Include Microsoft Common Control](#include-microsoft-common-control)
-   [Set the ISOLATION\_AWARE\_ENABLED directive](#set-the-isolation-aware-enabled-directive)
-   [Reference the manifest file](#reference-the-manifest-file)

For more information and a list of additional steps necessary to support themes in MFC snap-ins, see [Supporting Visual Styles in MFC Snap-ins](supporting-visual-styles-in-mfc-snap-ins.md).

## Create a manifest resource

To support visual styles, your snap-in must have a manifest resource that uses the Microsoft Common Controls version 6.0 assembly. The manifest resource consists of XML. The manifest file is of the following format:


```XML
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
 <assemblyIdentity
    version="1.0.0.0"
    processorArchitecture="X86"
    name="YourCompanyName.YourDivision.YourApp"
    type="win32"/>
 <description>Your app description here</description>
 <dependency>
  <dependentAssembly>
   <assemblyIdentity
      type="win32"
      name="Microsoft.Windows.Common-Controls"
      version="6.0.0.0"
      processorArchitecture="X86"
      publicKeyToken="6595b64144ccf1df"
      language="*"/>
  </dependentAssembly>
 </dependency>
</assembly>
```



You can choose the values for your **name** and **description** attributes. If you are building for a 64-bit architecture, indicate it with the appropriate value for both occurrences of **processorArchitecture**. Other than the values for **name**, **description** and **processorArchitecture** (if necessary), do not change the text in the manifest.

Specify a name for the manifest file. This example assumes the file is named "YourApp.manifest", and the file is in the same folder as your snap-in's resource file (.rc).

## Include Microsoft Common Control

Include the common control header file in your snap-in source.


```C++
#include "commctrl.h"
```



## Set the ISOLATION\_AWARE\_ENABLED directive

Compile your snap-in with the -D ISOLATION\_AWARE\_ENABLED flag, or insert the following statement before the `#include "windows.h"` statement.


```C++
#define ISOLATION_AWARE_ENABLED 1
```



## Reference the manifest file

Define a manifest resource ID of 2.


```C++
#define MANIFEST_RESOURCE_ID 2
```



In your resource script (.rc) file, use the manifest resource ID to define a resource of type **RT\_MANIFEST**. The manifest file that you created corresponds to the **RT\_MANIFEST** resource.

``` syntax
MANIFEST_RESOURCE_ID RT_MANIFEST "YourApp.manifest"
```

Your snap-in is ready to compile and test.

 

 




