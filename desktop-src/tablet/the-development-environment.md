---
description: You do not need a Tablet PC to develop Tablet PC applications, but you do need a personal computer capable of running the software listed later in this topic.
ms.assetid: 82034950-78a7-4bab-b449-1b8ea7d90676
title: The Development Environment
ms.topic: article
ms.date: 05/31/2018
---

# The Development Environment

You do not need a Tablet PC to develop Tablet PC applications, but you do need a personal computer capable of running the software listed later in this topic.

We strongly recommend that you test your application on an actual Tablet PC to ensure that all differences in hardware, such as the higher resolution digitizer, are accounted for.

A typical, minimal development system consists of the following hardware and software.

## Hardware

-   8 MB of hard disk space for a complete installation.
-   A pointing device for input. This includes devices such as a mouse, an external tablet, or a Tablet PC with an HID digitizer.

HID stands for Human Interface Device, a standard for input devices. Non-HID compliant digitizers are treated like a regular mouse, while HID compliant digitizers have higher resolution and more metadata on strokes, such as pressure, similar to those that are installed on Tablet PC hardware.

## Software

The following operating systems can be used to develop Tablet PC applications:

-   Windows 7
-   Windows Vista
-   Windows Server 2008
-   Windows XP Tablet PC Edition 2005
-   Windows Server 2003
-   Windows XP Professional

You also need:

-   Visual Studio version 6 with Service Pack 5, or Visual Studio .NET, or Visual Studio .NET 2005
-   Microsoft Internet Explorer 6, or higher (recommended)

### Details on Developing on Non-Tablet PC SKUs of Windows

The Tablet PC platform components can be installed on Windows XP Professional with Service Pack 2 or Windows Server 2003. On these operating systems, your application can collect ink with the [**InkCollector**](inkcollector-class.md) class and can be tested and debugged. However, no recognition is available unless you also install the Microsoft Windows XP Tablet PC Edition 2005 Recognizer Pack. You can download that pack from the Download Center on MSDN.

After installing the Windows SDK on to a Windows XP Professional or Windows Server 2003 system, you will have all the development files necessary to build ink applications (such as msinkaut.h for a COM developer). However, you will be unable to run or debug your application on that system until you install the runtime files. For instance, in the case of a COM developer, inkobj.dll must be installed and registered. Because you are not on a system where these platform files exist, you must install the Tablet PC platform components from the redistributable merge module, mstpcrt.msm, to get the runtime files on your system.

The simplest way to get the platform runtimes installed on a Windows XP Professional or Windows 2000 system for development purposes is to compile the sample setup project provided with the Mobile PC and Tablet PC Samples and deploy it to the development machine.

> [!Note]  
> Windows Vista and Windows XP Tablet PC Edition 2005 already have the platform components installed, so they do not require additional steps to run and debug Tablet PC applications.

 

The [InkEdit](inkedit-control-reference.md) and [InkPicture](inkpicture-control-reference.md) controls can be used to collect ink on Windows 2000 with Service Pack 4 or Windows XP Professional with Service Pack 2 when the Tablet PC platform components are present by installing the Tablet PC SDK version 1.7, but are not able to collect ink on non-Tablet PC systems that do not have the Tablet PC platform components installed.

The Windows SDK provides all the necessary components to develop Tablet PC applications on non-Tablet SKUs of Windows. Set the following **DWORD** registry key to 1 in order to collect ink on non-Tablet SKUs of Windows:

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\TabletPC\Controls\EnableInkCollectionOnNonTablets`

This key is intended for development purposes only.

 

 



