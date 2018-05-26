---
title: How to Create a Visual Studio Project for an MI Provider
description: While you can use the Convert-MofToProvider tool to generate the source code files for an MI provider and then build those files at the command prompt, using a robust IDE such as Microsoft Visual Studio makes the process much easier.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E2904906-21C9-4B02-9EC5-93BF749C6D7F
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to: Create a Visual Studio Project for an MI Provider

While you can use the **Convert-MofToProvider** tool to generate the source code files for an MI provider and then build those files at the command prompt, using a robust IDE such as Microsoft Visual Studio makes the process much easier. This topic illustrates how to create an empty Win32 DLL project to which you can subsequently add the MI provider source code files generated using the **Convert-MofToProvider** tool.

1.  Start Visual Studio.
2.  Create a new project by clicking **&lt;Ctrl&gt;&lt;Shift&gt;&lt;N&gt;**.
3.  When the **New Project** dialog displays, expand the **Templates** entry on the left side of the dialog until you locate the **Win32** entry. Click that template.
4.  In the **Name** field, specify the name for your project. One technique is to use the following form: **&lt;ProviderName&gt;Provider**. For example, if you're writing an MI provider to enable management of Win32 processes, you might want to call the provider **Process**, which would yield a project name of **ProcessProvider**.
5.  Click **OK**.
6.  When the **Win32 Application Wizard** displays, click **Next** to display the **Application Settings** page.
7.  Under **Application type**, select **DLL**.
8.  Under **Additional options**, select **Empty project**.
9.  Click **Finish** to generate the project.
10. Once you've created the Visual Studio project that will house your MI provider, the next step is to [generate an MI Provider from a MOF file](how-to-generate-an-mi-provider-from-a-mof-file.md).

 

 




