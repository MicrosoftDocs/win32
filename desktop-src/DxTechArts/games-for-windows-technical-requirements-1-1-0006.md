---
title: Games for Windows Technical Requirements Best Practices for Games on Windows XP, Windows Vista, Windows 7, and Windows 8
description: This article provides technical requirements and best practices for games that run on Windows.
ms.assetid: 8b816e9f-de68-cf84-1501-a9c36c6b75d8
ms.topic: article
ms.date: 05/31/2018
---

# Games for Windows Technical Requirements: Best Practices for Games on Windows XP, Windows Vista, Windows 7, and Windows 8

This article provides technical requirements and best practices for games that run on Windows. We wrote these technical requirements and best practices primarily to cover Windows Vista and Windows 7, as well as the legacy Windows XP operating system. These best practices also generally apply to desktop Win32 games on Windows 8.

This articles contains these sections:

-   [Differences for Windows 8](#differences-for-windows-8)
    -   [Additional Information](#additional-information)
-   [Games for Windows](#games-for-windows-technical-requirements-best-practices-for-games-on-windows-xp-windows-vista-windows-7-and-windows-8)
    -   [1.1 Games Explorer Integration](#11-games-explorer-integration)
    -   [1.2 Support Family Safety / Parental Controls](/windows)
    -   [1.3 Support Rich Saved Games](#13-support-rich-saved-games)
    -   [1.4 Support the Xbox 360 Common Controller for Windows \[Conditional Requirement\]](#14-support-the-xbox-360-common-controller-for-windows-conditional-requirement)
    -   [1.5 Support Multiple Aspect Ratios and Resolutions](#15-support-multiple-aspect-ratios-and-resolutions)
    -   [1.6 Support Launch from Windows Media Center](#16-support-launch-from-windows-media-center)
    -   [1.7 Direct3D Support](#17-direct3d-support)
    -   [1.8 Enable High-DPI-Aware](#18-enable-high-dpi-aware)
-   [Security and Compatibility](#security-and-compatibility)
    -   [2.1 Follow User Account Control Guidelines](#21-follow-user-account-control-guidelines)
    -   [2.2 Support Windows x64 Versions](#22-support-windows-x64-versions)
    -   [2.3 Sign Files](#23-sign-files)
    -   [2.4 Sign Drivers](#24-sign-drivers)
    -   [2.5 Perform Proper Version Checking](#25-perform-proper-version-checking)
    -   [2.6 Support Concurrent User Sessions](#26-support-concurrent-user-sessions)
    -   [2.7 Support Long Names](#27-support-long-names)
-   [Installation](#32-support-user-account-control-for-installation)
    -   [3.1 Support Easy Installation](#31-support-easy-installation)
    -   [3.2 Support User Account Control for Installation](#32-support-user-account-control-for-installation)
    -   [3.3 Install to Correct Folders](#33-install-to-correct-folders)
    -   [3.4 Install Windows Resources Properly](#34-install-windows-resources-properly)
    -   [3.5 Avoid Reboots During Installation](#35-avoid-reboots-during-installation)
    -   [3.6 Use File Versioning Correctly](#36-use-file-versioning-correctly)
    -   [3.7 Support Autorun \[Conditional Requirement\]](#37-support-autorun-conditional-requirement)
-   [Reliability](#reliability)
    -   [4.1 Eliminate Unnecessary Reboots](#41-eliminate-unnecessary-reboots)
    -   [4.2 Eliminate Application Verifier Failures](#42-eliminate-application-verifier-failures)
    -   [4.3 Support Windows Error Reporting and File Version Information](#43-support-windows-error-reporting-and-file-version-information)
-   [Xbox 360 Common Controller for Windows Terminology](#xbox-360-common-controller-for-windows-terminology)
-   [Guidelines for Game Middleware Products](#guidelines-for-game-middleware-products)
    -   [Introduction](#introduction)
    -   [Additional Recommendations](#additional-recommendations)
    -   [Games for Windows Showcases](#games-for-windows-showcases)
-   [Resources](#resources)

## Differences for Windows 8

Here is a summary of the key differences when applying these technical requirements and best practices to Windows 8.

<dl> <dt>

<span id="The_Games_Explorer_UI_is_not_visible"></span><span id="the_games_explorer_ui_is_not_visible"></span><span id="THE_GAMES_EXPLORER_UI_IS_NOT_VISIBLE"></span>**The Games Explorer UI is not visible**
</dt> <dd>

All games that you register with the [Games Explorer](/previous-versions/windows/desktop/legacy/hh437965(v=vs.85)) are surfaced as tiles in new Windows UI, but much of the metadata that is associated with the title is no longer visible. You still use the Games Definition File Maker tool (GDFMAKER.EXE), which is now available in the Windows Software Development Kit (SDK), to author the metadata. You also use the existing mechanisms for deploying the metadata. Continue to test your Games Explorer registration by using Windows 7, and verify that the new Windows UI tile shows up when you install it on Windows 8 (see [1.1 Games Explorer Integration](#11-games-explorer-integration)).

To download the Windows 8 SDK, see [Downloads for developing desktop apps](https://msdn.microsoft.com/windows/desktop/aa904949).

</dd> <dt>

<span id="Registration_with_the_Game_Explorer_APIs_continues_to_be_the_mechanism_for_registering_your_game_with_Windows_Parental_Controls"></span><span id="registration_with_the_game_explorer_apis_continues_to_be_the_mechanism_for_registering_your_game_with_windows_parental_controls"></span><span id="REGISTRATION_WITH_THE_GAME_EXPLORER_APIS_CONTINUES_TO_BE_THE_MECHANISM_FOR_REGISTERING_YOUR_GAME_WITH_WINDOWS_PARENTAL_CONTROLS"></span>**Registration with the Game Explorer APIs continues to be the mechanism for registering your game with Windows Parental Controls**
</dt> <dd>

We recommend that you run the Windows SDK version of GDFMAKER on the released version of Windows 8 to ensure that it can populate all currently supported rating systems.

> [!Note]  
> This version of GDFMAKER requires .NET 4.0.

 

See [1.2 Support Family Safety / Parental Controls](/windows).

</dd> <dt>

<span id="There_are_now_three_choices_for_using_the_XINPUT_API_depending_on_your_requirements"></span><span id="there_are_now_three_choices_for_using_the_xinput_api_depending_on_your_requirements"></span><span id="THERE_ARE_NOW_THREE_CHOICES_FOR_USING_THE_XINPUT_API_DEPENDING_ON_YOUR_REQUIREMENTS"></span>**There are now three choices for using the XINPUT API depending on your requirements**
</dt> <dd>

XINPUT 1.4 is built into Windows 8. Both Windows Store apps and desktop Win32 apps can use XINPUT 1.4. All versions of Windows can use XINPUT 9.1.0 for simplified common controllers, but there is no redistribution package with XINPUT 9.1.0. All versions of Windows can also use the existing DirectX SDK version XINPUT 1.3, which requires DirectSetup to deploy.

See [1.4 Support the Xbox 360 Common Controller for Windows](#14-support-the-xbox-360-common-controller-for-windows-conditional-requirement).

</dd> <dt>

<span id="Only_a_limited_set_of_desktop_Win32_apps_are_supported_on_"></span><span id="only_a_limited_set_of_desktop_win32_apps_are_supported_on_"></span><span id="ONLY_A_LIMITED_SET_OF_DESKTOP_WIN32_APPS_ARE_SUPPORTED_ON_"></span>**Only a limited set of desktop Win32 apps are supported on Windows RT**
</dt> <dd>

Games that run on Windows 7 can and should run correctly on Windows 8 x86 and x64 platforms.

See [2.2 Support Windows x64 Versions](#22-support-windows-x64-versions).

</dd> <dt>

<span id="Ensure_any_OS_checks_are_done_correctly"></span><span id="ensure_any_os_checks_are_done_correctly"></span><span id="ENSURE_ANY_OS_CHECKS_ARE_DONE_CORRECTLY"></span>**Ensure any OS checks are done correctly**
</dt> <dd>

The Windows 8 OS version is  6.2 . Windows 8 passes the current  minimum bar  tests that we recommend for game deployment.

</dd> <dt>

<span id="The__DirectX_End-User_Redistribution__package_runs_successfully_on_Windows_8__as_it_does_on_Windows_7__to_deploy_D3DX9__D3DX10__D3DX11__XINPUT_1.3__XAUDIO_2.7__XACTEngine__and_so_on"></span><span id="the__directx_end-user_redistribution__package_runs_successfully_on_windows_8__as_it_does_on_windows_7__to_deploy_d3dx9__d3dx10__d3dx11__xinput_1.3__xaudio_2.7__xactengine__and_so_on"></span><span id="THE__DIRECTX_END-USER_REDISTRIBUTION__PACKAGE_RUNS_SUCCESSFULLY_ON_WINDOWS_8__AS_IT_DOES_ON_WINDOWS_7__TO_DEPLOY_D3DX9__D3DX10__D3DX11__XINPUT_1.3__XAUDIO_2.7__XACTENGINE__AND_SO_ON"></span>**The  DirectX End-User Redistribution  package runs successfully on Windows 8, as it does on Windows 7, to deploy D3DX9, D3DX10, D3DX11, XINPUT 1.3, XAUDIO 2.7, XACTEngine, and so on**
</dt> <dd>

But, a known issue exists with DirectSetup on systems with only .NET 4.0 installed due to the deployment handling of the legacy Managed DirectX 1.1 assemblies. This issue applies to both Windows 8, which comes with .NET 4.5 by default, and  fresh  Windows XP computers with the .NET 4.0 runtime installed. But, this issue does not apply to any version of .NET prior to .NET 4.0. While Windows 8 has an application compatibility behavior to resolve this issue automatically (which requires network access), we recommend that games that continue to deploy DirectSetup update to the DirectX SDK (June 2010) refreshed version of the REDIST files. As always, if you use DirectSetup for your title, trim your title down to the minimum required set of CABs.

See [3.4 Install Windows Resources Properly](#34-install-windows-resources-properly).

</dd> <dt>

<span id="Games_that_require_the_.NET__2.0__compatible_runtime__2.0__3.0__3.5__continue_to_use_existing_deployment_mechanisms"></span><span id="games_that_require_the_.net__2.0__compatible_runtime__2.0__3.0__3.5__continue_to_use_existing_deployment_mechanisms"></span><span id="GAMES_THAT_REQUIRE_THE_.NET__2.0__COMPATIBLE_RUNTIME__2.0__3.0__3.5__CONTINUE_TO_USE_EXISTING_DEPLOYMENT_MECHANISMS"></span>**Games that require the .NET  2.0  compatible runtime (2.0, 3.0, 3.5) continue to use existing deployment mechanisms**
</dt> <dd>

These games trigger an application compatibility behavior on Windows 8 to enable the .NET 3.5 runtime automatically (which requires network access). But, we recommend that .NET developers move to the .NET 4.0 runtime.

> [!Note]  
> The legacy Managed DirectX 1.1 assemblies are not compatible with the .NET 4.x runtime.

 

See [3.4 Install Windows Resources Properly](#34-install-windows-resources-properly).

</dd> <dt>

<span id="Use_of_an__autorunner__or_other_pre-install_technology_that_relies_on_.NET_is_not_recommended"></span><span id="use_of_an__autorunner__or_other_pre-install_technology_that_relies_on_.net_is_not_recommended"></span><span id="USE_OF_AN__AUTORUNNER__OR_OTHER_PRE-INSTALL_TECHNOLOGY_THAT_RELIES_ON_.NET_IS_NOT_RECOMMENDED"></span>**Use of an  autorunner  or other pre-install technology that relies on .NET is not recommended**
</dt> <dd>

You can assume that only .NET 2.0 compatible runtimes (2.0, 3.0, 3.5) are present on Windows Vista and Windows 7. Only the .NET 4.0 compatible runtime is present on Windows 8 by default.

See [3.7 Support Autorun](#37-support-autorun-conditional-requirement).

</dd> <dt>

<span id="There_is_an_updated_Application_Verifier_for_Windows_8"></span><span id="there_is_an_updated_application_verifier_for_windows_8"></span><span id="THERE_IS_AN_UPDATED_APPLICATION_VERIFIER_FOR_WINDOWS_8"></span>**There is an updated Application Verifier for Windows 8**
</dt> <dd>

The Windows 8 SDK includes this updated Application Verifier.

See [4.2 Eliminate Application Verifier Failures](#42-eliminate-application-verifier-failures).

</dd> </dl>

### Additional Information

<dl>

[Windows 8 and Windows Server 2012 compatibility cookbook](/windows/desktop/w8cookbook/windows-8-and-windows-server-8-compatibility-cookbook-portal)  
[Where is the DirectX SDK?](/windows/desktop/directx-sdk--august-2009-)  
</dl>

## Games for Windows

**Summary of Games Requirements**

**Customer Benefits**

Computer games are a key entertainment experience on Windows, but ease-of-use concerns have caused customer frustration over the years. Traditionally, games are installed like applications, but they are utilized more like entertainment media (movies or songs, for example). Innovations, such as Games Explorer, expose games in a consistent manner that is different from standard applications. These innovations also give games first-class citizen status in Windows, together with Music and Pictures. The following requirements help ensure that Windows Vista and Windows 7 provide an improved, more accessible, and unified gaming experience. At the same time, they ensure compatibility with Windows XP.

### 1.1 Games Explorer Integration

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game must be visible within Games Explorer (the **Games** folder) on Windows Vista and Windows 7. When selected, the game must also display correct meta data, which includes publisher, developer, release date, version, Windows Experience Index scores, rating (if applicable), and associated hyperlinks.

If the game is digitally distributed through an online game service, then the service provider should also appear in Games Explorer. To ensure proper handling of the provider and to enable use of RSS feeds, version 2 of the schema for game definition files (GDFs) should be used. (For more information about GDFs, see Additional Information.)

In addition, game installers must observe the following rules when they run on Windows Vista and Windows 7:

-   The installation must not create a shortcut to launch the game on the desktop, in the Start menu, or in any other location.
-   Tasks and shortcuts for removal must not be created.
-   Users must be able to remove the game by using Programs and Features in Control Panel on Windows Vista and Windows 7, or Add or Remove Programs in Control Panel on Windows XP.

On Windows XP, and on previous versions of Windows, the game installer is free to create program groups, desktop icons, or shortcuts as needed.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Windows Games Explorer is similar in concept to the Windows XP folders **My Documents** or **My Pictures**. The idea is to centralize similar content in one place and allow for easier organization and context-sensitive activities. Games Explorer extends the **My Documents** or **My Pictures** concept by allowing richer organization and control over games. Games Explorer allows gamers to view, organize, and interact with all the games installed on their systems. It also allows game publishers to communicate important game information more effectively. The system is data-driven, making it easy for a game publisher to update game information over the life of the product.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Integration with Games Explorer requires that you author a game definition file (GDF), which is an XML text file that is embedded within a binary file (an executable file or a DLL) as a resource, along with a Windows icon. The game must then be registered with Games Explorer. The GDF also enables the exposure of supplied information such as the game title, publisher, developer, links to websites and optional tasks. Note that support tasks can be only links to Web sites, but play tasks can be used for optional support tasks as well.

Games Explorer can make use of a thumbnail bitmap image, but it is recommended that, instead, you provide a Windows icon resource with large icons (256 256). The icon resource should include image sizes of 256 256 48 48, 32 32, and 16 16 in both 24-bit (True Color) and 8-bit (256) color depths. The icon editor provided in Visual Studio 2008 and 2010 supports these large icon formats, as does IconWorkshop Lite.

Details on integrating with **Windows Games Explorer** are provided in the DirectX SDK. The DirectX SDK includes a game definition file (GDF) editor, as well as an example GDF that is included in GDFExampleBinary, a sample. Another sample, GameUxInstallHelper, provides routines for integrating the required functionality into existing installation systems. The Game Definition File Validator (gdftrace.exe) provides debugging support for evaluating a GDF. Also see "Windows Games Explorer Integration" in the DirectX SDK Documentation for C++.

Windows 7 introduces support for the second version of a schema for GDF files. The new version includes a simplified method for creating play tasks and support for update notifications, game service providers, game statistics, and RSS feeds for game service providers. The latest version of GameUxInstallHelper handles all of the registration and legacy support needed to use a version 2 GDF file with Windows Vista. Use the tools and sample code from the DirectX SDK from August 2009 or later. Using a version 2 GDF file is recommended to enable support for RSS feeds, game statistics, and update notifications. Also, see the samples ProviderGDFExampleBinary and GameStatisticsExample.

On Windows Vista Business Edition, Windows 7 Professional Edition, and Enterprise Edition of both Windows Vista and Windows 7, the Games link on the Start menu is hidden. Games Explorer is still available on the Start menu by clicking **All Programs**, and then clicking **Games**.

For associated applications that are installed with your game, but not themselves games, you are free to create Start menu program groups, shortcuts, and desktop icons on all versions of Windows, including Windows Vista and Windows 7. Such associated applications should pass applicable Games for Windows requirements; for details, see [Guidelines for Game Middleware Products](#guidelines-for-game-middleware-products). Game services are encouraged to register with Games Explorer as a Game Provider for Windows 7. 1

</dd> </dl>

### 1.2 Support Family Safety / Parental Controls

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games must fully support Windows Family Safety by adhering to the following rules:

-   Games must not require that the user have administrative credentials to play. Installation, patching, and removal can require administrative credentials, subject to the requirements in section 3. (Related to this is requirement 2.1, Follow User Account Control Guidelines.)
-   Games rated by Windows-supported ratings boards, such as ESRB and PEGI, must include their assigned ratings information in their game definition file (GDF). All available ratings data must be included in every localized version of the GDF, as well as in the language-neutral version.
-   Games must list their executables in the GDF to provide a good user experience for General Application Restrictions, unless the game uses an anti-piracy technology that creates randomly named executables at runtime.
-   Games must call the **VerifyAccess** method of the Games Explorer interface during startup, if available, and exit if it returns \*pfHasAccess as FALSE.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

All games must execute within the context of a Standard User account to allow accounts that are controlled by Windows Parental Controls to play the game. Parents want the ability to monitor and control their children's access to games. Moreover, numerous industry, government and advocacy groups desire better ways to allow parents to monitor and control the games to which their children are exposed. In conjunction with the architecture offered by Games Explorer, Microsoft provides parents this ability through Windows Parental Controls.

Even for games that do not participate in a ratings board program, requiring elevated privileges creates a poor play experience for the majority of user accounts. This is particularly the case if Parental Controls are enabled, which would require the parent to enter the administrator password every time the game is launched.

The Windows Parental Controls system allows parents to select the ratings that they believe are appropriate for their children. Parental Controls support many of the worldwide ratings systems. Parental Controls also allow parents to restrict access to games based on Content Descriptors (if the applicable rating system supports them) and to allow or disallow access to individual games.

The default choice of rating system for Windows Parental Controls is based on the system's locale setting, but can be modified by the user in **Regional and Language Options** in **Control Panel**. Therefore, every supported language should provide all available ratings data so that the user has the freedom to select whatever ratings board they desire.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Games without a rating must still meet the requirements to support play as a Standard User and to call **VerifyAccess**. Such games default to the Unrated category, display the text "No Rating Provided" in Games Explorer, and are subject to the **Game Restrictions** setting in **Parental Controls** for unrated games. The default **Restrictions** setting is Allow.

Rating information in the GDF will be ignored if the containing binary is not properly Authenticode signed. See requirement 2.3.

The Game Definition File Editor in the DirectX SDK includes all supported ratings systems and will correctly replicate this information to all localized versions of the GDF, as well as a language neutral version. The GDFTrace tool will decode and verify all ratings information present. Use the August 2009 version or later of these tools.

The GDF for a game provider typically contains no rating information, and it is subject to the settings for unrated content.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operating System</th>
<th>Supported rating systems</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Vista</td>
<td><ul>
<li>CERO (Japan)</li>
<li>ESRB (USA)</li>
<li>OFLC (Australia)</li>
<li>PEGI (Europe)</li>
<li>PEGI Finland (deprecated)</li>
<li>PEGI Portugal</li>
<li>PEGI/BBFC (United Kingdom)</li>
<li>USK (Germany)</li>
</ul></td>
</tr>
<tr class="even">
<td>Windows Vista with a service pack</td>
<td>Service packs for Windows Vista add support for the following:<br/>
<ul>
<li>GRB (South Korea)</li>
<li>ESRB &quot;Mild&quot; variant content descriptors</li>
</ul></td>
</tr>
<tr class="odd">
<td>Windows 7</td>
<td>Windows 7 supports the ratings systems supported by Windows Vista and adds support for the following: <br/>
<ul>
<li>CSRR (Taiwan)</li>
</ul></td>
</tr>
<tr class="even">
<td>Windows 8</td>
<td>Windows 8 supports the previous ratings systems and adds support for the following:<br/>
<ul>
<li>COB-AU (Australia)</li>
<li>DJCTQ (Brazil)</li>
<li>PFB (South Africa)</li>
<li>OFLC-NZ (New Zealand)</li>
</ul>
Windows 8 retires support for the following now deprecated systems:<br/>
<ul>
<li>PEGI-FI (Finland)</li>
<li>OFLC (Australia)</li>
</ul></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> Any title that includes new ESRB Windows Vista Service Pack 1 (SP1) content descriptors will show as  Unrated  on Windows Vista without a service pack.

 

Newer ratings data are ignored on versions of operating systems without support for them. The PEGI (Finland) variant is now deprecated in favor of the standard PEGI (Europe) rating system. The OFLC system is now deprecated in favor of COB-AU for Australia.

For more information about making a game compatible with standard user privileges, see the DirectX article [User Account Control for Game Developers](/windows/desktop/DxTechArts/user-account-control-for-game-developers).

See requirement 1.1 for more details on the game definition file (GDF).

</dd> </dl>

### 1.3 Support Rich Saved Games

\[This requirement has been retired\]

### 1.4 Support the Xbox 360 Common Controller for Windows \[Conditional Requirement\]

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games that support gamepad controllers must support the Xbox 360 Controller for Windows using the [XInput](/windows/desktop/xinput/xinput-game-controller-apis-portal) API. If DirectInput peripherals are also supported, then DirectInput can also be used. However, XInput must be the default API if an Xbox 360 compatible device is used.

All references to common controller triggers and buttons must use the Xbox 360 names. See the [Xbox 360 Common Controller for Windows Terminology](#xbox-360-common-controller-for-windows-terminology) list for details.

Controller vibration must be turned off when the game is in a paused or suspended state.

Mouse/keyboard control cannot be fully disabled at any time. At a minimum, an option to return to game menus must be available.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

This requirement gives gamers freedom of choice to use either the Xbox 360 controller or the keyboard and mouse, depending on which input method is more natural and intuitive interface.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

This requirement does not apply to games that use only the mouse and/or the keyboard.

We recommend that menu navigation be implemented to use the widely accepted standard controller buttons:

-   A - Accept
-   B - Cancel
-   Start - Accept or pause
-   Back - Cancel, back one screen or up a menu level

For more info, see [XInput](/windows/desktop/xinput/xinput-game-controller-apis-portal).

The topic [XInput and DirectInput](/windows/desktop/xinput/xinput-and-directinput) discusses issues with using both APIs at the same time.

It is recommended that DirectInput not be used to implement keyboard or mouse controls. Keyboard and mouse controls should only be implemented using Windows messages and Win32 APIs. For details on getting high-resolution mouse movement information without using DirectInput, see [Taking Advantage of High-Definition Mouse Movement](/windows/desktop/DxTechArts/taking-advantage-of-high-dpi-mouse-movement).

</dd> </dl>

### 1.5 Support Multiple Aspect Ratios and Resolutions

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game must support at least the following aspect ratios and associated screen resolutions:

-   4:3 normal (800 600 or 1024 768)
-   16:9 widescreen (1280 720)
-   16:10 widescreen (1152 720 or 1680 1050 or 800 480)

For screen resolution configuration and detection, the game must adhere to the following rules:

-   The game uses the desktop resolution of the display device by default if it is a supported resolution. The desktop aspect ratio must be used as a search criterion if the game chooses a different default resolution.
-   The game must prompt the user to confirm new display settings when a change is made. If the user does not accept within 15 seconds, the display must revert to the previous setting.
-   The game must not stretch pixels or center a 4:3 render window to support widescreen aspect ratios. However, letterboxing is acceptable.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

With the Windows 3D desktop, a particular aspect ratio or resolution cannot be assumed, because of the following factors:

-   Support for high-detail displays.
-   Increased market share of widescreen monitors.
-   HDTV deployments for Windows Media Center.
-   Accessibility requirements.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Ideally, the game defaults to the native aspect ratio of the display. However, obtaining this information reliably can be a challenge, so as a more general solution the game can assume that the desktop is running at the native aspect ratio. The desktop resolution can be obtained by calling [**EnumDisplaySettings**](/windows/desktop/api/winuser/nf-winuser-enumdisplaysettingsa) with ENUM\_REGISTRY\_SETTINGS.

For more details, see the Aspect Ratio and Widescreen sections of the DirectX article [Introduction to the 10-Foot Experience for Windows Game Developers](/windows/desktop/DxTechArts/introduction-to-the-10-foot-experience-for-windows-game-developers).

</dd> </dl>

### 1.6 Support Launch from Windows Media Center

\[This requirement has been retired.\]

### 1.7 Direct3D Support

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

If the game uses Direct3D, then the minimum version supported must be Direct3D 9, and Direct3D must be the default renderer selected.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

The Windows Vista and Windows 7 core graphics architecture is designed around Direct3D. Direct3D 8 and earlier versions are supported by remapping legacy interfaces.

Use of versions of Direct3D newer than Direct3D 9 is strongly encouraged. See the Games for Windows Showcase S.1. Requiring Direct3D 10 or Direct3D 11 is fully compliant with requirement 1.7.

</dd> </dl>

### 1.8 Enable High-DPI-Aware

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games and their installers must run correctly without visual problems when dots-per-inch (DPI) scaling is enabled (tested with 144 DPI for 150% scaling at display resolution of 1600 1200) on Windows Vista and Windows 7.

This typically requires the game executable to declare being DPI-aware. This is accomplished by embedding a manifest element: <dpiAware>true<dpiAware> .

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

High-quality LCD monitors are commonplace as computer displays, and they look best when driven at their native resolutions (typically 1280 1024, 1600 1200, and so on). Customers who have difficulty reading text and seeing images at this resolution often set their computer desktops to a lower resolution and suffer visual artifacts from LCD scaling. Instead, customers can leave the resolution at the native size and change the DPI of the Windows display, thus making item and text appearance larger without sacrificing image quality.

While this feature has been available in some form since Windows XP, it is seldom enabled by customers or by OEMs. More than half of all computer displays today are set to a lower resolution than the monitor's native resolution, based on customer feedback. Windows 7 makes this feature much more visible to customers during initial setup and when changing display settings, encouraging them to use DPI scaling rather than change the desktop resolution.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

The [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function can be used instead, if called early in the process startup code. Adding to the manifest is preferred, to ensure there are no race conditions with software elements (such as DLLs) that might initialize before the main entry point is called. Note that **SetProcessDPIAware** is only present on Windows Vista and Windows 7.

Adding the manifest element is easy to do with Visual Studio 2005 and 2008; create a file named dpiaware.manifest that contains the following text:

``` syntax
            <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
            <asmv3:application>
            <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
            <dpiAware>true</dpiAware>
            </asmv3:windowsSettings>
            </asmv3:application>
            </assembly>
```

Then, inside Visual Studio, add dpiware.manifest to the project. Ensure that **Embed Manifest** is set to **Yes** in the project's properties. Note that older versions of the Manifest Tool (Mt.exe) will generate a spurious warning with the DPI-aware manifest elements. To resolve this, update Mt.exe to the latest version from the Windows SDK.

Visual Studio 2010 includes a setting in the project properties, named **Enable DPI Awareness**, that eliminates the need for a file like dpiaware.manifest. Find **Enable DPI Awareness** by expanding **Configuration Properties** and **Manifest Tool**, and then selecting **Input & Output**.

On Windows, the traditional display mode defaults to 96 DPI, which was common for CRT monitors.

While full-screen applications change the display resolution, they often use window messages and metrics when setting up buffers and display rectangles. DPI virtualization causes these full-screen display modes to appear cropped, and declaring DPI-aware will prevent these problems. For more information, see [Writing DPI-Aware Win32 Applications](../hidpi/high-dpi-desktop-application-development-on-windows.md).

</dd> </dl>

## Security and Compatibility

**Summary of Security and Compatibility Requirements**

**Customer Benefits**

The following requirements improve the overall security of games and help ensure that they work with Windows on different architectures, under different configurations, and in different modes.

### 2.1 Follow User Account Control Guidelines

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Every executable file (that is, every file that has a .exe extension) must contain an embedded manifest that defines its execution level by including the following tag:

``` syntax
            <requestedExecutionLevel>
```

Per requirement 1.2, the main game and Autorun executable must have the execution level of asInvoker to support Standard User contexts.

User data files that have file associations registered with **File Explorer** must be placed in a subfolder of the folder that is specified by CSIDL\_PERSONAL (also called **Documents** or **My Documents**). All other user data files must be stored in a subfolder of the folders that are specified by CSIDL\_LOCAL\_APPDATA or CSIDL\_COMMON\_APPDATA. (These directories are hidden by default for individual users and for all users.)

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

A user's Windows experience is more secure if applications run only with the permissions needed.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

If only a few features in an application require administrative privileges (for example, an application that needs to configure a firewall), the main process of the application must still be run by using standard user privileges. Features that require administrative privileges must be moved into a separate process, such as an installer or configuration utility.

If administrative privileges are not required, the embedded manifest XML should include the following:

``` syntax
            <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
            <ms_asmv2:trustInfo xmlns:ms_asmv2="urn:schemas-microsoft-com:asm.v2">
            <ms_asmv2:security>
            <ms_asmv2:requestedPrivileges>
            <ms_asmv2:requestedExecutionLevel level="asInvoker" uiAccess="false" />
            </ms_asmv2:requestedPrivileges>
            </ms_asmv2:security>
            </ms_asmv2:trustInfo>
            </assembly>
```

If administrative privileges are required, the embedded manifest XML should include the following:

``` syntax
            <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
            <ms_asmv2:trustInfo xmlns:ms_asmv2="urn:schemas-microsoft-com:asm.v2">
            <ms_asmv2:security>
            <ms_asmv2:requestedPrivileges>
            <ms_asmv2:requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
            </ms_asmv2:requestedPrivileges>
            </ms_asmv2:security>
            </ms_asmv2:trustInfo>
            </assembly>
```

With Visual Studio 2005 this is easily embedded by just adding a manifest (.manifest) file that contains one of the preceding blocks to the project, and ensuring that **Embed Manifest** is set to **Yes** in the project properties for Manifest Tool. For Visual Studio 2008 and 2010, UAC properties can be set directly in the project properties for the linker on the **Manifest File** page. Note that older versions of the Manifest Tool (Mt.exe) generate a spurious warning with the UAC manifest elements. To resolve this, update Mt.exe to the latest version from the Windows SDK.

See requirement 3.1 for details on the special cases of installation, patching, and removal.

Dynamic Link Libraries (DLLs) do not require such manifests.

For more information about User Account Control, see [User Account Control for Game Developers](/windows/desktop/DxTechArts/user-account-control-for-game-developers).

</dd> </dl>

### 2.2 Support Windows x64 Versions

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

To maintain compatibility with 64-bit editions of Windows, games should meet the following requirements.

-   Titles and title installers must not contain any 16-bit code or rely on any 16-bit component.
-   If the game is dependent on kernel-mode drivers for operation, x64 versions of these drivers must be available. The game setup must detect and install the proper drivers and components for the 64-bit editions of Windows.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Many Windows Vista and Windows 7 users will run 64-bit editions of the operating system over the life of the product, so it is crucial for applications to be compatible with this operating system.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Windows on Windows 64 (WOW64) allows 32-bit code to run on 64-bit editions of Windows, so it is not necessary that the application be native 64-bit code on 64-bit editions of Windows. Sixteen-bit code does not run on 64-bit editions of Windows.

Maintaining compatibility with Windows XP Professional x64 Edition is not required, but it is strongly encouraged.

For details, see [64-bit programming for Game Developers](/windows/desktop/DxTechArts/sixty-four-bit-programming-for-game-developers).

</dd> </dl>

### 2.3 Sign Files

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

All executable code files (typically, files with the extension .exe or .dll) must be signed with a publicly valid Authenticode certificate, and must have a valid timestamp server URL for production signing.

If your game uses Windows Installer, the installer package files (.msi files) must be signed.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Signing a file helps users decide whether to trust an application, and assures users that files have not been tampered with. It also allows applications to run properly in locked-down environments.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

For details, see [Authenticode Signing for Game Developers](/windows/desktop/DxTechArts/authenticode-signing-for-game-developers).

If your game uses Windows Installer, we recommend that you enable UAC/LUA patching, by including an MsiPatchCertificate table. For more information, see [User Account Control (UAC) Patching](/windows/desktop/Msi/user-account-control--uac--patching).

We do not recommend signing cabinet (.cab) files, unless they are relatively small (less than 100 MB).

</dd> </dl>

### 2.4 Sign Drivers

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Any kernel-mode driver that is installed by the game must be signed with a publicly valid Authenticode certificate.

Any kernel-mode hardware device driver that is installed by the game must have a Microsoft signature, which can be obtained from the Windows Hardware Quality Labs (WHQL) or from the Driver Reliability Signature (DRS) program.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Poorly written or malware drivers can severely affect the stability and security of a system. On 64-bit editions of Windows Vista and Windows 7, unsigned drivers do not load. This policy can also be enabled for 32-bit editions of Windows Vista and Windows 7.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Both 32-bit and 64-bit native versions of all kernel-mode drivers are needed per requirement 2.2.

More information about Microsoft driver signing programs can be found at the [Windows Hardware Developer portal](https://www.microsoft.com/whdc/winlogo/hwrequirements.mspx).

</dd> </dl>

### 2.5 Perform Proper Version Checking

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games must not fail to run on future operating systems as indicated by changes in the Windows version number, unless the End User License Agreement prohibits use on future operating systems. If the game is supposed to fail, it must do so gracefully by displaying an appropriate message to the user.

If Windows version checks are made, the version-checking APIs ([**GetVersionEx**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversionexa) or [**VerifyVersionInfo**](/windows/desktop/api/winbase/nf-winbase-verifyversioninfoa)) must be used to check the operating system version. Registry keys must not be read to determine the version.

Explicit version checks for the DirectX runtime must not be present in the game. These version checks must not be present in the installation that launches the DirectX runtime setup (DirectSetup).

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

When Windows users upgrade their operating systems, they should not be blocked from playing current games simply because the Windows version number has increased. Poorly written version checkers continue to create problems for software that, otherwise, works fine on newer versions of Windows or simply with the addition of a Windows service pack.

Fragile version check comparison logic for the DirectX runtime has created numerous failed installations when it is run on different versions of Windows. The DirectX version number applies only to the core operating system components. It does not apply to the side-by-side DirectX SDK components that are used by many games.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

It is quite common to see installers check for a minimum OS version. This check, however, needs to be done with care to ensure that it tests for greater than or equal to, rather than simple equality, thereby locking to a specific version of the operating system. Using Application Verifier's **HighVersionLie** test is a quick and easy way to determine how your installer will react to a significant change in the OS version number.

Proper use of the DirectX runtime redistribution package (DirectX Setup) involves always launching it during installation, preferably in silent mode. This allows the code that is provided by Microsoft to perform any required version updates. It also allows installation of any optional side-by-side DirectX SDK components, such as D3DX, XACT, MDX, or XInput.

For best practices for deploying the DirectX runtime, see [DirectX Installation for Game Developers](/windows/desktop/DxTechArts/directx-setup-for-game-developers).

It is recommended that games that support Windows XP check for a service pack level of 2 or higher, because Service Pack 2 (SP2) and Service Pack 3 (SP3) provide significant security improvements, a simplified DirectX Runtime Redistribution requirement, and extremely broad deployment. Most modern Microsoft technologies that support Windows XP require SP2 or SP3 (XAudio2, Games for Windows - LIVE, and so on).

</dd> </dl>

### 2.6 Support Concurrent User Sessions

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games that rely on 3D graphics are not required to work over a remote desktop connection, but the user must be alerted when the game fails.

Games must support standard Windows multitasking scenarios by adhering to the following rules:

-   Games must not block the use of concurrent user sessions.
-   A game must run in a new user session when it is already running in another session.
-   Game sound in one user session must not be heard when another user is active in a different session.
-   Games must support Fast User Switching.
-   Games must not attempt to disable standard task switching. Games must not disable the ALT+TAB keyboard shortcut. Games are allowed to disable accessibility keyboard shortcuts, as described in [Disabling Shortcut Keys in Games](/windows/desktop/DxTechArts/disabling-shortcut-keys-in-games).

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Windows users should be able to run concurrent sessions without conflict or disruption. This is a common scenario for a Windows computer that is shared by a family, roommates, or others.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

To test whether the game is launched in a remote session, call [**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics)(SM\_REMOTESESSION). A nonzero value indicates that the session is remote.

For more information, see [Fast User Switching](/windows-hardware/drivers/display/fast-user-switching). Note that Fast User Switching occurs if Parental Controls time restrictions are enabled when the user's time is up. See requirement 1.2 for more details.

</dd> </dl>

### 2.7 Support Long Names

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

If a game supports saving files, it must be able to save files that have long names and paths. The game must properly handle special file system characters, such as \\ / : \* ? " < >, in any user input fields that are used to create file names or paths.

Games must work properly when a user has a long user name.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Players are accustomed to using long names on deep paths that are supported by the underlying operating system.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Long names are defined as those that contain the maximum values that are defined in the Windows SDK.

</dd> </dl>

## Installation

**Summary of Security and Compatibility Requirements**

**Customer Benefits**

Customers can be confident that applications will install on Windows without degrading the operating system or other applications if applications use official system component distribution methods. A streamlined installation experience provides a more accessible and trouble-free out-of-box experience for games.

### 3.1 Support Easy Installation

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games must provide a simplified path in the setup user interface by implementing the following:

-   Display a maximum of one EULA prompt.
-   The default installation path must bypass all selections for the installation (such as installation folder or component selections), assume the default selections, and then run the game or launcher upon successful installation, without additional prompts. If desired, a custom installation option can be provided for advanced configuration options.
-   Install any required operating system components (such as the DirectX and Visual C runtimes) using the correct Microsoft redistribution packages. The installation should be performed silently, without prompting and without being guarded by component version checks.
-   Provide removal through **Programs and Features** in **Control Panel** for both the game application and generated working files. An option for deleting any data files that are created by the user is recommended. The removal process must ensure that all installed files are removed and all settings (for example, firewall exception list entries and registry keys) are cleared. Redistributed operating system components must not be removed.
-   If the game requires exceptions to be added to the Windows Firewall, the setup process can prompt to inform users that this change is required. This prompt should appear before installation begins.

Installation and removal can require administrative rights. Patching can require prompting for administrative credentials, depending on frequency of update. Normal play of the game must not require administrative rights, per requirement 2.1 Follow User Account Control Guidelines.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Easy installation is a Windows-centric game development philosophy that is designed to simplify and streamline the sometimes tedious and confusing process of installing games on computers that are running Windows operating systems. Easy installation is enabled by utilizing a set of technologies and best practices that reduce the unnecessary complexity and perceived risk of installing games on Windows computers.

The key goals are to:

-   Reduce the amount of time to get into the game and begin play.
-   Reduce the number of dialog boxes and choices to very few, or none, in order to simplify the game installation experience.

Some traditional installations have prompts that allow non-functional installations, even though the application appears to be successfully installed. For example, a game can require a user to accept a EULA. The game is then installed, and then the DirectX EULA appears. This EULA allows users to decline, and thus skip installation of the DirectX runtime. This scenario can result in a game that fails to run because of missing components.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

For more information about game installation, non-traditional game installation techniques, UAC-compatible patching solutions, and handling frequent patching, see the following DirectX articles:

-   [Simplifying Game Installation](/windows/desktop/DxTechArts/simplifying-game-installation)
-   [Install-on-Demand for Games](/windows/desktop/DxTechArts/install-on-demand-for-games)
-   [Patching Game Software in Windows XP, Windows Vista, and Windows 7](/windows/desktop/DxTechArts/patching-methods-in-windows-xp-and-vista)
-   [Installation Best Practices for Massively Multiplayer Online Games](/windows/desktop/DxTechArts/mmo-installation-best-practices)

> [!Note]  
> Removing user-specific generated data files should be performed only for the current user and for common shared user locations. There is no robust way to scan the system to remove user-specific files for other users, even if the removal requires administrative credentials.

 

</dd> </dl>

### 3.2 Support User Account Control for Installation

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game installer must not assume that it is running in the same context as the user. User-specific locations will be different from the installer and the player even for single-user systems due to administrator credentials elevation. Therefore, when a game runs for the first time, it must perform user-specific tasks, separately from the installation process.

The Windows Firewall exception dialog box must not appear when a user hosts or joins a multiplayer game. Any required configuration must be done at installation time. The setup instructions should inform the user that this operation will occur as part of the setup.

The game installer must provide an embedded manifest that designates the required execution level, per requirement 2.1 Follow User Account Control Guidelines.

If the game is launched by the installer after installation is complete, it must be launched in the context of the original user.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

One of the largest changes to the Windows operating system in Windows Vista is the addition of User Account Control (UAC), which runs applications with reduced privileges by default. As a result, installers need to manage privilege levels accordingly. Windows 7 also makes extensive use of UAC. While Windows 7 improves the user experience of UAC, installers must still meet the same requirements as on Windows Vista to function properly, without relying on potentially confusing virtualization behavior.

UAC is active by default on Windows Vista and Windows 7, and the vast majority of customers (88% or more, based on feedback) leave this feature enabled.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

For more details on configuring the Windows Firewall, see the DirectX article [Windows Firewall for Game Developers](/windows/desktop/DxTechArts/games-and-firewalls) and the FirewallInstallHelper sample.

Standard launch of the game at the end of the installation process fails to meet the last aspect of this requirement if the installation is launched by a standard user, and if the setup process requires administrative privileges (that is, prompts for a administrator credentials). It also inherits administrative privileges, which is a potential security risk. Instead, a setup bootstrap loader should launch the game after returning from a successful invocation of the installer. For more information, see the MSDN Magazine article [Teach Your Apps to Play Nicely with Windows Vista User Account Control](/archive/msdn-magazine/2007/january/teach-your-apps-to-work-with-windows-vista-user-account-control).

</dd> </dl>

### 3.3 Install to Correct Folders

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games that are installed for all users must be installed to the Program Files folder by default. User data must be written when the game runs for the first time, not during the installation.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Users should have the flexibility to install applications where they need them. They should also have a consistent and secure experience with the default location of files.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Games can make use of the various known folder locations (such as those specified by CSIDL\_LOCAL\_APPDATA and CSIDL\_COMMON\_APPDATA) to store significant amounts of game data and supporting executable files to implement advanced install-on-demand and patching scenarios.

Because installation can require elevation to a different user account during the all users installation process, there is no correct user location in which to store data at installation time. Also, if file encryption is enabled, encrypted files can be only accessed by the user account that created them.

</dd> </dl>

### 3.4 Install Windows Resources Properly

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Applications must not attempt to install files or registry keys that are protected by Windows Resource Protection (WRP). If the application requires newer versions of system components, it must update these components by using a Microsoft Service Pack or a Microsoft-approved installation package that contains the system component. System components must never be repackaged.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Windows Resource Protection (WRP) is designed to ensure that protected system resources are updated only by using Microsoft-approved installation or update mechanisms. WRP improves system reliability by ensuring that the results of an installation are predictable.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

WRP is the successor to Windows File Protection, which protects the majority of the system components that are installed in the Windows folder. WRP protects most registry keys that store settings for COM object creation. It also reserves certain folders for use exclusively by the operating system. Attempts to access protected resources typically result in an access denial error.

For details of best practices when the DirectX runtime is deployed with a game, see the DirectX article [DirectX Installation for Game Developers](/windows/desktop/DxTechArts/directx-setup-for-game-developers).

</dd> </dl>

### 3.5 Avoid Reboots During Installation

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game installer should not assume that installation of Windows components from redistribution packages requires a reboot, unless the reboot is indicated by a return result or by Microsoft documentation.

If the game installer always forces a reboot, this must be approved by Microsoft.

Files-in-use dialog boxes that are included in Windows Installer packages must contain an option to automatically close applications and attempt to restart them after setup is complete.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Rebooting the system after an installation is an inconvenient disruption for users and is usually unnecessary.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

For more information, see [Using Windows Installer with Restart Manager](/windows/desktop/Msi/using-windows-installer-with-restart-manager).

</dd> </dl>

### 3.6 Use File Versioning Correctly

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game installation program must properly check to ensure that the latest file versions are installed. Installing a game must never regress any files that you do not produce or that are shared by applications that you do not produce.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Shared components and system components are often updated for security fixes and expanded functionality. An installation that includes an older version of updated components should not result in the loss of updates and fixes that already have been applied.

</dd> </dl>

### 3.7 Support Autorun \[Conditional Requirement\]

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

For games distributed on CD, DVD, or other removable media that support Autorun, when the disc is inserted for the first time, the application must automatically run or prompt the user to install the game, unless the user has disabled the Autorun feature.

After the application is successfully installed, re-inserting the disc in the drive must not cause installation to automatically begin again. It is acceptable to ask users if they want to update or change their installation choices.

The autorun application must not prompt for elevation (that is, it must have asInvoker in the manifest, per requirement 2.1, although it can launch the setup program or another utility that requires administrative rights. Elevation should occur only if the game is not installed, or if the user specifically selects it.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Autorun simplifies the experience of using media-distributed applications, such as games that typically require the disc to be present in the drive in order to play the game.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

It is not acceptable to require the user to navigate in File Explorer to launch the installation from the CD or DVD.

For games that are distributed on multiple discs, subsequent discs should ideally either use the Autorun feature or continue installation without prompting the user to press a key or take other action.

When authoring an Autorun program, ensure all required components are present on fresh installs of Windows. Typical applications rely on technologies installed by the setup, but Autorun itself executes before any such setup occurs. One common example is the failure of Autorun programs because the Visual C Runtime DLLs were not included as part of the Windows setup. The Autorun program, therefore, must use application local CRT deployment or must statically link the CRT.

Autorun programs written for use on versions of Windows before Windows Vista should not use the .NET runtime because this technology is not included with Windows XP or older versions of Windows. Windows Server 2003 and Windows Vista are the first versions of Windows to include .NET runtime as part of their operating system.

For similar reasons, Autorun programs cannot require the presence of DirectX SDK optional side-by-side components such as D3DX9, D3DX10, D3DX11, XAudio2, X3DAudio, XACT, XINPUT, and MDX 1.1.

For an example of using Autorun, see AutoRun Sample.

</dd> </dl>

## Reliability

**Summary of Security and Compatibility Requirements**

**Customer Benefits**

These requirements make an application more reliable by minimizing the number of crashes, hangs, and reboots. The reliability requirements can help ensure that software is more predictable, maintainable, resilient, and recoverable.

### 4.1 Eliminate Unnecessary Reboots

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

All application installers must take advantage of the restart manager APIs to avoid system reboots (see requirement 3.5).

Games must not block shutdown.

All applications must respond to the restart manager by listening and responding to the following shutdown messages:

<dl> <dt>

<span id="WM_QUERYENDSESSION_with_LPARAM___ENDSESSION_CLOSEAPP__0x1___"></span><span id="wm_queryendsession_with_lparam___endsession_closeapp__0x1___"></span><span id="WM_QUERYENDSESSION_WITH_LPARAM___ENDSESSION_CLOSEAPP__0X1___"></span>WM\_QUERYENDSESSION with LPARAM = ENDSESSION\_CLOSEAPP (0x1) 
</dt> <dd>

GUI applications must respond (TRUE) immediately in preparation for a restart.

</dd> <dt>

<span id="WM_ENDSESSION_with_LPARAM___ENDSESSION_CLOSEAPP__0x1___"></span><span id="wm_endsession_with_lparam___endsession_closeapp__0x1___"></span><span id="WM_ENDSESSION_WITH_LPARAM___ENDSESSION_CLOSEAPP__0X1___"></span>WM\_ENDSESSION with LPARAM = ENDSESSION\_CLOSEAPP (0x1) 
</dt> <dd>

Applications must return a 0 value within 5 seconds, and then close.

</dd> <dt>

<span id="CTRL_C__"></span><span id="ctrl_c__"></span>CTRL+C 
</dt> <dd>

Console applications that receive this message must close immediately.

</dd> </dl> </dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

System reboots are a major disruption. They lead to a bad user experience, and should be minimized. Some operations, such as critical system updates can require reboots. By listening to shutdown messages, the game and other applications can react promptly to requests from restart manager. In this way, they can avoid unnecessarily delays in valid reboot requests.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

If a game installer uses the Windows Installer technology (MSI) without any custom actions, this functionality is provided automatically. Microsoft redistribution packages also support the Restart Manager.

For more information about the Restart Manager, see the MSDN article [About Restart Manager](/windows/desktop/RstMgr/about-restart-manager).

</dd> </dl>

### 4.2 Eliminate Application Verifier Failures

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game must generate no failures running under Microsoft Application Verifier (AppVerifier), version 4.0 or later, in the following tests:

-   Basics: Handles, Heaps, Locks, Memory, TLS
-   Miscellaneous: DangerousAPIs, DirtyStacks

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

AppVerifier tests for many known issues that cause crashes and hangs in Windows applications, as well as known security vulnerabilities.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

For more information about Application Verifier, see [Application Verifier](/previous-versions/ms220948(v=vs.80)) and [Using Application Verifier Within Your Software Development Lifecycle](/previous-versions/aa480483(v=msdn.10)) on MSDN. You can download Application Verifier from [Download details: Application Verifier](https://www.microsoft.com/downloads/details.aspx?familyid=c4a25ab9-649d-4a1b-b4a7-c9d8b095df18) on Microsoft Download Center.

This requirement does not apply to pure managed applications without native interop.

These tests should be run on a release build. Debugging builds can generate false failures. Some anti-piracy and anti-cheat technologies can interfere with the execution of AppVerifier. Therefore, these tests should be performed without anti-piracy and anti-cheat technologies enabled.

It may be necessary to set the Full property of the Basics:Heaps test to FALSE, because the full PageHeap greatly increases the memory pressure of the running application. Failures will still be detected, but they might be more difficult to track down if you use only partial PageHeap.

If you use the UAC/LUA-related tests in Application Verifier to meet the User Account Control requirements 2.1 and 3.2, you should use the [Standard User Analyzer](/windows/desktop/Win7AppQual/standard-user-analyzer--sua--tool-and-standard-user-analyzer-wizard--sua-wizard-) to review the results. There are also numerous other useful tests provided by Application Verifier which you are strongly encouraged to use in development and testing to ensure a high level of compatibility with current and future versions of Windows. The **HighVersionLie** test is used to verify compliance with requirement 2.5.

Visual Studio Team System includes a subset of the AppVerifier functionality that is integrated into the debugging environment. This may prove useful for tracking down and resolving issues with Basics: Heaps, Handles, and Locks tests.

</dd> </dl>

### 4.3 Support Windows Error Reporting and File Version Information

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

To enable support of Windows Error Reporting, games must meet the following requirements:

-   Games must handle only exceptions that are known and expected. Windows Error Reporting must not be disabled. If a fault such as an Access Violation appears in a game, it must allow Windows Error Reporting to report the crash.
-   All executable files (for example, .exe files or DLLs) must contain an accurate product name, company name, and file version.
-   Normal exit of the game must not result in an unknown exception fault.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

The Windows Error Reporting APIs provide vital feedback to Microsoft for detecting widespread crashes and hangs in applications. This allows Microsoft and its partners to quickly detect and resolve system and driver issues that lead to application failures quickly.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Games can include custom unhandled exception handlers to perform custom support and reporting functionality, but they must pass any error on to the **ReportFault** or **WerReportSubmit** functions.

Proper file version information can be verified by viewing the file properties in the Windows desktop UI and checking the Version property page.

For more information about the Windows Error Reporting APIs, and how to analyze the crash dumps that are generated when you use this service, see the DirectX article [Crash Dump Analysis](/windows/desktop/DxTechArts/crash-dump-analysis).

</dd> </dl>

## Xbox 360 Common Controller for Windows Terminology



| Name                                          | Description                                                                                                 |
|------------------------------------------|--------------------------------------------------------------------------------------------------|
| A                                        | The A button.                                                                                     |
| B                                        | The B button.                                                                                     |
| BACK                                     | The Back button.                                                                                  |
| (right/left) bumper                      | The button at the top right and left edge of the controller. Equivalent to a shoulder button.    |
| directional pad                          | The controller directional pad.                                                                   |
| D-pad                                    | Accepted abbreviation of directional pad.                                                         |
| DP                                       | Directional pad abbreviation and controller label.                                                |
| RB, LB                                   | Right and left bumper abbreviations and controller labels.                                        |
| RS, LS                                   | Right and left stick abbreviations and controller labels.                                         |
| RT, LT                                   | Right and left trigger abbreviations and controller labels.                                       |
| RSB, LSB                                 | Right and left stick abbreviations and controller labels.                                         |
| START                                    | The Start button.                                                                                 |
| (right/left) stick                       | The controller stick. Formerly thumbstick.                                                       |
| (right/left) stick button                | The controller stick button. Formerly thumbstick button.                                         |
| (right/left) trigger                     | The controller trigger.                                                                          |
| Vibration                                | Gameplay feedback produced by the controller motor. Do not use rumble.                           |
| X                                        | The X button.                                                                                     |
| Y                                        | The Y button.                                                                                     |
| Xbox 360 Controller for Windows          | The Xbox 360 gamepad sold as a PC hardware SKU, including a Windows device driver disc.          |
| Xbox 360 Wireless Controller for Windows | The Xbox 360 wireless gamepad sold as a PC hardware SKU, including a Windows device driver disc. |



 

## Guidelines for Game Middleware Products

### Introduction

For games to qualify for the Games for Windows program, they must meet a list of technical requirements. Any third-party components that are shipped with a title (executable files, DLLs, drivers, and so forth) must also meet these requirements for the game to qualify. This document highlights the most common requirements that must also be met by the third-party components for the game to pass the compliance tests. Installers and complete game engine/production packages should review the full Games for Windows technical requirements document, because many of these requirements are affected by these tools.

### Additional Recommendations

Beyond ensuring that your component supports the creation of titles that are compliant with the requirements for Games for Windows, there are a number of other considerations you should take into account when designing and deploying a library or support utility for a Windows game.

-   To support developers working on 64-bit native x64 applications, provide both 32-bit and 64-bit native versions of your libraries. The 32-bit version must be 64-bit compatible per 2.2. Libraries for 32-bit applications should not assume that the high bit of any 32-bit address is unused in order to support use within LARGEADDRESSAWARE x86 applications.
-   If you provide native code (C/C++) headers, use Standard Annotation Language (SAL) attribute syntax to decorate your public API routines. This will allow users of your library to get the maximum benefit of using Static Code Analysis (/analyze), which is part of Visual Studio Team System 2005, Visual Studio Team System 2008, Visual Studio 2010 Premium, and Visual Studio 2010 Ultimate, as well as the publicly available Windows SDK compiler tools.
-   If your product creates threads within the user's process, be sure to name each thread so that debugging tools can properly annotate running threads.
-   If you write routines that are intended to be called within a game's main loop, use the D3DX routines D3DPERF\_BeginEvent/EndEvent and D3DPERF\_SetMarker to annotate high-level operations for easier identification of bottlenecks using PIX for Windows.
    > [!Note]  
    > For the Visual Studio 2012 graphics diagnostics functionality, these D3DX and PIX routines are replaced by the [**ID3DUserDefinedAnnotation**](/windows/desktop/api/d3d11_1/nn-d3d11_1-id3duserdefinedannotation) interface.

     

-   For networking libraries, provide IP-neutral implementations and avoid deprecated IPv4 only routines to support the IPv6 and Teredo technologies in Windows XP with Service Pack 2, Windows Vista, and Windows 7.
-   Game service providers should register themselves with Games Explorer using version 2 of the GDF schema, and make use of the RSS feature to provide service-related news.

### Games for Windows Showcases

### Introduction

Games for Windows showcases go beyond providing a solid gaming experience on Windows PCs. By implementing these features, games can add more excitement to the user experience on the latest Windows platforms.

Games for Windows titles must fulfill all technical requirements listed in this article, but showcase features are optional. These titles are free to implement some, none, or all of these showcases.

### S.1 Exploit Direct3D 11

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Direct3D 11 is the next-generation rendering API for Windows Vista and Windows 7. Games exploiting Direct3D 11 use optimized content, advanced rendering techniques, and new hardware features to create a compelling experience on hardware that supports 10, 10.1, and 11.

If the game also implements Direct3D 9, a side-by-side comparison should demonstrate a perceptible improvement in content quality, visual fidelity, performance, scene complexity, and other areas of graphics fidelity for Direct3D 11. This support is subject to the Games for Windows Technical Requirement 1.7.

Direct3D 10level9 technology can be used to support Shader Model 2.0/3.0 Direct3D 9-class video hardware on Windows Vista and Windows 7, rather than using a side-by-side Direct3D 9 implementation for broad hardware support. However, this is not sufficient to demonstrate this showcase.

On computers running Windows Vista or Windows 7 with Direct3D 11 installed, the game should default to using Direct3D 11.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

The Direct3D 11 API builds on the Windows Display Driver Model (WDDM) and Direct3D 10.1 infrastructure to support new capabilities: hardware tessellation, compute shaders, multithreaded rendering and resource creation, new texture compression formats, and a more flexible shader language. Direct3D 11 provides unified hardware support for modern video cards, including the latest generation Direct3D 11 parts, all Direct3D 10 and 10.1 video cards, and many Shader Model 2.0/3.0 Direct3D 9 video cards, which is the minimum video hardware required for the Aero 3D desktop.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Migrating a Direct3D 9 rendering engine to use the new Direct3D 11 interface is a well-defined task:

-   Eliminate all fixed-function operations in favor of programmable shaders.
-   Update all existing shaders to the new syntax of Shader Model 4.x/5.
-   Update resource management to support the new view model.
-   Convert all assets to use a new list of available formats.
-   Update render state handling to use immutable state blocks, and rework shader constants into constant buffers.

This conversion is essential to enable the Direct3D 11 showcase, although the result does not meet the showcase requirement of exploiting the new API.

The new API and associated HLSL programming model offers many opportunities for enhanced content:

-   Leveraging existing Direct3D 10 hardware features, such as Geometry Shader, Stream Out, texture arrays, and the BC4/BC5 compressed texture formats.
-   Leveraging existing Direct3D 10.1 hardware features, such as independent per-render-target blend modes, MSAA depth read back, MSAA per-sample shader access, cube map arrays, and rendering to block-compressed (BC) formats.
-   Implementing advanced GPU algorithms using Compute Shader with CS4.x on existing Direct3D 10/10.1 video cards (enabled by updated video drivers) or CS 5.0 on next-generation Direct3D 11 video cards.
-   Rendering on multiple threads using free-threaded resource creation and multiple device contexts for improved performance on multicore systems (with updated video drivers). For more information, see the Games for Windows Showcase S.3.
-   Utilizing new features of Direct3D 11-class video hardware, such as hardware tessellation with hull and domain shaders, Shader Model 5.0 HLSL shader hardware features BC6HBC7 compressed texture formats, and Dynamic Shader Linkage.

Techniques that can be implemented with Direct3D 9 (largely through high CPU cost) can be off loaded to the GPU in an efficient manner, thus freeing CPU resources to support other game demands.

Direct3D 11 APIs, supporting tools, and samples are available in the DirectX SDK. Also see Graphics APIs in Windows.

</dd> </dl>

### S.2 Exploit x64 Native

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game includes a 64-bit native executable that delivers a compelling new experience enabled by x64 editions of Windows running on x64-capable hardware. A side-by-side comparison with the 32-bit version of the game should show a perceptible improvement in content complexity, reduced overall load times, and performance.

On 64-bit editions of Windows, installation should always set up the 64-bit native version of the game as the default for shortcuts in Games Explorer and Windows XP Professional x64 Edition. If dual installation is desired, then an additional play task can be specified for Games Explorer on Windows Vista and Windows 7 that points to the 32-bit version, but the default should remain the 64-bit native version.

Note that the game should support the 64-bit editions of Windows Vista and Windows 7 to meet this showcase recommendation. Support for Windows XP Professional x64 Edition is encouraged, but not required.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

x64 technology provides 64-bit addressing capabilities for both the consumer and server markets that includes full-speed 32-bit backwards compatibly for existing applications. x64 is a key part of the roadmap for both AMD (AMD64) and Intel (EMT64), and, with the exception of ultra-mobile CPUs, support the technology for all current and future generation processors.

Windows XP Professional x64 Edition was the first consumer-oriented Windows operating system (OS) to support x64 technology, and Windows Vista and Windows 7 greatly expand the availability of the OS-enablement for 64-bit consumer computing. With 2 GB of RAM as standard on many new computers, further improvements in memory scaling will not benefit 32-bit individual applications that are unable to address more than 2 GB of physical RAM. Many games today are facing challenges fitting all of the available content into the constraints of 2 GB of virtual address space, especially when combined with the large video memories available on high-end GPUs, and moving to x64 technology greatly increases the supportable levels of detail.

x64 compatibility for 32-bit games is a Games for Windows technical requirement (2.2), but taking full advantage of the new technologies requires a 64-bit native implementation.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

The primary benefit of 64-bit addressing is the ability to directly access more than 2 GB of physical and virtual memory. The large virtual memory address space allows for extensive use of memory-mapped I/O without concern for VM address space exhaustion problems prevalent in 32-bit programming. Games can take advantage of the new space to greatly improve load times or, in some instances, to eliminate pauses for loading content.

Existing 32-bit applications can benefit from x64 editions by having the capability to process addresses with full 32-bit data when built with the Enable Large Addresses (**/LARGEADDRESSAWARE**) linker option. On 32-bit versions of Windows XP, special boot modes allowed such applications to address up to 3 GB of RAM, and x64 editions provide access up to 4 GB of RAM for Large Address Aware (LAA) apps. While use of LAA in a 32-bit application does not meet this showcase requirement, this bridge technology is an extremely useful way of providing additional scaling benefits on x64 versions of Windows for those not fully implementing this showcase requirement.

For more information, see [64-bit programming for Game Developers](/windows/desktop/DxTechArts/sixty-four-bit-programming-for-game-developers) and [RAM, VRAM, and More RAM: 64-bit Gaming Is Here](https://www.gamasutra.com/view/feature/3602/sponsored_feature_ram_vram_and_.php) in Gamasutra.

> [!Note]  
> A key challenge for this showcase is ensuring any third-party libraries or components your game relies on are available for 64-bit native development. Many legacy Microsoft APIs also have been eliminated from the 64-bit native environment, which can prove a challenge for engine code bases containing older implementations of key systems.

 

</dd> </dl>

### S.3 Exploit Many-Core Processors

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

The game implements features that take advantage of multicore processors, scaling to 3, 4, or more cores, when available.

If the game supports single-processor or dual-core systems, a side-by-side comparison with a quad-core system should demonstrate perceptible new features, additional compelling effects, improvement in content quality, and/or improved performance.

Because dual-core scaling is already widely supported by games, as well as automatically utilized by various Direct3D driver enhancements, dual-core scaling is not sufficient to demonstrate this showcase.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

The continuing growth in performance for CPUs has switched from clock rate improvements to the addition of computational cores. Both AMD and Intel roadmaps are based on scalable, multicore designs. All next-generation game platforms have multicore CPUs because of this fundamental shift in the evolution of processors. Single-threaded applications no longer will see significant gains from next-generation CPUs. Simple multithreading also will fail to scale as the number of CPU cores in common use grows to three or more.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Note that core counts need not be a power of two, so games should scale linearly and handle core counts of 3, 4, 5, 6, 7, 8, and so on.

Scaling by increasing the number of threads in an application only provides a return if the cost of communication and thread synchronization are kept in check. Feature-based scaling may prove an easier solution in the short-term, allowing the game to operate normally without the additional threads on single-core systems and enabling them when the additional CPU power is available.

For more information, see [Coding For Multiple Cores on Xbox 360 and Microsoft Windows](/windows/desktop/DxTechArts/coding-for-multiple-cores) and [Lockless Programming Considerations for Xbox 360 and Microsoft Windows](/windows/desktop/DxTechArts/lockless-programming) in the DirectX articles, as well as the DXUTLockFreePipe utility and the CoreDetection sample.

Making use of the Direct3D 11 free-threaded resource creation and device contexts is useful in achieving many-core scalability in rendering and loading graphics resources. See Games for Windows Showcase S.1.

Note that using the CPU instruction rdtsc directly, instead of using Windows APIs to compute timing on multicore systems, can lead to problems on some hardware and OS configurations; see [Game Timing and Multicore Processors](/windows/desktop/DxTechArts/game-timing-and-multicore-processors) in the DirectX articles.

</dd> </dl>

### S.4 Support Games for Windows - LIVE

Games for Windows - LIVE is no longer supported by Microsoft.

### S.5 Support Windows Touch

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Windows touch-capable games are playable using touch and/or gestures on computers running Windows 7 with a touch display. Keyboard input can be used as well, but the primary play interface must be touch-based.

Enabling touch should not prevent the use of the mouse or common controller, subject to Technical Requirement 1.4.

The game's installer is not expected to support Windows Touch functionality.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Multi-touch-capable displays for computers are available for laptops and desktops, and they represent a key hardware feature being promoted with the release of Windows 7. Windows 7 supports Windows Touch throughout the desktop and common controls interfaces.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Native code applications can access multi-touch through the WM\_TOUCH messages, in combination with the [**RegisterTouchWindow**](/windows/desktop/api/winuser/nf-winuser-registertouchwindow) function. See also the Manipulations and Inertia API.

Windows Presentation Foundation (WPF) 4.0 provides a managed solution for multi-touch interfaces.

For more information, see the Windows Touch SDK.

</dd> </dl>

### S.6 Support High Color

<dl> <dt>

<span id="Requirement"></span><span id="requirement"></span><span id="REQUIREMENT"></span>**Requirement**
</dt> <dd>

Games that support High Color use a 10:10:10:2 (DXGI\_FORMAT\_R10G10B10A2, D3DFMT\_A2B10G10R10) or a 16:16:16:16 (DXGI\_FORMAT\_R16G16B16A16, D3DFMT\_A16B16G16R16) format for the rendering back-buffer and full-screen display mode.

By using a  High Color  render target, High-Dynamic Range (HDR) content can be rendered with an extended or wide gamut when performing tone mapping to a 10-bit or 16-bit range.

</dd> <dt>

<span id="Rationale"></span><span id="rationale"></span><span id="RATIONALE"></span>**Rationale**
</dt> <dd>

Monitors have been capable of displaying more than 256 color levels per channel for many years, even when CRT displays were prevalent. The scan out hardware on video cards has been the limiting factor. Modern GPUs, including most Direct3D 9-class hardware and all Direct3D 10-class and better hardware, have scan-out hardware capable of at least 10-bits per channel, and hardware capability is set to grow to 16-bits per color channel in the future. HD TV interconnect systems (HDMI, DisplayPort) have been designed to handle more than 8-bits per channel as well, and analog VGA will already carry such signals.

</dd> <dt>

<span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>**Additional Information**
</dt> <dd>

Note that High Color, or Hi Color, historically refers to moving from 256 (8-bit) color displays to 15- or 16-bit color displays. Most display systems have long since moved on to True Color which is 24-bit color, or 8-bits per color channel for red, green, and blue. By High Color here we mean a new generation of displays systems that can operate with more than 8-bits per individual color channel. The is also referred to as Deep Color.

</dd> </dl>

### Recommended Best Practices

### Introduction

In addition to meeting the Technical Requirements and adopting one or more Showcases in your title, there are a number of best practices that should be followed for all Windows games. While these recommendations fall outside the scope of the core Technical Requirements, you are strongly encouraged to employ them for all Games for Windows titles.

### Additional Recommendations

-   Use the most recent Visual Studio compiler and runtime. Newer versions of the compiler implement significant improvements for the quality of code generated and for security issues, and they employ modern processor optimization strategies. Updating the compiler and using the latest C Runtime is an easy way to migrate to modern coding practices.
-   Use the dynamic-link library (DLL) version of the C Runtime, rather than static linking, and make use of Secure CRT. (Exceptions can be made in special pre-installation cases, like for an Autorun program or for the installer itself).
-   For game audio, use XAudio2, X3DAudio, and/or XACT, rather than DirectSound. For audio engines that do all mixing and source-rate conversion and need only a low-latency solution for audio output, use DirectSound on Windows XP (only) and WASAPI on Windows Vista and Windows 7.
-   Avoid using legacy and deprecated APIs: DirectDraw, DirectSound, DirectPlay, DirectMusic's performance layer, DirectPlay Voice, and Direct3D Retained Mode. Note that DirectPlay Voice and Direct3D Retained Mode are not available at all on Windows Vista or Windows 7. DirectPlay and DirectMusic's performance layer are not available to x64-native applications.
-   Optimize using SSE/SSE2 SIMD instruction sets. See the [DirectXMath](/windows/desktop/dxmath/directxmath-portal) API in the Windows SDK as a cross-platform solution for SIMD-optimized math operations.
-   Use modern best practices for Windows security (including compiler and linker options like **/NXCOMPAT**, **/GS**, **/SAFESEH**, **/DYNAMICBASE**, **/SDL**, and so on). For more information, see [Best Security Practices in Game Development](/windows/desktop/DxTechArts/best-security-practices-in-game-development).
-   Use the latest Windows SDK components and libraries. Remove dependencies on the legacy DirectSetup deployed out-of-band components such as D3DX9, D3DX10, and D3DX11. Consider using [DirectXTex](https://github.com/Microsoft/DirectXTex) or [DirectXTK](https://github.com/Microsoft/DirectXTK) or both.
-   Avoid using the older HLSL compiler, and instead, use the modern HLSL compiler. If support for Pixel Shader 1.x is required by your application, use shader assembly rather than HLSL, or limit the use of the older compiler to just those scenarios.

## Resources



| Term                                                                                                                                                                                                                         | Description                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Games_for_Windows__Test_Cases__"></span><span id="games_for_windows__test_cases__"></span><span id="GAMES_FOR_WINDOWS__TEST_CASES__"></span>Games for Windows: Test Cases <br/>                              | Best Practices for Games on Windows XP, Windows Vista, and Windows 7<br/>                                                                               |
| <span id="Windows_SDK__"></span><span id="windows_sdk__"></span><span id="WINDOWS_SDK__"></span>Windows SDK <br/>                                                                                                      | [Windows SDKs](https://msdn.microsoft.com/bb980924.aspx)<br/>                                                                                      |
| <span id="User_Account_Control_Guidelines__"></span><span id="user_account_control_guidelines__"></span><span id="USER_ACCOUNT_CONTROL_GUIDELINES__"></span>User Account Control Guidelines <br/>                      | [Windows Vista Application Development Requirements for User Account Control Compatibility](/previous-versions/dotnet/articles/bb530410(v=msdn.10))<br/> |
| <span id="WinQual_Developer_Portal__"></span><span id="winqual_developer_portal__"></span><span id="WINQUAL_DEVELOPER_PORTAL__"></span>WinQual Developer Portal <br/>                                                  | [Windows Quality Online Services (Winqual)](/windows-hardware/drivers/dashboard/winqual-submission-tool--winqualexe-)<br/>                                                                         |
| <span id="DirectX_Developer_Portal__"></span><span id="directx_developer_portal__"></span><span id="DIRECTX_DEVELOPER_PORTAL__"></span>DirectX Developer Portal <br/>                                                  | [Directx Developer Center](/previous-versions/windows/apps/hh452744(v=win.10))<br/>                                                                               |
| <span id="Games_for_Windows_and_DirectX_SDK_Blog"></span><span id="games_for_windows_and_directx_sdk_blog"></span><span id="GAMES_FOR_WINDOWS_AND_DIRECTX_SDK_BLOG"></span>Games for Windows and DirectX SDK Blog<br/> | [Games for Windows and the DirectX SDK](https://walbourn.github.io/)<br/>                                                                           |
| <span id="Additional_DirectX_Articles"></span><span id="additional_directx_articles"></span><span id="ADDITIONAL_DIRECTX_ARTICLES"></span>Additional DirectX Articles<br/>                                             | [DirectX Technical Articles](/windows/desktop/DxTechArts/dx9-technical-articles)<br/>                                                                                    |



 

 

