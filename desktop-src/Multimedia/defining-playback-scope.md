---
title: Defining Playback Scope
description: Defining Playback Scope
ms.assetid: f2563226-7af1-4cb3-b468-c59738feeda2
keywords:
- MCIWndPlayFrom macro
- MCIWndPlayTo macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Defining Playback Scope

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

MCIWnd provides macros that allow you to define the playback *scope*. The scope is the portion of the playback you want to play. For example, you can play the content from a position other than the beginning position by using the [**MCIWndPlayFrom**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfrom) macro. This macro moves to the specified position, begins playback, and continues to the end of the content. Similarly, you can play the content to a specified end point by using the [**MCIWndPlayTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayto) macro. This macro starts at the current playback position and plays until it reaches the specified position or the end of the content is reached, whichever comes first.

Also, you can define both the beginning and ending positions by using the [**MCIWndPlayFromTo**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayfromto) macro. This macro moves to the specified starting position and plays until the specified ending position or the end of the content is reached.

 

 




