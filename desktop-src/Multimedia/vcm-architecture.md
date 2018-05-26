---
title: VCM Architecture
description: VCM Architecture
ms.assetid: cb0b036d-b8b1-4611-965f-08f932dbddb7
keywords:
- Video for Windows (VFW),VCM architecture
- VFW (Video for Windows),VCM architecture
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VCM Architecture

VCM is an intermediary between an application and compression and decompression drivers. The compression and decompression drivers compress and decompress individual frames of data.

When an application makes a call to VCM, VCM translates the call into a message. The message is sent by using the [**ICSendMessage**](/windows/win32/Vfw/nf-vfw-icsendmessage?branch=master) function to the appropriate compressor or decompressor, which compresses or decompresses the data. VCM receives the return value from the compression or decompression driver and then returns control to the application.

If a macro is defined for a message, the macro expands to an **ICSendMessage** function call supplying appropriate parameters for that message. If a macro is defined for a message, your application should use it rather than the message. In this overview, these macros follow messages in parentheses.

 

 




