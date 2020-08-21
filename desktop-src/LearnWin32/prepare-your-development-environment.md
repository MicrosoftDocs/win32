---
title: Prepare Your Development Environment
description: Prepare Your Development Environment
ms.assetid: 5a3fd27e-ec8f-41eb-9d31-86d6d9f70862
ms.topic: article
ms.date: 10/03/2019
---

# Prepare Your Development Environment

To write a Windows program in C or C++, you must install the Microsoft Windows Software Development Kit (SDK) or Microsoft Visual Studio. The Windows SDK contains the headers and libraries necessary to compile and link your application. The Windows SDK also contains command-line tools for building Windows applications, including the Visual C++ compiler and linker. Although you can compile and build Windows programs with the command-line tools, we recommend using Microsoft Visual Studio. You can download a free download of Visual Studio Community or free trials of other versions of Visual Studio [here](https://visualstudio.microsoft.com/downloads/).

Each release of the Windows SDK targets the latest version of Windows as well as several previous versions. The release notes list the specific platforms that are supported, but unless you are maintaining an application for a very old version of Windows, you should install the latest release of the Windows SDK. You can download the latest Windows SDK [here](https://developer.microsoft.com/windows/downloads/windows-10-sdk).

The Windows SDK supports development of both 32-bit and 64-bit applications. The Windows APIs are designed so that the same code can compile for 32-bit or 64-bit without changes.

> [!Note]  
> The Windows SDK does not support hardware driver development, and this series will not discuss driver development. For information about writing a hardware driver, see [Getting Started with Windows Drivers](/windows-hardware/drivers/gettingstarted/).

## Next

[Windows Coding Conventions](windows-coding-conventions.md)

## Related topics

* [Download Visual Studio](https://visualstudio.microsoft.com/downloads/)
* [Download Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk)