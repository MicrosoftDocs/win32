---
title: DirectX Installation for Game Developers
description: This article is intended to address some of the common questions about the DirectX runtime, and using DirectSetup to install DirectX.
ms.assetid: 2ab439be-8d99-bcf8-89af-d4274e044c88
ms.topic: article
ms.date: 05/31/2018
---

# DirectX Installation for Game Developers

This article is intended to address some of the common questions about the DirectX runtime, and using DirectSetup to install DirectX.

-   [DirectX Runtime](#directx-runtime)
-   [DirectX Version Number](#directx-version-number)
-   [DirectX Libraries](#directx-libraries)
-   [Installation of DirectX by the Game's Installer](#installation-of-directx-by-the-games-installer)
-   [Small Installation Packages](#small-installation-packages)
-   [Internal Deployment of the Debug DirectX Runtime](#internal-deployment-of-the-debug-directx-runtime)

> [!IMPORTANT]
> The legacy DirectX SDK is at end-of-life, but it's still available in order to support old games, tutorials, and projects. New projects should not use it. Using the legacy DirectX SDK requires the use of the deprecated DirectSetup for components such as D3DX9, D3DX10, D3DX11, XAudio 2.7, XInput 1.3, and XACT. For more details on the current state of the DirectX SDK, see [Where is the DirectX SDK?](../directx-sdk--august-2009-.md), and the blog post [Not So Direct Setup](https://walbourn.github.io/not-so-direct-setup/).

## DirectX Runtime

The DirectX runtime consists of core components and optional components.

The core components, such as Direct3D and DirectInput, are considered part of the operating system. The core components for DirectX 9.0c have not changed since the DirectX SDK Summer 2004 Update, and they match what was released with Microsoft Windows XP SP2, Windows XP Pro x64 Edition, and Windows Server 2003 SP1. Windows Vista includes DirectX 10, which supports the Windows Display Driver Model (WDDM) and Direct3D 10.x. Windows 7 and Windows Vista (see [KB971644](https://support.microsoft.com/kb/971644)) support DirectX 11, which supports Direct3D 11, Direct2D, DirectWrite, the WARP10 software rendering device, and the 10level9 feature levels. See [Graphics APIs in Windows](/windows/desktop/direct3darticles/graphics-apis-in-windows-vista) for more details.

The optional components are released in updates of DirectX SDK, and they include D3DX, XACT, XAudio2, XINPUT, Managed DirectX, and other such components. Many of the optional components are regularly updated to integrate customer feedback and expose new features.

## DirectX Version Number

The DirectX version number, such as 9.0c, refers only to the version of the core components, such as Direct3D, DirectInput, or DirectSound. This number does not cover the versions of the various optional components that are released in the DirectX SDK, such as D3DX, XACT, XINPUT, and so on.

Generally speaking, the DirectX version number is not meaningful except as a quick reference to the core run-time bits. This number should not be used to check if the correct DirectX runtime is already installed, because it doesn't take into account the optional DirectX components.

## DirectX Libraries

In the past, the optional components of the DirectX SDK, including D3DX, were released as static libraries. However, these are now released as dynamic-like libraries (DLL) because of the increased demand for better security practices. DLLs allow servicing of previously released code. If these components were deployed as static libraries, there would be no way for Microsoft to address security issues found after release.

As features are added or changed to the optional components, the names of the corresponding DLLs are also changed to ensure that no regressions are caused to existing games that are using released components. The DLLs for each component live side by side, and game developers can choose exactly which DLL version that the game uses by linking to the corresponding import library.

While ensuring that DLLs are installed on a system isn't as easy as simply linking to static libraries, some changes have been made to the DirectX SDK to address the pain of the DLL model:

-   The DirectX redistributable can be configured to contain only those components that your application requires to minimize distribution and media sizes.
-   The redistributable folder, Program Files\\DirectX SDK\\Redist\\, now contains a cabinet (.cab) file for every possible optional component, so you don't have to dig up an older SDK to find them.
-   Installing the SDK itself installs every possible optional component.
-   A DirectX redistributable that contains all the optional components is available as both a Web-based installer and as a downloadable package; see the DirectX Developer Center ([DirectX](/previous-versions/windows/apps/hh452744(v=win.10))) for more information.

## Installation of DirectX by the Game's Installer

> [!Note]  
> See [Direct3D 11 Deployment for Game Developers](/windows/desktop/direct3darticles/direct3d11-deployment).

 

The following are the best practices for adding installation of DirectX to a game's installer:




| Term | Description | 
|------|-------------|
| <span id="Install_the_redistributable_components_every_time.__"></span><span id="install_the_redistributable_components_every_time.__"></span><span id="INSTALL_THE_REDISTRIBUTABLE_COMPONENTS_EVERY_TIME.__"></span>Install the redistributable components every time. <br /> | A game's installation process should install the DirectX redistributable components during every single installation without allowing users to opt-out of it. If you allow opting-out, then some users will guess that they don't need it, and if they actually do, the game will not run. <br /> | 
| <span id="Let_the_DirectX_installer_check_for_optional_components.__"></span><span id="let_the_directx_installer_check_for_optional_components.__"></span><span id="LET_THE_DIRECTX_INSTALLER_CHECK_FOR_OPTIONAL_COMPONENTS.__"></span>Let the DirectX installer check for optional components. <br /> | Do not assume that the latest optional components are already installed on a system, because Windows Update and Service Packs do not provide any of DirectX's optional components. You must install the DirectX runtime either by running dxsetup.exe directly or calling DirectSetup. <br /> | 
| <span id="Set_up_silently.__"></span><span id="set_up_silently.__"></span><span id="SET_UP_SILENTLY.__"></span>Set up silently. <br /> | Launch setup in silent mode so that users do not accidentally skip updating the DirectX runtime. You can do this by launching dxsetup.exe with the following command: <br /><pre class="syntax" data-space="preserve"><code>   path-to-redistributable\dxsetup.exe /silent</code></pre>or by calling DirectSetup and not showing any UI. <br /> | 
| <span id="Combine_EULA_acceptances.__"></span><span id="combine_eula_acceptances.__"></span><span id="COMBINE_EULA_ACCEPTANCES.__"></span>Combine EULA acceptances. <br /> | If you prompt the user to accept a EULA, then combine that with prompting for acceptance of the DirectX EULA when installing in silent mode so that prompting for acceptance of EULAs happens just once. Prompting should happen before you install anything so that if user doesn't accept, you don't end up with a failed and partial installation. <br /> | 
| <span id="Just_run_dxsetup_or_call_DirectSetup.__"></span><span id="just_run_dxsetup_or_call_directsetup.__"></span><span id="JUST_RUN_DXSETUP_OR_CALL_DIRECTSETUP.__"></span>Just run dxsetup or call DirectSetup. <br /> | Because the DirectX version number doesn't refer to anything except the core DirectX components, do not check an installed version before running dxsetup.exe or calling DirectSetup. Also, do not check for a file's existence to test if an optional component is already installed, since this usually will not correctly determine when a component exists but needs updating. However, the DirectX setup package will quickly determine this, and perform the right action. <br /> | 




 

## Small Installation Packages

You can create smaller installation packages for DirectX by stripping the contents of the DirectX redistributable folder down to the minimal set of files required to make the installer work, and retaining any additional components that your game uses.

Depending on your minimum specifications, you might not even need to include the core DirectX 9.0c cabinet files in the redistributable folder of your installation media. A large majority of Windows XP installations have Service Pack 2, which includes the core DirectX 9.0c components, so the DirectX setup operation will be very fast, and will not require a reboot. The smallest package that can be created is about 3 MB, and it can be compressed to about half that size. A package like this contains one version of the D3DX DLL, and it requires that DirectX 9.0c be already present.

The minimal set of files that are required to build a redistributable package are the following files, located in the DirectX SDK Redist folder (Program Files\\DirectX SDK\\Redist\):

-   dxsetup.exe
-   dsetup32.dll
-   dsetup.dll
-   dxupdate.cab

Add to these the cabinet files for the components that you want to install. If you require the users of your application to already have DirectX 9.0c, then you do not need to include DirectX.cab or dxnt.cab, which make up most of the space requirement. DirectX.cab is only needed for Windows 98 and Windows ME; dxnt.cab is only needed for Windows 2000, Windows XP, and Windows XP SP1; and dxdllreg\_x86.cab is only required for Windows 2000, Windows XP RTM, Windows XP SP1, and Windows Server 2003 RTM. Also, if you do not make use of DirectShow, or you assume that it is already installed, you can omit BDA.cab, BDANT.cab, and BDAXP.cab.

> [!Note]  
> You can assume that users of your application already have DirectX 9.0c if it was installed by a previous version of your application, you force users to manually update via the Web Installer, or you assume that they have Windows XP SP2 or later.

 

Continuing with this example, if you are using only the 32-bit version of D3DX for April 2006, you can add Apr2006\_d3dx9\_30\_x86.cab. If you are using the 32-bit August 2006 32-bit version of XINPUT, you add Aug2006\_xinput\_x86.cab.

If you have a native 64-bit application, you'll need to add the \_x64 versions. However, if you have a 32-bit application running on a 64-bit OS, the 32-bit versions of the DLLs will work.

You can then distribute this package of files and launch DirectSetup in silent mode or run dxsetup.exe in the command shell in silent mode. Remember not to guard this package by any version checking of files, and make sure that your users cannot opt out of running the DirectX setup. Either of these events creates a fallible installation process.

## Internal Deployment of the Debug DirectX Runtime

The debug runtimes of the DirectX components are installed when the DirectX SDK is installed, but installing the SDK on every test computer can be painful. You need to design your setup process to copy the debug runtime DLLs from Program Files\\Microsoft DirectX SDK\\Developer Runtime\\architecture\\ to Windows\\system32\\ or to the game's folder.

However, we strongly recommend that you do not simply copy the released run-time DLLs because it is easy to forget to remove them for the final product. Instead, put the DirectX setup files in a shared folder and run the setup silently from the shared folder.

## Desktop Bridge applications 

Desktop Bridge applications that use D3DX9, D3DX10, D3DX11, XAudio 2.7, XInput 1.3, or XACT must download either the [Microsoft.DirectX.x86](https://download.microsoft.com/download/c/c/2/cc291a37-2ebd-4ac2-ba5f-4c9124733bf1/UAPSignedBinary_Microsoft.DirectX.x86.appx) or the [Microsoft.DirectX.x64](https://download.microsoft.com/download/c/c/2/cc291a37-2ebd-4ac2-ba5f-4c9124733bf1/UAPSignedBinary_Microsoft.DirectX.x64.appx) framework in order to deploy these legacy DirectX SDK side-by-side components. Alternatively, you can remove all such dependencies&mdash;(see [Developer guide for redistributable version of XAudio 2.9](../xaudio2/xaudio2-redistributable.md), and the blog posts [Living without D3DX](https://walbourn.github.io/living-without-d3dx/) and [XINPUT and Windows 8](https://walbourn.github.io/xinput-and-windows-8/)).
