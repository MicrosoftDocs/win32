---
title: Installing the Online Store Plug-in Wizard
description: Installing the Online Store Plug-in Wizard
ms.assetid: 75f7c279-4800-4146-8198-1dc76472237d
keywords:
- Windows Media Player online stores,plug-ins
- online stores,plug-ins
- type 1 online stores,plug-ins
- Windows Media Player online stores,plug-in wizard
- online stores,plug-in wizard
- type 1 online stores,plug-in wizard
- Windows Media Player online stores,installing plug-in wizard
- online stores,installing plug-in wizard
- type 1 online stores,installing plug-in wizard
- plug-ins,Windows Media Player online stores
- plug-ins,online stores
- plug-ins,type 1 online stores
- plug-ins,installing plug-in wizard
- plug-ins,plug-in wizard
- Windows Media Player plug-ins,type 1 online stores
- Windows Media Player plug-ins,online stores
- Windows Media Player plug-ins,Windows Media Player online stores
- Windows Media Player plug-ins,installing plug-in wizard
- Windows Media Player plug-ins,plug-in wizard
- installing plug-in wizard
- plug-in wizard
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Installing the Online Store Plug-in Wizard

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To set up your development environment for creating type 1 online store plug-ins, you must install the following items:

-   Microsoft Visual Studio 2005 or later
-   Windows Media Player 11 or later
-   Windows SDK, which includes the Windows Media Player SDK
-   Online store plug-in wizard

## Installing the Wizard

Use the following steps to install the online store plug-in wizard in Visual Studio.

1.  Locate the folder where you installed the Windows SDK. Expand the folder to view its subfolders, and navigate to Samples\\Multimedia\\WMP\\wizards\\services.
2.  Locate the following three files:
    -   wmpservices.vsz
    -   wmpservices.vsdir
    -   wmpservices.ico
3.  Using a text editor such as Notepad, edit the wmpservices.vsz file.

    Locate the following line:

    ```
    Wizard=VsWizard.<VsWizardEngine version goes here>
    ```

    

    Change `<VsWizardEngine version goes here>` to one of the following values, depending on which version of Visual Studio you have installed.

    

    | Value              | Visual Studio version |
    |--------------------|-----------------------|
    | VsWizardEngine.8.0 | Visual Studio 2005    |
    | VsWizardEngine.9.0 | Visual Studio 2008    |

    

     

    Locate the following line:

    ```
    Param="ABSOLUTE_PATH = <path to wmpservices directory goes here>"
    ```

    

    Change `<path to wmpservices directory goes here>` to the path where the wizard files are located.

    For example, suppose you have Visual Studio 2008, and your wizard files are here: C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\WMP\\wizards\\services. Then your wmpservices.vsz file would look like this:

    ```
    VSWIZARD 7.0
    Wizard=VsWizard.VsWizardEngine.9.0

    Param="WIZARD_NAME = wmpservices"
    Param="ABSOLUTE_PATH = C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\Multimedia\WMP\wizards\services"
    Param="FALLBACK_LCID = 1033"
    ```

    

4.  Locate the folder where you installed Visual Studio. Expand the folder to view its subfolders, and locate a folder named vcprojects.
5.  Copy the three files listed in step 2 to the vcprojects folder. The wizard is now installed.

## Related topics

<dl> <dt>

[Building the Plug-in for a Type 1 Online Store](building-the-plug-in-for-a-type-1-online-store.md)
</dt> </dl>

 

 




