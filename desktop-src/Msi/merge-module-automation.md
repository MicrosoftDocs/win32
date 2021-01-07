---
description: Mergemod.dll provides a COM object that implements merge operations and source image generation for merge modules. The main object implements interfaces for C/C++ programs and automation clients, including Visual Basic and VBScript.
ms.assetid: 877d3691-948f-4aea-89d8-0ff008126ccc
title: Merge Module Automation
ms.topic: article
ms.date: 05/31/2018
---

# Merge Module Automation

Mergemod.dll provides a COM object that implements merge operations and source image generation for merge modules. The main object implements interfaces for C/C++ programs and automation clients, including Visual Basic and VBScript.

The preferred method for installing Mergemod.dll is by using the Windows Installer. The Component ID for the component containing the Mergemod.dll COM interface is {FD153241-37EC-11D2-8892-00A0C981B015}. The same binary can be used on all Windows systems and the dll will self-register through regsvr32 on older systems.

Note that Mergemod.dll requires that the Msvcrt.dll be installed on the system.

Note that Mergemod.dll 2.0 is required to create [Configurable Merge Modules](configurable-merge-modules.md). Mergemod.dll version 2.0 provides extended functionality at build time through the [**IMsmMerge2**](/windows/desktop/api/Mergemod/nn-mergemod-imsmmerge2) Interface. This CLSID supports all the existing functionality of the [**IMsmMerge**](/windows/win32/api/mergemod/nn-mergemod-imsmmerge) Interface provided by Mergemod.dll version 1.0. The default interface on the [**Merge**](merge-object.md) object of Mergemod.dll 2.0 is the **IMsmMerge2** interface instead of the **IMsmMerge** interface.

[Object Model for Mergemod.dll Version 1.0](object-model-for-mergemod-dll-version-1-0.md)

[Object Model for Mergemod.dll Version 2.0](object-model-for-mergemod-dll-version-2-0.md)

 

 
