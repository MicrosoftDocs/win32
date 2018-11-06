---
title: Environment Setup
description: The installed Platform Software Development Kit (SDK) provides a Setenv.bat file located in the root directory of the Platform SDK that you can run to set up your environment for building applications that use the Platform SDK.
ms.assetid: 2dec3d7a-acac-4ff7-9d4a-d3540e6d441d
ms.topic: article
ms.date: 05/31/2018
---

# Environment Setup

The installed Platform Software Development Kit (SDK) provides a Setenv.bat file located in the root directory of the Platform SDK that you can run to set up your environment for building applications that use the Platform SDK.

## Settings and Variables

You can also manually set up your environment by adding something like the following to your Autoexec.bat file. Using Windows, you can edit the Autoexec.bat file to include these commands. Using Windows Server 2003, Windows XP, Windows 2000, or Windows NT, you can edit or add these settings to your environment variables using the System dialog that you can run from the Control Panel.


```cmd
  SET INCLUDE=D:\MSSDK\INCLUDE;C:\MSDEV\INCLUDE;C:\MSDEV\ATL\INCLUDE
  SET LIB=D:\MSSDK\LIB;C:\MSDEV\LIB
  SET MSSDK=D:\MSSDK
  SET MSTOOLS=D:\MSSDK
  SET CPU=i386
  SET PATH=C:\WIN95;C:\WIN95\COMMAND;C:\DOS;D:\MSSDK\BIN;C:\MSDEV\BIN
```



These settings are appropriate for an Intel 80386 or later platform running Windows Me, Windows 98, or Windows 95 with both Microsoft Visual C++ and the Platform SDK installed. For example, on this system, Visual C++ version 5.0 is installed under the C:\\MSDEV directory. The Platform SDK is installed under the D:\\MSSDK directory. Your disk configuration may be different. The Platform SDK directories (for this example, those with D:\\MSSDK in them) are all earlier in each path sequence. This sequence assumes that command line compilations are intended to be run in the Command Prompt window and that the .h include and .lib library files in the Platform SDK are preferred for those compilations.

The CPU environment variable is defined to control the Win32 builds, depending on the platform. Current possible values include i386, MIPS, ALPHA, and PPC. For more information, see the Win32.mak file provided in the Platform SDK in the \\MSSDK\\INCLUDE directory. All of the COM tutorial code sample makefiles include Win32.mak.

 

 




