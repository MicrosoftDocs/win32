---
description: The DbgHelp library is implemented by DbgHelp.dll.
ms.assetid: 8ef1740d-c791-4fbd-8297-7207a987c09d
title: DbgHelp Versions
ms.topic: article
ms.date: 05/31/2018
---

# DbgHelp Versions

The DbgHelp library is implemented by DbgHelp.dll. Although this DLL is included in all supported versions of Windows, it is rarely the most current version of DbgHelp available. Furthermore, the version of DbgHelp that ships in Windows has reduced functionality from the other releases-- specifically, it lacks support for Symbol Server and Source Server.

The most current versions of DbgHelp.dll, SymSrv.dll, and SrcSrv.dll are available as a part of the [Debugging Tools For Windows](https://developer.microsoft.com/windows/downloads/windows-10-sdk) package. The redistribution policies make it possible for people to include the Debugging Tools For Windows installer in their own packages and releases.

> [!Caution]  
> Users should never attempt to install the [Debugging Tools For Windows](https://developer.microsoft.com/windows/downloads/windows-10-sdk) versions of DbgHelp.dll into the Windows system directories because they are untested in this scenario and likely to destabilize the system. There are separate X64 and X86 versions of the debugging package and both are necessary for people interested in supporting both platforms.

To obtain the latest version of DbgHelp.dll, go to [https://developer.microsoft.com/windows/downloads/windows-10-sdk](https://developer.microsoft.com/windows/downloads/windows-10-sdk) and download Debugging Tools for Windows. Refer to [Calling the DbgHelp Library](calling-the-dbghelp-library.md) for information on proper installation.

> [!Note]  
> The DbgHelp.dll file that ships in Windows is not redistributable.

Many versions of DbgHelp include additional functionality. To ensure that the correct version of DbgHelp is available for your application, review the Requirements information in the specific API reference documentation.
