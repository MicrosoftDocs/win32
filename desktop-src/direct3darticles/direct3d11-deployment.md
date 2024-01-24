---
title: Direct3D 11 deployment for game developers
description: This article describes how to deploy the Direct3D 11 components on a system if necessary.
ms.assetid: 1fd43638-0d67-4a94-3be6-8789095f491e
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 11 deployment for game developers

This article describes how to deploy the Direct3D 11 components on a system if necessary.

-   [Overview](#overview)
-   [Direct3D 11.3](#direct3d-113)
-   [Direct3D 11.2](#direct3d-112)
-   [Direct3D 11.1](#direct3d-111)
-   [D3D11InstallHelper.dll](#d3d11installhelperdll)
-   [D3D11Install.exe](#d3d11installexe)
-   [Integrating into Installation Programs](#integrating-into-installation-programs)
    -   [Integrating into InstallShield](#integrating-into-installshield)
    -   [Integrating into an MSI Package](#integrating-into-an-msi-package)
-   [Debugging Tips](#debugging-tips)
-   [Corporate Settings](#corporate-settings)
-   [Related Articles](#related-articles)

## Overview

The Direct3D 11 API extends the existing Direct3D 10.1 API with support for multithreaded rendering and resource creation, Compute Shader, hardware tessellation, BC6H/BC7 texture compression, and HLSL Shader Model 5.0 with Dynamic Shader Linkage. In addition to the Direct3D 11 component, a number of additional graphics components are included in the DirectX 11 runtime: Direct3D 11, DXGI 1.1, 10level9 feature levels, WARP10 software rendering device, Direct2D, DirectWrite, and an updated Direct3D 10.1 with support for 10level9 and WARP10. For information on these and other Windows graphics components, see [Graphics APIs in Windows](graphics-apis-in-windows-vista.md).

All of these new graphics components are built into the Windows 7 and Windows Server 2008 R2 operating systems. The Direct3D 11 API and related components can also be installed on Windows Vista by using a system update from Windows Update. This update requires Windows Vista and Service Pack 2. End-users with automatic updates enabled will, therefore, likely already have the Direct3D 11 components installed, as will all Windows 7 users.

The D3D11InstallHelper sample is designed to simplify detection of the Direct3D 11 API, automatically install the system update if applicable to an end-user's computer, and to provide appropriate messages to the end-user on manual procedure if a newer Service Pack is required.

> [!Note]  
> The HLSL compiler (D3DCompile\*.dll) and the D3DX utility library for Direct3D 11 (D3DX11\*.dll) are not built into any version of the Windows operating system, but they can be deployed as part of an application's installer by using the existing DirectSetup technology; for more information about using DirectSetup, see [DirectX Installation for Game Developers](/windows/desktop/DxTechArts/directx-setup-for-game-developers). "Effects 11" is available as a shared source support library at [Effects for Direct3D 11 Update](https://github.com/Microsoft/FX11), and you can include it directly into an app (much like the DXUT utility library). Thus, it doesn't have any additional run-time redistribution requirements.

## Direct3D 11.3

Windows 10 ships with the Direct3D 11.3 API built in. See [Direct3D 11.3 Features](/windows/desktop/direct3d11/direct3d-11-3-features) for a list of new features in the Direct3D 11.3 API.

## Direct3D 11.2

Windows 8.1 and Windows Server 2012 R2 ship with the Direct3D 11.2 API built in. See [Direct3D 11.2 Features](/windows/desktop/direct3d11/direct3d-11-2-features) for a list of new features in the Direct3D 11.2 API.

## Direct3D 11.1

Windows 8 and Windows Server 2012 ship with the [Direct3D 11.1 API](/windows/desktop/direct3d11/direct3d-11-1-features) built in. Partial support for the Direct3D 11.1 API is available on Windows 7 or Windows Server 2008 R2 with the [Platform Update for Windows 7](https://support.microsoft.com/kb/2670838) installed. For more info about the Platform Update for Windows 7, see [Platform Update for Windows 7](platform-update-for-windows-7.md).

## D3D11InstallHelper.dll

D3D11InstallHelper.dll hosts the core functionality for detecting Direct3D 11 components, and performing the system update through the Windows Update service if applicable. The DLL displays no messages or dialog boxes directly.

The DLL consists of the following entry points:

<dl> <dt>

<span id="CheckDirect3D11Status"></span><span id="checkdirect3d11status"></span><span id="CHECKDIRECT3D11STATUS"></span>CheckDirect3D11Status
</dt> <dd>

This function performs the necessary checks and returns the status of Direct3D 11 on this computer. This function does not require administrator rights.

-   A status of D3D11IH\_STATUS\_INSTALLED indicates that Direct3D 11 is already installed on the computer and is ready for use.
-   D3D11IH\_STATUS\_NOT\_SUPPORTED indicates that this version of Windows does not support Direct3D 11 or related technologies.
-   A status of D3D11IH\_STATUS\_NEED\_LATEST\_SP indicates that the latest Windows Vista Service Pack should be installed by the user.
-   Finally, a status of D3D11IH\_STATUS\_REQUIRES\_UPDATE indicates that the system does not have Direct3D 11 installed, but that the system update does apply to this version of Windows.

</dd> <dt>

<span id="DoUpdateForDirect3D11"></span><span id="doupdatefordirect3d11"></span><span id="DOUPDATEFORDIRECT3D11"></span>DoUpdateForDirect3D11
</dt> <dd>

This function uses the Windows Update API to perform the system update for installing Direct3D 11 on this system, if applicable. Note that this function requires network connectivity to Windows Update to succeed, as well as administrative rights. It takes an optional progress callback function and user-context pointer, and returns a final result code when complete.

-   The D3D11IH\_RESULT\_SUCCESS result indicates that the system update was applied and is ready for use, while D3D11IH\_RESULT\_SUCCESS\_REBOOT indicates that the system update requires the computer is restarted before it is complete. Note that this function does not schedule a system restart.
-   D3D11IH\_RESULT\_NOT\_SUPPORTED indicates that the system update does not apply to this version of Windows. This result should not occur if this function is only called after getting a D3D11IH\_STATUS\_REQUIRES\_UPDATE status from CheckDirect3D11Status.
-   A result of D3D11IH\_RESULT\_UPDATE\_NOT\_FOUND indicates that the system update package was not found on the Windows Update servers.
-   If the Windows Update download or installation fails, then D3D11IH\_RESULT\_UPDATE\_DOWNLOAD\_FAILED or D3D11IH\_RESULT\_UPDATE\_INSTALL\_FAILED will be returned as the result.
-   If a network connectivity error is returned from the Windows Update API, then the D3D11IH\_RESULT\_WU\_SERVICE\_ERROR result is returned, indicating that the problem might be intermittent or related to network configuration or firewall settings. Trying the update function again may succeed.

</dd> </dl>

For more information on the Windows Update API, see [Windows Update Agent API](/windows/desktop/Wua_Sdk/portal-client).

## D3D11Install.exe

> [!Note]  
> D3D11Install.exe requires D3D11InstallHelper.dll to execute.

D3D11Install.exe is a tool for using D3D11InstallHelper.dll as a stand-alone installer complete with UI and end-user messages, as well as acting as an example for proper use of the DLL. The process exits with a 0 if Direct3D 11 is already installed, if the system update applies successfully without requiring a system restart, if a Service Pack installation is required, or if Direct3D 11 is not supported by this computer. A 1 is returned if the system update is applied successfully and requires a system restart to complete. A 2 is returned for other error conditions. Note that this executable file requires administrator rights to run, and it has a manifest that requests elevation when run on Windows Vista or Windows 7 with UAC enabled. D3D11Install.exe can be used as a stand-alone tool for deploying the Direct3D 11 update, or it can be used directly by installers.

It supports the following command-line switches:

<dl> <dt>

<span id="_quiet__"></span><span id="_QUIET__"></span>/quiet 
</dt> <dd>

Displays no messages, prompts, progress dialog boxes, or error messages.

</dd> <dt>

<span id="_passive__"></span><span id="_PASSIVE__"></span>/passive 
</dt> <dd>

Displays no messages, prompts, or error messages, but will show the progress dialog box.

</dd> <dt>

<span id="_minimal__"></span><span id="_MINIMAL__"></span>/minimal 
</dt> <dd>

Shows only minimal prompts.

</dd> <dt>

<span id="_y__"></span><span id="_Y__"></span>/y 
</dt> <dd>

Suppresses prompting to confirm installing the update, if needed and applicable, for a standard and minimal installation.

</dd> <dt>

<span id="_langid_decimal__"></span><span id="_LANGID_DECIMAL__"></span>/langid decimal 
</dt> <dd>

Forces which language identifier code to use when displaying end-user messages and dialog box resources. The default value is 1024, which uses the system default language setting.

</dd> <dt>

<span id="_wu__"></span><span id="_WU__"></span>/wu 
</dt> <dd>

Forces use of Windows Update rather than the system default, which may be Windows Server Update Services (WSUS) running on a managed server or some other non-standard configuration.

</dd> </dl>

## Integrating into installation programs

To comply with Support Easy Installation, [Technical Requirement 3.1 for Games for Windows](/windows/desktop/DxTechArts/games-for-windows-technical-requirements-1-1-0006), care needs to be taken so that any end-user prompts are presented early in the installation process, and to ensure that there are not multiple UAC-related elevation prompts. There are three basic choices for achieving this goal:

1.  The most basic method is to execute the D3D11Install.exe with the command-line switch **/minimal**. This should be done early in the installer Q&A, and the installation should use the return value of 1 to indicate that a restart should be scheduled at the end of the installation. Executing the program requires administrative rights.
2.  Use D3D11InstallHelper.dll directly to detect the need for the update, providing any end-user messages necessary for the status D3D11IH\_STATUS\_NEED\_LATEST\_SP, where the resolution requires manual user operations. The status result of D3D11IH\_STATUS\_NOT\_SUPPORTED could be used to control installation of Direct3D 11–related assets, or as an error condition for Direct3D 11–only applications, but it is otherwise not necessarily a useful end-user message. For the status D3D11IH\_STATUS\_REQUIRES\_UPDATE, the installer can directly use the DLL entry point DoUpdateForDirect3D11 to perform the update and handle the various resulting end-user messages. Examples of standard messages can be found by examining the D3D11Install.exe dialog box and string table resources. The update entry point requires administrator rights.
3.  A hybrid approach is to check status with D3D11InstallHelper.dll, and in the case of the status code D3D11IH\_STATUS\_NEED\_LATEST\_SP or D3D11IH\_STATUS\_REQUIRES\_UPDATE, D3D11Install.exe can be executed with the switches **/minimal** and **/y** to display the dialog box or to perform the update, as needed. These steps should be performed early in the installation process, usually immediately after the Q&A, and running the executable requires administrative rights.

### Integrating into InstallShield

Handling the Direct3D 11 deployment from InstallShield's InstallScript is easily done using the D3D11InstallHelper sample. The steps required to integrate with InstallShield using InstallScript are as follows (using method 3, described in the previous section):

1.  Open an InstallScript project in the InstallShield editor.
2.  Add D3D11InstallHelper.dll and D3D11Install.exe to the project in **Support Files**.

    **To add the files to the InstallShield Project**

    1.  On the **Installation Designer** tab, click **Support Files/Billboards** under **Behavior and Logic** in the navigation pane on the left.
    2.  Click **Language Independent**, then right-click in the **Files** window and select **Insert Files**. Browse to add D3D11InstallHelper.dll and D3D11Install.exe. The default location for these files is: SDK root\\Samples\\C++\\Misc\\Bin\\x86

3.  In the InstallScript explorer, click the InstallScript file (usually Setup.rul) that will call the DLL or executable, located under **Behavior and Logic** in the navigation pane on the left.
4.  Paste the following InstallScript into the file near the top:

    ``` syntax
#define D3D11IH_STATUS_INSTALLED       0
#define D3D11IH_STATUS_NOT_SUPPORTED   1
#define D3D11IH_STATUS_REQUIRES_UPDATE 2
#define D3D11IH_STATUS_NEED_LATEST_SP  3
#define D3D11IH_STATUS_ERROR           -1
    prototype NUMBER D3D11InstallHelper.CheckDirect3D11StatusIS();

#define D3D11IH_RESULT_SUCCESS                0
#define D3D11IH_RESULT_SUCCESS_REBOOT         1
#define D3D11IH_RESULT_NOT_SUPPORTED          2
#define D3D11IH_RESULT_UPDATE_NOT_FOUND       3
#define D3D11IH_RESULT_UPDATE_DOWNLOAD_FAILED 4
#define D3D11IH_RESULT_UPDATE_INSTALL_FAILED  5
#define D3D11IH_RESULT_WU_SERVICE_ERROR       6
#define D3D11IH_RESULT_ERROR                  -1
    prototype NUMBER D3D11InstallHelper.DoUpdateForDirect3D11IS(BOOL);
    ```

5.  Paste the following InstallScript into the file in the **OnFirstUIBefore** function, just before the return 0:

    ``` syntax
    Dlg_D3D11:
        UseDLL( SUPPORTDIR ^ "D3D11InstallHelper.DLL" );
        nResult = D3D11InstallHelper.CheckDirect3D11StatusIS();   
        UnUseDLL( SUPPORTDIR ^ "D3D11InstallHelper.DLL" );
        
        if ( nResult = D3D11IH_STATUS_REQUIRES_UPDATE
             || nResult = D3D11IH_STATUS_NEED_LATEST_SP) then
            nResult = LaunchAppAndWait(
    SUPPORTDIR^"D3D11Install.exe",
    "/minimal /y", WAIT);
            if ( nResult < 0 ) then
                MessageBox("Unable to launch D3D11Install.exe",
     SEVERE);
            elseif ( nResult == 1 ) then
                BATCH_INSTALL = 1;
            endif;          
        endif;
    ```

### Integrating into an MSI package

The following is a high-level description of the steps required to integrate Direct3D 11 deployment using MSI custom actions (using method 3, described earlier in this topic):

1.  Add a property to the MSI Property table called **RelativePathToD3D11IH** that contains the relative path to D3D11Install.exe and D3D11InstallHelper.dll during installation (this is typically in the media image). This also sets an MSI property D3D11IH\_STATUS to the status returned by CheckDirect3D11Status (a string property equal to the enumeration symbol or "ERROR").
2.  After the CostFinalize action, call the D3D11InstallHelper.dll function **SetD3D11InstallMSIProperties** as an immediate custom action to set the appropriate MSI properties for the other custom actions.
3.  Upon installation, trigger a deferred custom action after the InstallFiles action that calls the D3D11InstallHelper.dll function **DoD3D11InstallUsingMSI**. The custom action must set the flag msidbCustomActionTypeNoImpersonate to run in an elevated context.
4.  After the InstallFinalize action, call the D3D11InstallHelper.dll function **FinishD3D11InstallUsingMSI** as an immediate custom action to handle the successful reboot request result code, if needed.

This procedure is described in detail in the following instructions, which describe a process that can be done using an MSI editor, such as the [Orca editor](/windows/desktop/Msi/orca-exe). Some MSI editors have wizards that simplify some of these configuration steps.

**To configure an MSI package for integration with D3D11InstallHelper.dll**

1.  Open the MSI package in Orca.
2.  Add the row shown in the following table to the Binary table in the MSI package.

    | Name    | Data                                         |
    |---------|----------------------------------------------|
    | D3D11IH | File path to the DLL\\D3D11InstallHelper.dll |

    

     

    > [!Note]  
    > This file will be embedded in the MSI package, so you must do this step every time that you recompile D3D11InstallHelper.dll.

     

3.  Add the rows shown in the following table to the CustomAction table in the MSI package. 

    | Action              | Type                                                                                                                                                                   | Source  | Target                       |
    |---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|------------------------------|
    | Direct3D11SetProps  | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue = 65                                                                        | D3D11IH | SetD3D11InstallMSIProperties |
    | Direct3D11DoInstall | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeInScript + msidbCustomActionTypeNoImpersonate = 3137 | D3D11IH | DoD3D11InstallUsingMSI       |
    | Direct3D11Finish    | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue = 65                                                                        | D3D11IH | FinishD3D11InstallUsingMSI   |

    

     

4.  Add the values shown for Action, Condition, and Sequence in the following table to the InstallExecuteSequence table in the MSI package. 

    | Action              | Condition     | Sequence | Notes                                                                                                                                                          |
    |---------------------|---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Direct3D11SetProps  |               | 1016     | The sequence number places the action soon after CostFinalize.                                                                                                 |
    | Direct3D11DoInstall | NOT Installed | 4004     | This custom action will only happen during a new installation for all users. The sequence number places the action after InstallFiles and after the rollbacks. |
    | Direct3D11Finish    |               | 6615     | The sequence number places the action soon after InstallFinalize.                                                                                              |

    

     

5.  Add the row shown in the following table to the **Property** table in the MSI package. 

    | Property              | Value                                                                        |
    |-----------------------|------------------------------------------------------------------------------|
    | RelativePathToD3D11IH | relative file path that contains D3D11Install.exe and D3D11InstallHelper.dll |

    

     

    > [!Note]  
    > The location specified by the path is relative to the location specified by the installation path—for example, "redist\\".

     

6.  Save the MSI package. For more detailed information about MSI packages and Windows Installer, see [Windows Installer](/windows/desktop/Msi/windows-installer-portal).

## Debugging tips

Both D3D11InstallHelper.dll and D3D11Install.exe can be built with the Debug configuration in Visual Studio, and these versions will print messages to the standard Windows debug output mechanism.

## Corporate settings

The D3D11InstallHelper sample is designed for standard deployment through Windows Update, which is the most common scenario for installation of a game by consumers. However, Many game developers, working for publishers and in development studios, do so in enterprise settings that have a locally managed server providing software updates by using Windows Server Update Services (WSUS) technology. In this type of environment, the local IT administrator has approval control over which updates are made available to computers within the corporate network, and the standard consumer version of update KB 971644 is not available.

There are three basic solutions for deploying DirectX 11 in corporate/enterprise settings:

-   In some configurations, it is possible to directly check Windows Update rather than use the locally managed WSUS server. For this reason, D3D11InstallHelper supports the **/wu** command-line switch. However, not all corporate networks allow connections to the public Microsoft servers.
-   The local IT administrator can approve KB 971512, an enterprise-supported update deployed from WSUS, that includes the Direct3D 11 API. This is the only option for a Standard User to obtain the Direct3D 11 update in an environment that is fully locked down.
-   Alternatively, [KB 971512](https://support.microsoft.com/kb/971512/) can be manually installed.

It is very rare that a gamer's computer can only get updates from a locally managed WSUS server, and it is only developers in large organizations who are likely to be in such environments.

## Related articles

[Windows Firewall for Game Developers](/windows/desktop/DxTechArts/games-and-firewalls)

[Windows Games Explorer for Game Developers](/windows/desktop/DxTechArts/windows-game-explorer-integration)
