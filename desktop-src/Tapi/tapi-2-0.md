---
description: TAPI 2.0 provides a small number of enhancements to the basic TAPI 1.4 functionality.
ms.assetid: f3a319b4-5e82-4bf9-bd89-a027d58ad126
title: TAPI 2.0
ms.topic: article
ms.date: 05/31/2018
---

# TAPI 2.0

TAPI 2.0 provides a small number of enhancements to the basic TAPI 1.4 functionality. However, there were some major architectural changes that greatly improved its stability. Most of the changes were fundamental changes necessary to bring TAPI to Windows NT 4.0 and take advantage of its features (full 32-bit support, services, and Unicode). However, these changes were internal to TAPI and had little effect on TAPI applications.

Applications that support TAPI 1.3 and 1.4 (16-bit applications by way of a thunking layer) work well on Windows Server 2003 operating systems, Windows XP, Windows 2000, and Windows NT. However, the effect on service-provider developers was significant. Service providers for these operating systems must be fully 32-bit Unicode DLLs that can run in the context of TAPISRV, not in the context of the TAPI application (as did all earlier Win16-based TSPs). TSPs designed for TAPI 1.4 do not work on Windows Server 2003 operating systems, Windows XP, Windows 2000, or Windows NT.

TAPI 2.0 also adds the important features of call center support and Quality of Service (QOS) support.

The TAPI system binaries that come with Windows support TAPI versions 1.3 and 1.4 for all applications. However, 16-bit applications cannot use TAPI 2.0, and you cannot use a 16-bit TAPI 2.x TSP.

 

 



