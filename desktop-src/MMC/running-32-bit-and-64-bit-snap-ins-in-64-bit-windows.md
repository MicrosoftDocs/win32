---
title: Running 32-bit and 64-bit Snap-ins in 64-bit Windows
description: Microsoft 64-bit operating systems can run both 32-bit MMC (MMC32) and 64-bit MMC (MMC64).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 75634482-c1ca-4a3d-968f-8bc13e6fbda9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Running 32-bit and 64-bit Snap-ins in 64-bit Windows

Microsoft 64-bit operating systems can run both 32-bit MMC (MMC32) and 64-bit MMC (MMC64). MMC64 cannot run 32-bit snap-ins, and MMC32 cannot run 64-bit snap-ins. This topic describes how to determine and control which version of MMC is executed in 64-bit Windows.

MMC can be executed with command-line parameters, such as a console file name. Additionally, the following command-line switches are recognized by MMC64:

-   -32
-   -64

If both of the preceding switches are specified on the command line, the rightmost switch is in effect.

## Start-up considerations if -32 or -64 is in effect.

If MMC64 is started with no command-line parameters, or if MMC64 is started with the -64 switch, it executes as the MMC64 application. If MMC64 is started with the -32 switch, MMC32 is launched, using the same parameters initially passed to MMC64 (except the -32 switch), and MMC64 will terminate.

## Start-up considerations if a console file is specified.

If the MMC64 command line does not contain a -32 or -64 switch, but the command line does contain a console file name, then MMC64 examines the console file before determining which version of MMC remains in execution. MMC64 uses the following algorithm.

1.  If all snap-ins referenced by the console file are available in 64-bit form, then MMC64 will remain as the executing version (the remaining algorithm Steps are not executed). A snap-in is considered available in 64-bit form if it exists as an HKEY\_CLASSES\_ROOT\\ **CLSID**\\snap-in clsid\\InprocServer32 key in the registry, where snap-in clsid is the registered CLSID for the snap-in.
2.  If not all snap-ins referenced by the console file are available in 64-bit form, but all of them are available in 32-bit form, then MMC64 starts MMC32; MMC32 executes using the console file as specified on the command line, and MMC64 terminates (the remaining algorithm Steps are not executed). A snap-in is considered available in 32-bit form if it exists as a HKEY\_CLASSES\_ROOT\\Wow6432Node\\ **CLSID**\\snap-in clsid\\InprocServer32 key in the registry, where snap-in clsid is the registered CLSID for the snap-in.
3.  If the number of unavailable 64-bit snap-ins is a subset of the unavailable 32-bit snap-ins, then MMC64 remains as the executing version (the remaining algorithm Steps are not executed).
4.  If the number of unavailable 32-bit snap-ins is a subset of the unavailable 64-bit snap-ins, then MMC64 starts MMC32, and MMC64 terminates (the remaining algorithm Step is not executed).
5.  If none of the previous Steps yields a conclusion, then a user interface is presented to the user, prompting the user to specify which version of MMC to execute (an option to cancel is also presented to the user).

> [!Note]  
> In any event where MMC64 fails to successfully start MMC32, MMC64 continues executing. After MMC32 has been successfully started by MMC64, then MMC64 terminates. If an error occurs after MMC32 has successfully started, MMC64 is not notified, as it will have already been terminated.

 

 

 




