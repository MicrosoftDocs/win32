---
title: Defining Playback Scope
description: Defining Playback Scope
ms.assetid: f2563226-7af1-4cb3-b468-c59738feeda2
keywords:
- MCIWndPlayFrom macro
- MCIWndPlayTo macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Defining Playback Scope

MCIWnd provides macros that allow you to define the playback *scope*. The scope is the portion of the playback you want to play. For example, you can play the content from a position other than the beginning position by using the [**MCIWndPlayFrom**](/windows/win32/Vfw/nf-vfw-mciwndplayfrom?branch=master) macro. This macro moves to the specified position, begins playback, and continues to the end of the content. Similarly, you can play the content to a specified end point by using the [**MCIWndPlayTo**](/windows/win32/Vfw/nf-vfw-mciwndplayto?branch=master) macro. This macro starts at the current playback position and plays until it reaches the specified position or the end of the content is reached, whichever comes first.

Also, you can define both the beginning and ending positions by using the [**MCIWndPlayFromTo**](/windows/win32/Vfw/nf-vfw-mciwndplayfromto?branch=master) macro. This macro moves to the specified starting position and plays until the specified ending position or the end of the content is reached.

 

 




