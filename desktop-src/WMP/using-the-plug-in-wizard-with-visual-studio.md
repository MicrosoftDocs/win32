---
title: Using the Plug-in Wizard with Visual Studio
description: Using the Plug-in Wizard with Visual Studio
ms.assetid: 5d5521b7-5cbc-4259-92b1-a7250853fa2e
keywords:
- Windows Media Player plug-ins,Visual Studio
- plug-ins,Visual Studio
- building plug-ins,Visual Studio
- Windows Media Player Plug-in Wizard,Visual Studio
- Visual Studio,Windows Media Player Plug-in Wizard
- plug-in wizard
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Plug-in Wizard with Visual Studio

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

After you have installed the necessary components, you can quickly create a plug-in that will serve as a starting point. The following steps will guide you.

1.  Start Microsoft Visual Studio.
2.  From the **File** menu, point to **New** and then click **Project**.
3.  In **Project Types**, select **Visual C++ Projects**.
4.  In **Templates**, select **Windows Media Player Plug-in Wizard**.
5.  Enter a name for your project.
6.  Enter a location for your project. This is the folder to which your project files will be copied.
7.  Click **OK** to start the wizard.
8.  Select the type of plug-in you want to create.
9.  Complete any remaining dialog boxes in the wizard.
10. Use the Visual Studio development environment to build your project.
    > [!Note]  
    > In Windows Vista and later, the project will not build successfully unless you run Visual Studio with a full administrator access token. Right-click the Visual Studio name or icon, and click **Run as administrator**.

     

Before attempting to build the project, be sure to configure your development environment to point to the folders named Include and Lib where you installed the Windows SDK. Your compiler and linker will need access to some of the files in these folders.

If you ran the Visual Studio Registration utility that comes with the Windows SDK, your development environment has probably already been configured to point to the Windows SDK Include and Lib folders. Otherwise, you must manually configure your development environment.

To manually configure Visual Studio, use the following steps.

1.  On the **Tools** menu, click **Options**.
2.  Click **Projects and Solutions**, and then click **VC++ Directories**.
3.  Under **Show directories for**, click **Include files** or **Library files**.
4.  Add the directories for the required files.

## Related topics

<dl> <dt>

[Building a Plug-in](building-a-plug-in.md)
</dt> </dl>

 

 




