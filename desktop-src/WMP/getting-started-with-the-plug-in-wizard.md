---
title: Getting Started with the Plug-in Wizard
description: Getting Started with the Plug-in Wizard
ms.assetid: 77fc1b0c-20f5-434d-9142-f112489a7f08
keywords:
- Windows Media Player plug-ins,installing plug-in wizard
- plug-ins,installing plug-in wizard
- building plug-ins,installing plug-in wizard
- Windows Media Player Plug-in Wizard,installing
- installing plug-in wizard
- plug-in wizard
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Getting Started with the Plug-in Wizard

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To set up your development environment for creating Windows Media Player plug-ins, you must install the following items:

-   Microsoft Visual Studio .NET 2003 or later
-   Windows Media Player 9 Series or later
-   Windows SDK, which includes the Windows Media Player SDK
-   Windows Media Player Plug-in Wizard

## Installing the Wizard

Perform the following steps to install the Windows Media Player Plug-in Wizard.

1.  Locate the folder where you installed the Windows SDK. Expand the folder to view its subfolders, and navigate to Samples\\Multimedia\\WMP\\wizards\\wmpwiz.
2.  Locate the following three files:
    -   wmpwiz.vsz
    -   wmpwiz.vsdir
    -   wmpwiz.ico
3.  Using a text editor, such as Notepad, edit the wmpwiz.vsz file.

    Locate the following line:

    ```
    Wizard=VsWizard.<VsWizardEngine version goes here>
    ```

    

    Change `<VsWizardEngine version goes here>` to one of the following values, depending on which version of Visual Studio you have installed.

    

    | Value              | Visual Studio version   |
    |--------------------|-------------------------|
    | VsWizardEngine.7.1 | Visual Studio .NET 2003 |
    | VsWizardEngine.8.0 | Visual Studio 2005      |
    | VsWizardEngine.9.0 | Visual Studio 2008      |

    

     

    Locate the following line:

    ```
    Param="ABSOLUTE_PATH = <path to wmpwiz directory goes here>"
    ```

    

    Change `<path to wmpwiz directory goes here>` to the path where the wizard files are located.

    For example, suppose you have Visual Studio 2008, and your wizard files are here: C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\WMP\\wizards\\wmpwiz. Then your wmpwiz.vsz file would look like this:

    ```
    VSWIZARD 7.0
    Wizard=VsWizard.VsWizardEngine.9.0

    Param="WIZARD_NAME = Windows Media Player Plug-in Wizard"
    Param="ABSOLUTE_PATH = C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\Multimedia\WMP\wizards\wmpwiz"
    Param="FALLBACK_LCID = 1033"
    ```

    

4.  Locate the folder where you installed Visual Studio. Expand the folder to view its subfolders, and locate a folder named vcprojects.
5.  Copy the three files listed in step 2 to the vcprojects folder. The wizard is now installed.

## Related topics

<dl> <dt>

[Building a Plug-in](building-a-plug-in.md)
</dt> <dt>

[Using the Plug-in Wizard with Visual Studio](using-the-plug-in-wizard-with-visual-studio.md)
</dt> </dl>

 

 




