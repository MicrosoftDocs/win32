---
description: Resource preparation for a MUI application supports both Win32 PE and non-Win32 PE models.
ms.assetid: e528dac7-c157-42d7-808d-709a4ae84f1e
title: Preparing Resources
ms.topic: article
ms.date: 05/31/2018
---

# Preparing Resources

Resource preparation for a MUI application supports both Win32 PE and non-Win32 PE models. Win32 PE resources are provided in PE-based files, such as .dll, .exe, or .sys files. Non-Win32 PE resources are furnished in a customized module of your choosing.

> [!Note]  
> It is highly recommended for you to use Win32 PE resources for Win32 MUI applications, as these resources are completely supported by the MUI resource technology. Non-Win32 PE resource files can be located by calling the [**GetFileMUIPath**](/windows/desktop/api/Winnls/nf-winnls-getfilemuipath) function as described in [Locating Non-Win32 PE Resources](locating-non-win32-pe-resources.md), but the application must provide its own functionality to find and load the required resources.

 

This section contains the following topics:

-   [Creating the Base Language Resource File](creating-the-base-language-resource-file.md)
-   [Using Registry String Redirection](using-registry-string-redirection.md)
-   [Preparing a Resource Configuration File](preparing-a-resource-configuration-file.md)

 

 



