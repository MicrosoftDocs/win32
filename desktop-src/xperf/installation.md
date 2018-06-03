---
title: Installation
description: Installation
ms.assetid: 8ab613f2-3327-465f-9b02-1e63023a0053
keywords:
- Windows Performance Analyzer, installation
- .msi
- PATH
- install
- target system
- perfctrl.dll
- x64
- Windows XP
- Windows Server 2003
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Installation

### Installation Overview

Windows Performance Analyzer (WPA) is distributed as part of the Windows Performance Toolkit (WPT). WPT is installed as part of the entire SDK installation in the following versions of the SDK:

-   Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1

-   Microsoft Windows SDK for Windows Server 2008 and .NET Framework 3.5

Starting with the Microsoft Windows SDK for Windows 7 and .NET Framework 4, WPT can also be installed without requiring a full SDK installation. To install only WPT, follow these steps:

1.  From the [Windows Performance Analysis Developers Center](http://go.microsoft.com/fwlink/p/?linkid=185272), download the Windows SDK for Windows 7 and .NET Framework 4 (or a later version of the SDK).

2.  When the Windows SDK Wizard starts, click **Next** until you reach the **Installation Options** page.

3.  On the **Installation Options** page, clear all options and then select **Windows Performance Toolkit** from the **Common Utilities** option.

4.  Click **Next** to continue with the installation of the selected SDK components.

For more information about how to acquire WPT, see [Windows Performance Analysis Developers Center](http://go.microsoft.com/fwlink/p/?linkid=185272).

### WPA Installation Files

The following installation files are in an .msi format:

<dl> <dt>

<span id="Xperf_x86.msi"></span><span id="xperf_x86.msi"></span><span id="XPERF_X86.MSI"></span>*Xperf\_x86.msi*
</dt> <dd>

Contains the WPA binary files for x86-based systems.

</dd> <dt>

<span id="Xperf_x64.msi"></span><span id="xperf_x64.msi"></span><span id="XPERF_X64.MSI"></span>*Xperf\_x64.msi*
</dt> <dd>

Contains the WPA binary files for x64-based systems.

</dd> <dt>

<span id="Xperf_ia64.msi"></span><span id="xperf_ia64.msi"></span><span id="XPERF_IA64.MSI"></span>*Xperf\_ia64.msi*
</dt> <dd>

Contains the WPA binary files for Itanium-based systems.

</dd> </dl>

These installation files are located in the *bin* subdirectory of the SDK when WPT is installed from the followings versions of the SDK:

-   Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1

-   Windows SDK for Windows Server 2008 and .NET Framework 3.5

Starting with the Windows SDK for Windows 7 and .NET Framework 4, these installation files are located in the *Redist\\Windows Performance Toolkit* subdirectory of the SDK.

### WPA Installation Instructions

The installation can be performed by double clicking the appropriate .msi file or manually running the installation file. For information on running the file manually, see the online MSDN documentation.

By default WPA installs in the \\Program Files\\Microsoft Windows Performance Analyzer directory. This path is automatically added to the system PATH variable. If you choose to install WPA in a folder other than the default folder, the system PATH variable must include your WPA executable directory.

### WPA Installation on Windows XP SP2 and Windows Server 2003 SP1

WPA can be installed and used on Windows XP SP2 and Windows Server 2003 SP1 to gather trace information. Note that the stackwalk function is not available in these environments, because in Windows XP SP2 and Windows Server 2003 SP1 the required event gathering capabilities are not available. Furthermore, all operations that require trace decoding must be done on Vista or Windows Server 2008. This includes viewing traces in the Windows Performance Analyzer tool (*Xperfview.exe*).

In order to capture trace information on Windows XP SP2 or Windows Server 2003 SP1 take the following steps:

1.  From the Windows Performance Analyzer directory on a Windows Vista or Windows Server 2008 machine, copy *Xperf.exe* and *Perfctrl.dll* to a directory that is in the PATH environment variable of the Windows XP SP2 or Windows Server 2003 target system.

2.  On the Windows XP SP2 or Windows Server 2003 target system, run the trace using standard WPA syntax.

3.  Copy the "etl" files to a Windows Vista or Windows Server 2008 system that has a full installation of WPA.

4.  Use Performance Analyzer, as detailed in the [Windows Performance Analyzer Basics](quick-start-guide--wpa-basics.md) section of this document.

### Enabling Stack Walking on x64 Systems

Stackwalking on x64 systems requires the **DisablePagingExecutive** registry value to be set in **HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management**. For more information, see [DisablePagingExecutive](http://go.microsoft.com/fwlink/p/?linkid=141517).

The following examples show how to set this value by using command scripts:

-   **QueryStackwalk64.cmd:**

    ```
    ----8<----
    @REG QUERY "HKLM\System\CurrentControlSet\Control\Session Manager\Memory Management" -v DisablePagingExecutive
    ----8<----
    ```

    

-   **TurnOnStackwalk64.cmd:**

    ```
    ----8<----
    @REG ADD "HKLM\System\CurrentControlSet\Control\Session Manager\Memory Management" -v DisablePagingExecutive -d 0x1 -t REG_DWORD -f
    @IF NOT %ERRORLEVEL% == 0 echo error: Could not configure system for 64-bit stackwalking.  Please run this script from an elevated administrator console.
    ----8<----
    ```

    

    > [!Note]  
    > To make these changes effective, you must restart the system.

     

-   **TurnOffStackwalk64.cmd:**

    ```
    ----8<----
    @REG ADD "HKLM\System\CurrentControlSet\Control\Session Manager\Memory Management" -v DisablePagingExecutive -d 0x0 -t REG_DWORD -f
    @IF NOT %ERRORLEVEL% == 0 echo error: Could not remove 64-bit stackwalking configuration.  Please run this script from an elevated administrator console.
    ----8<----
    ```

    

    > [!Note]  
    > To make these changes effective, you must restart the system.

     

 

 




