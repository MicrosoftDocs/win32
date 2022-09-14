---
title: Compiling the Sample Project
description: Compiling the Sample Project
ms.assetid: c605042e-ec45-44c7-afca-42a874882eab
keywords:
- Windows Media Player online stores,compiling sample projects
- online stores,compiling sample projects
- type 2 online stores,compiling sample projects
- Windows Media Player online stores,sample projects
- online stores,sample projects
- type 2 online stores,sample projects
- Windows Media Player online stores,project wizard
- online stores,project wizard
- type 2 online stores,project wizard
- plug-ins,project wizard
- Windows Media Player plug-ins,project wizard
- compiling sample projects
- samples,type 2 online stores
- project wizard
ms.topic: article
ms.date: 05/31/2018
---

# Compiling the Sample Project

The wizard generates all the files you need to compile the sample project, so you shouldn't need to change the default project settings. In Visual Studio, from the **Build** menu, click **Build Solution** to build and register the COM component. By default, the Debug configuration is active.

> [!Note]  
> In Windows Vista and later, the project will not build successfully unless you run Visual Studio with a full administrator access token. Right-click the Visual Studio name or icon, and click **Run as administrator**.

 

Before attempting to build the project, be sure to configure your development environment to point to the folders named Include and Lib where you installed the Windows SDK. Your compiler and linker will need access to some of the files in these folders.

If you ran the Visual Studio Registration utility that comes with the Windows Vista SDK, your development environment has probably already been configured to point to the Windows SDK Include and Lib folders. Otherwise, you must manually configure your development environment.

To manually configure Visual Studio, use the following steps.

1.  On the **Tools** menu, click **Options**.
2.  Click **Projects and Solutions**, and then click **VC++ Directories**.
3.  Under **Show directories for**, click **Include files** or **Library files**.
4.  Add the directories for the required files.

## Related topics

<dl> <dt>

[Building the Plug-in for a Type 2 Online Store](building-the-plug-in-for-a-type-2-online-store.md)
</dt> </dl>

 

 




