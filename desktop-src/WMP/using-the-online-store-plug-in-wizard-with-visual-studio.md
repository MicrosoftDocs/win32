---
title: Using the Online Store Plug-in Wizard with Visual Studio
description: Using the Online Store Plug-in Wizard with Visual Studio
ms.assetid: 0bf670cd-897d-4cd6-ae95-ae16b2dacc96
keywords:
- Windows Media Player online stores,plug-ins
- online stores,plug-ins
- type 1 online stores,plug-ins
- Windows Media Player online stores,plug-in wizard
- online stores,plug-in wizard
- type 1 online stores,plug-in wizard
- Windows Media Player online stores,Visual Studio
- online stores,Visual Studio
- type 1 online stores,Visual Studio
- plug-ins,Windows Media Player online stores
- plug-ins,online stores
- plug-ins,type 1 online stores
- plug-ins,Visual Studio
- plug-ins,plug-in wizard
- Windows Media Player plug-ins,type 1 online stores
- Windows Media Player plug-ins,online stores
- Windows Media Player plug-ins,Windows Media Player online stores
- Windows Media Player plug-ins,Visual Studio
- Windows Media Player plug-ins,plug-in wizard
- Visual Studio,Windows Media Player Online Stores Wizard
- plug-in wizard
ms.topic: article
ms.date: 05/31/2018
---

# Using the Online Store Plug-in Wizard with Visual Studio

After you have installed the necessary components, you can quickly create a plug-in that will serve as a starting point. The following steps will guide you:

1.  Start Microsoft Visual Studio.
2.  From the **File** menu, point to **New** and then click **Project**.
3.  In **Project Types**, click **Visual C++ Projects**.
4.  In **Templates**, click **Windows Media Player Online Stores Wizard**.
5.  Enter a name for your project.
6.  Enter a location for your project. This is the folder to which your project files will be copied.
7.  Click **OK** to start the wizard.
8.  Select **Type 1 (Deep integration)**, and click **Next**.
9.  Enter a friendly name and a content distributor. Click **Finish**.
10. Use the Visual Studio development environment to build your project.
    > [!Note]  
    > In Windows Vista and later, the project will not build successfully unless you run Visual Studio with a full administrator access token. Right-click the Visual Studio name or icon, and click **Run as administrator**.

     

Before attempting to build the project, be sure to configure your development environment to point to the folders named Include and Lib where you installed the Windows SDK. Your compiler and linker will need access to some of the files in these folders.

If you ran the Visual Studio Registration utility that comes with the Windows SDK, your development environment has probably already been configured to point to the Windows SDK Include and Lib folders. Otherwise, you must manually configure your development environment.

To manually configure Visual Studio, use the following steps.

1.  On the **Tools** menu, click Options.
2.  Click **Projects and Solutions**, and then click **VC++ Directories**.
3.  Under **Show directories for**, click **Include files** or **Library files**.
4.  Add the directories for the required files.

## Related topics

<dl> <dt>

[Building the Plug-in for a Type 1 Online Store](building-the-plug-in-for-a-type-1-online-store.md)
</dt> </dl>

 

 




