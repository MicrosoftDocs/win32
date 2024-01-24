---
description: Because of the lack of recognizers on non-Tablet PC editions of Microsoft Windows XP, you cannot use InkEdit to render ink on Windows 2000, Windows Server 2003, and non-Tablet PC editions of Windows XP, and you cannot use the control to input ink on these operating systems.
ms.assetid: eb80ff91-5c09-43d1-afd4-6391097000c1
title: Using InkEdit on Earlier Versions of Windows
ms.topic: article
ms.date: 05/31/2018
---

# Using InkEdit on Earlier Versions of Windows

Because of the lack of recognizers on non-Tablet PC editions of Microsoft Windows XP, you cannot use [InkEdit](inkedit-control.md) to render ink on Windows 2000, Windows Server 2003, and non-Tablet PC editions of Windows XP, and you cannot use the control to input ink on these operating systems.

The control's [**InkMode**](/windows/desktop/api/inked/nf-inked-iinkedit-get_inkmode) property is set to **Disabled** (**IEM\_Disabled** for C++), and attempting to change the property has no effect. You can assign values to other properties and copy and paste ink to other applications, but you cannot use the control to accept gestures or collect ink.

 

 



