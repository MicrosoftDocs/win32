---
title: Snap-in Development Tools
description: Lists snap-in development tools.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0c0231eb-e973-4517-a5ba-0d42148e053d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in development tools MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Snap-in Development Tools

You can create snap-ins in any development environment that supports producing COM components. Some of the most common development environments are Microsoft Visual C++ 5.0 and 6.0, and Microsoft Visual Basic 6.0. Each development tool has slightly different requirements, as follows:

<dl> <dt>

<span id="Visual_C___5.0"></span><span id="visual_c___5.0"></span><span id="VISUAL_C___5.0"></span>Visual C++ 5.0
</dt> <dd>

Current Platform Software Development Kit (SDK), including the MMC SDK; must use LINK.exe

</dd> <dt>

<span id="Visual_C___6.0"></span><span id="visual_c___6.0"></span><span id="VISUAL_C___6.0"></span>Visual C++ 6.0
</dt> <dd>

Current Platform SDK, including the MMC SDK

</dd> <dt>

<span id="Visual_Basic_6.0"></span><span id="visual_basic_6.0"></span><span id="VISUAL_BASIC_6.0"></span>Visual Basic 6.0
</dt> <dd>

MMC Snap-in Designer for Visual Basic

</dd> </dl>

The MMC Programmer's Guide (for C++ programmers) and the MMC Snap-in Designer for Visual Basic (for Visual Basic programmers) provide additional information to snap-in developers. A brief overview of each is included here.

## MMC Programmer's Guide

The MMC Programmer's Guide is part of the MMC SDK. Because a snap-in is a COM in-process server DLL, you should be familiar with creating COM DLLs before starting work with the SDK.

In addition, the reference portion of the MMC SDK documentation covers approximately 30 COM interfaces that you need to become acquainted with, although you may need only a few for your snap-in. You need to know what each interface does so that you can choose the ones you need. Snap-ins implement some of these interfaces and expose them to MMC. MMC implements the remaining interfaces and exposes them to snap-ins to use.

For more specific information, see the [MMC Programmer's Guide](mmc-programmer-s-guide.md).

 

 




