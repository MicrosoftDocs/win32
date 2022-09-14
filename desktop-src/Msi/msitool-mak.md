---
description: Msitool.mak is a makefile that you can use to build tools and custom actions.
ms.assetid: c05da933-7e0e-4fbb-a936-517902a363c4
title: Msitool.mak
ms.topic: article
ms.date: 05/31/2018
---

# Msitool.mak

Msitool.mak is a makefile that you can use to build tools and custom actions. It may be used with Visual C++ version 4.0 or later. For more information, see the header file. It requires a set of values to be defined before including this file. Typically developers put those at the start of the .cpp, ifdef'd to be skipped by the C compiler. Likewise resources are added to the end of the .cpp file. See samples for details.

VCBIN can be defined to the directory where the Visual C++ tools are found or the makefile uses MSVCDIR and MSDEVDIR. If those are not defined, it does not specify a location, assuming the tools to be on the PATH. An issue with the environment variables in Visual C++ version 5.0 is that if both are not on you path, the linker cannot find Msdis100.dll. If you copy that from MSDEVDIR to MSVCDIR, it works. The other option is to copy Msdis100.dll and Rc.exe and Rcdll.dll to MSVCDIR, and set VCBIN to that.

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



